# TEAM — Day04, K4-L3B

**Làm nhóm.** Mỗi thành viên phụ trách một phiên bản chính và phối hợp kiểm thử theo các checkpoint CP0 → FINAL.

## Thông tin bài nộp

- Tên nhóm: Northstar IT Helpdesk Team (Nhóm 4 - K4-L3B)
- Người đại diện / MSSV: Hoàng Văn Nam / 2A202602853
- Tên repo: `K4-L3-DAY04-HoangVanNam-2A202602853-PromptEngineeringToolCalling`
- URL repo: <https://github.com/namhv521/K4-L3-DAY04-HoangVanNam-2A202602853-PromptEngineeringToolCalling>
- Nhánh và commit chốt: nhánh `main`, commit `Complete Lab 04 v3`.
- Deadline: 23:59 ngày 15/09/2026 (Asia/Ho_Chi_Minh).

## Thành viên và phân công

| Họ và tên | MSSV | GitHub | Vai trò và công việc | File/sản phẩm phụ trách |
|---|---|---|---|---|
| Hoàng Văn Nam | 2A202602853 | <https://github.com/namhv521> | **Nhóm trưởng, v0 và tích hợp.** Thực hiện CP0–CP1: khởi tạo repo, cài môi trường, chạy preflight, chốt luồng Helpdesk và chạy baseline v0. Quản lý tích hợp, UI, báo cáo, tài liệu, version log và toàn bộ file không được giao riêng cho thành viên khác; kiểm tra bản nộp tại FINAL. | `starter_v0/runs/v0_B_base_...json`, `starter_v0/ui.py`, `starter_v0/ui_models.py`, `starter_v0/app_core.py`, `starter_v0/artifacts/REPORT.md`, `starter_v0/analysis/v0-v3-analysis.md`, `README.md`, `TEAM.md` và các file còn lại. |
| Nguyễn Hải Hoàng | 2A202602489 | <https://github.com/hoang9605> | **Prompt/Tool Engineer v1.** Thực hiện phần đầu CP2: rà soát prompt và hợp đồng tool, tạo thay đổi v1 theo một giả thuyết rõ ràng, chạy lại cùng bộ base 30 cases, lưu hash/run và phân tích sai tool, sai input, lỗi tool. | `starter_v0/artifacts/versions/v1/system_prompt.md`, `starter_v0/artifacts/tools.yaml`, `starter_v0/runs/v1_B_base_...json`; nội dung phân tích v1. |
| Lê Tuấn Đạt | 2A202602623 | <https://github.com/TuanDatt08> | **Prompt Engineer v2 và Test Generation.** Thực hiện phần tiếp theo CP2 và CP4: bổ sung quy tắc thiếu thông tin/xác nhận cho v2; thiết kế bộ 10 test nhóm gồm 5 single-turn và 5 multi-turn; chạy group eval và ghi nhận trung thực các case đạt/chưa đạt. | `starter_v0/artifacts/versions/v2/system_prompt.md`, `starter_v0/data/eval_group.json`, `starter_v0/runs/v2_B_base_...json`, `starter_v0/runs/v3_B_group_...json`. |
| Đinh Kim Thái | 2A202602417 | <https://github.com/thaidinh1206> | **Prompt/Safety Engineer v3.** Hoàn thiện phần cuối CP2 và CP3: tối ưu routing/arguments và trust boundary cho v3; chạy bộ 12 adversarial cases; kiểm tra thiếu thông tin, sửa/hủy/xác nhận và chuẩn bị transcript minh chứng cho demo. | `starter_v0/artifacts/versions/v3/system_prompt.md`, `starter_v0/runs/v3_B_base_...json`, `starter_v0/runs/v3_B_adversarial_...json`, `starter_v0/transcripts/v3_...transcript.json`. |

## Tiến độ theo checkpoint

