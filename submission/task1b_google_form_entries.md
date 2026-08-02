# Các mục Task 1B sẵn sàng nhập Google Form cho Bảo

## Trạng thái gửi

- Sinh viên: Lê Mai Hoài Bảo (MSSV 23127326)
- Email sinh viên: **Bảo phải nhập/xác nhận email sinh viên thật; không tìm thấy email trong kho mã nguồn.**
- Kịch bản: A — Quản trị viên tạo và quản lý sự kiện
- Hệ thống đã kiểm thử: `https://prod-dev.ems-fitus.cloud/`
- Ngày kiểm thử: 2026-08-02 (Asia/Ho_Chi_Minh)
- Bản nháp được giữ lại: `23127326_TASK1B_20260802_163308`, mã sự kiện 80; không xuất bản hoặc xóa
- Google Form: https://forms.gle/CJQFQCAXcsDbXDMM9
- Trạng thái gửi bên ngoài: **Chưa thực hiện. Bảo vẫn kiểm soát việc gửi.**
- Thời điểm gửi biểu mẫu: **Chờ đồng bộ sau khi Bảo gửi.**

Trước khi gửi, Bảo phải nhập email sinh viên thật, mở từng ảnh minh chứng và xác nhận tên trường trên Google Form khớp với các giá trị dưới đây. Sau mỗi phản hồi, thay thời điểm đang chờ trong tệp này và `bug_usability_findings_log.md` bằng thời điểm nhận thực tế.

## Các mục đã chuẩn bị

### T1B-A1-01

- Màn hình: A1 Danh sách sự kiện
- Loại: Tính khả dụng
- Mã checklist: IA-03-06, IA-04-07
- Mô tả: Trạng thái tìm kiếm rỗng không có hành động đặt lại/xóa bộ lọc.
- Các bước: Mở `Events`; nhập truy vấn không khớp sự kiện nào; quan sát trạng thái rỗng.
- Kết quả mong đợi: Trạng thái rỗng giải thích kết quả và có hành động `Reset`/xóa bộ lọc trực tiếp.
- Kết quả thực tế: Thông báo giải thích không có sự kiện phù hợp nhưng không có hành động xóa truy vấn/bộ lọc.
- Mức độ nghiêm trọng: 2 — Trung bình
- Đề xuất khắc phục: Thêm nút `Reset filters` nổi bật trong trạng thái rỗng và trả tiêu điểm về ô tìm kiếm sau khi đặt lại.
- Ảnh minh chứng: `screenshots/task1b/a1-f01-empty-no-reset.png`
- Tác vụ nguồn: Task 1B
- Thời điểm gửi biểu mẫu: Chờ đồng bộ sau khi Bảo gửi

### T1B-A1-03

- Màn hình: A1 Danh sách sự kiện
- Loại: Tính khả dụng
- Mã checklist: IA-01-10
- Mô tả: Bảng sự kiện yêu cầu cuộn ngang trong cửa sổ Safari 1171×768.
- Các bước: Mở `Events` trong cửa sổ Safari 1171×768; quan sát bảng và cạnh dưới.
- Kết quả mong đợi: Các cột và hành động cốt lõi hiển thị mà không cần cuộn ngang không cần thiết trong cửa sổ máy tính có kích thước gọn.
- Kết quả thực tế: Bảng rộng tràn ngang, che các cột/hành động phía sau cho đến khi người dùng cuộn ngang.
- Mức độ nghiêm trọng: 2 — Trung bình
- Đề xuất khắc phục: Ưu tiên cột cốt lõi, cho phép xuống dòng có kiểm soát và chuyển dữ liệu phụ sang phần chi tiết ở chiều rộng hẹp.
- Ảnh minh chứng: `screenshots/task1b/a1-overview.png`
- Tác vụ nguồn: Task 1B
- Thời điểm gửi biểu mẫu: Chờ đồng bộ sau khi Bảo gửi

### T1B-A1-04

