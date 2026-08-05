# Task 1B - Thực thi checklist cho D3

| Trường | Giá trị |
| --- | --- |
| Người kiểm thử | Lê Trung Kiên |
| MSSV | `23127075` |
| Kịch bản | D - Người dùng gửi yêu cầu hỗ trợ và Admin xử lý |
| Màn hình | D3 - Admin xem danh sách Support Requests, tab Pending/Resolved và search |
| Vai trò sử dụng | Admin |
| SUT | `https://prod-dev.ems-fitus.cloud` |
| Ngày kiểm thử | 2026-08-03 |
| Nguồn checklist | `submission/group/gui_usability_checklist_final.md` |
| Có sửa checklist gốc không? | Không |

## 1. Prompt đầy đủ đã dùng để AI hỗ trợ test D3

```text
@Superpowers Đọc các file trong folder docs để hiểu bối cảnh bài tập. Thực hiện Task 1B cho Kiên trên Scene D3. Dùng submission/group/gui_usability_checklist_final.md (không thay đổi file này) để làm check list. Tạo 1 file markdown cho task1b_D3.md trong folder submission/task1B cho việc testing dựa trên checklist đó. Hãy tận dụng MCP Playwright và Chrome Devtools trong quá trình test. Thông tin link web, tài khoản admin và user đã được cung cấp trong submission/test_environment_access.md. Tuyệt đối tuân theo rule được ghi trong  submission/test_environment_access.md. Nếu cần thêm gì thì hãy yêu cầu tôi cung cấp. Format cho output của D3 cũng nên tương tự như D1 và D2.
```

## 2. Nhật ký kiểm thử

| Bước | Công cụ | Quan sát |
| --- | --- | --- |
| Đọc bối cảnh HW03 | Shell `rtk` | Đã đọc tài liệu trong `docs/`, `submission/test_environment_access.md`, checklist final, D1 và D2 để giữ đúng phạm vi Scenario D và format báo cáo. |
| Chuẩn bị dữ liệu an toàn | Playwright MCP | Đăng nhập bằng user account của Kiên và tạo một request test mới để D3 có dữ liệu Pending thuộc đúng tài khoản được phép thao tác. Request tạo thành công qua `POST /api/complaints => 201`. |
| Request test được tạo | Playwright MCP | Request mới có URL user `/complaints/58`, title `QA D3 pending list search test - 2026-08-03`, status `Pending`, category `Support`, requester `KiênL Lê · G18D126AA`. Request này không được resolve trong lần test D3. |
| Đăng nhập admin | Playwright MCP | Đăng xuất user Kiên, đăng nhập `admin@gmail.com`, vào `Admin dashboard` rồi mở `Support requests`. |
| Mở D3 | Playwright MCP | URL `/dashboard/admin/complaints`; page title `Support Request Management \| HCMUS EMS`; H1 `Support request management`; sidebar active `Support requests`. |
| Kiểm tra Pending tab | Playwright MCP | Pending tab hiển thị count `7`; list có request test của Kiên ở dòng đầu và các filter `Search name, email or title`, `Member code`, `Category`, `From date`, `To date`, `Reset`. |
| Kiểm tra search theo title | Playwright MCP | Nhập `QA D3 pending list search test`; URL đổi thành `search=QA+D3+pending+list+search+test`, nhưng kết quả vẫn có thêm một request không liên quan `Test support request - 23127097 - 8:02 25/07`. |
| Kiểm tra search theo member code | Playwright MCP | Nhập `G18D126AA`; URL đổi thành `userMemberCode=G18D126AA`; list chỉ còn request Pending của Kiên. |
| Kiểm tra category filter | Playwright MCP | Chọn category `Support`; URL đổi thành `category=SUPPORT&userMemberCode=G18D126AA`; list vẫn chỉ còn request test của Kiên. |
| Kiểm tra Resolved tab | Playwright MCP | Bấm `Resolved`; URL đổi thành `?tab=resolved`, hiển thị count `51` và các request resolved, gồm request của Kiên `/dashboard/admin/complaints/56` và `/dashboard/admin/complaints/55`. Các filter đang áp dụng trước đó bị clear khi đổi tab. |
| Kiểm tra no-result state | Playwright MCP | Ở Pending tab, nhập `not-found-D3-2026`; UI hiển thị `No matching requests.` và vẫn có nút `Reset`. |
| Kiểm tra responsive mobile | Playwright MCP | Ở viewport `390x844`, sidebar admin vẫn chiếm khoảng 256 px, phần content còn rất hẹp, tiêu đề/filter/card bị wrap thành cột chữ khó đọc và pagination nằm ngoài vùng nhìn thấy. |
| Kiểm tra network/console | Playwright MCP | Các API D3 chính trả `200`: `/api/complaints/admin/complaints?...` và `/api/complaints/admin/complaints/stats`. Console có lỗi `500` từ `/api/analytics/overview/all-time` khi vào admin dashboard, không phải API complaints của D3. |
| Kiểm tra bằng Chrome DevTools | Chrome DevTools MCP | Không khởi động được vì môi trường báo `Missing X server to start the headful browser`; không tạo bằng chứng Chrome DevTools giả. |

