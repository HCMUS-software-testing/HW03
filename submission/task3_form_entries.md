# Nội dung điền Google Form cho Task 3

Mỗi defect bên dưới là **một lần gửi form riêng**. Không gửi lỗi khởi tạo BrowserStack/Playwright vì đó không phải lỗi của EMS. Sau khi gửi, chép timestamp nhận được vào `cross_platform_matrix.md` và `bug_usability_findings_log.md`.

## CP-BUG-001 - A1 Events list

| Câu hỏi trên form | Nội dung cần điền |
| --- | --- |
| Tốc độ tải trang của hệ thống như thế nào? | **Bình thường** |
| Trong quá trình sử dụng, bạn có gặp lỗi nào không? | **Có** |
| Nếu có, vui lòng mô tả lỗi bạn gặp phải. | `[CP-BUG-001][Task 3][A1-CP-04] Trên Samsung Galaxy S24, Android 14, Samsung Internet 29 (Phone), màn hình Events list không responsive. Expected: navigation và danh sách vừa viewport hoặc chuyển sang bố cục mobile, không cần cuộn ngang toàn trang. Actual: sidebar chiếm phần lớn chiều rộng, vùng nội dung bên phải bị cắt và page-level horizontal overflow là 664 px. Severity: 3.` |
| Hình ảnh/video lỗi | `submission/screenshots/task3/a1-cp-04-android-samsung-internet-phone.png` |
| Điều bạn thích nhất ở hệ thống EMS là gì? | `Màn hình tải được đầy đủ nội dung và luồng Events hoạt động ổn trên các môi trường desktop và tablet đã kiểm thử.` |
| Điều gì khiến bạn chưa hài lòng khi sử dụng EMS? | `Bố cục phone không thu gọn sidebar và làm nội dung danh sách bị cắt, buộc người dùng cuộn ngang.` |
| Bạn mong muốn EMS bổ sung hoặc cải thiện tính năng nào? | `Thêm breakpoint phone: chuyển sidebar thành drawer/hamburger, bỏ fixed/min-width gây tràn và bảo đảm danh sách vừa chiều rộng viewport.` |

- Thời điểm gửi biểu mẫu: **22:44 ngày 05/08/2026**

## CP-BUG-002 - A2 Add Event form

| Câu hỏi trên form | Nội dung cần điền |
| --- | --- |
| Tốc độ tải trang của hệ thống như thế nào? | **Bình thường** |
| Trong quá trình sử dụng, bạn có gặp lỗi nào không? | **Có** |
| Nếu có, vui lòng mô tả lỗi bạn gặp phải. | `[CP-BUG-002][Task 3][A2-CP-04] Trên Samsung Galaxy S24, Android 14, Samsung Internet 29 (Phone), form Create Event không responsive. Expected: nhãn, trường nhập và khu vực upload co giãn/xuống hàng trong viewport phone. Actual: form bị ép hẹp, chữ và điều khiển bị cắt, phải cuộn ngang; page-level horizontal overflow là 156 px. Severity: 3.` |
| Hình ảnh/video lỗi | `submission/screenshots/task3/a2-cp-04-android-samsung-internet-phone.png` |
| Điều bạn thích nhất ở hệ thống EMS là gì? | `Form có các nhóm thông tin rõ ràng và hiển thị ổn trên Edge, Safari, Firefox desktop và Chrome tablet trong ma trận.` |
| Điều gì khiến bạn chưa hài lòng khi sử dụng EMS? | `Ở phone, các cột và khu vực upload không xuống hàng đúng cách nên nội dung khó đọc và khó thao tác.` |
| Bạn mong muốn EMS bổ sung hoặc cải thiện tính năng nào? | `Đổi form/grid sang một cột ở breakpoint phone, cho text và upload area co giãn theo 100% viewport, đồng thời loại bỏ min-width gây tràn.` |

- Thời điểm gửi biểu mẫu: **22:46 ngày 05/08/2026**

## CP-BUG-003 - A3 Registration & Roles

| Câu hỏi trên form | Nội dung cần điền |
| --- | --- |
| Tốc độ tải trang của hệ thống như thế nào? | **Bình thường** |
| Trong quá trình sử dụng, bạn có gặp lỗi nào không? | **Có** |
| Nếu có, vui lòng mô tả lỗi bạn gặp phải. | `[CP-BUG-003][Task 3][A3-CP-04] Trên Samsung Galaxy S24, Android 14, Samsung Internet 29 (Phone), panel Registration & Roles trong trang Edit Event không responsive. Expected: panel và các điều khiển vừa viewport phone, không cuộn ngang toàn trang. Actual: panel/form bị cắt và page-level horizontal overflow là 216 px. Severity: 3.` |
| Hình ảnh/video lỗi | `submission/screenshots/task3/a3-cp-04-android-samsung-internet-phone.png` |
| Điều bạn thích nhất ở hệ thống EMS là gì? | `Các nhóm cấu hình Registration & Roles vẫn tải đủ và hoạt động ổn trên các môi trường desktop/tablet đã kiểm thử.` |
| Điều gì khiến bạn chưa hài lòng khi sử dụng EMS? | `Trên phone, vùng cấu hình bị cắt và yêu cầu cuộn ngang nên khó đọc, đối chiếu và chỉnh các tùy chọn.` |
| Bạn mong muốn EMS bổ sung hoặc cải thiện tính năng nào? | `Cho panel chuyển sang một cột trên phone, dùng width/max-width responsive và thêm regression test cho các breakpoint mobile.` |

- Thời điểm gửi biểu mẫu: **22:48 ngày 05/08/2026**
