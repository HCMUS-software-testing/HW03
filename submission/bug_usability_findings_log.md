# Bug & Usability Findings Log - Scenario A

## 1. Quy tắc ghi log

- Mỗi bug hoặc usability improvement trong Tasks 1-3 phải được submit lên Google Form: https://forms.gle/CJQFQCAXcsDbXDMM9
- File này phải khớp số lượng và nội dung với Google Form.
- Không ghi finding nếu chưa có bằng chứng thật từ EMS, user testing, hoặc cross-platform run.

## 2. Severity scale

| Severity | Ý nghĩa |
| ---: | --- |
| 0 | Cosmetic, không ảnh hưởng task |
| 1 | Minor, gây khó chịu nhẹ |
| 2 | Moderate, làm chậm hoặc gây nhầm lẫn đáng kể |
| 3 | Major, cản trở hoàn thành task với nhiều người dùng |
| 4 | Blocker, không thể hoàn thành task chính |

## 3. Log tổng hợp

| ID | Scenario/Screen | Type | Description | Steps/Heuristic | Expected | Actual | Severity | Suggested fix | Screenshot ref | Source task | Form-submission timestamp |
| --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- |
| UX-A1-001 | A1 Events list | Usability | Icon quan trọng trong cột Actions chưa có nhãn hiển thị trong ảnh chụp. | IA-01-07; mở Admin > Events Management và quan sát cột Actions. | Icon xem/sửa/cảnh báo/xóa có nhãn hoặc tooltip rõ nghĩa. | Các action chỉ hiển thị icon trong ảnh, chưa thấy nhãn hoặc tooltip. | 1 | Bổ sung tooltip rõ nghĩa hoặc nhãn accessible/visible cho từng icon action. | ![A1 ref](screenshots/A1.png) | Task 1B | [Chưa submit] |
| UX-A1-002 | A1 Events list | Usability | Nút điều hướng/action trong từng dòng chưa có tên gọi cụ thể ở trạng thái ảnh chụp. | IA-03-04; mở Admin > Events Management và quan sát các nút action của từng event. | Nút có tên cụ thể như View Details, Edit Event, Delete. | Cột Actions chỉ hiển thị icon, không có nhãn cụ thể trong trạng thái ảnh chụp. | 1 | Thêm tooltip/aria-label và cân nhắc nhãn text cho các action quan trọng. | ![A1 ref](screenshots/A1.png) | Task 1B | [Chưa submit] |
| UX-A1-003 | A1 Events list | Usability | Danh sách event chưa hiển thị phân trang, tổng số kết quả hoặc chỉ báo đã tải hết trong ảnh chụp. | IA-03-07; mở Admin > Events Management và quan sát cuối bảng danh sách event. | Danh sách dài có phân trang, tổng số kết quả hoặc trạng thái đã tải hết. | Ảnh không hiển thị phân trang, tổng số kết quả hoặc trạng thái đã tải hết. | 1 | Hiển thị pagination, tổng số event, hoặc thông báo đã tải hết danh sách. | ![A1 ref](screenshots/A1.png) | Task 1B | [Chưa submit] |
| UX-001 | A1/A2/A3 | Usability | [Mô tả vấn đề usability] | [Observation từ participant hoặc probe question] | [ ] | [ ] | [0-4] | [ ] | [screenshots/...] | Task 2 | [YYYY-MM-DD HH:mm] |
| CP-BUG-001 | A1/A2/A3 | Bug | [Mô tả lỗi compatibility] | [Cell ID trong cross-platform matrix] | [ ] | [ ] | [0-4] | [ ] | [screenshots/...] | Task 3 | [YYYY-MM-DD HH:mm] |

## 4. Đối soát với Google Form

| Tổng finding trong file | Tổng đã submit form | Chênh lệch | Ghi chú xử lý |
| ---: | ---: | ---: | --- |
| [ ] | [ ] | [ ] | [Nếu có chênh lệch, giải thích] |