## 3. Danh mục giao diện D3

| Nhóm | Thành phần D3 quan sát được |
| --- | --- |
| Màn hình và route | Admin support list tại `/dashboard/admin/complaints`; Pending tab; Resolved tab. |
| Vai trò | Admin account `admin@gmail.com`; dữ liệu test an toàn được tạo từ user account của Kiên. |
| Luồng chính | Vào admin dashboard, mở Support requests, xem Pending/Resolved, search theo title, search theo member code, lọc category, reset filter, kiểm tra no-result state. |
| Widget | Sidebar admin, header admin, H1, `Export Excel`, tab buttons `Pending`/`Resolved` có count, filter panel, search textbox, member-code textbox, category dropdown, date fields, reset button, request cards, status badges, pagination, rows-per-page control. |
| Trạng thái động | Pending list có dữ liệu, Resolved list có dữ liệu, search có kết quả, search trả kết quả thừa, filter member code/category, no-result state, filter reset, responsive mobile, network loading qua API. |

## 4. Bằng chứng screenshot

| ID bằng chứng | Đường dẫn | Mục đích |
| --- | --- | --- |
| E-D3-001 | `submission/screenshots/D3/D3_pending_overview.png` | Tổng quan D3 Pending tab ở desktop, có request test của Kiên. |
| E-D3-002 | `submission/screenshots/D3/D3_member_code_filter_kien_pending.png` | Member-code filter `G18D126AA` cô lập request Pending của Kiên. |
| E-D3-003 | `submission/screenshots/D3/D3_category_support_filter.png` | Category filter `Support` kết hợp member-code filter. |
| E-D3-004 | `submission/screenshots/D3/D3_resolved_tab_overview.png` | Resolved tab hiển thị danh sách resolved requests và count. |
| E-D3-005 | `submission/screenshots/D3/D3_no_matching_requests.png` | No-result state khi search không có kết quả. |
| F-D3-001 | `submission/screenshots/checklist-failures/F-D3-001_search-title-returns-extra-result.png` | Search theo title cụ thể vẫn trả thêm request không liên quan. |
| F-D3-002 | `submission/screenshots/checklist-failures/F-D3-002_tab-switch-loses-filter-context.png` | Đổi tab từ trạng thái đang filter làm mất search/member-code/category filter. |
| F-D3-003 | `submission/screenshots/checklist-failures/F-D3-003_mobile-sidebar-overflow.png` | Mobile admin layout bị sidebar chiếm chỗ, content bị bó hẹp và khó đọc. |

## 5. Bảng thực thi checklist - D3

