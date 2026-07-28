# Protocol kiểm thử người dùng cho Kịch bản C

## Mục tiêu

Đánh giá liệu admin có thể tìm và quản lý tài khoản người dùng trong EMS một cách hiệu quả hay không, bao gồm chỉnh vai trò, chặn/bỏ chặn, đặt lại mật khẩu và nhận biết phản hồi xác nhận.

## Tiêu chí người tham gia

Tuyển 5 người dùng thật ngoài lớp. Người tham gia không cần có kinh nghiệm với EMS, nhưng nên quen với các ứng dụng web thông thường. Thông tin liên hệ phải được che một phần trong báo cáo.

## Pilot

Chạy 1 phiên pilot trước 5 phiên chính thức. Nếu người tham gia hiểu sai cách diễn đạt nhiệm vụ, chỉnh lại wording trước khi thu dữ liệu chính thức.

## Kịch bản nhiệm vụ

Đọc nội dung sau cho từng người tham gia:

```text
Bạn là admin của EMS. Có một yêu cầu hỗ trợ cần bạn tìm người dùng mục tiêu, kiểm tra trạng thái tài khoản, thay đổi vai trò nếu cần, chặn/bỏ chặn người dùng hoặc đặt lại mật khẩu, rồi xác nhận xem hệ thống đã hoàn tất thao tác hay chưa.
```

Không đưa hướng dẫn từng cú click. Yêu cầu người tham gia think-aloud trong lúc thao tác.

## Dữ liệu cần thu thập

| Chỉ số | Quy tắc ghi nhận |
| --- | --- |
| Mức hoàn thành | Hoàn thành; hoàn thành với trợ giúp; thất bại |
| Thời gian thực hiện | Bắt đầu khi người tham gia thao tác; kết thúc khi thấy xác nhận/trạng thái cuối |
| Lỗi | Bấm nhầm, hiểu sai, gửi dữ liệu không hợp lệ, lặp thao tác nguy hiểm |
| Do dự | Dừng hoặc thể hiện không chắc chắn ít nhất 3 giây |
| SUS | Thu 10 câu trả lời từ 1 hoàn toàn không đồng ý đến 5 hoàn toàn đồng ý |
| Câu hỏi mở | Hỏi về độ rõ ràng, độ tin cậy, khả năng phục hồi và tốc độ |

## Cách tính SUS

Với câu lẻ, điểm đóng góp là `score - 1`. Với câu chẵn, điểm đóng góp là `5 - score`. Cộng toàn bộ điểm đóng góp và nhân `2.5`.

## Câu hỏi sau nhiệm vụ

1. Phần nào trong luồng quản lý tài khoản làm bạn thấy chưa rõ?
2. Các thông báo xác nhận có khiến bạn tin rằng thao tác đã thành công không?
3. Bạn muốn thay đổi điều gì để thao tác chỉnh vai trò hoặc đặt lại mật khẩu an toàn hơn?
4. Bạn đã do dự ở đâu và vì sao?
