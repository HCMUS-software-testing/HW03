# Việc cần làm tiếp theo sau Task 1B

| Trường | Giá trị |
| --- | --- |
| Người thực hiện | Lê Trung Kiên |
| MSSV | `23127075` |
| Kịch bản | D - Người dùng gửi yêu cầu hỗ trợ và Admin xử lý |
| Màn hình đã chạy Task 1B | D1, D2, D3 |
| Nguồn Task 1B | `submission/task1B/task1b_D1.md`, `submission/task1B/task1b_D2.md`, `submission/task1B/task1b_D3.md` |
| Ngày lập checklist tiếp theo | 2026-08-03 |

## 1. Trạng thái hiện tại

Task 1B đã có đủ ba file thực thi checklist cho Scenario D:

| Màn hình | File | Findings cần xử lý tiếp |
| --- | --- | ---: |
| D1 - User tạo support request | `submission/task1B/task1b_D1.md` | 4 |
| D2 - User xem My Requests/detail | `submission/task1B/task1b_D2.md` | 3 |
| D3 - Admin xem Support Requests list | `submission/task1B/task1b_D3.md` | 3 |
| **Tổng** |  | **10** |

Các bảng `Draft finding cho Bug & Usability Log` trong từng file đã có đủ thông tin để review và copy sang Google Form: `ID`, màn hình, loại, mô tả, bước/heuristic, kỳ vọng, thực tế, severity, đề xuất sửa và ảnh tham chiếu.

## 2. Việc cần làm ngay với output Task 1B

| STT | Việc cần làm | Input từ Task 1B | Output cần có | Trạng thái |
| ---: | --- | --- | --- | --- |
| 1 | Review lại từng screenshot lỗi để chắc chắn finding mô tả đúng bằng chứng. | Screenshot trong `submission/screenshots/D1`, `submission/screenshots/D2`, `submission/screenshots/D3`, `submission/screenshots/checklist-failures` | Danh sách finding đã xác nhận hoặc loại bỏ | `[Chưa làm]` |
| 2 | Submit từng finding đã xác nhận lên Google Form của bài. | 10 draft findings trong D1-D3 | 10 form submissions hoặc số lượng thực tế sau khi review | `[Chưa làm]` |
| 3 | Ghi lại `Form-submission timestamp` cho từng finding. | Timestamp sau khi submit Google Form | Cột timestamp trong log tổng hợp và/hoặc file D1-D3 được điền | `[Chưa làm]` |
| 4 | Tạo/cập nhật aggregated log. | Các bảng draft findings D1-D3 | `submission/bug_usability_findings_log.md` có số lượng khớp Google Form | `[Chưa làm]` |
| 5 | Phân loại finding nào sẽ tái sử dụng trong Task 2 hoặc Task 3. | F-D1-001..F-D3-003 | Ghi chú trong usability report hoặc compatibility report nếu người dùng/cross-platform cũng gặp lại | `[Chưa làm]` |
| 6 | Commit riêng bước Task 1B và bug logging. | Các file Task 1B, screenshot, findings log | Git commit log có commit cho checklist execution và bug logging | `[Chưa làm]` |

## 3. Mapping 10 findings từ Task 1B sang Google Form/log