| Màn hình | Checklist ID | Kết quả | Bằng chứng | Ghi chú | Ảnh tham chiếu | ID finding |
| --- | --- | --- | --- | --- | --- | --- |
| D3 Admin Support Requests list | IA-01-01 | Đạt | Sidebar, header, typography, card style và filter panel nhất quán trong admin dashboard. | D3 khớp bố cục admin management. | E-D3-001 |  |
| D3 Admin Support Requests list | IA-01-02 | Đạt | Thuật ngữ `Support requests`, `Pending`, `Resolved`, `Member code`, `Category` được dùng ổn định trong D3. | Không thấy dùng lẫn thuật ngữ khác cho cùng trạng thái support. | E-D3-001, E-D3-004 |  |
| D3 Admin Support Requests list | IA-01-03 | Đạt | `Export Excel`, `Reset`, tab `Pending`/`Resolved` và request cards có mức nhấn thị giác phân biệt được. | Hành động chính/phụ có thể nhận diện trên desktop. | E-D3-001 |  |
| D3 Admin Support Requests list | IA-01-04 | Đạt | Status `Pending` và `Resolved` hiển thị bằng text badge; tab count giúp phân biệt trạng thái. | Mã trạng thái chính nhất quán trên list. | E-D3-001, E-D3-004 |  |
| D3 Admin Support Requests list | IA-01-05 | Không đạt | Desktop đọc được, nhưng viewport `390x844` làm content còn rất hẹp, text trong heading/card/filter bị wrap thành nhiều dòng ngắn khó đọc. | Lỗi responsive làm giảm khả năng đọc trên mobile. | F-D3-003 | F-D3-003 |
| D3 Admin Support Requests list | IA-01-06 | Đạt | Card request ưu tiên status, title, submitted time, requester name và member code/email. | Admin thấy thông tin thiết yếu trước khi mở detail. | E-D3-001 |  |
| D3 Admin Support Requests list | IA-01-07 | Đạt | Các action chính đều có text label: `Export Excel`, `Reset`, `Pending`, `Resolved`. | Không thấy icon-only action mơ hồ trong D3 list. | E-D3-001 |  |
| D3 Admin Support Requests list | IA-01-08 | Đạt | Search, member-code input, category dropdown, tabs, reset và pagination đều có thể tương tác; tab active thể hiện trong accessibility tree. | Trạng thái tương tác chính quan sát được trên desktop. | E-D3-002, E-D3-003, E-D3-004 |  |
| D3 Admin Support Requests list | IA-01-09 | Đạt | Mỗi row hiển thị lại status, title, time và requester nên admin không cần nhớ thông tin từ màn hình khác. | List đủ ngữ cảnh để chọn request cần xử lý. | E-D3-001 |  |
| D3 Admin Support Requests list | IA-01-10 | Không đạt | Ở `390x844`, sidebar fixed chiếm gần hết chiều ngang, content bị đẩy sang cột hẹp và nhiều control/pagination nằm ngoài vùng nhìn thấy. | Mobile/tablet nhỏ khó dùng hoặc không dùng được. | F-D3-003 | F-D3-003 |
| D3 Admin Support Requests list | IA-01-11 | Đạt | Desktop chia nhóm rõ: title/action, tabs, filter panel, list, pagination. | Mật độ desktop dễ quét. | E-D3-001 |  |
| D3 Admin Support Requests list | IA-01-12 | Đạt | Có search, member-code filter, category filter, date filters, Pending/Resolved tabs và Reset. | Admin có công cụ truy cập nhanh request cần xem. | E-D3-001, E-D3-002 |  |
| D3 Admin Support Requests list | IA-01-13 | Không áp dụng | Chưa kiểm tra chuyển đổi EN/VI trong lần chạy D3 này. | Cần lượt test i18n riêng nếu yêu cầu. |  |  |
| D3 Admin Support Requests list | IA-02-01 | Không áp dụng | D3 không có form required-field để gửi dữ liệu mới. | Filter/search không có required field. |  |  |
| D3 Admin Support Requests list | IA-02-02 | Đạt | Search, member code, category, from date và to date đều có label gần control. | Filter không chỉ dựa vào placeholder. | E-D3-001 |  |
| D3 Admin Support Requests list | IA-02-03 | Đạt | Search/member code dùng textbox; category và rows-per-page dùng dropdown; date filter có field riêng cho ngày. | Kiểu control phù hợp với dữ liệu lọc ở mức quan sát GUI. | E-D3-001, E-D3-003 |  |
| D3 Admin Support Requests list | IA-02-04 | Không áp dụng | Không kiểm tra validation date range hoặc dữ liệu invalid trong D3. | D3 focus vào tabs/search/list theo scope. |  |  |
| D3 Admin Support Requests list | IA-02-05 | Không áp dụng | Không phát sinh validation error form trong D3. | No-result search được đánh giá ở IA-04-07. |  |  |
| D3 Admin Support Requests list | IA-02-06 | Không áp dụng | D3 không submit form nên không có nhánh submit thất bại cần giữ dữ liệu nhập. | Filter preservation được đánh giá ở IA-03-09. |  |  |
| D3 Admin Support Requests list | IA-02-07 | Đạt | Filter panel gom các tiêu chí liên quan trong cùng một vùng; list và pagination tách bên dưới. | Nhóm control theo nhiệm vụ tìm request. | E-D3-001 |  |
| D3 Admin Support Requests list | IA-02-08 | Đạt | Các control chính xuất hiện theo thứ tự hợp lý: tabs, filters, list, pagination. | Thứ tự focus dự kiến bám theo luồng đọc desktop. | E-D3-001 |  |
| D3 Admin Support Requests list | IA-02-09 | Không áp dụng | D3 không có nút submit/save form. | Không áp dụng cho màn hình list/filter. |  |  |
| D3 Admin Support Requests list | IA-02-10 | Đạt | Pending tab và `All categories` là trạng thái mặc định; filter đã chọn hiển thị trong URL và control. | Default/filter state dễ hiểu. | E-D3-001, E-D3-003 |  |
| D3 Admin Support Requests list | IA-02-11 | Không áp dụng | D3 không có cancel/reset form làm mất dữ liệu nhập quan trọng. | `Reset` chỉ xóa filter, không xóa dữ liệu server. |  |  |
| D3 Admin Support Requests list | IA-02-12 | Không áp dụng | D3 là list admin, không kiểm tra upload hoặc media preview. | Image lightbox thuộc D4 detail. |  |  |
| D3 Admin Support Requests list | IA-02-13 | Không áp dụng | D3 không có rich-text editor. | Official response/internal note thuộc D4 detail. |  |  |
| D3 Admin Support Requests list | IA-03-01 | Đạt | Sidebar admin có `Support requests` và các khu vực quản trị khác; menu phản ánh vai trò admin. | Điều hướng đúng vai trò admin. | E-D3-001 |  |
| D3 Admin Support Requests list | IA-03-02 | Đạt | H1 `Support request management`, URL `/dashboard/admin/complaints`, page title và sidebar active cho biết vị trí hiện tại. | Admin biết đang ở màn hình quản lý support requests. | E-D3-001 |  |
| D3 Admin Support Requests list | IA-03-03 | Không áp dụng | Không mở request detail trong D3 để tránh chồng phạm vi với D4. | D3 chỉ kiểm tra list, tabs và search. |  |  |
| D3 Admin Support Requests list | IA-03-04 | Đạt | Nhãn cụ thể: `Support requests`, `Pending`, `Resolved`, `Search name, email or title`, `Member code`, `Category`, `Reset`. | Không thấy link/nút mơ hồ kiểu `Click here`. | E-D3-001 |  |
| D3 Admin Support Requests list | IA-03-05 | Đạt | D3 nằm trong `/dashboard/admin`; user flow D1/D2 không có sidebar admin. | Không thấy chức năng admin trong tài khoản user trong lần test trước đó. | E-D3-001 |  |
| D3 Admin Support Requests list | IA-03-06 | Không đạt | Search/filter dễ thấy và URL phản ánh criteria, nhưng search title `QA D3 pending list search test` vẫn trả thêm request không liên quan. | Search quá rộng làm admin phải tự lọc lại kết quả. | F-D3-001 | F-D3-001 |
| D3 Admin Support Requests list | IA-03-07 | Đạt | Pagination hiển thị `1-7 of 7 results`, `1-20 of 51 results`, rows-per-page và trạng thái disabled/next phù hợp. | Admin biết phạm vi dữ liệu đang xem. | E-D3-001, E-D3-004 |  |
| D3 Admin Support Requests list | IA-03-08 | Không áp dụng | D3 không phải luồng đăng ký/checkout nhiều bước. | Không cần stepper. |  |  |
| D3 Admin Support Requests list | IA-03-09 | Không đạt | Sau khi đang filter `userMemberCode=G18D126AA&category=SUPPORT`, bấm `Resolved` làm URL chỉ còn `?tab=resolved` và filter bị clear. | Admin mất ngữ cảnh khi muốn so sánh Pending/Resolved của cùng requester/category. | E-D3-003, F-D3-002 | F-D3-002 |
| D3 Admin Support Requests list | IA-03-10 | Không đạt | Mobile admin layout không chuyển sang drawer/collapsed sidebar; content bị bó hẹp và nhiều control nằm ngoài viewport. | Navigation mobile không hỗ trợ thao tác D3. | F-D3-003 | F-D3-003 |
| D3 Admin Support Requests list | IA-03-11 | Đạt | Filter đặt ngay trên list; request card dẫn tới detail request; `Export Excel` nằm cạnh title list. | Hành động/nội dung liên quan đặt đúng ngữ cảnh desktop. | E-D3-001 |  |
| D3 Admin Support Requests list | IA-03-12 | Không áp dụng | Không kiểm tra URL không tồn tại hoặc request đã bị xóa trong lần chạy D3. | Tránh thao tác ngoài phạm vi list và dữ liệu người khác. |  |  |
| D3 Admin Support Requests list | IA-04-01 | Đạt | Tabs/filter cập nhật list rõ ràng; request Pending và Resolved hiển thị trạng thái đúng theo tab. | Admin thấy phản hồi của hệ thống sau thao tác lọc/tab. | E-D3-002, E-D3-004 |  |
| D3 Admin Support Requests list | IA-04-02 | Đạt | Các API D3 trả `200`; list/filter cập nhật nhanh, không thấy trạng thái treo trong lần test. | Không cần progress dài trong thao tác list/filter ngắn. | E-D3-001, E-D3-002 |  |
| D3 Admin Support Requests list | IA-04-03 | Không áp dụng | D3 không có submit action. | Official response submit thuộc D4 detail. |  |  |
| D3 Admin Support Requests list | IA-04-04 | Đạt | API complaints admin và stats trả `200`; UI D3 không hiển thị mã lỗi kỹ thuật. | Console error `analytics/overview/all-time` là lỗi dashboard khác, không phải D3 complaints API. | E-D3-001 |  |
| D3 Admin Support Requests list | IA-04-05 | Không áp dụng | D3 không có toast/banner kết quả trong luồng list/filter. | No-result state được đánh giá ở IA-04-07. |  |  |
| D3 Admin Support Requests list | IA-04-06 | Đạt | `Pending` và `Resolved` hiển thị bằng tab count và badge text trên từng row. | Trạng thái request dễ quét. | E-D3-001, E-D3-004 |  |
| D3 Admin Support Requests list | IA-04-07 | Đạt | Search không có kết quả hiển thị `No matching requests.` và vẫn có `Reset`. | Empty/no-result state giúp admin phục hồi. | E-D3-005 |  |
| D3 Admin Support Requests list | IA-04-08 | Không áp dụng | D3 list không có hành động nguy hiểm như delete/block/reset. | Không thực hiện thao tác server rủi ro. |  |  |
| D3 Admin Support Requests list | IA-04-09 | Không áp dụng | D3 không có undo cho thao tác destructive; mất filter khi đổi tab được ghi ở IA-03-09. | Không áp dụng riêng cho list read/filter. |  |  |
| D3 Admin Support Requests list | IA-04-10 | Không áp dụng | Không kích hoạt trạng thái session expired trong lần chạy D3. | Cần test riêng cho expired-token. |  |  |
| D3 Admin Support Requests list | IA-04-11 | Không áp dụng | Không kiểm tra realtime khi admin khác xử lý request cùng lúc. | D3 chỉ kiểm tra trạng thái hiện tại của list. |  |  |
| D3 Admin Support Requests list | IA-04-12 | Đạt | D3 có mô tả ngắn `Review and respond to support requests.` và label filter rõ. | Có trợ giúp ngữ cảnh cơ bản cho tác vụ quản lý support. | E-D3-001 |  |
| D3 Admin Support Requests list | IA-04-13 | Không áp dụng | D3 không phải quy trình dài có màn hình hoàn tất. | Hoàn tất phản hồi thuộc D4 detail. |  |  |

