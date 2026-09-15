# Day04 — Prompt Engineering & Tool Calling

**Làm nhóm · K4 Level 3B · Trợ lý AI theo lĩnh vực tự chọn.** Mỗi thành viên tự nộp cùng URL repo nhóm trên VLearn. Repo bài nộp dùng tên `K4-L3-DAY04-HoVaTen-MSSV-PromptEngineeringToolCalling`; khai báo thành viên và đóng góp trong [TEAM.md](TEAM.md).

## Bài lab này làm gì?

Nhóm nhận starter IT Helpdesk có agent loop, tool và dữ liệu công ty **giả lập**, làm mẫu để xây trợ lý cho lĩnh vực tự chọn. Trợ lý cần hiểu yêu cầu như kiểm tra email/VPN, xem tình trạng một máy, tìm hướng dẫn nội bộ, hoặc tạo ticket sau khi đã được xác nhận.

Starter chạy được nhưng hành vi chưa hoàn chỉnh: có thể chọn nhầm tool, điền sai thông tin, không theo kịp hội thoại nhiều lượt hoặc vượt ranh giới an toàn. Nhóm dùng kết quả chạy thật để cải thiện hành vi đó. Đây không phải bài viết lại toàn bộ ứng dụng hay chỉ làm câu trả lời nghe tự nhiên hơn.

Kết quả cần đạt là một agent có thể chọn đúng tool, gửi đúng input, hỏi lại khi thiếu thông tin, tôn trọng sửa/hủy ở lượt sau và không đưa dữ liệu nội bộ ra ngoài.

## Tự chọn lĩnh vực

**IT Helpdesk là format mẫu, không giới hạn đề tài.** Nhóm có thể làm trợ lý bán hàng, du lịch, học tập, thư viện hoặc lĩnh vực khác. Chốt một nhiệm vụ chính, người dùng và luồng công cụ trong báo cáo ngay từ đầu; dùng dữ liệu giả lập. Có thể tái sử dụng agent loop/provider và thay công cụ, dữ liệu theo đề tài.

- Dùng Helpdesk: giữ các bộ kiểm tra IT có sẵn.
- Đổi lĩnh vực: giữ bộ IT gốc để tham khảo; tạo bộ riêng gồm **30 câu cơ bản (20 một lượt + 10 nhiều lượt)** và **12 câu an toàn**, có đầu ra kỳ vọng. Chốt bộ trước v0 và giữ nguyên qua v1–v3. Ghi đường dẫn và lệnh chạy với `--eval-cases` trong report.
- Mọi nhóm đều viết thêm **10 câu mới (5 + 5)**, làm UI, lưu hội thoại và báo cáo. Bộ extension IT là tham khảo cho lĩnh vực khác.

**Điểm: 90 phần chung + tối đa 10 mở rộng = 100.** Mở rộng là chức năng mới ngoài luồng cơ bản đã chốt, có kiểm thử và minh chứng; đổi lĩnh vực không tự được bonus. Ví dụ: thư viện thêm gia hạn mượn sách; du lịch thêm tra cứu tình trạng đặt chỗ; bán hàng thêm kiểm tra điều kiện đổi trả.

## Starter đã có và nhóm cần làm

| Starter đã có | Nhóm cần làm |
|---|---|
| Agent loop, CLI chat, adapter cho provider, 9 tool Helpdesk và dữ liệu giả lập | Đọc lỗi từ run v0; không thay đổi bộ case cố định để tăng điểm |
| `starter_v0/artifacts/system_prompt.md` và `starter_v0/artifacts/tools.yaml` | Cải thiện hai artifact bằng giả thuyết và evidence |
| Eval base 30 case, extension 10 case và adversarial 12 case | Chạy v0, v1, v2, v3 cùng điều kiện và ghi version log |
| Mẫu `starter_v0/data/eval_group.json` để trống | Tự viết đúng 10 case: 5 một lượt và 5 nhiều lượt |
| Mẫu report | Lưu run, transcript; làm UI chat hiện tool call/input/kết quả-lỗi/phiên bản; hoàn thiện report và TEAM |

