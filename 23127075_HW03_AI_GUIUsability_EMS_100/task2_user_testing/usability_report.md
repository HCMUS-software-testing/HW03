# Task 2 - Usability Report

| Trường | Giá trị |
| --- | --- |
| Người thực hiện | Lê Trung Kiên |
| MSSV | `23127075` |
| Scenario | D - User requests Support and Admin resolves it |
| Màn hình | D1, D2, D3 |
| SUT | `https://prod-dev.ems-fitus.cloud` |
| Method | Moderated user testing, think-aloud, SUS |
| Nguồn dữ liệu | `session_notes/P01_session_notes.md` đến `session_notes/P05_session_notes.md` |

## 1. Scenario Và Mục Tiêu Test

```text
Bạn đang dùng hệ thống EMS của khoa. Bạn gặp một vấn đề khi tham gia hoặc đăng ký sự kiện và muốn gửi yêu cầu hỗ trợ kèm ảnh minh chứng.

Hãy gửi một yêu cầu hỗ trợ, sau đó kiểm tra lại yêu cầu của mình trong danh sách support requests và cho biết bạn thấy trạng thái/phản hồi ở đâu.
```

Phần admin D3:

```text
Sau khi trải nghiệm phía user, hãy dùng màn hình admin đã được chuẩn bị để tìm request theo tiêu đề, member code, category hoặc trạng thái, rồi cho biết bạn tìm thấy request ở tab nào.
```

Mục tiêu đánh giá:

- Người dùng có tạo được support request có ảnh minh chứng không.
- Người dùng có hiểu required fields, category, validation và trạng thái submit không.
- Người dùng có tìm lại request và hiểu status/response trong My Requests không.
- Người xử lý hoặc observer có tìm đúng support request trong admin list bằng search/filter/status không.
- Người dùng có cảm thấy luồng user/admin nhất quán và đủ tin cậy không.

## 2. Pilot

| Trường | Giá trị |
| --- | --- |
| Pilot participant | Không có file pilot riêng trong thư mục nộp |
| Ngày giờ | Không có evidence riêng |
| Vấn đề phát hiện trong protocol | Không đủ dữ liệu để kết luận từ folder `session_notes` |
| Điều chỉnh trước 5 sessions chính | Không ghi nhận trong artifact hiện có |

Ghi chú: 5 phiên chính có dữ liệu đầy đủ, nhưng phần pilot là khoảng trống bằng chứng cần bổ sung nếu giảng viên yêu cầu kiểm tra riêng.

## 3. Participants

Tham chiếu file: `participant_table.md`.

| ID | Họ tên | Số điện thoại đã mask | Device/browser | Session date/time | Consent |
| --- | --- | --- | --- | --- | --- |
| P01 | Võ Trung Hiếu | `0365****99` | Windows 11 - Chrome | `2026-08-03 12:12` | Yes |
| P02 | Nguyễn Hoàng Danh | `0909****76` | Windows 11 - Edge | `2026-08-04 21:36` | Yes |
| P03 | Nguyễn Hữu Anh Trí | `0947****02` | Windows 11 - Edge | `2026-08-04 22:31` | Yes |
| P04 | Trần Hoài Thiện Nhân | `0702****41` | Windows 11 - Chrome | `2026-08-05 14:20` | Yes |
| P05 | Nguyễn Trần Thiên Phú | `0948****45` | Windows 11 - Chrome | `2026-08-05 20:28` | Yes |

## 4. Metrics

| Participant | Success | Time on task | Errors | Hesitations | SUS score | Key friction |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| P01 | Completed | 10:48 | 0 | 3 | 82.5 | Tìm request ở phía admin chậm hơn mong đợi; request description bị tràn chữ. |
| P02 | Completed | 03:43 | 2 | 3 | 85.0 | Bị lẫn giữa luồng support phía user và trang quản trị; tab trạng thái chưa đủ nổi bật. |
| P03 | Completed | 05:14 | 0 | 2 | 75.0 | Form tạo request làm chậm nhất; bố cục bảng/filter admin giảm khả năng quét thông tin. |
| P04 | Completed | 03:01 | 2 | 3 | 82.5 | Chậm ở D3 do lẫn giữa support request phía user và trang xử lý của admin. |
| P05 | Completed | 01:50 | 2 | 3 | 50.0 | Admin navigation còn lẫn với luồng user; status filter dễ bị hiểu như card tổng quan; giao diện user/admin chưa đồng nhất. |
| **Summary** | Success rate: 5/5 = 100% | Mean: 04:55 | Total/mean: 6 / 1.2 | Total/mean: 14 / 2.8 | Mean: 75.0 | Luồng hoàn tất được, nhưng D3 tạo nhiều nhầm lẫn hơn D1-D2. |

## 5. Observation Summary

