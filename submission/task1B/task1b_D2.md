# Task 1B - Thực thi checklist cho D2

| Trường | Giá trị |
| --- | --- |
| Người kiểm thử | Lê Trung Kiên |
| MSSV | `23127075` |
| Kịch bản | D - Người dùng gửi yêu cầu hỗ trợ và Admin xử lý |
| Màn hình | D2 - User xem My Requests list/detail có phản hồi |
| Vai trò sử dụng | User |
| SUT | `https://prod-dev.ems-fitus.cloud` |
| Ngày kiểm thử | 2026-08-03 |
| Nguồn checklist | `submission/group/gui_usability_checklist_final.md` |
| Có sửa checklist gốc không? | Không |

## 1. Prompt đầy đủ đã dùng để AI hỗ trợ test D2

```text
@Superpowers Đọc các file trong folder docs để hiểu bối cảnh bài tập. Thực hiện Task 1B cho Kiên trên Scene D2. Dùng submission/group/gui_usability_checklist_final.md (không thay đổi file này) để làm check list. Tạo 1 file markdown cho task1b_D2.md trong folder submission/task1B cho việc testing dựa trên checklist đó. Hãy tận dụng MCP Playwright và Chrome Devtools trong quá trình test. Thông tin link web, tài khoản admin và user đã được cung cấp trong submission/test_environment_access.md. Tuyệt đối tuân theo rule được ghi trong  submission/test_environment_access.md. Nếu cần thêm gì thì hãy yêu cầu tôi cung cấp. Format cho output của D2 cũng nên tương tự như D1.
```

## 2. Nhật ký kiểm thử

| Bước | Công cụ | Quan sát |
| --- | --- | --- |
| Đọc bối cảnh HW03 | Shell `rtk` | Đã đọc tài liệu trong `docs/`, `submission/test_environment_access.md`, checklist final và file D1 để giữ đúng phạm vi Scenario D và format báo cáo. |
| Mở EMS | Playwright MCP | Mở `https://prod-dev.ems-fitus.cloud`; session hiện tại đã là user Kiên (`ltkien23@clc.fitus.edu.vn`) tại `/dashboard`. |
| Điều hướng D2 | Playwright MCP | Từ menu user mở `Support requests`; URL `/complaints`; page title `Yêu cầu hỗ trợ \| HCMUS EMS`; H1 `Support requests`. |
| Kiểm tra list My Requests | Playwright MCP | List hiển thị 2 request thuộc tài khoản Kiên: `/complaints/56` và `/complaints/55`, đều có status `Resolved`, category, title/description và submitted time. |
| Kiểm tra detail có response | Playwright MCP | Mở `/complaints/56`; page title `Chi tiết yêu cầu \| HCMUS EMS`; detail có status `Resolved`, category `Complaint`, ID `#56`, submitted time, nội dung request, attachments và mục `Support response`. |
| Kiểm tra official response | Playwright MCP | `Support response` hiển thị nội dung phản hồi chính thức: `[QA TEST - HW03 Task 1B] This is a test response to verify the submit/loading/toast behavior of the response form.` kèm hướng dẫn tạo request mới nếu cần hỗ trợ tiếp. |
| Kiểm tra attachment preview/lightbox | Playwright MCP | Click `Open attachment 1`; modal/lightbox mở ảnh lớn với tiêu đề `attachment_1` và nút `Close`; đóng modal thành công. |
| Kiểm tra search không có kết quả | Playwright MCP | Nhập `not-found-D2-2026`; URL đổi thành `/complaints?search=not-found-D2-2026&page=1`; empty state hiển thị `No requests yet`, chưa phản ánh rõ đây là trạng thái không có kết quả do filter/search. |
| Kiểm tra status filter | Playwright MCP | Dropdown status có `All statuses`, `Pending`, `Resolved`; chọn `Resolved` đổi URL thành `status=RESOLVED` và trả đúng 2 resolved requests. |
| Kiểm tra giữ ngữ cảnh khi quay lại | Playwright MCP | Mở detail từ `/complaints?status=RESOLVED&search=keyboard`; bấm `Back` trong detail đưa về `/complaints`, làm mất search/status filter đang áp dụng. |
| Kiểm tra responsive mobile | Playwright MCP | Ở viewport `390x844`, list và detail xếp dọc, không thấy cuộn ngang; tuy nhiên nút floating social links che sát vùng pagination/list và có thể cản trở thao tác ở mép phải. |
| Kiểm tra network/console | Playwright MCP | D2 APIs chính trả thành công: `GET /api/complaints/me?page=1&limit=10 => 200`, `GET /api/complaints/me/56 => 200`. Console có một lỗi cũ `GET /api/users/me => 401` trước khi D2 ổn định; không thấy lỗi API D2 khi list/detail tải. |
| Kiểm tra bằng Chrome DevTools | Chrome DevTools MCP | Không khởi động được vì môi trường báo `Missing X server to start the headful browser`; không tạo bằng chứng Chrome DevTools giả. |