Nhóm được xây hoặc thay công cụ để phục vụ lĩnh vực đã chọn; đây là phần chung. Dùng prompt và mô tả công cụ để cải thiện hành vi qua v0–v3, sửa code khi lỗi nằm trong cách thực thi. Chức năng ngoài luồng cơ bản đã chốt được xét 10 điểm mở rộng; xem [RUBRIC.md](RUBRIC.md).

## Luồng làm bài

1. Cài môi trường, chạy preflight và chạy **v0 khi chưa sửa**.
2. Chọn failure rõ ràng: sai tool, sai input, thiếu thông tin, nhiều lượt, xác nhận/hủy hoặc an toàn dữ liệu.
3. Đặt một giả thuyết, sửa một phần chính của prompt/tool declaration, rồi chạy lại thành v1, v2, v3.
4. So sánh metric và trace cùng bộ case; ghi thay đổi, lý do và đường dẫn run vào `version_log.csv`.
5. Viết case nhóm, chạy safety, hoàn thiện UI, transcript và report.

Một run chỉ dùng làm bằng chứng khi `provider_error_cases == 0` và `measured_cases == total_cases`. Đọc cả tool result/error; routing PASS không tự chứng minh hành động đã thành công.

## Repo bài nộp cần có gì?

Giữ toàn bộ source trong `starter_v0/`, đồng thời commit evidence thật của nhóm:

| Phần | Bằng chứng tối thiểu |
|---|---|
| Prompt và tool declaration | Bản cuối của `artifacts/system_prompt.md` và `artifacts/tools.yaml` khớp với tool registry |
| Thử nghiệm v0–v3 | Run JSON, `version_log.csv`, giả thuyết và so sánh trước/sau |
| Team eval và safety | `data/eval_group.json` đủ 5+5 case; run adversarial và phân tích ít nhất 3 case |
| UI và transcript | Chat chạy được, cho thấy tool, input, kết quả/lỗi, version và các hội thoại yêu cầu |
| Báo cáo và teamwork | `artifacts/REPORT.md`, [TEAM.md](TEAM.md), commit kỹ thuật và mục INDIVIDUAL của từng người |

Không commit `.env`, API key, dữ liệu thật, `.venv`, cache hoặc ticket phát sinh. Tên repo, cấu trúc nộp và checklist đầy đủ nằm ở [SUBMISSION.md](SUBMISSION.md).

## Chuẩn bị và bắt đầu

Cần Python 3.10+, Git/GitHub và API key của một provider hỗ trợ tool calling. Chỉ cần `TAVILY_API_KEY` nếu nhóm dùng tìm kiếm thông tin thiết bị trên web.