| Theme | Evidence from sessions | Related screen | Related Task 1B finding nếu có |
| --- | --- | --- | --- |
| Nhầm lẫn giữa support request phía user và khu vực admin | P02, P04, P05 đều bị lẫn khi đăng nhập bằng admin hoặc khi chọn menu support request. | D3 | Liên quan nhóm finding D3 về navigation/search/filter. |
| `Pending`/`Resolved` chưa được nhận diện như tab/filter có thể thao tác | P02 không để ý có 2 tab; P03 không nhận ra tab switch; P05 thấy filter status dễ gây nhầm. | D3 | Liên quan F-D3-001/F-D3-002 nếu dùng nhóm finding Task 1B về admin filter/status. |
| Tính nhất quán user/admin chưa tốt | P05 nhận xét sidebar user sáng, sidebar admin tối; P04 ghi nhận label `My Support Requests` trong admin không nhất quán. | D2/D3 | N/A hoặc nhóm consistency của Task 1B. |
| Feedback và trạng thái ghi nhận request nhìn chung đủ tin cậy | P01, P02, P03, P04, P05 đều tin request đã được ghi nhận nhờ trạng thái `Pending`, request nằm trong danh sách hoặc đúng thời gian/nội dung. | D1/D2 | N/A |
| Một số chi tiết form/list làm giảm tốc độ hoặc khả năng đọc | P04 thấy caret/focus form chưa rõ; P01 thấy description dài bị tràn; P03 góp ý cột `REQUEST` rộng và date range nên tách hàng. | D1/D3 | Liên quan nhóm form/layout Task 1B. |

## 6. Ranked Usability Findings

Severity dùng thang `0-4`.

| Severity | Ý nghĩa |
| ---: | --- |
| 0 | Không phải vấn đề |
| 1 | Cosmetic hoặc minor annoyance |
| 2 | Minor usability issue, có workaround |
| 3 | Major issue, gây chậm hoặc lỗi đáng kể |
| 4 | Critical issue, chặn task hoặc gây mất dữ liệu |

| ID | Screen | Type | Description | Evidence | Severity | Suggested fix | Screenshot/recording ref | Submit Google Form? |
| --- | --- | --- | --- | --- | ---: | --- | --- | --- |
| UT-D-001 | D3 | Usability | Admin vẫn nhìn thấy/đi vào các lựa chọn support request mang tính user, làm participant lẫn giữa danh sách request cá nhân và khu vực xử lý request của admin. | P02, P04, P05 đều ghi nhận nhầm luồng admin/user. | 2 | Tách rõ menu admin và user; đổi label admin thành `Admin Support Requests`; ẩn hoặc phân nhóm các mục user khi đang ở admin context. | `../findings/defect-screenshots/UT-D-001_admin-user-navigation-confusion.png` | No |
| UT-D-002 | D3 | Usability | `Pending`/`Resolved` chưa đủ affordance như tab/filter, khiến participant không nhận ra ngay có thể chuyển trạng thái hoặc hiểu nhầm là card tổng quan. | P02 không để ý có 2 tab; P03 không nhận ra tab switch; P05 nói filter status dễ gây nhầm. | 2 | Thiết kế lại thành segmented control/tab rõ ràng, đặt gần nhóm filter và hiển thị active state mạnh hơn. | `../findings/defect-screenshots/UT-D-002_pending-resolved-tab-affordance.png` | No |
| UT-D-003 | D3 | Usability | Request description chứa chuỗi dài không tự xuống dòng, bị tràn ngang khỏi khung nội dung và giảm khả năng đọc khi xử lý request. | P01 ghi nhận nội dung request description bị tràn ra ngoài. | 2 | Áp dụng `word-break`/`overflow-wrap`, giới hạn chiều rộng cột và cho phép xem đầy đủ trong detail/modal. | `../findings/defect-screenshots/UT-D-003_request-description-overflow.png` | No |
| UT-D-004 | D1 | Usability | Khi click vào field của form tạo support request, caret/focus chưa đủ rõ, làm participant không chắc field đã sẵn sàng nhập. | P04 ghi nhận con trỏ không nhấp nháy rõ từ đầu; P02 cũng nhắc màu field làm khó thấy dấu nháy. | 1 | Tăng contrast focus ring/caret, dùng border rõ hơn khi input active. | `../findings/defect-screenshots/UT-D-004_form-focus-caret-weak.png` | No |
| UT-D-005 | D3 | Usability | Bố cục bảng admin dành nhiều chiều rộng cho cột `REQUEST`, trong khi date range/filter chưa được nhóm trực quan, làm giảm khả năng quét và lọc request. | P03 nhận xét cột `REQUEST` khá rộng và filter date range nên để một hàng mới. | 1 | Cân lại width các cột, gom filter theo hàng/cụm rõ ràng và giữ nhãn filter gần control. | `../findings/defect-screenshots/UT-D-005_admin-table-filter-layout.png` | No |
| UT-D-006 | D2/D3 | Usability | Control `Rows per page` xuất hiện nhưng participant ghi nhận số lượng dòng mỗi trang bị cố định ở cả user/admin, làm giảm cảm giác kiểm soát khi danh sách dài. | P03 ghi nhận rows per page bị fixed. | 1 | Nếu không cho đổi số dòng thì ẩn control; nếu có control thì cho chọn các giá trị hợp lệ. | `../findings/defect-screenshots/UT-D-006_rows-per-page-fixed.png` | No |
| UT-D-007 | D2/D3 | Usability | Giao diện user/admin chưa đồng nhất về màu sắc và sidebar, khiến hai khu vực có cảm giác thuộc hai hệ giao diện khác nhau. | P05 ghi nhận sidebar user sáng, sidebar admin tối và layout user/admin không đồng nhất. | 1 | Chuẩn hóa design token/layout giữa dashboard user và admin, chỉ dùng khác biệt màu sắc để thể hiện role khi có chủ đích. | `../findings/defect-screenshots/UT-D-007_user-admin-visual-inconsistency.png` | No |

