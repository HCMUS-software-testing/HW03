# Cross-Browser / Cross-Platform Matrix - Scenario A

## 1. Thông tin chung

| Trường | Nội dung |
| --- | --- |
| Sinh viên | Lê Mai Hoài Bảo |
| MSSV | 23127326 |
| Scenario | A - Admin creates and manages events |
| Màn hình | A1 Events list, A2 Add/Edit Event, A3 Registration & Roles |
| Công cụ | Playwright 1.59.1 và Selenium WebDriver 4.35 trên BrowserStack Automate |
| Email overlay duy nhất | `23127326@student.hcmus.edu.vn` |
| Ngày chạy | 2026-08-04 |

## 2. Coverage bắt buộc theo đề

Mỗi màn hình dùng cùng năm ô CP-01 đến CP-05. Tổ hợp được chọn bao phủ đủ từng dimension mà không cần chạy tích Descartes 3 x 5 x 3.

| Dimension | Yêu cầu | Coverage thực tế trên mỗi màn hình | Kết quả |
| --- | --- | --- | --- |
| Operating systems | Ít nhất 3 OS | Windows, macOS, Android | Đủ |
| Browsers | Ít nhất 5 browsers | Edge, Safari, Firefox, Samsung Internet, Chrome | Đủ |
| Device classes | Desktop, tablet, phone | Desktop, phone, tablet | Đủ |
| Screens | Ít nhất 3 màn hình | A1, A2, A3 | Đủ |
| Screenshot | Một ảnh thật cho mỗi cell | 15/15 ảnh; overlay chỉ có email sinh viên theo yêu cầu | Đủ |

> `Samsung Internet` là lựa chọn thay thế `Opera/Samsung Internet` cho browser thứ năm theo mẫu Task 3. API BrowserStack Automate của tài khoản chỉ cung cấp Opera 12.x, không phù hợp để kiểm thử EMS hiện đại. Thông tin OS/device mobile được đối soát từ capability BrowserStack trong phiên chạy.

## 3. Ma trận chi tiết

### 3.1 A1 - Events list with status filters and notification dots

| Cell ID | OS | Browser | Device class | Device/Version | URL | Overlay | Result | Screenshot | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A1-CP-01 | Windows 11 | Edge 150 | Desktop | BrowserStack 1280x720 | `/dashboard/admin/events` | Đúng email | Pass | [Ảnh](screenshots/task3/a1-cp-01-windows-edge-desktop.png) | Nội dung/marker có mặt; không redirect; overflow 0 px. |
| A1-CP-02 | macOS Sequoia | Safari 18.4 | Desktop | BrowserStack, viewport rộng 1324 px | `/dashboard/admin/events` | Đúng email | Pass | [Ảnh](screenshots/task3/a1-cp-02-macos-safari-desktop.png) | Nội dung/marker có mặt; không redirect; overflow 0 px. |
| A1-CP-03 | macOS Sequoia | Firefox 151 | Desktop | BrowserStack 1280x720 | `/dashboard/admin/events` | Đúng email | Pass | [Ảnh](screenshots/task3/a1-cp-03-macos-firefox-desktop.png) | Nội dung/marker có mặt; không redirect; overflow 0 px. |
| A1-CP-04 | Android 14 | Samsung Internet 29 | Phone | Samsung Galaxy S24 | `/dashboard/admin/events` | Đúng email | **Fail** | [Ảnh](screenshots/task3/a1-cp-04-android-samsung-internet-phone.png) | Thanh bên và nội dung không co theo phone; overflow ngang 664 px. |
| A1-CP-05 | Android 16 | Chrome 149 | Tablet | Galaxy Tab S11, landscape 1204x579 | `/dashboard/admin/events` | Đúng email | Pass | [Ảnh](screenshots/task3/a1-cp-05-android-chrome-tablet.png) | Nội dung/marker có mặt; không redirect; overflow 0 px. |

### 3.2 A2 - Add/Edit Event form

| Cell ID | OS | Browser | Device class | Device/Version | URL | Overlay | Result | Screenshot | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A2-CP-01 | Windows 11 | Edge 150 | Desktop | BrowserStack 1280x720 | `/dashboard/admin/events/create` | Đúng email | Pass | [Ảnh](screenshots/task3/a2-cp-01-windows-edge-desktop.png) | Form/marker có mặt; không redirect; overflow 0 px. |
| A2-CP-02 | macOS Sequoia | Safari 18.4 | Desktop | BrowserStack, viewport rộng 1324 px | `/dashboard/admin/events/create` | Đúng email | Pass | [Ảnh](screenshots/task3/a2-cp-02-macos-safari-desktop.png) | Form/marker có mặt; không redirect; overflow 0 px. |
| A2-CP-03 | macOS Sequoia | Firefox 151 | Desktop | BrowserStack 1280x720 | `/dashboard/admin/events/create` | Đúng email | Pass | [Ảnh](screenshots/task3/a2-cp-03-macos-firefox-desktop.png) | Form/marker có mặt; không redirect; overflow 0 px. |
| A2-CP-04 | Android 14 | Samsung Internet 29 | Phone | Samsung Galaxy S24 | `/dashboard/admin/events/create` | Đúng email | **Fail** | [Ảnh](screenshots/task3/a2-cp-04-android-samsung-internet-phone.png) | Form bị ép hẹp/cắt chữ và phải cuộn ngang; overflow 156 px. |
| A2-CP-05 | Android 16 | Chrome 149 | Tablet | Galaxy Tab S11, landscape 1204x579 | `/dashboard/admin/events/create` | Đúng email | Pass | [Ảnh](screenshots/task3/a2-cp-05-android-chrome-tablet.png) | Form/marker có mặt; không redirect; overflow 0 px. |