## 3. Danh mục giao diện D2

| Nhóm | Thành phần D2 quan sát được |
| --- | --- |
| Màn hình và route | List `Support requests` tại `/complaints`; detail request tại `/complaints/56`; lightbox attachment trong detail. |
| Vai trò | Chỉ dùng user account của Kiên để xem requests của chính tài khoản Kiên; không thao tác dữ liệu/tài khoản người khác. |
| Luồng chính | Mở support requests, xem danh sách My Requests, search theo title/description, lọc status, mở detail, xem official response, mở/đóng attachment, quay lại list. |
| Widget | Header, user menu, H1, search textbox, status dropdown, `Create request`, request cards, status/category badges, submitted time, rows-per-page dropdown, pagination, `Back`, attachment thumbnail, lightbox modal, `Close`, floating social links. |
| Trạng thái động | List có dữ liệu, filter resolved, search no-result, detail resolved, response official, attachment lightbox, mobile responsive, API loading qua network. |

## 4. Bằng chứng screenshot

| ID bằng chứng | Đường dẫn | Mục đích |
| --- | --- | --- |
| E-D2-001 | `submission/screenshots/D2/D2_my_requests_overview.png` | Tổng quan D2 list ở desktop với 2 resolved requests của Kiên. |
| E-D2-002 | `submission/screenshots/D2/D2_detail_with_response.png` | Detail request `/complaints/56` có status, nội dung, attachment và `Support response`. |
| E-D2-003 | `submission/screenshots/D2/D2_attachment_lightbox.png` | Attachment mở trong lightbox/modal. |
| E-D2-004 | `submission/screenshots/D2/D2_search_status_filter.png` | Search `keyboard` kết hợp filter `Resolved` trả 1 kết quả. |
| E-D2-005 | `submission/screenshots/D2/D2_mobile_detail_response.png` | Detail và response ở viewport mobile `390x844`. |
| F-D2-001 | `submission/screenshots/checklist-failures/F-D2-001_back-loses-filter-context.png` | `Back` từ detail làm mất search/status filter. |
| F-D2-002 | `submission/screenshots/checklist-failures/F-D2-002_search-no-results-misleading-empty-state.png` | Empty state khi search không có kết quả dùng message `No requests yet` và không có reset action rõ. |
| F-D2-003 | `submission/screenshots/checklist-failures/F-D2-003_mobile-floating-button-near-pagination.png` | Floating social links button chồng sát/che vùng pagination trên mobile list. |

## 5. Bảng thực thi checklist - D2