- Màn hình: A1 Danh sách sự kiện
- Loại: Lỗi
- Mã checklist: IA-01-13
- Mô tả: Bảng thông báo tiếng Anh còn văn bản tiếng Việt chưa dịch.
- Các bước: Giữ giao diện ở tiếng Anh; mở `Notifications`; đọc các thông báo.
- Kết quả mong đợi: Toàn bộ nội dung thông báo dùng ngôn ngữ tiếng Anh đã chọn.
- Kết quả thực tế: Bảng hiển thị `Phản hồi khiếu nại` trong khi phần giao diện xung quanh là tiếng Anh.
- Mức độ nghiêm trọng: 1 — Nhẹ
- Đề xuất khắc phục: Đưa mọi mẫu thông báo qua cùng tài nguyên bản địa hóa và bổ sung kiểm thử hồi quy EN/VI.
- Ảnh minh chứng: `screenshots/task1b/a1-f04-notification-mixed-language.png`
- Tác vụ nguồn: Task 1B
- Thời điểm gửi biểu mẫu: Chờ đồng bộ sau khi Bảo gửi

### T1B-A1-05

- Màn hình: A1 Danh sách sự kiện
- Loại: Tính khả dụng
- Mã checklist: IA-01-07
- Mô tả: Hành động sự kiện chỉ có biểu tượng không hiển thị chú giải khi có tiêu điểm.
- Các bước: Di chuyển tiêu điểm bàn phím tới hành động chỉ có biểu tượng; dừng tại phần tử; quan sát phần giải thích trực quan.
- Kết quả mong đợi: Hành động chỉ có biểu tượng hiển thị nhãn/chú giải rõ khi di chuột hoặc có tiêu điểm.
- Kết quả thực tế: Biểu tượng `Delete` có viền tiêu điểm nhưng không hiển thị nhãn/chú giải.
- Mức độ nghiêm trọng: 2 — Trung bình
- Đề xuất khắc phục: Thêm tên hỗ trợ truy cập bền vững và chú giải được kích hoạt bằng cả di chuột lẫn tiêu điểm bàn phím.
- Ảnh minh chứng: `screenshots/task1b/a1-f05-action-focus-no-tooltip.png`
- Tác vụ nguồn: Task 1B
- Thời điểm gửi biểu mẫu: Chờ đồng bộ sau khi Bảo gửi

### T1B-A1-06

- Màn hình: A1 Danh sách sự kiện
- Loại: Lỗi
- Mã checklist: IA-03-03, IA-03-09
- Mô tả: Trạng thái tìm kiếm/bộ lọc bị mất sau khi mở sự kiện và quay lại.
- Các bước: Tìm bản nháp Task 1B có tên duy nhất; mở chi tiết; dùng nút `Back` của trình duyệt.
- Kết quả mong đợi: Danh sách `Events` khôi phục truy vấn, các dòng đã lọc và vị trí danh sách trước đó.
- Kết quả thực tế: Toàn bộ danh sách trở lại với ô tìm kiếm bị xóa.
- Mức độ nghiêm trọng: 2 — Trung bình
- Đề xuất khắc phục: Lưu trạng thái truy vấn/bộ lọc/trang trong URL hoặc trạng thái điều hướng và khôi phục khi quay lại.
- Ảnh minh chứng: trước `screenshots/task1b/a1-f05-action-focus-no-tooltip.png`; sau `screenshots/task1b/a1-f06-filter-not-retained.png`
- Tác vụ nguồn: Task 1B
- Thời điểm gửi biểu mẫu: Chờ đồng bộ sau khi Bảo gửi

### T1B-A2-01

