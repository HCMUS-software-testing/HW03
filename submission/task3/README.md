# Task 3 - Cross-Browser / Cross-Platform cho Scenario D

| Trường | Giá trị |
| --- | --- |
| Sinh viên | Lê Trung Kiên |
| MSSV | `23127075` |
| Email overlay dùng trong screenshot | `23127075@clc.fitus.edu.vn` |
| Scenario | D - User requests Support and Admin resolves it |
| SUT | `https://prod-dev.ems-fitus.cloud` |
| Nguồn yêu cầu | `docs/2026.HW03.GUI Usability EMS_En.md`, `docs/HW03_EMS_Intro_EN.md`, `submission/HW03_step_by_step_guide.md` |
| Nguồn checklist nền | `submission/group/gui_usability_checklist_final.md` |
| Tài khoản test | `submission/test_environment_access.md` |

## 1. Mục tiêu Task 3

Task 3 kiểm tra ba màn hình đã chọn của Scenario D trên nhiều OS, browser và loại thiết bị để phát hiện lỗi tương thích giao diện như vỡ layout, tràn nội dung, overlap, text khó đọc, control không thao tác được hoặc hành vi khác nhau giữa browser.

Task này không thay thế Task 1B. Task 1B là chạy checklist GUI/usability sâu trên từng màn hình; Task 3 dùng cùng màn hình và checklist nền nhưng tập trung vào tính tương thích khi đổi môi trường chạy.

Matrix hiện tại dùng `5` cell cho mỗi màn hình, tổng `15` screenshot thật. Bộ cell này vẫn phủ đủ `3 OS`, `5 browser/platform`, và `3 device class` cho từng screen theo yêu cầu đề.

## 2. Màn hình cần test

| Screen ID | Màn hình | Vai trò | URL/đường dẫn cần mở | Trạng thái đại diện cần chụp |
| --- | --- | --- | --- | --- |
| D1 | User tạo support request có đính kèm ảnh | User | `https://prod-dev.ems-fitus.cloud/complaints/new` | Form hiển thị request type, issue, detailed description, upload zone và action buttons. |
| D2 | User My Requests list/detail có phản hồi | User | `https://prod-dev.ems-fitus.cloud/complaints` và một detail của Kiên, ví dụ `/complaints/56` nếu còn tồn tại | List có request của Kiên; detail có status, attachment và `Support response`. |
| D3 | Admin Support Requests list, Pending/Resolved tabs và search/filter | Admin | `https://prod-dev.ems-fitus.cloud/dashboard/admin/complaints` | Pending tab, Resolved tab hoặc trạng thái filter/search có request của Kiên. |

Nếu dữ liệu cũ bị reset, tạo request mới bằng user account của Kiên trước, rồi dùng admin account để kiểm tra D3.

## 3. Yêu cầu bằng chứng

Mỗi ô trong matrix phải có screenshot thật. Screenshot cần thấy đủ:

| Thành phần | Bắt buộc |
| --- | --- |
| EMS URL | Phải thấy URL đang mở, ví dụ `https://prod-dev.ems-fitus.cloud/...`. |
| Browser/OS/device identity | Ưu tiên chụp bằng TestingBot Live để thấy tên thiết bị, OS và browser trong giao diện TestingBot. |
| Overlay sinh viên | Phải có `23127075@clc.fitus.edu.vn` trên màn hình EMS. |
| Màn hình đúng | Screenshot phải thể hiện đúng D1, D2 hoặc D3 theo matrix. |
| Lỗi nếu có | Nếu cell Fail, ảnh phải chụp đúng vấn đề: overflow, overlap, text unreadable, control không bấm được, sai responsive layout, hoặc lỗi render. |

## 4. File trong thư mục này

| File | Mục đích |
| --- | --- |
| `task3_checklist_scope.md` | Xác định subset checklist Task 1A nên dùng cho compatibility và các mục N/A hợp lý. |
| `matrix_template.md` | Matrix D1-D2-D3 với `5` cell/màn hình để điền kết quả thật và screenshot ref. |
| `screenshot_protocol.md` | Quy trình chụp ảnh trên TestingBot, cách đặt overlay và naming convention. |
| `cross_platform_report_template.md` | Template report Task 3 để đưa vào main report. |
| `task3_findings_log_template.md` | Template log defect/usability riêng cho Task 3, dùng để đồng bộ với Google Form và aggregated log chung. |
| `screenshots/README.md` | Quy ước lưu ảnh Task 3. |

## 5. Thứ tự làm đề xuất

1. Mở `matrix_template.md` và chạy lần lượt từng cell cho D1, D2, D3.
2. Với mỗi cell, đăng nhập đúng account, mở đúng màn hình, đặt overlay email, chụp screenshot trên TestingBot.
3. Đánh dấu `Pass` nếu layout và thao tác chính dùng được; đánh dấu `Fail` nếu có lỗi tương thích.
4. Với mỗi `Fail`, ghi defect vào `task3_findings_log_template.md`, submit Google Form, rồi copy entry vào aggregated findings log chung của bài.
5. Tổng hợp kết quả cuối vào `cross_platform_report_template.md`.