## 6. Tóm tắt

| Chỉ số | Số lượng |
| --- | ---: |
| Tổng checklist items | 51 |
| Đạt | 28 |
| Không đạt | 5 |
| Không áp dụng | 18 |
| Cần submit Google Form | 3 findings |

## 7. Draft finding cho Bug & Usability Log

| ID | Kịch bản/Màn hình | Loại | Mô tả | Bước/Heuristic | Kỳ vọng | Thực tế | Mức độ nghiêm trọng | Đề xuất sửa | Ảnh tham chiếu | Thời điểm submit Form |
| --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- |
| F-D3-001 | D3 Admin Support Requests list | Usability | Search theo title cụ thể vẫn trả thêm request không liên quan. | IA-03-06. Steps: mở `/dashboard/admin/complaints`; ở Pending tab nhập `QA D3 pending list search test` vào `Search name, email or title`. | Kết quả nên ưu tiên hoặc chỉ hiển thị request khớp cụm từ/title rõ ràng, đặc biệt khi query có chuỗi định danh `QA D3`. | List trả request của Kiên `/dashboard/admin/complaints/58`, nhưng vẫn trả thêm request `/dashboard/admin/complaints/6` không có `QA D3` trong title/requester. | 2 | Điều chỉnh search thành match theo phrase hoặc AND-token cho title/email/name, hoặc highlight phần khớp để admin hiểu vì sao row xuất hiện. | `submission/screenshots/checklist-failures/F-D3-001_search-title-returns-extra-result.png` | `[Điền thủ công sau khi submit Google Form]` |
| F-D3-002 | D3 Admin Support Requests list | Usability | Đổi Pending/Resolved tab làm mất filter context đang áp dụng. | IA-03-09. Steps: filter `Member code = G18D126AA`; chọn category `Support`; bấm tab `Resolved`. | Khi admin đổi tab để xem cùng requester/category ở trạng thái khác, hệ thống nên giữ `userMemberCode` và `category`, chỉ đổi `status/tab`. | URL chuyển từ trạng thái đã filter sang `/dashboard/admin/complaints?tab=resolved`; filter fields bị clear và list hiển thị tất cả resolved requests. | 2 | Giữ query filter khi đổi tab, hoặc hỏi/reset rõ ràng bằng một action riêng để admin không mất ngữ cảnh. | `submission/screenshots/D3/D3_category_support_filter.png`, `submission/screenshots/checklist-failures/F-D3-002_tab-switch-loses-filter-context.png` | `[Điền thủ công sau khi submit Google Form]` |
| F-D3-003 | D3 Admin Support Requests list | Bug | Admin D3 mobile layout bị vỡ vì sidebar fixed chiếm hầu hết chiều ngang. | IA-01-05, IA-01-10, IA-03-10. Steps: resize viewport `390x844`; mở `/dashboard/admin/complaints?tab=pending`. | Mobile admin nên dùng collapsed sidebar/drawer, content chiếm đủ chiều ngang và filter/list không bị wrap cực đoan hoặc tràn khỏi viewport. | Sidebar rộng khoảng 256 px vẫn hiển thị cố định; phần content chỉ còn cột rất hẹp, tiêu đề và card bị wrap thành nhiều dòng ngắn, pagination/controls nằm ngoài vùng nhìn thấy. | 3 | Ở breakpoint mobile, tự collapse sidebar thành drawer/hamburger, đặt content full width, và cho filter/list xếp dọc với chiều rộng tối thiểu hợp lý. | `submission/screenshots/checklist-failures/F-D3-003_mobile-sidebar-overflow.png` | `[Điền thủ công sau khi submit Google Form]` |

## 8. Ghi chú hoàn tất

- Lần thực thi checklist D3 dùng checklist shared từ `submission/group/gui_usability_checklist_final.md` và không sửa file này.
- Playwright MCP đã được dùng để tương tác EMS thật, tạo dữ liệu test an toàn bằng tài khoản Kiên, đăng nhập admin, kiểm tra Pending/Resolved tabs, search, filter, no-result, mobile responsive, chụp screenshot và kiểm tra console/network.
- Chrome DevTools MCP đã được thử nhưng không khởi động được trong môi trường hiện tại vì tool báo thiếu X server cho headful browser startup.
- Request test thật đã được tạo bằng tài khoản user của Kiên để phục vụ D3: `/complaints/58`, hiển thị trong admin tại `/dashboard/admin/complaints/58`, status `Pending`, category `Support`, member code `G18D126AA`. Request này chưa được xử lý/resolve trong lần test D3.
- Không mở hoặc chỉnh sửa detail của request người khác, không đổi role, không reset mật khẩu, không khóa/xóa tài khoản, không resolve dữ liệu không thuộc Kiên.
- Các findings ở trên là draft. Kiên cần review screenshot, submit các finding đã xác nhận lên Google Form, rồi điền giá trị `Form-submission timestamp`.
