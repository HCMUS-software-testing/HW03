# Prompt AI cho checklist GUI dùng chung

## Prompt 1 - Tạo bản nháp checklist

```text
[@superpowers](plugin://superpowers@openai-api-curated) Tạo một danh sách kiểm tra (checklist) tính khả dụng của GUI (GUI usability) để kiểm thử ứng dụng web Hệ thống Quản lý Sự kiện (Event Management System).
Danh sách kiểm tra phải có hơn 40 mục và bao gồm:
- IA-01 Các tiêu chuẩn UI chung,
- IA-02 Biểu mẫu,
- IA-03 Điều hướng,
- IA-04 Phản hồi và trạng thái hệ thống.
Xây dựng danh sách kiểm tra dựa trên các nguyên tắc Heuristic của Nielsen, các nguyên lý của Norman, và 8 quy tắc vàng của Shneiderman.
Trả kết quả dưới dạng bảng Markdown với các cột: ID, Khía cạnh giao diện, Mục kiểm tra, Tiêu chuẩn đối chiếu, Lý do.
Output sẽ nằm trong folder submission. Nhớ trích nguồn tham khảo.
```

## Tóm tắt review thủ công

Nhóm đã review bản nháp AI, loại bỏ hoặc sửa reference yếu, đồng thời thêm các mục đặc thù EMS mà AI chưa nhấn mạnh đủ.

| Checklist ID | Hành động của nhóm | Vì sao AI bỏ sót hoặc viết chưa đủ cụ thể |
| --- | --- | --- |
| IA-01-02 | Giữ và nhấn mạnh thuật ngữ nghiệp vụ EMS | AI có nhắc thuật ngữ, nhưng nhóm xác nhận tiêu chí này đặc biệt quan trọng vì EMS có nhiều vai trò và nhiều nhãn liên quan đến sự kiện |
| IA-01-04 | Thêm Nielsen visibility of system status | AI xem màu trạng thái chủ yếu là tính nhất quán; nhóm bổ sung góc nhìn visibility of system status |
| IA-01-06 | Đổi reference Norman sang conceptual model | Thứ tự ưu tiên thông tin trên card liên quan đến cách người dùng hiểu cấu trúc nội dung |
| IA-01-13 | Thêm mục chuyển đổi ngôn ngữ EN/VI | Prompt ban đầu chưa ép AI bao phủ i18n thật chi tiết |
| IA-02-10 | Đổi reference Norman sang signifiers | Giá trị mặc định và gợi ý nhập liệu đóng vai trò tín hiệu hướng dẫn thao tác |
| IA-02-13 | Thêm mục Rich-Text editor | EMS có rich-text trong tạo/sửa sự kiện, nhưng AI chưa bao phủ rủi ro paste formatting hoặc hiển thị HTML thô |
| IA-04-04 | Bỏ reference Norman yếu | Reference này không phải nguyên lý Norman cụ thể mà nhóm dùng để đối chiếu |
| IA-04-07 | Bỏ reference Norman yếu | Empty state phù hợp hơn với Nielsen help/documentation |
| IA-04-13 | Thêm mục closure cho quy trình dài | AI tập trung vào toast/trạng thái riêng lẻ và bỏ sót điểm kết thúc rõ ràng của toàn luồng |