- Màn hình: A2 Thêm/Sửa sự kiện
- Loại: Lỗi
- Mã checklist: IA-02-12
- Mô tả: Phần tải ảnh `Thumbnail` chấp nhận tệp `.txt` như một ảnh.
- Các bước: Mở biểu mẫu Thêm/Sửa sự kiện; chọn `upload_invalid.txt` trong phần `Thumbnail`; quan sát phần xem trước.
- Kết quả mong đợi: Tệp không phải ảnh bị từ chối trước khi xem trước/tải lên và có thông báo kiểm tra hợp lệ cụ thể.
- Kết quả thực tế: Tệp `.txt` được chấp nhận và phần xem trước bị hỏng hiển thị mà không có lỗi.
- Mức độ nghiêm trọng: 2 — Trung bình
- Đề xuất khắc phục: Giới hạn bộ chọn tệp và kiểm tra MIME, chữ ký tệp, phần mở rộng và kích thước trước khi tạo phần xem trước.
- Ảnh minh chứng: `screenshots/task1b/a2-f01-invalid-thumbnail-accepted.png`
- Tác vụ nguồn: Task 1B
- Thời điểm gửi biểu mẫu: Chờ đồng bộ sau khi Bảo gửi

### T1B-A2-02

- Màn hình: A2 Thêm/Sửa sự kiện
- Loại: Lỗi
- Mã checklist: IA-02-11, IA-03-09
- Mô tả: Rời biểu mẫu chỉnh sửa đã có dữ liệu không có cảnh báo thay đổi chưa lưu và làm mất tiêu đề chưa lưu.
- Các bước: Đổi tiêu đề trong biểu mẫu chỉnh sửa; dùng `Back` trước khi lưu; quan sát điều hướng và ngữ cảnh chỉnh sửa bị xóa.
- Kết quả mong đợi: Ứng dụng yêu cầu xác nhận và giữ thay đổi chưa lưu cho đến khi người dùng chọn hủy bỏ rõ ràng.
- Kết quả thực tế: Điều hướng xảy ra ngay, không có cảnh báo; tiêu đề chưa lưu bị mất.
- Mức độ nghiêm trọng: 3 — Nghiêm trọng
- Đề xuất khắc phục: Theo dõi trạng thái biểu mẫu đã thay đổi và hiển thị hộp thoại xác nhận cho điều hướng trong ứng dụng/trình duyệt.
- Ảnh minh chứng: trước `screenshots/task1b/a2-f02-unsaved-before.png`; sau `screenshots/task1b/a2-f02-unsaved-after-no-warning.png`
- Tác vụ nguồn: Task 1B
- Thời điểm gửi biểu mẫu: Chờ đồng bộ sau khi Bảo gửi

### T1B-A2-03

- Màn hình: A2 Thêm/Sửa sự kiện
- Loại: Tính khả dụng
- Mã checklist: IA-01-07
- Mô tả: Các nút chỉ có biểu tượng `Back`, `Thumbnail` và `Banner` không có nhãn/chú giải khi di chuột hoặc dùng bàn phím; biểu tượng soạn thảo văn bản có chú giải.
- Các bước: Mở biểu mẫu chỉnh sửa đã giữ lại; di chuột trên `Back` và các nút máy ảnh; dùng bàn phím đưa tiêu điểm tới nút máy ảnh `Thumbnail` rồi dừng lại.
- Kết quả mong đợi: Mọi hành động chỉ có biểu tượng cung cấp nhãn/chú giải rõ khi di chuột và có tiêu điểm.
- Kết quả thực tế: `Back` và các nút máy ảnh `Thumbnail`/`Banner` không hiển thị nhãn/chú giải trong các trạng thái đã kiểm thử.
- Mức độ nghiêm trọng: 2 — Trung bình
- Đề xuất khắc phục: Thêm tên hỗ trợ truy cập và chú giải kích hoạt bằng di chuột/tiêu điểm, hoặc thêm nhãn hiển thị.
- Ảnh minh chứng: `screenshots/task1b/a2-icon-hover-back-no-tooltip.png`; `screenshots/task1b/a2-icon-keyboard-focus-unlabeled-camera.png`; `screenshots/task1b/a2-icon-hover-thumbnail-camera-no-tooltip.png`; `screenshots/task1b/a2-icon-hover-banner-camera-no-tooltip.png`
- Tác vụ nguồn: Task 1B
- Thời điểm gửi biểu mẫu: Chờ đồng bộ sau khi Bảo gửi