| Màn hình | Checklist ID | Kết quả | Bằng chứng | Ghi chú | Ảnh tham chiếu | ID finding |
| --- | --- | --- | --- | --- | --- | --- |
| D2 My Requests list/detail | IA-01-01 | Đạt | Header, footer, typography, card style và spacing nhất quán giữa `/complaints` và `/complaints/56`. | Bố cục D2 nhất quán với flow support user. | E-D2-001, E-D2-002 |  |
| D2 My Requests list/detail | IA-01-02 | Đạt | Thuật ngữ `Support requests`, `Resolved`, `Complaint`, `Support`, `Support response` được dùng ổn định trong list/detail. | Không thấy dùng lẫn thuật ngữ khác cho cùng trạng thái support. | E-D2-001, E-D2-002 |  |
| D2 My Requests list/detail | IA-01-03 | Đạt | `Create request` nổi bật ở list; `Back` trong detail là hành động phụ rõ ràng. | Mức nhấn thị giác phân biệt được hành động chính/phụ. | E-D2-001, E-D2-002 |  |
| D2 My Requests list/detail | IA-01-04 | Đạt | Status `Resolved` và category badge hiển thị bằng text + màu nhất quán trên list/detail. | Trạng thái chính dễ nhận biết. | E-D2-001, E-D2-002 |  |
| D2 My Requests list/detail | IA-01-05 | Đạt | Label, title, badge, timestamp và response text đọc được trên desktop/mobile. | Không thấy text tương phản quá thấp trong D2. | E-D2-001, E-D2-005 |  |
| D2 My Requests list/detail | IA-01-06 | Đạt | Card request ưu tiên status/category, title, mô tả ngắn và submitted time. | Thông tin thiết yếu của support request nằm trước. | E-D2-001 |  |
| D2 My Requests list/detail | IA-01-07 | Đạt | Attachment button có tên `Open attachment 1`; lightbox có nút `Close`. | Icon/media action có nhãn nhận diện được qua accessibility snapshot. | E-D2-003 |  |
| D2 My Requests list/detail | IA-01-08 | Đạt | Search, status dropdown, card link, pagination, attachment và close modal đều có thể tương tác. | Trạng thái focus/expanded xuất hiện khi dùng dropdown/lightbox. | E-D2-003, E-D2-004 |  |
| D2 My Requests list/detail | IA-01-09 | Đạt | Detail hiển thị lại title, ID, status, category, submitted time, description, attachment và response. | Người dùng không cần nhớ thông tin từ list khi vào detail. | E-D2-002 |  |
| D2 My Requests list/detail | IA-01-10 | Không đạt | Mobile không cuộn ngang, nhưng floating social links button che sát vùng pagination/right edge của list. | Control nổi có thể cản thao tác pagination hoặc làm người dùng tưởng là action của request. | F-D2-003 | F-D2-003 |
| D2 My Requests list/detail | IA-01-11 | Đạt | List, filters, pagination, detail header, attachments và response được tách nhóm rõ. | Mật độ nội dung vừa phải, dễ quét. | E-D2-001, E-D2-002 |  |
| D2 My Requests list/detail | IA-01-12 | Đạt | Có search, status filter, pagination và link tạo request mới. | Người dùng thường xuyên có cách truy cập nhanh request cần xem. | E-D2-001, E-D2-004 |  |
| D2 My Requests list/detail | IA-01-13 | Không áp dụng | Chưa kiểm tra chuyển đổi EN/VI trong lần chạy D2 này. | Cần lượt test i18n riêng nếu yêu cầu. |  |  |
| D2 My Requests list/detail | IA-02-01 | Không áp dụng | D2 không có form required-field để submit dữ liệu mới. | Search/filter không phải form bắt buộc. |  |  |
| D2 My Requests list/detail | IA-02-02 | Đạt | Search textbox có label `Search title or description` nằm gần input. | Không chỉ dựa vào placeholder. | E-D2-001 |  |
| D2 My Requests list/detail | IA-02-03 | Đạt | Search dùng textbox; status và rows per page dùng combobox/dropdown; page dùng spinbutton. | Kiểu control phù hợp dữ liệu lọc/danh sách. | E-D2-001, E-D2-004 |  |
| D2 My Requests list/detail | IA-02-04 | Không áp dụng | Không có dữ liệu nhập hợp lệ/không hợp lệ cần validate trước submit ở D2. | Search không có rule invalid cụ thể. |  |  |
| D2 My Requests list/detail | IA-02-05 | Không áp dụng | Không phát sinh validation error form trong D2. | Không có field lỗi để kiểm tra error placement. |  |  |
| D2 My Requests list/detail | IA-02-06 | Không áp dụng | D2 không submit form nên không có nhánh submit thất bại cần giữ dữ liệu nhập. | Search/filter preservation được đánh giá ở IA-03. |  |  |
| D2 My Requests list/detail | IA-02-07 | Đạt | Filter/search nằm cùng vùng đầu trang; list kết quả và pagination được gom trong region `My support requests`. | Nhóm control theo nhiệm vụ tìm/xem request. | E-D2-001 |  |
| D2 My Requests list/detail | IA-02-08 | Đạt | Các control chính xuất hiện trong accessibility tree theo thứ tự search, status, create request, list, pagination. | Thứ tự focus dự kiến đi theo luồng đọc tự nhiên. | E-D2-001 |  |
| D2 My Requests list/detail | IA-02-09 | Không áp dụng | D2 không có nút submit/save form. | Không áp dụng cho list/detail read-only. |  |  |
| D2 My Requests list/detail | IA-02-10 | Đạt | Status filter mặc định là `All statuses`, và khi chọn `Resolved` trạng thái đang áp dụng hiển thị ngay trên nút. | Default/filter state dễ hiểu. | E-D2-001, E-D2-004 |  |
| D2 My Requests list/detail | IA-02-11 | Không áp dụng | D2 không có cancel/reset form có nguy cơ mất dữ liệu nhập. | Trường hợp mất filter được đánh giá ở navigation. |  |  |
| D2 My Requests list/detail | IA-02-12 | Đạt | Detail hiển thị attachment thumbnail; click mở lightbox ảnh lớn và đóng được. | Media preview/read path dùng được. | E-D2-002, E-D2-003 |  |
| D2 My Requests list/detail | IA-02-13 | Không áp dụng | D2 không có rich-text editor. | Response chỉ hiển thị read-only text. |  |  |
| D2 My Requests list/detail | IA-03-01 | Đạt | User menu có `Support requests`; không thấy menu admin trong user flow D2. | Điều hướng phản ánh vai trò user. | E-D2-001 |  |
| D2 My Requests list/detail | IA-03-02 | Đạt | H1 `Support requests`, page title và URL `/complaints`/`/complaints/56` cho biết vị trí hiện tại. | Người dùng biết đang ở list hay detail. | E-D2-001, E-D2-002 |  |
| D2 My Requests list/detail | IA-03-03 | Không đạt | Mở detail từ list đang filter `status=RESOLVED&search=keyboard`, sau đó bấm `Back` thì quay về `/complaints` và mất filter. | Người dùng phải thiết lập lại search/status khi quay lại list. | F-D2-001, E-D2-004 | F-D2-001 |
| D2 My Requests list/detail | IA-03-04 | Đạt | Nhãn cụ thể: `Support requests`, `Create request`, `Back`, `Open attachment 1`, `Close`. | Không thấy link/nút mơ hồ kiểu `Click here`. | E-D2-001, E-D2-003 |  |
| D2 My Requests list/detail | IA-03-05 | Đạt | User chỉ thấy và mở requests của chính tài khoản Kiên trong list/detail D2. | Không thấy chức năng admin hoặc dữ liệu người khác trong D2. | E-D2-001 |  |
| D2 My Requests list/detail | IA-03-06 | Không đạt | Search/filter dễ thấy và URL phản ánh criteria, nhưng không có nút clear/reset rõ; khi no-result UI khuyến khích tạo request thay vì sửa/clear filter. | Recovery khỏi trạng thái lọc rỗng chưa đủ rõ. | F-D2-002 | F-D2-002 |
| D2 My Requests list/detail | IA-03-07 | Đạt | Pagination hiển thị `1-2 of 2 results`, rows per page, current page và disabled previous/next khi chỉ có một trang. | Phạm vi kết quả rõ ràng. | E-D2-001 |  |
| D2 My Requests list/detail | IA-03-08 | Không áp dụng | D2 không phải luồng đăng ký/checkout nhiều bước. | Không cần stepper. |  |  |
| D2 My Requests list/detail | IA-03-09 | Không đạt | `Back` từ detail làm mất filter/search đang áp dụng ở list. | Điều hướng quay lại không bảo toàn ngữ cảnh người dùng đang xem. | F-D2-001 | F-D2-001 |
| D2 My Requests list/detail | IA-03-10 | Không đạt | Mobile navigation xếp dọc dùng được, nhưng floating social links button nằm chồng sát pagination/list card. | Control nổi có thể che thao tác ở màn hình nhỏ. | F-D2-003 | F-D2-003 |
| D2 My Requests list/detail | IA-03-11 | Đạt | `Back` đặt đầu detail; attachment action nằm trong section `Attachments`; response nằm trong section `Support response`. | Hành động/nội dung liên quan đặt đúng ngữ cảnh. | E-D2-002, E-D2-003 |  |
| D2 My Requests list/detail | IA-03-12 | Không áp dụng | Không kiểm tra URL không tồn tại hoặc request đã bị xóa trong lần chạy D2. | Cần test riêng để tránh đụng dữ liệu không thuộc tài khoản Kiên. |  |  |
| D2 My Requests list/detail | IA-04-01 | Đạt | List và detail tải thành công; resolved request hiển thị response chính thức rõ. | Người dùng biết request đã được xử lý và nội dung phản hồi là gì. | E-D2-002 |  |
| D2 My Requests list/detail | IA-04-02 | Đạt | Các API list/detail trả `200`; không thấy trạng thái treo trong lần test. | Không phát sinh thao tác lâu cần progress đặc biệt. | E-D2-001, E-D2-002 |  |
| D2 My Requests list/detail | IA-04-03 | Không áp dụng | D2 không có submit action. | Không có nguy cơ gửi trùng trong màn hình read-only. |  |  |
| D2 My Requests list/detail | IA-04-04 | Đạt | `GET /api/complaints/me` và `GET /api/complaints/me/56` trả `200`; UI không hiển thị lỗi kỹ thuật khi tải list/detail. | D2 không lộ mã lỗi cho người dùng trong lần chạy này. | E-D2-001, E-D2-002 |  |
| D2 My Requests list/detail | IA-04-05 | Không áp dụng | Không có toast/banner kết quả trong luồng read-only D2. | Floating social button được đánh giá ở responsive/navigation. |  |  |
| D2 My Requests list/detail | IA-04-06 | Đạt | Status `Resolved` hiển thị bằng badge text/màu trên cả list và detail. | Trạng thái request dễ quét. | E-D2-001, E-D2-002 |  |
| D2 My Requests list/detail | IA-04-07 | Không đạt | Khi search không có kết quả, empty state ghi `No requests yet` dù tài khoản thật sự có requests và chỉ đang bị filter. | Message có thể làm người dùng hiểu nhầm dữ liệu đã mất/chưa từng tạo request. | F-D2-002 | F-D2-002 |
| D2 My Requests list/detail | IA-04-08 | Không áp dụng | D2 không có hành động nguy hiểm như delete/cancel submitted request. | Không có confirmation destructive action cần kiểm tra. |  |  |
| D2 My Requests list/detail | IA-04-09 | Không áp dụng | D2 không có undo cho thao tác destructive; mất filter đã được ghi ở IA-03-03/IA-03-09. | Không áp dụng riêng cho D2 read-only. |  |  |
| D2 My Requests list/detail | IA-04-10 | Không áp dụng | Không kích hoạt trạng thái session expired trong lần chạy D2. | Console có 401 cũ từ `/api/users/me`, nhưng D2 APIs vẫn tải `200`. |  |  |
| D2 My Requests list/detail | IA-04-11 | Không áp dụng | Không kiểm tra cập nhật realtime khi admin đổi trạng thái trong cùng lúc. | D2 hiện chỉ xem resolved data đã có. |  |  |
| D2 My Requests list/detail | IA-04-12 | Đạt | Empty state có hướng dẫn tạo request; detail response có câu hướng dẫn `If you need further assistance, please create a new request.` | Có trợ giúp ngắn đúng ngữ cảnh cơ bản. | E-D2-002, F-D2-002 |  |
| D2 My Requests list/detail | IA-04-13 | Đạt | Request resolved có response chính thức và lời nhắc bước tiếp theo nếu cần hỗ trợ thêm. | Luồng xem phản hồi có closure rõ trong detail. | E-D2-002 |  |