| Checkpoint | Người chính | Nội dung hoàn thành | Bằng chứng |
|---|---|---|---|
| CP0 | Hoàng Văn Nam | Chốt lĩnh vực IT Helpdesk, luồng cơ bản, repo, phân công và môi trường. | `README.md`, `TEAM.md`, `starter_v0/.env.example`, `starter_v0/scripts/preflight_provider.py` |
| CP1 | Hoàng Văn Nam | Chạy v0 trên bộ base 30 cases, lưu baseline và nhận diện nhóm lỗi ban đầu. | `starter_v0/runs/v0_B_base_...json`, `starter_v0/artifacts/version_log.csv` |
| CP2 — v1 | Nguyễn Hải Hoàng | Rà soát prompt/tool contract, chạy v1 trên cùng bộ base và so sánh với v0. | `starter_v0/artifacts/versions/v1/system_prompt.md`, `starter_v0/artifacts/tools.yaml`, `starter_v0/runs/v1_B_base_...json` |
| CP2 — v2 | Lê Tuấn Đạt | Bổ sung missing-info và confirmation boundary; chạy base v2. | `starter_v0/artifacts/versions/v2/system_prompt.md`, `starter_v0/runs/v2_B_base_...json` |
| CP2 — v3 | Đinh Kim Thái | Làm rõ routing, category, arguments và tool trust boundary; chạy base v3. | `starter_v0/artifacts/versions/v3/system_prompt.md`, `starter_v0/runs/v3_B_base_...json` |
| CP3 | Đinh Kim Thái | Chạy 12 adversarial cases, phân tích confirmation và rò rỉ dữ liệu. | `starter_v0/runs/v3_B_adversarial_...json`, transcript và phần B4a/B6 của report |
| CP4 — tests | Lê Tuấn Đạt | Sinh 10 case nhóm (5 single-turn + 5 multi-turn) và chạy group eval. | `starter_v0/data/eval_group.json`, `starter_v0/runs/v3_B_group_...json` |
| CP4 — UI | Hoàng Văn Nam | Hoàn thiện UI dùng agent loop thật, hiển thị tool trace và xuất transcript. | `starter_v0/ui.py`, `starter_v0/ui_models.py`, `starter_v0/app_core.py` |
| FINAL/DEMO | Hoàng Văn Nam | Tích hợp, rà soát report, TEAM, README, kịch bản demo và bằng chứng. | `starter_v0/artifacts/REPORT.md`, `starter_v0/analysis/v0-v3-analysis.md`, `starter_v0/DEMO_CASES.md` |

## Kết quả chung

- Base accuracy: v0 **70.00%** (21/30), v1 **66.67%** (20/30), v2 **80.00%** (24/30), v3 **90.00%** (27/30).
- Bản v3 đạt routing accuracy **96.67%**, argument accuracy **90.00%** và multi-turn accuracy **100.00%** trên base run được chọn.
- Group eval đạt **80.00%** (8/10); adversarial eval đạt **75.00%** (9/12).
- Các run dùng làm bằng chứng có `provider_error_cases == 0` và đo đủ số case.
- Cải thiện chính từ v1 → v2 là ranh giới xác nhận và xử lý thiếu thông tin; từ v2 → v3 là routing/category, arguments tường minh và tool trust boundary.
- Giới hạn còn lại: đôi lúc nhầm phòng ban với employee ID, dùng `check=all` cho yêu cầu kép và chưa chặn bền vững forged/stale confirmation ở tầng prompt.

## INDIVIDUAL

### Hoàng Văn Nam — 2A202602853

- **Phần việc:** Nhóm trưởng; phụ trách v0, CP0–CP1, UI, tích hợp, tài liệu và các file còn lại.
- **Công việc đã làm:** Khởi tạo cấu trúc bài; cấu hình môi trường và preflight; chạy baseline 30 cases; theo dõi `version_log.csv`; tích hợp v1–v3; xây dựng UI Streamlit sử dụng agent loop thật; tổng hợp report, phân tích, demo cases và kiểm tra bản nộp.
- **Khó khăn và xử lý:** Baseline còn lỗi đoán ID, sai tool/argument và gọi action trước xác nhận. Các failure được phân loại theo trace rồi giao thành giả thuyết cải tiến cho từng phiên bản, luôn giữ nguyên bộ base để so sánh.
- **Điều học được:** Cần quản lý artifact, hash, run và evidence cùng lúc; một thay đổi prompt chỉ được xem là cải tiến khi có run hợp lệ và phân tích failure hỗ trợ.
- **AI/công cụ và cách kiểm tra:** Dùng AI hỗ trợ rà soát prompt/report; kiểm tra bằng `run_eval.py`, unit tests, run JSON, transcript và chạy UI cục bộ.
- **File chính:** `starter_v0/runs/v0_B_base_...json`, `starter_v0/artifacts/version_log.csv`, `starter_v0/ui.py`, `starter_v0/app_core.py`, `starter_v0/artifacts/REPORT.md`, `README.md`, `TEAM.md` và các file không giao riêng.

### Nguyễn Hải Hoàng — 2A202602489