### T1B-A3-01

- Màn hình: A3 Đăng ký và vai trò
- Loại: Lỗi
- Mã checklist: IA-02-04
- Mô tả: `Max Slots` vẫn hoạt động khi bật `Is Unlimited`.
- Các bước: Bật `Student Registration`; bật `Is Unlimited`; kiểm tra và chỉnh sửa `Max Slots`.
- Kết quả mong đợi: Khi không giới hạn số lượng, điều khiển `Max Slots` mâu thuẫn phải bị vô hiệu hóa, xóa hoặc ẩn.
- Kết quả thực tế: `Max Slots` vẫn hiển thị và chỉnh sửa được khi `Is Unlimited` đang bật.
- Mức độ nghiêm trọng: 2 — Trung bình
- Đề xuất khắc phục: Vô hiệu hóa và xóa `Max Slots` khi bật `Is Unlimited`; chỉ khôi phục khi tắt `Is Unlimited`.
- Ảnh minh chứng: `screenshots/task1b/a3-f01-unlimited-max-slots-active.png`
- Tác vụ nguồn: Task 1B
- Thời điểm gửi biểu mẫu: Chờ đồng bộ sau khi Bảo gửi

### T1B-A3-03

- Màn hình: A3 Đăng ký và vai trò
- Loại: Lỗi
- Mã checklist: IA-02-04
- Mô tả: `Waitlist` vẫn bật sau khi tắt `Student Registration`.
- Các bước: Bật `Student Registration` và `Waitlist`; tắt `Student Registration`; quan sát `Waitlist`.
- Kết quả mong đợi: Khi tắt chế độ đăng ký cha, trạng thái `Waitlist` phụ thuộc phải bị vô hiệu hóa hoặc xóa.
- Kết quả thực tế: Các điều khiển vai trò `Student` biến mất nhưng `Waitlist` vẫn bật.
- Mức độ nghiêm trọng: 3 — Nghiêm trọng
- Đề xuất khắc phục: Xóa/vô hiệu hóa `Waitlist` khi `Student Registration` tắt và kiểm tra lại khi lưu.
- Ảnh minh chứng: `screenshots/task1b/a3-f03-waitlist-with-student-off.png`
- Tác vụ nguồn: Task 1B
- Thời điểm gửi biểu mẫu: Chờ đồng bộ sau khi Bảo gửi

### T1B-A3-04

- Màn hình: A3 Đăng ký và vai trò
- Loại: Lỗi
- Mã checklist: IA-02-11, IA-03-09
- Mô tả: Thay đổi chưa lưu trong `Registration & Roles` bị mất mà không có cảnh báo.
- Các bước: Đổi `Reminder` từ 24 thành 25; dùng `Back` mà không lưu; mở lại bản nháp.
- Kết quả mong đợi: Ứng dụng cảnh báo trước khi điều hướng và giữ thay đổi cho đến khi người dùng chọn hủy bỏ rõ ràng.
- Kết quả thực tế: Điều hướng quay về `Events` ngay; khi mở lại, giá trị đã lưu là 24, nên giá trị 25 chưa lưu bị mất.
- Mức độ nghiêm trọng: 3 — Nghiêm trọng
- Đề xuất khắc phục: Thêm cơ chế bảo vệ biểu mẫu đã thay đổi dùng chung, bao quát trạng thái vai trò/tùy chọn lồng nhau và điều hướng trong ứng dụng/trình duyệt.
- Ảnh minh chứng: `screenshots/task1b/a3-unsaved-reminder-25-before-back.png`; `screenshots/task1b/a3-unsaved-back-no-warning-destination.png`; `screenshots/task1b/a3-unsaved-reopen-reminder-24-persisted.png`
- Tác vụ nguồn: Task 1B
- Thời điểm gửi biểu mẫu: Chờ đồng bộ sau khi Bảo gửi
