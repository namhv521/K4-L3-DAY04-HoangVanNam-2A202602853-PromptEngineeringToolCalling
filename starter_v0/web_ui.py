"""Web UI cho IT Helpdesk Agent.

Dùng cùng agent loop, cùng artifact và cùng định dạng transcript như `chat.py`,
chỉ thay lớp hiển thị từ terminal sang trình duyệt. Chỉ dùng thư viện chuẩn của
Python nên không cần cài thêm phụ thuộc nào.

    python web_ui.py --provider openrouter --version v3
"""

from __future__ import annotations

import argparse
import json
import threading
import webbrowser
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any

from chat import (
    ROOT,
    ARTIFACTS_DIR,
    now_iso,
    run_model_tool_loop,
    safe_slug,
    trim_history,
    write_transcript,
)
from providers import make_provider
from tools import load_tool_declarations, to_openai_tools
from versioning import artifact_version_dict, build_artifact_version

UI_DIR = ROOT / "ui"


class Session:
    """Giữ lịch sử hội thoại và transcript cho một phiên chat."""

    def __init__(self, cfg: argparse.Namespace, provider: Any, tools: list[dict[str, Any]], system_prompt: str) -> None:
        self.cfg = cfg
        self.provider = provider
        self.tools = tools
        self.system_prompt = system_prompt
        self.model = cfg.model or getattr(provider, "default_model", None)
        self.artifact_version = build_artifact_version(cfg.version, cfg.system_prompt, cfg.tools)
        self.lock = threading.Lock()
        self.reset()

    def reset(self) -> None:
        timestamp = datetime.now().strftime("%Y%m%dT%H%M%S%f")
        transcript_id = "_".join([safe_slug(self.cfg.version), safe_slug(self.cfg.provider), timestamp])
        self.transcript_path = self.cfg.transcripts_dir / f"{transcript_id}.transcript.json"
        self.history: list[dict[str, str]] = []
        self.turn_index = 0
        self.transcript: dict[str, Any] = {
            "transcript_id": transcript_id,
            **artifact_version_dict(self.artifact_version),
            "provider": self.cfg.provider,
            "model": self.model,
            "system_prompt": str(self.cfg.system_prompt),
            "tools": str(self.cfg.tools),
            "history_window": self.cfg.history_window,
            "max_tool_rounds": self.cfg.max_tool_rounds,
            "ui": "web",
            "created_at": now_iso(),
            "updated_at": now_iso(),
            "turns": [],
        }

    def info(self) -> dict[str, Any]:
        return {
            "artifact_version": self.artifact_version.artifact_version,
            "provider": self.cfg.provider,
            "model": self.model,
            "transcript_path": str(self.transcript_path),
            "turn_index": self.turn_index,
        }

    def ask(self, user_text: str) -> dict[str, Any]:
        with self.lock:
            self.turn_index += 1
            messages = [
                {"role": "system", "content": self.system_prompt},
                *trim_history(self.history, self.cfg.history_window),
                {"role": "user", "content": user_text},
            ]
            turn: dict[str, Any] = {
                "turn_index": self.turn_index,
                "started_at": now_iso(),
                "user": user_text,
                "status": "started",
                "assistant_text": None,
                "rounds": [],
                "tool_events": [],
            }

            try:
                result = run_model_tool_loop(
                    provider=self.provider,
                    messages=messages,
                    tools=self.tools,
                    model=self.cfg.model,
                    max_tool_rounds=self.cfg.max_tool_rounds,
                )
                turn.update(result)
                self.history.append({"role": "user", "content": user_text})
                self.history.append({"role": "assistant", "content": result["assistant_text"]})
            except Exception as exc:  # lỗi provider vẫn phải hiện ra UI, không nuốt
                turn.update({"status": "provider_error", "error": f"{type(exc).__name__}: {exc}"})

            turn["ended_at"] = now_iso()
            self.transcript["turns"].append(turn)
            write_transcript(self.transcript_path, self.transcript)

            return {
                "turn_index": self.turn_index,
                "status": turn["status"],
                "assistant_text": turn.get("assistant_text"),
                "tool_events": turn.get("tool_events", []),
                "error": turn.get("error"),
                "transcript_path": str(self.transcript_path),
            }


def make_handler(session: Session):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, fmt: str, *args: Any) -> None:
            return  # giữ terminal sạch; tool trace đã in trong run_model_tool_loop

        def _send(self, status: int, body: bytes, content_type: str) -> None:
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def _json(self, payload: dict[str, Any], status: int = 200) -> None:
            body = json.dumps(payload, ensure_ascii=False, default=str).encode("utf-8")
            self._send(status, body, "application/json; charset=utf-8")

        def do_GET(self) -> None:
            if self.path in ("/", "/index.html"):
                page = (UI_DIR / "index.html").read_bytes()
                self._send(200, page, "text/html; charset=utf-8")
            elif self.path == "/api/info":
                self._json(session.info())
            else:
                self._json({"error": "not_found"}, 404)

        def do_POST(self) -> None:
            length = int(self.headers.get("Content-Length") or 0)
            raw = self.rfile.read(length) if length else b"{}"
            try:
                payload = json.loads(raw.decode("utf-8") or "{}")
            except json.JSONDecodeError:
                self._json({"error": "invalid_json"}, 400)
                return

            if self.path == "/api/chat":
                message = (payload.get("message") or "").strip()
                if not message:
                    self._json({"error": "empty_message"}, 400)
                    return
                print(f"\n[user] {message}")
                self._json(session.ask(message))
            elif self.path == "/api/reset":
                session.reset()
                print(f"\n--- phiên mới: {session.transcript_path.name} ---")
                self._json(session.info())
            else:
                self._json({"error": "not_found"}, 404)

    return Handler


def main() -> None:
    parser = argparse.ArgumentParser(description="Web UI cho IT Helpdesk Agent, kèm transcript logging.")
    parser.add_argument("--provider", choices=["openrouter", "openai", "anthropic", "gemini"], required=True)
    parser.add_argument("--model", default=None)
    parser.add_argument("--version", required=True, help="Nhãn phiên bản artifact, ví dụ v3.")
    parser.add_argument("--system-prompt", type=Path, default=ARTIFACTS_DIR / "system_prompt.md")
    parser.add_argument("--tools", type=Path, default=ARTIFACTS_DIR / "tools.yaml")
    parser.add_argument("--transcripts-dir", type=Path, default=ROOT / "transcripts")
    parser.add_argument("--history-window", type=int, default=5)
    parser.add_argument("--max-tool-rounds", type=int, default=4)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--no-browser", action="store_true", help="Không tự mở trình duyệt.")
    args = parser.parse_args()

    system_prompt = args.system_prompt.read_text(encoding="utf-8")
    tools = to_openai_tools(load_tool_declarations(args.tools))
    provider = make_provider(args.provider)
    session = Session(args, provider, tools, system_prompt)

    url = f"http://{args.host}:{args.port}"
    print(f"IT Helpdesk Agent — web UI")
    print(f"  artifact_version : {session.artifact_version.artifact_version}")
    print(f"  provider/model   : {args.provider} / {session.model}")
    print(f"  transcript       : {session.transcript_path}")
    print(f"  mở trình duyệt   : {url}")
    print("  Ctrl+C để dừng.\n")

    server = ThreadingHTTPServer((args.host, args.port), make_handler(session))
    if not args.no_browser:
        threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nĐã dừng. Transcript cuối:", session.transcript_path)
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
