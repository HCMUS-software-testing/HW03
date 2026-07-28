# AI Critique

AI hữu ích trong việc biến yêu cầu HW03 thành các template có cấu trúc, nhưng không thể thay thế phần kiểm thử thật của sinh viên. Giới hạn lớn nhất là AI không thể tự xác nhận hành vi của EMS nếu chưa quan sát màn hình thật, chưa có ảnh chụp từ browser/device thật và chưa có người tham gia thật. AI có thể gợi ý các rủi ro GUI thường gặp như xác nhận thao tác nguy hiểm chưa rõ, phản hồi trạng thái yếu hoặc bảng bị tràn trên mobile, nhưng các gợi ý đó phải được kiểm chứng trước khi trở thành finding.

AI cũng có xu hướng tạo báo cáo trông như đã hoàn tất quá sớm. Điều này nguy hiểm với bài HW03 vì dữ liệu người tham gia giả, ảnh chụp giả hoặc timestamp Google Form bị thiếu sẽ vi phạm yêu cầu anti-cheat. Để kiểm soát rủi ro đó, tất cả bằng chứng chưa thu thập đều được đánh dấu `Chờ kiểm thử` hoặc `Chờ điền`, và mỗi finding sau này phải liên kết với ảnh chụp cùng timestamp submit form.

Một điểm yếu khác là AI có thể gắn vấn đề usability với nguồn tham khảo nghe có vẻ đúng nhưng chưa thật sự chính xác. Nhóm đã sửa điều này trong checklist chung bằng cách đổi các reference Norman chưa chặt, thêm mục EN/VI và Rich-Text editor, đồng thời giải thích vì sao AI bỏ sót các chi tiết đó.

Bài học chính là nên dùng AI như trợ lý tạo cấu trúc, prompt và kiểm tra tính nhất quán, còn sinh viên vẫn chịu trách nhiệm về bằng chứng, severity, wording cuối cùng và tính trung thực của bài nộp.