## 6. Tóm tắt

| Chỉ số | Số lượng |
| --- | ---: |
| Tổng checklist items | 51 |
| Đạt | 29 |
| Không đạt | 6 |
| Không áp dụng | 16 |
| Cần submit Google Form | 3 findings |

## 7. Draft finding cho Bug & Usability Log

| ID | Kịch bản/Màn hình | Loại | Mô tả | Bước/Heuristic | Kỳ vọng | Thực tế | Mức độ nghiêm trọng | Đề xuất sửa | Ảnh tham chiếu | Thời điểm submit Form |
| --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- |
| F-D2-001 | D2 My Requests list/detail | Usability | `Back` từ request detail làm mất ngữ cảnh search/status filter của list. | IA-03-03, IA-03-09. Steps: mở `/complaints?status=RESOLVED&search=keyboard`; mở request `/complaints/56`; bấm `Back`. | Quay lại đúng list đã filter, giữ `search=keyboard` và `status=RESOLVED`. | Trang quay về `/complaints`, search textbox rỗng và status trở lại `All statuses`. | 2 | Lưu query trước khi vào detail và để `Back` dùng `router.back()` hoặc link về URL list có query hiện tại. | `submission/screenshots/checklist-failures/F-D2-001_back-loses-filter-context.png` | `[Điền thủ công sau khi submit Google Form]` |
| F-D2-002 | D2 My Requests list/detail | Usability | Empty state khi search/filter không có kết quả dùng message gây hiểu nhầm là tài khoản chưa có request. | IA-03-06, IA-04-07. Steps: mở `/complaints`; nhập search `not-found-D2-2026`. | Empty state nên nói rõ `No matching requests found`, hiển thị criteria đang áp dụng và có nút `Clear filters`. | UI hiển thị `No requests yet` và `Create a request when you need help.` dù tài khoản vẫn có 2 requests khi bỏ search. | 2 | Tách empty state thật sự chưa có dữ liệu khỏi no-result do filter/search; thêm `Clear search`/`Clear filters`. | `submission/screenshots/checklist-failures/F-D2-002_search-no-results-misleading-empty-state.png` | `[Điền thủ công sau khi submit Google Form]` |
| F-D2-003 | D2 My Requests list/detail | Usability | Floating social links button chồng sát/che vùng thao tác ở mobile list. | IA-01-10, IA-03-10. Steps: resize viewport `390x844`; mở `/complaints`; quan sát cuối list/pagination. | Floating button nên tránh vùng pagination/card content hoặc tự ẩn/đổi vị trí trên mobile. | Nút social links màu xanh nằm ở mép phải vùng card/pagination, có thể che hoặc gây nhầm với action của request. | 2 | Đặt offset cao hơn pagination, giới hạn trong footer, hoặc ẩn social floating button trên các trang tác vụ có pagination ở mobile. | `submission/screenshots/checklist-failures/F-D2-003_mobile-floating-button-near-pagination.png` | `[Điền thủ công sau khi submit Google Form]` |

## 8. Ghi chú hoàn tất

- Lần thực thi checklist D2 dùng checklist shared từ `submission/group/gui_usability_checklist_final.md` và không sửa file này.
- Playwright MCP đã được dùng để tương tác EMS thật, lấy accessibility snapshot, kiểm tra search/filter/detail/lightbox/mobile, chụp screenshot, và kiểm tra console/network.
- Chrome DevTools MCP đã được thử nhưng không khởi động được trong môi trường hiện tại vì tool báo thiếu X server cho headful browser startup.
- Không tạo support request mới và không dùng admin account trong lần D2 này vì tài khoản Kiên đã có resolved requests đủ để kiểm tra official response.
- Các findings ở trên là draft. Kiên cần review screenshot, submit các finding đã xác nhận lên Google Form, rồi điền giá trị `Form-submission timestamp`.