### 3.3 A3 - Registration & Roles configuration panel

| Cell ID | OS | Browser | Device class | Device/Version | URL | Overlay | Result | Screenshot | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A3-CP-01 | Windows 11 | Edge 150 | Desktop | BrowserStack 1280x720 | `/dashboard/admin/events/edit?id=114` | Đúng email | Pass | [Ảnh](screenshots/task3/a3-cp-01-windows-edge-desktop.png) | Registration marker có mặt; không redirect; overflow 0 px. |
| A3-CP-02 | macOS Sequoia | Safari 18.4 | Desktop | BrowserStack, viewport rộng 1324 px | `/dashboard/admin/events/edit?id=114` | Đúng email | Pass | [Ảnh](screenshots/task3/a3-cp-02-macos-safari-desktop.png) | Registration marker có mặt; không redirect; overflow 0 px. |
| A3-CP-03 | macOS Sequoia | Firefox 151 | Desktop | BrowserStack 1280x720 | `/dashboard/admin/events/edit?id=114` | Đúng email | Pass | [Ảnh](screenshots/task3/a3-cp-03-macos-firefox-desktop.png) | Registration marker có mặt; không redirect; overflow 0 px. |
| A3-CP-04 | Android 14 | Samsung Internet 29 | Phone | Samsung Galaxy S24 | `/dashboard/admin/events/edit?id=114` | Đúng email | **Fail** | [Ảnh](screenshots/task3/a3-cp-04-android-samsung-internet-phone.png) | Panel/form bị cắt và phải cuộn ngang; overflow 216 px. |
| A3-CP-05 | Android 16 | Chrome 149 | Tablet | Galaxy Tab S11, landscape 1204x579 | `/dashboard/admin/events/edit?id=114` | Đúng email | Pass | [Ảnh](screenshots/task3/a3-cp-05-android-chrome-tablet.png) | Registration marker có mặt; không redirect; overflow 0 px. |

## 4. Compatibility defects

| ID | Cell ID | Màn hình | Mô tả lỗi | Expected | Actual | Severity | Screenshot | Form timestamp |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- |
| CP-BUG-001 | A1-CP-04 | A1 | Layout danh sách sự kiện không responsive trên phone Samsung Internet. | Navigation và vùng danh sách vừa viewport hoặc chuyển sang bố cục mobile mà không cần cuộn ngang toàn trang. | Sidebar chiếm phần lớn chiều rộng, nội dung bên phải bị cắt; overflow ngang 664 px. | 3 | [Ảnh](screenshots/task3/a1-cp-04-android-samsung-internet-phone.png) | Chờ sinh viên gửi; nội dung tại `task3_form_entries.md`. |
| CP-BUG-002 | A2-CP-04 | A2 | Form tạo sự kiện bị ép hẹp/cắt nội dung trên phone Samsung Internet. | Trường, nhãn và khu vực upload xuống hàng/co giãn trong viewport phone. | Nội dung bị cắt và yêu cầu cuộn ngang; overflow 156 px. | 3 | [Ảnh](screenshots/task3/a2-cp-04-android-samsung-internet-phone.png) | Chờ sinh viên gửi; nội dung tại `task3_form_entries.md`. |
| CP-BUG-003 | A3-CP-04 | A3 | Panel Registration & Roles không responsive trên phone Samsung Internet. | Panel và điều khiển hiển thị đủ trong viewport phone, không cuộn ngang toàn trang. | Panel/form bị cắt; overflow ngang 216 px. | 3 | [Ảnh](screenshots/task3/a3-cp-04-android-samsung-internet-phone.png) | Chờ sinh viên gửi; nội dung tại `task3_form_entries.md`. |

## 5. Kết luận compatibility

- Đã chạy đủ **15/15 cells**: 5 môi trường cho từng màn hình A1, A2, A3.
- Tổng kết: **12 Pass, 3 Fail**. Edge/Windows desktop, Safari/macOS desktop, Firefox/macOS desktop và Chrome/Android tablet đều đạt các kiểm tra nội dung, redirect và overflow.
- Ba Fail đều nằm ở Samsung Internet/Android phone và thể hiện cùng một rủi ro responsive ở cả ba màn hình. Vì ma trận không có Chrome/phone cùng kích thước, kết luận an toàn là lỗi xảy ra trong tổ hợp CP-04; chưa đủ dữ liệu để khẳng định chỉ do browser hay chỉ do breakpoint phone.
- Khuyến nghị ưu tiên: thu gọn sidebar thành drawer ở breakpoint phone, bỏ chiều rộng tối thiểu/fixed width gây tràn, cho form/grid xuống một cột và bổ sung regression test ở viewport phone.