| ID | Screen | Type | Severity | Screenshot ref | Ghi chú khi submit |
| --- | --- | --- | ---: | --- | --- |
| F-D1-001 | D1 Tạo support request | Usability | 2 | `submission/screenshots/checklist-failures/F-D1-001_validation-not-inline.png` | Nhấn mạnh validation không inline và submit vẫn bật khi thiếu required fields. |
| F-D1-002 | D1 Tạo support request | Bug | 3 | `submission/screenshots/checklist-failures/F-D1-002_category-submit-400-no-clear-ui-error.png` | Nhấn mạnh mismatch giữa placeholder/default category và payload/API validation. |
| F-D1-003 | D1 Tạo support request | Usability | 2 | `submission/screenshots/checklist-failures/F-D1-003_cancel-discards-without-confirmation.png` | Nhấn mạnh mất dữ liệu form khi bấm `Cancel` không xác nhận. |
| F-D1-004 | D1 Tạo support request | Bug | 3 | `submission/screenshots/D1/D1_submit_success_redirect.png` | Nhấn mạnh success message sai ngữ cảnh support request. |
| F-D2-001 | D2 My Requests list/detail | Usability | 2 | `submission/screenshots/checklist-failures/F-D2-001_back-loses-filter-context.png` | Nhấn mạnh `Back` từ detail làm mất filter/search context. |
| F-D2-002 | D2 My Requests list/detail | Usability | 2 | `submission/screenshots/checklist-failures/F-D2-002_search-no-results-misleading-empty-state.png` | Nhấn mạnh no-result state dùng message `No requests yet` gây hiểu nhầm. |
| F-D2-003 | D2 My Requests list/detail | Usability | 2 | `submission/screenshots/checklist-failures/F-D2-003_mobile-floating-button-near-pagination.png` | Nhấn mạnh floating social button chồng sát vùng pagination/list trên mobile. |
| F-D3-001 | D3 Admin Support Requests list | Usability | 2 | `submission/screenshots/checklist-failures/F-D3-001_search-title-returns-extra-result.png` | Nhấn mạnh search theo title cụ thể trả thêm request không liên quan. |
| F-D3-002 | D3 Admin Support Requests list | Usability | 2 | `submission/screenshots/D3/D3_category_support_filter.png`, `submission/screenshots/checklist-failures/F-D3-002_tab-switch-loses-filter-context.png` | Nhấn mạnh đổi tab làm mất member-code/category filter context. |
| F-D3-003 | D3 Admin Support Requests list | Bug | 3 | `submission/screenshots/checklist-failures/F-D3-003_mobile-sidebar-overflow.png` | Nhấn mạnh mobile admin layout bị sidebar fixed làm content hẹp/khó đọc. |

## 4. Checklist trước khi chuyển sang Task 2

- [ ] Đã review 10 findings và loại bỏ finding nào không đủ bằng chứng nếu có.
- [ ] Đã submit Google Form cho từng finding được giữ lại.
- [ ] Đã ghi timestamp vào nơi tổng hợp.
- [ ] Đã tạo `submission/bug_usability_findings_log.md`.
- [ ] Số lượng findings trong log khớp số lượng form submissions.
- [ ] Các screenshot path trong log mở được.
- [ ] Đã ghi lại finding nào có thể dùng làm giả thuyết quan sát trong Task 2, ví dụ D1 cancel mất dữ liệu, D2 back mất filter, D2 empty state, D3 mobile layout.

## 5. Gợi ý dùng Task 1B để chuẩn bị Task 2

Task 2 không được dựa hoàn toàn vào đánh giá heuristic của tester. Tuy nhiên, findings từ Task 1B có thể dùng để chuẩn bị câu hỏi quan sát và probe sau phiên:

| Chủ đề từ Task 1B | Cách dùng trong Task 2 |
| --- | --- |
| D1 validation và category | Quan sát participant có hiểu request type/required fields không; không gợi ý trước lỗi. |
| D1 cancel mất dữ liệu | Quan sát participant có do dự khi rời form hoặc có mất nội dung đã nhập không. |
| D2 list/detail/filter | Quan sát participant có tìm lại request đã gửi và hiểu trạng thái `Pending`/`Resolved` không. |
| D2 empty/no-result state | Nếu participant search sai, ghi họ có hiểu là không có kết quả hay tưởng chưa từng có request. |
| D3 admin list/search/filter | Nếu Task 2 có vai trò admin hoặc người hỗ trợ, quan sát khả năng tìm đúng request bằng title/member code/category. |

Lưu ý: Khi chạy interview, không nói trước cho participant biết các lỗi đã tìm ở Task 1B. Hãy để họ thực hiện mục tiêu thật và ghi nhận nếu các vấn đề xuất hiện tự nhiên.
