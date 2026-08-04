# Ma trận kiểm thử đa nền tảng cho Kịch bản C

| Trường           | Giá trị                       |
| ---------------- | ----------------------------- |
| Sinh viên        | Lâm Hữu Khánh - 23127205      |
| Kịch bản         | C - Admin quản lý người dùng  |
| Overlay trên ảnh | 23127205@student.hcmus.edu.vn |
| Công cụ chính    | BrowserStack                  |

## Tổng quan phạm vi bao phủ (Scope Overview)

Ma trận áp dụng đồng nhất cho cả 3 màn hình (C1, C2, C3) với **5 môi trường tổ hợp đại diện** cho mỗi màn hình (tổng cộng 15 cells), đảm bảo bao phủ 100% các tiêu chí yêu cầu của đề bài:

- **3 Hệ điều hành (OS):** `Windows 11`, `macOS (Sonoma)`, `Android`.
- **5 Trình duyệt (Browsers):** `Google Chrome`, `Microsoft Edge`, `Opera`, `Mozilla Firefox`, `Samsung Internet`.
- **3 Lớp thiết bị (Device Classes):**
  - **Desktop:** `1920x1080` (Win Chrome), `1366x768` (Win Edge), `1440x900` (macOS Opera).
  - **Phone:** `375x667` (Android Firefox Phone).
  - **Tablet:** `768x1024` (Android Samsung Internet Tablet).

## C1 Danh sách người dùng

| Hệ điều hành | Trình duyệt      | Lớp thiết bị | Thiết bị/profile | Kết quả | Ảnh minh chứng                                                        | Ghi chú                                                                                   |
| ------------ | ---------------- | ------------ | ---------------- | ------- | --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Windows 11   | Chrome           | Desktop      | 1920x1080        | Pass    | `submission/screenshots/cross-platform/C1_win_chrome_desktop.png`     | Hiển thị chuẩn admin layout 1440px+                                                       |
| Windows 11   | Edge             | Desktop      | 1366x768         | Pass    | `submission/screenshots/cross-platform/C1_win_edge_desktop.png`       | Bố cục bảng và phân trang hiển thị ổn định                                                |
| macOS        | Opera            | Desktop      | 1440x900         | Pass    | `submission/screenshots/cross-platform/C1_macos_opera_desktop.png`    | Font và màu sắc hiển thị đúng chuẩn Opera trên macOS                                      |
| Android      | Firefox          | Phone        | 375x667          | Fail    | `submission/screenshots/cross-platform/C1_android_firefox_phone.png`  | **Lỗi UI:** Bảng danh sách bị tràn viền, ẩn các cột dữ liệu chính (Bug `C-F001`)          |
| Android      | Samsung Internet | Tablet       | 768x1024         | Fail    | `submission/screenshots/cross-platform/C1_android_samsung_tablet.png` | **Lỗi UI:** Bố cục bảng bị lệch cột và rách phân trang trên Android Tablet (Bug `C-F001`) |

## C2 Gán vai trò / chỉnh sửa người dùng

| Hệ điều hành | Trình duyệt      | Lớp thiết bị | Thiết bị/profile | Kết quả | Ảnh minh chứng                                                        | Ghi chú                                                                    |
| ------------ | ---------------- | ------------ | ---------------- | ------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Windows 11   | Chrome           | Desktop      | 1920x1080        | Pass    | `submission/screenshots/cross-platform/C2_win_chrome_desktop.png`     | Dialog Edit User hiển thị 2 cột chuẩn                                      |
| Windows 11   | Edge             | Desktop      | 1366x768         | Pass    | `submission/screenshots/cross-platform/C2_win_edge_desktop.png`       | Input và dropdown phản hồi đúng trên Edge                                  |
| macOS        | Opera            | Desktop      | 1440x900         | Pass    | `submission/screenshots/cross-platform/C2_macos_opera_desktop.png`    | Form gán vai trò hiển thị mượt trên Opera                                  |
| Android      | Firefox          | Phone        | 375x667          | Fail    | `submission/screenshots/cross-platform/C2_android_firefox_phone.png`  | **Lỗi UI:** Form dialog tràn quá chiều rộng màn hình mobile (Bug `C-F003`) |
| Android      | Samsung Internet | Tablet       | 768x1024         | Pass    | `submission/screenshots/cross-platform/C2_android_samsung_tablet.png` | Form dialog gán vai trò trên tablet hiển thị vừa vặn, chuẩn xác            |

## C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu

| Hệ điều hành | Trình duyệt      | Lớp thiết bị | Thiết bị/profile | Kết quả | Ảnh minh chứng                                                        | Ghi chú                                                                                   |
| ------------ | ---------------- | ------------ | ---------------- | ------- | --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Windows 11   | Chrome           | Desktop      | 1920x1080        | Fail    | `submission/screenshots/cross-platform/C3_win_chrome_desktop.png`     | **Lỗi tính năng:** Thiếu chức năng Chặn/Bỏ chặn & Reset Password (Bug `C-F012`, `C-F013`) |
| Windows 11   | Edge             | Desktop      | 1366x768         | Fail    | `submission/screenshots/cross-platform/C3_win_edge_desktop.png`       | **Lỗi tính năng:** Thiếu chức năng Chặn/Bỏ chặn & Reset Password (Bug `C-F012`, `C-F013`) |
| macOS        | Opera            | Desktop      | 1440x900         | Fail    | `submission/screenshots/cross-platform/C3_macos_opera_desktop.png`    | **Lỗi tính năng:** Thiếu chức năng Chặn/Bỏ chặn & Reset Password (Bug `C-F012`, `C-F013`) |
| Android      | Firefox          | Phone        | 375x667          | Fail    | `submission/screenshots/cross-platform/C3_android_firefox_phone.png`  | **Lỗi tính năng:** Thiếu chức năng Chặn/Bỏ chặn & Reset Password (Bug `C-F012`, `C-F013`) |
| Android      | Samsung Internet | Tablet       | 768x1024         | Fail    | `submission/screenshots/cross-platform/C3_android_samsung_tablet.png` | **Lỗi tính năng:** Thiếu chức năng Chặn/Bỏ chặn & Reset Password (Bug `C-F012`, `C-F013`) |

## Kiểm tra độ bao phủ

| Màn hình | Đủ 3 hệ điều hành | Đủ 5 trình duyệt | Đủ 3 lớp thiết bị | Đã kiểm tra overlay ảnh |
| -------- | ----------------- | ---------------- | ----------------- | ----------------------- |
| C1       | Đạt               | Đạt              | Đạt               | Đạt                     |
| C2       | Đạt               | Đạt              | Đạt               | Đạt                     |
| C3       | Đạt               | Đạt              | Đạt               | Đạt                     |
