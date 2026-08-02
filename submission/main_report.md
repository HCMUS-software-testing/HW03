# HW03 - Kiểm thử GUI và tính khả dụng trên EMS

## 1. Thông tin sinh viên và scenario

| Trường                  | Giá trị                                                                                                                   |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| MSSV                    | 23127205                                                                                                                  |
| Họ và tên               | Lâm Hữu Khánh                                                                                                             |
| Kịch bản                | Kịch bản C - Admin quản lý người dùng                                                                                     |
| Hệ thống kiểm thử       | https://prod-dev.ems-fitus.cloud/dashboard                                                                                |
| Tài khoản admin sử dụng | admin@gmail.com                                                                                                           |
| Màn hình kiểm thử       | C1 Danh sách người dùng; <br />C2 Gán vai trò / chỉnh sửa người dùng; <br />C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu |

Kịch bản C được chọn để đánh giá luồng công việc của admin khi tìm người dùng, thay đổi vai trò, kiểm soát trạng thái tài khoản, đặt lại mật khẩu và xác nhận giao diện có cung cấp phản hồi đủ rõ cho các thao tác quản trị rủi ro hay không.

## 2. Tóm tắt checklist GUI dùng chung

Checklist nhóm được lưu tại `submission/group/gui_usability_checklist_final.md`.

| Mục                        | Kết quả                                                                                            |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| Số mục checklist           | 52                                                                                                 |
| Bao phủ IA                 | IA-01 Tiêu chuẩn UI chung; IA-02 Biểu mẫu; IA-03 Điều hướng; IA-04 Phản hồi và trạng thái hệ thống |
| Nguồn chính                | 10 heuristic của Nielsen; nguyên lý thiết kế của Norman; 8 quy tắc vàng của Shneiderman            |
| Minh chứng quá trình       | `submission/group/gui_usability_checklist_processing.md`                                           |
| Minh chứng prompt AI       | `submission/group/ai_prompts.md`                                                                   |
| Minh chứng nguồn tham khảo | `submission/group/references.md`                                                                   |

## 3. Thực thi checklist

Artifact thực thi: `submission/checklist_execution_scenario_c.md`.

| Màn hình                                      | Mục đích kiểm thử                                                                                                             | Trạng thái                                                                   |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| C1 Danh sách người dùng                       | Kiểm tra độ dễ đọc của danh sách, bộ lọc, cột vai trò/trạng thái hoạt động, tìm kiếm, phân trang, trạng thái rỗng/tải dữ liệu | Chờ thực thi trên EMS thật                                                   |
| C2 Gán vai trò / chỉnh sửa người dùng         | Kiểm tra nhãn form, điều khiển vai trò, hợp lệ hóa, luồng lưu/hủy và phản hồi                                                 | Đã thực thi bằng Playwright trên`https://prod-dev.ems-fitus.cloud/dashboard` |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | Kiểm tra xác nhận, nội dung cảnh báo thao tác rủi ro, đường hủy thao tác, phản hồi thành công/lỗi và khả năng truy vết audit  | Chờ thực thi trên EMS thật                                                   |

Mỗi checklist item bị `Fail` phải có đường dẫn ảnh chụp màn hình và mã finding tương ứng trong `submission/bug_usability_findings_log.md`.

## 4. Báo cáo user testing

Protocol và template được lưu trong `submission/user-testing/`.

Kịch bản nhiệm vụ cho người tham gia:

> Bạn là admin của EMS. Hãy tìm một người dùng mục tiêu, kiểm tra thông tin người dùng, thay đổi vai trò nếu cần, chặn/bỏ chặn người dùng hoặc đặt lại mật khẩu, rồi xác nhận từ giao diện xem thao tác đã thành công hay chưa.

Các chỉ số cần thu thập:

