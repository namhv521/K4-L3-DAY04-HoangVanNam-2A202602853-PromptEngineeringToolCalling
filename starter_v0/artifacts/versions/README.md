# Versioned artifacts

Mỗi thư mục lưu prompt đúng với version được đánh giá. Tất cả version hiện dùng chung `../../tools.yaml`; hash tool trong `version_log.csv` chứng minh declaration không đổi. File `../../system_prompt.md` luôn là bản v3 đang chạy.

- `v0`: starter baseline.
- `v1`: control run, chỉ đổi nhãn version; nội dung artifact không đổi nên kết quả giảm không được xem là cải thiện.
- `v2`: confirmation boundary và xử lý thiếu thông tin.
- `v3`: routing và argument rules rút ra từ sáu failure của v2.
