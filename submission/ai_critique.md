# AI Critique — Bài phê bình sử dụng AI trong HW03

Trong quá trình thực hiện HW03, em sử dụng AI (Codex/GPT-5 và Antigravity/Gemini) như một trợ lý hỗ trợ lập kế hoạch, cấu trúc báo cáo, chuẩn hóa checklist execution, tính SUS và tạo Agent Skill. Tuy nhiên, em nhận thấy AI vẫn có nhiều giới hạn cần được kiểm soát chặt chẽ.

Thứ nhất, AI có **xu hướng hoàn thiện quá sớm (Optimistic Completion Bias)**: bản nháp nhìn có vẻ đầy đủ nhưng chưa chắc đã có bằng chứng thật. AI không thể thay em xác nhận trạng thái EMS live, độ trễ request, lỗi responsive trên thiết bị thật, watermark BrowserStack, hay phản ứng do dự của người tham gia usability testing.

Thứ hai, AI dễ **trích dẫn gượng ép heuristic** của Nielsen, Norman hoặc Shneiderman vào từng lỗi UI mà chưa hiểu đủ ngữ cảnh nghiệp vụ. Một số điểm đặc thù của EMS như EN/VI localization, mobile drawer, empty-state recovery, watermark MSSV và thiếu action Reset Password chỉ trở nên rõ khi em tự thao tác và đối chiếu ảnh minh chứng.

Thứ ba, AI chưa đáng tin khi phân loại mức độ lỗi. Có lúc AI xem thiếu Block/Unblock hoặc Reset Password là bug tuyệt đối, trong khi cần diễn đạt cẩn thận hơn: UI có Active/Inactive nhưng wording mơ hồ và thiếu entry point rõ ràng.

**Bài học cốt lõi về Bloom-AI G9.4:** AI nên được dùng như trợ lý cấu trúc và phản biện ban đầu, còn em phải là **người kiểm chứng dữ liệu gốc (Ground-Truth Validator)**. Mọi kết quả cuối cùng phải dựa trên thao tác EMS thật, ảnh thật, người dùng thật và review thủ công.