| Chỉ số                  | Mô tả                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------- |
| Mức hoàn thành nhiệm vụ | Hoàn thành, hoàn thành với trợ giúp, hoặc thất bại                                    |
| Thời gian thực hiện     | Tính từ khi người tham gia bắt đầu thao tác đến khi thấy xác nhận/trạng thái kết thúc |
| Lỗi                     | Bấm nhầm, hiểu sai, gửi dữ liệu không hợp lệ, lặp lại thao tác                        |
| Do dự                   | Dừng lại hoặc thể hiện không chắc chắn ít nhất 3 giây                                 |
| SUS                     | 10 câu hỏi System Usability Scale, tính theo hệ số 2.5 chuẩn                          |
| Câu hỏi mở              | Nhận xét về độ rõ ràng, độ tin cậy, khả năng phục hồi lỗi và tốc độ                   |

Các finding đã xếp hạng và đề xuất cải thiện sẽ được hoàn thiện sau 5 phiên người dùng thật.

## 5. Báo cáo cross-browser / cross-platform

Ma trận kiểm thử: `submission/cross-platform/matrix.md`.

Bao phủ tối thiểu cho mỗi màn hình:

| Chiều kiểm thử      | Yêu cầu                                    |
| ------------------- | ------------------------------------------ |
| Hệ điều hành        | Windows, macOS hoặc iOS, Android           |
| Trình duyệt         | Chrome, Firefox, Safari, Edge, Opera       |
| Lớp thiết bị        | Desktop, tablet, phone                     |
| Minh chứng ảnh chụp | Có URL EMS và overlay`23127205@....edu.vn` |

BrowserStack hoặc LambdaTest nên là nguồn chụp chính. Thiết bị thật có thể dùng để bổ sung các ô còn thiếu.

## 6. Tóm tắt bug và usability findings

Log tổng hợp: `submission/bug_usability_findings_log.md`.

Tất cả finding từ checklist execution, user testing và cross-platform testing phải được submit lên Google Form và ghi vào log cục bộ với timestamp khớp nhau.

## 7. Agent skills

Các skill cục bộ được lưu trong `.agents/skills/`, kèm danh mục nộp bài tại `submission/agent-skills/skill_inventory.md`.

| Skill                              | Mục đích                                                                            |
| ---------------------------------- | ----------------------------------------------------------------------------------- |
| `ems-gui-checklist-runner`         | Chạy checklist EMS dùng chung trên một màn hình và sinh bảng execution cho Task 1B  |
| `ems-usability-report-writer`      | Chuyển ghi chú kiểm thử người dùng và điểm SUS thành usability findings đã xếp hạng |
| `ems-compatibility-matrix-builder` | Tạo hoặc kiểm tra ma trận cross-platform và phát hiện thiếu bao phủ                 |
| `ai-audit-entry`                   | Ghi thêm entry có đánh số vào báo cáo AI audit                                      |

## 8. Sử dụng AI

Báo cáo AI audit: `submission/ai-audit/ai_audit_report.md`.

AI critique: `submission/ai_critique.md`.

Sinh viên phải review mọi artifact do AI tạo trước khi nộp và tự hoàn thành các trường đánh giá, lý do và phần sinh viên chỉnh sửa trong báo cáo AI audit.

## 9. Git commit log

Artifact commit log: `submission/git_commit_log.txt`.

Các mốc commit đề xuất:

1. `docs: finalize shared GUI checklist evidence`
2. `test: add scenario C checklist execution`
3. `docs: add user testing protocol and raw notes`
4. `docs: add cross-platform matrix`
5. `docs: add findings log and AI audit`
6. `feat: add EMS GUI testing agent skills`

## 10. Phụ lục

| Artifact               | Đường dẫn                                    |
| ---------------------- | -------------------------------------------- |
| Ảnh lỗi checklist      | `submission/screenshots/checklist-failures/` |
| Ảnh usability findings | `submission/screenshots/usability-findings/` |
| Ảnh cross-platform     | `submission/cross-platform/screenshots/`     |
| Link video demo        | `submission/demo-videos.md`                  |
