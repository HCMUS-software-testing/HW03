# AI Critique — Bài phê bình sử dụng AI trong HW03

Trong quá trình thực hiện HW03, công cụ AI (Codex/GPT-5 và Antigravity/Gemini) đóng vai trò trợ lý hiệu quả trong việc lập kế hoạch, cấu trúc bài báo cáo và tạo các Agent Skill tự động. Tuy nhiên, AI bộc lộ những hạn chế và thiên vị (bias) mang tính hệ thống cần sinh viên trực tiếp phản biện và hiệu chỉnh:

Thứ nhất, AI có **xu hướng hoàn thiện quá sớm (Optimistic Completion Bias)**, dễ dàng tạo ra các bản nháp trông như đã kiểm thử xong. AI không thể trực tiếp thao tác trên ứng dụng EMS thật (`prod-dev.ems-fitus.cloud`), không cảm nhận được độ trễ hệ thống, vỡ giao diện trên thiết bị mobile, hay đo lường chính xác cảm xúc do dự của 5 người dùng thật khi phỏng vấn Usability.

Thứ hai, AI dễ **trích dẫn gượng ép các Heuristics** (Nielsen, Norman, Shneiderman) vào các lỗi giao diện mà thiếu ngữ cảnh thực tế. AI thường bỏ sót các khía cạnh đặc thù của EMS như chuyển đổi ngôn ngữ EN/VI, responsive mobile drawer, watermark MSSV trên ảnh cross-platform hay lỗi thiếu nút khôi phục trong form.

Thứ ba, AI hoàn toàn thất bại trong việc tự phát hiện các lỗi logic và thiếu hụt tính năng hệ thống lớn, chẳng hạn như việc ứng dụng EMS thiếu hoàn toàn tính năng Chặn/Bỏ chặn và Đặt lại mật khẩu ở Kịch bản C3.

**Bài học cốt lõi về nguyên tắc hợp tác với AI (Bloom-AI G9.4):** Xem AI như một trợ lý cấu trúc tài liệu và kiểm tra tính nhất quán, nhưng sinh viên bắt buộc phải là **người kiểm chứng dữ liệu gốc (Ground-Truth Validator)**. Sinh viên chịu trách nhiệm 100% về tính trung thực của kết quả kiểm thử, ảnh chụp thực tế và tính chính xác của bài nộp.