- **Phần việc:** Phụ trách phiên bản v1 và rà soát hợp đồng công cụ.
- **Công việc đã làm:** Đối chiếu tool descriptions/schema với implementation; rà soát ranh giới giữa các tool; tạo artifact v1 và chạy cùng bộ base 30 cases để có đối chứng với v0.
- **Khó khăn và xử lý:** Run v1 có accuracy thấp hơn v0 dù artifact thay đổi ít/không tạo cải thiện hành vi rõ ràng. Kết quả được giữ nguyên để tránh tuyên bố sai rằng đổi nhãn phiên bản là một cải tiến.
- **Điều học được:** Sai tool, sai input và lỗi thực thi tool là ba loại lỗi khác nhau; cần đối chiếu tool call và result trước khi kết luận.
- **AI/công cụ và cách kiểm tra:** Dùng AI hỗ trợ kiểm tra schema và mô tả tool; xác minh bằng base eval v1, hash artifact và `provider_error_cases`.
- **File chính:** `starter_v0/artifacts/versions/v1/system_prompt.md`, `starter_v0/artifacts/tools.yaml`, `starter_v0/runs/v1_B_base_...json`.

### Lê Tuấn Đạt — 2A202602623

- **Phần việc:** Phụ trách phiên bản v2 và sinh bộ test nhóm.
- **Công việc đã làm:** Bổ sung quy tắc hỏi lại khi thiếu dữ liệu, confirmation boundary và vô hiệu hóa xác nhận cũ khi payload thay đổi; chạy base v2; thiết kế `eval_group.json` gồm đúng 5 single-turn và 5 multi-turn; chạy group eval.
- **Khó khăn và xử lý:** Test đa lượt dễ bị điều chỉnh theo kết quả model. Bộ expected được chốt trước khi chạy và giữ nguyên hai failure G07, G09 để báo cáo trung thực.
- **Điều học được:** Eval agent phải kiểm tra cả gọi đúng tool, đúng argument, từ chối phù hợp và duy trì/hủy ngữ cảnh qua nhiều lượt.
- **AI/công cụ và cách kiểm tra:** Dùng AI hỗ trợ tạo biến thể câu hỏi và rà cú pháp JSON; kiểm tra bằng base eval v2, group eval v3 và đọc trace từng case.
- **File chính:** `starter_v0/artifacts/versions/v2/system_prompt.md`, `starter_v0/data/eval_group.json`, `starter_v0/runs/v2_B_base_...json`, `starter_v0/runs/v3_B_group_...json`.

### Đinh Kim Thái — 2A202602417

- **Phần việc:** Phụ trách phiên bản v3, kiểm thử an toàn và transcript.
- **Công việc đã làm:** Làm rõ category mapping, ID/environment hợp lệ, argument bắt buộc và ranh giới dữ liệu nội bộ; chạy base v3 và bộ adversarial 12 cases; kiểm tra các luồng thiếu thông tin, sửa, hủy, xác nhận và lưu transcript demo.
- **Khó khăn và xử lý:** Prompt guardrail vẫn có thể bị vượt qua bởi forged tool result hoặc stale/role-spoof confirmation. Các failure A03, A10, A11 được giữ trong báo cáo; hướng cải tiến là enforcement confirmation state/token ở tầng code.
- **Điều học được:** Ranh giới an toàn cần được kiểm tra bằng trace và tool result, không chỉ dựa vào câu trả lời cuối hoặc automatic score.
- **AI/công cụ và cách kiểm tra:** Dùng AI hỗ trợ xây dựng tình huống adversarial; kiểm tra bằng base/adversarial eval v3, transcript và rà dữ liệu nhạy cảm trong tool calls.
- **File chính:** `starter_v0/artifacts/versions/v3/system_prompt.md`, `starter_v0/runs/v3_B_base_...json`, `starter_v0/runs/v3_B_adversarial_...json`, `starter_v0/transcripts/v3_...transcript.json`.

## Xác nhận trước khi nộp

- [x] Có đủ bốn thành viên, MSSV và GitHub.
- [x] Vai trò bám theo v0 → v3 và checkpoint CP0 → FINAL.
- [x] Có người phụ trách sinh test, adversarial test, UI, report và tích hợp.
- [ ] Cập nhật nhánh và commit chốt theo bản nộp cuối.
- [ ] Mỗi thành viên đọc lại phần INDIVIDUAL và tự nộp cùng URL repo trên VLearn.