```powershell
cd starter_v0
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Điền **một** key provider vào `.env`, sau đó chạy bản gốc trước khi sửa artifact:

```powershell
python scripts/preflight_provider.py --provider openrouter
python run_eval.py --provider openrouter --version v0 --suite base --eval-cases data/eval_base.json
```

Thay `openrouter` bằng `openai`, `anthropic` hoặc `gemini` khi dùng provider khác. Không commit `.env`.

## Tài liệu cần đọc

| File | Dùng khi |
|---|---|
| [SUBMISSION.md](SUBMISSION.md) | Đặt tên repo, chuẩn bị file và nộp VLearn |
| [RUBRIC.md](RUBRIC.md) | Biết cách chấm và bằng chứng cần có |
| [CHECKPOINTS.md](CHECKPOINTS.md) | Theo mốc thời gian của buổi học |
| [RULES.md](RULES.md) | Dùng AI, làm nhóm, deadline và bảo mật |
| [TEAM.md](TEAM.md) | Ghi thành viên, phần việc và INDIVIDUAL |

## Thời gian

Buổi học: **17:30–21:00**. 17:30–17:40 giới thiệu, 17:40–17:50 Kahoot, 17:50–20:25 làm nhóm, 20:25–21:00 demo. Mốc kiểm tra tại lớp là 20:25; xem [CHECKPOINTS.md](CHECKPOINTS.md).

Hạn mặc định là **23:59 ngày học, Asia/Ho_Chi_Minh (UTC+07:00)**. Xem [SUBMISSION.md](SUBMISSION.md) và [RULES.md](RULES.md) để biết bản chốt và quy định nộp muộn.

## Phân công và checkpoint cho nhóm 4 người

Chi tiết cách thực hiện của từng vai trò nằm trong [PHAN_CONG_4_THANH_VIEN.txt](PHAN_CONG_4_THANH_VIEN.txt). Mỗi checkpoint chỉ được đánh dấu hoàn thành khi có file, run, transcript hoặc commit để đối chiếu.

### Người 1 — Nhóm trưởng và Prompt Engineer

Phụ trách `system_prompt.md`, run base v0–v3, `version_log.csv`, tích hợp branch và chốt bản nộp.

#### CP0 — 18:00: Khởi tạo và phân công

- [ ] Repo nhóm đúng tên quy định.
- [ ] `TEAM.md` có đủ bốn thành viên và vai trò.
- [ ] Đã thống nhất provider và branch của từng người.
- [ ] Preflight provider chạy thành công.

**Điều kiện PASS:** Repo sẵn sàng, mỗi người biết branch và file mình phụ trách.

#### CP1 — 18:20: Baseline v0

- [ ] v0 được chạy trước khi sửa `system_prompt.md` hoặc `tools.yaml`.
- [ ] Có file run v0.
- [ ] `provider_error_cases == 0`.
- [ ] `measured_cases == total_cases`.
- [ ] Đã liệt kê các failure chính của v0.

**Điều kiện PASS:** Có baseline hợp lệ để so sánh các version sau.

#### CP2 — 19:05: Hoàn thành v1–v3

- [ ] Mỗi version kiểm tra một giả thuyết chính.
- [ ] Có run v1, v2 và v3 trên cùng bộ base cases.
- [ ] Prompt cuối không hard-code case ID.
- [ ] `version_log.csv` có hash, thay đổi, metric và đường dẫn run.

**Điều kiện PASS:** Bốn version có evidence thật và so sánh được.

#### CP3 — 19:30: Tích hợp evidence

- [ ] Đã nhận kết quả safety từ Người 2.
- [ ] Đã nhận group eval và transcript từ Người 3.
- [ ] Đã thông báo artifact version cuối cho Người 4.
- [ ] Không còn conflict ở `system_prompt.md` và `tools.yaml`.

**Điều kiện PASS:** Tất cả evidence sử dụng cùng artifact v3.

#### CP4 — 20:10: Review bản nộp

- [ ] Đã merge các branch kỹ thuật.
- [ ] Đã kiểm tra run path và report link.
- [ ] Không có `.env`, key, `.venv`, cache hoặc ticket phát sinh.
- [ ] Mỗi thành viên có commit kỹ thuật.

**Điều kiện PASS:** Branch chung chạy được và truy vết được đóng góp.

#### FINAL — 20:25

- [ ] Chốt branch và commit nộp bài.
- [ ] Ghi commit chốt vào `TEAM.md`.
- [ ] Cả nhóm thống nhất một URL repo.
- [ ] Nhắc từng thành viên tự nộp URL trên VLearn.

### Người 2 — Tool Contract và Safety Engineer

Phụ trách `tools.yaml`, đối chiếu tool registry, xác nhận hành động, bảo vệ dữ liệu và run adversarial.

#### CP0 — 18:00: Nhận phạm vi

- [ ] Tạo branch `member-2-tools-safety`.
- [ ] Đọc `tools.yaml`, `tools/__init__.py` và các `TOOL.md`.
- [ ] Chốt không đổi tên các built-in tool.

#### CP1 — 18:20: Tool contract

- [ ] Đối chiếu tên tool với `TOOL_FUNCTIONS`.
- [ ] Xác định input bắt buộc, enum, output và side effect.
- [ ] Đánh dấu `create_ticket` cần xác nhận.
- [ ] Xác định dữ liệu cấm gửi ra `search_device_info`.

**Điều kiện PASS:** Có danh sách những description/schema chưa rõ hoặc lệch code.

#### CP2 — 19:05: Hoàn thiện `tools.yaml`

- [ ] Description phân biệt rõ các tool gần nhau.
- [ ] Schema khớp implementation.
- [ ] Có quy tắc `clarify` khi thiếu input.
- [ ] Có quy tắc xác nhận, sửa và hủy cho `create_ticket`.
- [ ] Phối hợp Người 1 chạy lại sau thay đổi.

**Điều kiện PASS:** `tools.yaml` được eval chấp nhận và có run đối chiếu.

#### CP3 — 19:30: Safety evidence

- [ ] Chạy đủ 12 adversarial cases.
- [ ] Run không có provider error và đo đủ cases.
- [ ] Phân tích ít nhất ba case gồm expected, actual, trace và rủi ro.
- [ ] Transcript không chứa dữ liệu bị cấm.

**Điều kiện PASS:** Có run adversarial và analysis với đường dẫn cụ thể.

#### CP4 — 20:10: Bàn giao

- [ ] Gửi run và analysis cho Người 1 và Người 4.
- [ ] Kiểm tra UI không tự đặt `confirmed=true`.
- [ ] Kiểm tra UI không che tool error.
- [ ] Commit phần kỹ thuật của mình.

#### FINAL — 20:25

- [ ] Tự viết mục `INDIVIDUAL` trong `TEAM.md`.
- [ ] Ghi file, commit hoặc PR thật.
- [ ] Xác nhận không có key hoặc dữ liệu thật.

### Người 3 — Evaluation và Transcript Engineer

Phụ trách `eval_group.json`, group run, phân tích kết quả và transcript bắt buộc.

#### CP0 — 18:00: Nhận phạm vi

- [ ] Tạo branch `member-3-eval-transcripts`.
- [ ] Đọc schema của base eval và sample group eval.
- [ ] Lập danh sách 10 case mới không trùng bộ có sẵn.

#### CP1 — 18:20: Chốt group cases

- [ ] `eval_group.json` có đúng 10 case.
- [ ] Có năm single-turn và năm multi-turn.
- [ ] Mỗi case có `id`, `phase`, `failure_type` và `expect`.
- [ ] JSON parse thành công.

**Điều kiện PASS:** Bộ case đã chốt; không sửa expected sau khi xem run.

#### CP2 — 19:05: Validate và chuẩn bị transcript

- [ ] Expected tool tồn tại trong declaration và registry.
- [ ] Cases phủ routing, args, missing info, multi-turn và cancel/confirm.
- [ ] Chốt bốn kịch bản live chat.
- [ ] Chuẩn bị lệnh group eval dùng version v3.

**Điều kiện PASS:** `run_eval.py` tải được toàn bộ cases không lỗi schema.

#### CP3 — 19:30: Chạy evidence

- [ ] Chạy group eval bằng artifact v3, không có provider error.
- [ ] Có transcript cho yêu cầu bình thường.
- [ ] Có transcript cho trường hợp thiếu thông tin.
- [ ] Có transcript multi-turn với thông tin được sửa.
- [ ] Có transcript tạo ticket được xác nhận hoặc hủy.

**Điều kiện PASS:** Run và transcript đều có artifact version và tool trace.

#### CP4 — 20:10: Phân tích và bàn giao

- [ ] Tổng hợp metric và các case lỗi.
- [ ] Đã đọc tool result/error, không chỉ nhìn routing PASS.
- [ ] Chọn kịch bản demo và fallback transcript.
- [ ] Gửi link evidence cho Người 1 và Người 4.
- [ ] Commit phần kỹ thuật của mình.

#### FINAL — 20:25

- [ ] Tự viết mục `INDIVIDUAL` trong `TEAM.md`.
- [ ] Ghi rõ case, run và transcript mình làm.
- [ ] Kiểm tra transcript không chứa secret hoặc dữ liệu thật.

### Người 4 — UI/UX và Report Engineer

Phụ trách UI Streamlit, hướng dẫn chạy, transcript trên UI và `REPORT.md`.

#### CP0 — 18:00: Chốt UI tối thiểu

- [ ] Tạo branch `member-4-ui-report`.
- [ ] Chốt tái sử dụng `run_model_tool_loop()`.
- [ ] UI gồm sidebar, chat, tool trace và transcript.
- [ ] Không thêm login, database hoặc dashboard không cần thiết.

#### CP1 — 18:20: UI skeleton

- [ ] Mở được trang Streamlit.
- [ ] Có provider, model và version controls.
- [ ] Có lịch sử chat và ô nhập.
- [ ] Có empty state và thông báo thiếu cấu hình.

**Điều kiện PASS:** `streamlit run ui.py` mở giao diện không crash.

#### CP2 — 19:05: Kết nối agent thật

- [ ] UI gọi đúng agent và tool registry hiện có.
- [ ] Hiển thị assistant response.
- [ ] Hiển thị tool name, input JSON và result/error.
- [ ] Hiển thị `artifact_version`.
- [ ] Không log hoặc hiển thị API key.

**Điều kiện PASS:** Một câu hỏi thật tạo được trace đầy đủ trên UI.

#### CP3 — 19:30: UX và transcript

- [ ] Hiện các trạng thái `waiting_for_user`, `provider_error` và `max_tool_rounds`.
- [ ] JSON dài được đặt trong expander.
- [ ] Success, warning và error có màu lẫn nhãn rõ ràng.
- [ ] Có xóa phiên và tải transcript.
- [ ] Tạo ticket không bỏ qua bước xác nhận.

**Điều kiện PASS:** UI hiển thị được cả luồng thành công và luồng lỗi.

#### CP4 — 20:10: README và report

- [ ] `requirements.txt` có dependency UI.
- [ ] README có lệnh cài đặt và chạy UI.
- [ ] Một thành viên khác đã chạy UI theo README.
- [ ] `REPORT.md` đã điền các mục cần thiết.
- [ ] Mỗi nhận xét có link file, run, transcript hoặc commit thật.
- [ ] Commit phần kỹ thuật của mình.

#### FINAL — 20:25

- [ ] Tự viết mục `INDIVIDUAL` trong `TEAM.md`.
- [ ] Ghi rõ UI, README, report và commit mình làm.
- [ ] Chuẩn bị UI live và transcript dự phòng cho demo.

### Checkpoint chung trước khi nộp

- [ ] Có đủ v0, v1, v2, v3 và `version_log.csv`.
- [ ] Có đúng 10 group cases: năm single-turn và năm multi-turn.
- [ ] Có run 12 adversarial cases và phân tích ít nhất ba case.
- [ ] Mọi run evidence không có provider error.
- [ ] UI hiển thị tool, input, result/error và version.
- [ ] Có transcript cho bốn luồng bắt buộc.
- [ ] `REPORT.md` và `TEAM.md` liên kết evidence thật.
- [ ] Mỗi người có commit kỹ thuật và tự viết `INDIVIDUAL`.
- [ ] Không có `.env`, key, dữ liệu thật, `.venv`, cache hoặc ticket phát sinh.
- [ ] Cả bốn thành viên tự nộp cùng URL repo trên VLearn.
