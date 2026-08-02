# Test Environment Access

File này dùng để lưu thông tin truy cập EMS cho các task AI-first/manual testing. Chỉ dùng tài khoản test hoặc mật khẩu tạm; không commit thông tin nhạy cảm nếu repository được chia sẻ công khai.

## Web URL

| Field | Value |
| --- | --- |
| EMS URL mới | `https://prod-dev.ems-fitus.cloud` |
| Ghi chú môi trường | `Link production-dev mới thay cho link ngrok cũ đã hỏng. Playwright đã xác nhận mở được trang login ngày 2026-08-02.` |

## Accounts

### User Account

Tài khoản này dùng cho Scenario D màn hình `D1` và `D2`.

| Field | Value |
| --- | --- |
| Email / Username / MSSV | `ltkien23@clc.fitus.edu.vn` |
| Password | `Nothing2k@5` |
| Role | `User` |
| Ghi chú | `Playwright đã xác nhận đăng nhập thành công và vào được /dashboard. Chỉ dùng để tạo support request và kiểm tra My Requests của chính tài khoản này.` |

### Admin Account

Tài khoản này dùng cho Scenario D màn hình `D3`.

| Field | Value |
| --- | --- |
| Email / Username | `admin@gmail.com` |
| Password | `Admin@123` |
| Role | `Admin` |
| Ghi chú | `Theo docs/2026.HW03.GUI Usability EMS_En.md. Playwright đã xác nhận đăng nhập thành công, menu hiển thị Admin dashboard và Support requests.` |

## Testing Rules

1. Khi test trang admin, nếu có thao tác CRUD tài khoản user, chỉ được thao tác trên tài khoản user của Kiên được cung cấp trong file này.
2. Không sửa, khóa, reset mật khẩu, xóa, đổi role hoặc thay đổi dữ liệu cá nhân của tài khoản người khác.
3. Nếu cần dữ liệu để test admin, ưu tiên tạo dữ liệu mới bằng tài khoản user của Kiên rồi xử lý bằng tài khoản admin.
4. Trước mọi thao tác có thể ảnh hưởng dữ liệu thật, ghi rõ mục đích test và chụp/sao lưu bằng chứng trạng thái trước khi thao tác.
5. Nếu không chắc một thao tác có ảnh hưởng tới tài khoản người khác hay không, dừng lại và hỏi lại trước khi thực hiện.

## Scenario D Scope

| ID | Screen | Role | Intended Use |
| --- | --- | --- | --- |
| D1 | User - create support request form with image attachment | User | Tạo support request test bằng tài khoản user của Kiên. |
| D2 | User - My Requests list/detail with response | User | Kiểm tra danh sách, chi tiết, trạng thái và phản hồi chính thức của request thuộc tài khoản Kiên. |
| D3 | Admin - Support Requests list, Pending/Resolved tabs, search | Admin | Tìm và xử lý support request test do tài khoản Kiên tạo; không thao tác dữ liệu người khác. |