## 7. Recommendations

| Priority | Recommendation | Addresses | Expected impact |
| ---: | --- | --- | --- |
| 1 | Tách rõ navigation giữa role user và admin, đổi nhãn support request trong admin thành nhãn quản trị nhất quán. | UT-D-001, UT-D-007 | Giảm nhầm luồng ở D3, cải thiện tốc độ tìm request cho admin/observer. |
| 2 | Thiết kế lại `Pending`/`Resolved` thành tab/filter rõ ràng, active state nổi bật và đặt cùng ngữ cảnh với bộ lọc. | UT-D-002 | Giúp participant nhận ra ngay request đang nằm ở trạng thái nào và cách chuyển trạng thái. |
| 3 | Sửa khả năng đọc bảng admin: wrap description dài, cân lại cột `REQUEST`, nhóm filter/date range trực quan. | UT-D-003, UT-D-005 | Tăng scanability khi xử lý nhiều support request. |
| 4 | Cải thiện micro-interaction của form và list controls: focus state rõ, caret dễ thấy, `Rows per page` hoạt động hoặc được ẩn. | UT-D-004, UT-D-006 | Giảm do dự nhỏ trong D1/D2/D3, tăng cảm giác kiểm soát. |

## 8. Evidence Index

| Evidence ID | Path/link | Description |
| --- | --- | --- |
| UT-E-001 | `session_notes/P01_session_notes.md` | Raw notes P01, SUS `82.5`. |
| UT-E-002 | `session_notes/P02_session_notes.md` | Raw notes P02, SUS `85.0`. |
| UT-E-003 | `session_notes/P03_session_notes.md` | Raw notes P03, SUS `75.0`. |
| UT-E-004 | `session_notes/P04_session_notes.md` | Raw notes P04, SUS `82.5`. |
| UT-E-005 | `session_notes/P05_session_notes.md` | Raw notes P05, SUS `50.0`. |
| UT-D-001 | `../findings/defect-screenshots/UT-D-001_admin-user-navigation-confusion.png` | Ảnh đại diện cho nhầm lẫn navigation user/admin. |
| UT-D-002 | `../findings/defect-screenshots/UT-D-002_pending-resolved-tab-affordance.png` | Ảnh đại diện cho affordance yếu của `Pending`/`Resolved`. |
| UT-D-003 | `../findings/defect-screenshots/UT-D-003_request-description-overflow.png` | Ảnh đại diện cho description dài bị tràn. |
| UT-D-004 | `../findings/defect-screenshots/UT-D-004_form-focus-caret-weak.png` | Ảnh đại diện cho focus/caret field form chưa rõ. |
| UT-D-005 | `../findings/defect-screenshots/UT-D-005_admin-table-filter-layout.png` | Ảnh đại diện cho bố cục bảng/filter admin. |
| UT-D-006 | `../findings/defect-screenshots/UT-D-006_rows-per-page-fixed.png` | Ảnh đại diện cho control `Rows per page`. |
| UT-D-007 | `../findings/defect-screenshots/UT-D-007_user-admin-visual-inconsistency.png` | Ảnh đại diện cho thiếu nhất quán visual user/admin. |

## 9. Form/Log Consistency

| Check | Status |
| --- | --- |
| Mỗi usability/bug finding mới đã submit Google Form nếu thuộc phạm vi Task 2 | Chưa xác nhận từ dữ liệu trong folder; các session notes đang ghi `No`. |
| `../findings/bug_usability_findings_log.md` đã cập nhật findings Task 2 | Cần đối chiếu với aggregated findings log trước khi nộp cuối. |
| Số lượng findings trong report khớp số lượng form submissions | Chưa xác nhận vì không có timestamp Google Form trong Task 2 folder. |

## 10. Kết Luận

Luồng Scenario D nhìn chung hoàn tất được với `5/5` participant thành công và SUS trung bình `75.0`, tức mức chấp nhận được. D1-D2 tương đối dễ hiểu nhờ trạng thái `Pending` và request mới xuất hiện trong danh sách, giúp người dùng tin rằng hệ thống đã ghi nhận thao tác.

Rủi ro usability chính nằm ở D3: participant nhiều lần lẫn giữa support request phía user và khu vực admin, đồng thời `Pending`/`Resolved` chưa đủ rõ như tab/filter thao tác được. Nhóm cải tiến ưu tiên là tách navigation theo vai trò, làm rõ status filter, và cải thiện khả năng đọc/quét của bảng admin.
