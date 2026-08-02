# Task 1B - Thực thi checklist cho D1

| Trường | Giá trị |
| --- | --- |
| Người kiểm thử | Lê Trung Kiên |
| MSSV | `23127075` |
| Kịch bản | D - Người dùng gửi yêu cầu hỗ trợ và Admin xử lý |
| Màn hình | D1 - User tạo support request form có đính kèm ảnh |
| Vai trò sử dụng | User |
| SUT | `https://prod-dev.ems-fitus.cloud` |
| Ngày kiểm thử | 2026-08-02 |
| Nguồn checklist | `submission/group/gui_usability_checklist_final.md` |
| Có sửa checklist gốc không? | Không |

## 1. Prompt đầy đủ đã dùng để AI hỗ trợ test D1

```text
Bạn là QA tester cho HW03 GUI & Usability Testing trên EMS.

Hãy thực hiện Task 1B cho Lê Trung Kiên (MSSV 23127075), Scenario D, màn hình D1: User - create support request form with image attachment.

Nguồn bắt buộc:
- Đọc các tài liệu trong `docs/` để hiểu bối cảnh bài tập, EMS, Scenario D và yêu cầu Task 1B.
- Dùng checklist gốc `submission/group/gui_usability_checklist_final.md` làm checklist thực thi.
- Không sửa `submission/group/gui_usability_checklist_final.md`.
- Dùng thông tin URL/tài khoản trong `submission/test_environment_access.md`.
- Tuyệt đối tuân thủ Testing Rules trong `submission/test_environment_access.md`: chỉ dùng tài khoản user của Kiên cho D1/D2, không thao tác dữ liệu hoặc tài khoản người khác, chỉ tạo support request test của chính tài khoản Kiên nếu cần.

Công cụ:
- Dùng Playwright MCP để đăng nhập, điều hướng, lấy accessibility snapshot, thao tác form, upload ảnh, submit, chụp screenshot evidence và kiểm tra network/console.
- Dùng Chrome DevTools MCP nếu môi trường cho phép để kiểm tra bổ sung snapshot/console/network. Nếu Chrome DevTools MCP không chạy được, ghi rõ limitation và không bịa evidence.

Quy trình D1:
1. Mở EMS tại URL mới trong `submission/test_environment_access.md`.
2. Đăng nhập bằng user account của Kiên.
3. Điều hướng `Support requests -> Create request` hoặc route tương ứng.
4. Ghi lại URL, page title, heading, primary actions và danh sách widget hiển thị.
5. Chụp screenshot tổng quan của màn hình D1.
6. Chạy từng item trong `submission/group/gui_usability_checklist_final.md` trên riêng màn hình D1.
7. Với mỗi item, đánh dấu `Pass`, `Fail`, hoặc `N/A`.
8. Với mỗi `Fail`, ghi lý do cụ thể dựa trên quan sát UI/network/console, user impact, severity 0-4, screenshot ref và suggested fix.
9. Kiểm tra tối thiểu các trạng thái D1: submit rỗng, chọn request type, nhập issue/title, nhập detailed description, character counter, upload ảnh hợp lệ, preview/remove ảnh, submit thành công, cancel/back khi có dữ liệu chưa lưu, desktop và mobile responsive layout.
10. Không submit Google Form tự động. Chỉ tạo finding entries sẵn để sinh viên review và submit thủ công.

Output cần tạo:
- File Markdown `submission/task1B/task1b_D1.md`.
- Nội dung gồm: test scope, test log, UI inventory, bảng checklist execution theo ID checklist gốc, danh sách findings, screenshot evidence và completion notes.
```

## 2. Nhật ký kiểm thử

| Bước | Công cụ | Quan sát |
| --- | --- | --- |
| Mở EMS | Playwright MCP | Mở `https://prod-dev.ems-fitus.cloud`; session ban đầu đang là admin nên đã đăng xuất trước. |
| Đăng nhập user Kiên | Playwright MCP | Đăng nhập bằng `ltkien23@clc.fitus.edu.vn`; dashboard tải thành công. |
| Điều hướng đến Support | Playwright MCP | Menu user có mục `Support requests` trỏ tới `/complaints`. |
| Mở D1 | Playwright MCP | `Create request` mở `/complaints/new`; page title `Gửi yêu cầu hỗ trợ \| HCMUS EMS`; H1 hiển thị là `Create support request`. |
| Submit form rỗng | Playwright MCP | Alert hiển thị: `Request type, issue requiring support and detailed description are required.` |
| Điền form và upload | Playwright MCP | Form nhận title, description và file PNG; thumbnail ảnh và nút remove xuất hiện. |
| Submit khi gặp lỗi mặc định/category | Playwright MCP | Lần submit đầu tạo `POST /api/complaints => 400`; response body báo category phải thuộc `SUPPORT`, `COMPLAINT`, `CONTACT`, `OTHER`; console warning: `Select: Keys "S" passed to "selectedKeys" are not present in the collection.` |
| Submit sau khi chọn category bằng bàn phím | Playwright MCP | Chọn bằng bàn phím làm UI đổi sang `Complaint`; submit trả `POST /api/complaints => 201`; redirect tới `/complaints?created=1`; request mới xuất hiện trạng thái `Pending` với URL `/complaints/56`. |
| Kiểm tra responsive mobile | Playwright MCP | Ở viewport `390x844`, form không bị tràn ngang; các field xếp dọc hợp lý. |
| Kiểm tra bằng Chrome DevTools | Chrome DevTools MCP | Không khởi động được vì môi trường báo `Missing X server to start the headful browser`; không tạo bằng chứng Chrome DevTools giả. |

## 3. Danh mục giao diện D1

| Nhóm | Thành phần D1 quan sát được |
| --- | --- |
| Màn hình và route | Danh sách `Support requests` tại `/complaints`; form tạo mới tại `/complaints/new`. |
| Vai trò | Chỉ dùng user account của Kiên. |
| Luồng chính | Mở support requests, tạo request, chọn request type, nhập issue và detailed description, đính kèm ảnh, submit. |
| Widget | Header, user menu, `Back`, H1, select request type, textbox issue, bộ đếm `0/255`, textarea detailed description, vùng upload ảnh, thumbnail ảnh, nút remove attachment, `Cancel`, `Submit request`, vùng alert/toast. |
| Trạng thái động | Alert validation rỗng, lỗi validation category, preview/remove ảnh upload, layout mobile, redirect sau submit thành công, trạng thái lỗi API. |

## 4. Bằng chứng screenshot

| ID bằng chứng | Đường dẫn | Mục đích |
| --- | --- | --- |
| E-D1-001 | `submission/screenshots/D1/D1_create_request_overview.png` | Tổng quan D1 trước khi nhập dữ liệu. |
| E-D1-002 | `submission/screenshots/D1/D1_form_filled_with_attachment.png` | Form đã điền và có ảnh upload. |
| E-D1-003 | `submission/screenshots/D1/D1_mobile_validation_layout.png` | Layout mobile và trạng thái validation ở `390x844`. |
| E-D1-004 | `submission/screenshots/D1/D1_submit_success_redirect.png` | Redirect sau submit thành công và request mới trong danh sách. |
| F-D1-001 | `submission/screenshots/checklist-failures/F-D1-001_validation-not-inline.png` | Validation field bắt buộc dùng alert chung và submit vẫn bật khi form rỗng. |
| F-D1-002 | `submission/screenshots/checklist-failures/F-D1-002_category-submit-400-no-clear-ui-error.png` | Lỗi submit category/default và recovery message chưa rõ. |
| F-D1-003 | `submission/screenshots/checklist-failures/F-D1-003_cancel-discards-without-confirmation.png` | Cancel quay về danh sách không xác nhận dù form đã có dữ liệu. |

## 5. Bảng thực thi checklist - D1

| Màn hình | Checklist ID | Kết quả | Bằng chứng | Ghi chú | Ảnh tham chiếu | ID finding |
| --- | --- | --- | --- | --- | --- | --- |
| D1 Tạo support request | IA-01-01 | Đạt | Header, footer, typography và spacing nhất quán với support list và dashboard. | Bố cục D1 nhất quán. | E-D1-001 |  |
| D1 Tạo support request | IA-01-02 | Đạt | Các thuật ngữ `Support requests`, `Create support request`, `Request type`, `Complaint`, `Support` được dùng nhất quán trong UI D1. | Browser title bằng tiếng Việt, nhưng các thuật ngữ hiển thị vẫn dễ hiểu. | E-D1-001 |  |
| D1 Tạo support request | IA-01-03 | Đạt | Nút chính `Submit request` nổi bật hơn `Cancel`; `Back` là hành động phụ. | Hành động chính/phụ phân biệt được. | E-D1-001 |  |
| D1 Tạo support request | IA-01-04 | Không đạt | Trạng thái invalid của request type và alert có hiển thị, nhưng trạng thái chọn category/default gây hiểu nhầm và không nhất quán với giá trị nhìn thấy. | UI hiển thị như có giá trị ví dụ/default nhưng native validation vẫn xem select là rỗng. | F-D1-002 | F-D1-002 |
| D1 Tạo support request | IA-01-05 | Đạt | Label, placeholder, nút và alert đọc được trên desktop và mobile. | Không thấy chữ tương phản quá thấp trong lần test D1. | E-D1-001, E-D1-003 |  |
| D1 Tạo support request | IA-01-06 | Không áp dụng | Checklist item nói về card/list sự kiện. | D1 là form support request, không phải card/list sự kiện. |  |  |
| D1 Tạo support request | IA-01-07 | Đạt | Hành động remove attachment có accessible label `Remove D1_create_request_overview.png`. | Icon/action có thể nhận diện qua label. | E-D1-002 |  |
| D1 Tạo support request | IA-01-08 | Đạt | Input, button, upload zone và menu có thể focus/click; select invalid có trạng thái invalid. | Trạng thái tương tác quan sát được. | E-D1-003 |  |
| D1 Tạo support request | IA-01-09 | Đạt | Form giữ lại title, description và attachment sau submit thất bại. | Dữ liệu được bảo toàn sau lỗi validation/API. | F-D1-002 |  |
| D1 Tạo support request | IA-01-10 | Đạt | Ở `390x844`, các field xếp dọc và không thấy tràn ngang. | Layout mobile dùng được. | E-D1-003 |  |
| D1 Tạo support request | IA-01-11 | Đạt | Form được nhóm theo request type, issue, description, attachments và actions. | Mật độ nội dung vừa phải. | E-D1-001 |  |
| D1 Tạo support request | IA-01-12 | Đạt | D1 truy cập nhanh qua user menu `Support requests -> Create request`. | Không thấy luồng điều hướng dư thừa. | E-D1-001 |  |
| D1 Tạo support request | IA-01-13 | Không áp dụng | Chưa kiểm tra chuyển đổi ngôn ngữ trong lần chạy D1 này. | Cần một lượt test EN/VI riêng nếu yêu cầu. |  |  |
| D1 Tạo support request | IA-02-01 | Đạt | Field bắt buộc có dấu `*`: request type, issue, detailed description. | Field bắt buộc hiển thị trước submit. | E-D1-001 |  |
| D1 Tạo support request | IA-02-02 | Đạt | Label hiển thị gần control; form không chỉ dựa vào placeholder. | Placeholder chỉ đóng vai trò ví dụ. | E-D1-001 |  |
| D1 Tạo support request | IA-02-03 | Đạt | Request type dùng select; issue dùng text input; description dùng textarea; attachment dùng file input. | Kiểu control phù hợp với dữ liệu. | E-D1-001 |  |
| D1 Tạo support request | IA-02-04 | Không đạt | Submit form rỗng chỉ validation sau khi submit; nút submit vẫn bật khi thiếu required fields. | Error prevention yếu vì cho phép submit dữ liệu chưa hợp lệ. | F-D1-001 | F-D1-001 |
| D1 Tạo support request | IA-02-05 | Không đạt | Lỗi form rỗng là alert chung; hướng dẫn theo từng field chưa đầy đủ, đặc biệt với request type/category. | Người dùng phải tự suy luận field cần sửa và lý do category nhìn thấy vẫn invalid. | F-D1-001, F-D1-002 | F-D1-001, F-D1-002 |
| D1 Tạo support request | IA-02-06 | Đạt | Title, detailed description và image vẫn còn sau submit thất bại. | Không mất dữ liệu ở nhánh lỗi validation/API. | F-D1-002 |  |
| D1 Tạo support request | IA-02-07 | Đạt | Form D1 ngắn và được nhóm hợp lý; không có section dài không cần thiết. | Nhóm field khớp mô hình tinh thần của support request. | E-D1-001 |  |
| D1 Tạo support request | IA-02-08 | Đạt | Có thể focus request type bằng keyboard và chọn option; tab order đi theo thứ tự form. | Chọn bằng keyboard thành công và cho phép submit cuối cùng. | E-D1-002 |  |
| D1 Tạo support request | IA-02-09 | Không đạt | `Submit request` vẫn bật khi các field bắt buộc còn rỗng. | Người dùng có thể gây lỗi validation không cần thiết. | F-D1-001 | F-D1-001 |
| D1 Tạo support request | IA-02-10 | Không đạt | Request type hiển thị `For example: Support`, nhưng giá trị thật vẫn rỗng cho đến khi người dùng chọn option rõ ràng. | Default/signifier gây hiểu nhầm và dẫn đến lỗi category `400`. | F-D1-002 | F-D1-002 |
| D1 Tạo support request | IA-02-11 | Không đạt | `Cancel` bỏ form đã điền và attachment đã chọn mà không xác nhận. | Người dùng có thể mất nội dung support request chưa lưu. | F-D1-003 | F-D1-003 |
| D1 Tạo support request | IA-02-12 | Đạt | Vùng upload nêu format `JPG, PNG, GIF or WEBP`, tối đa 5 ảnh và 5 MB mỗi ảnh; upload PNG hợp lệ có thumbnail và nút remove. | Điều kiện upload và preview rõ ràng. | E-D1-002 |  |
| D1 Tạo support request | IA-02-13 | Không áp dụng | Checklist item nói về rich-text editor. | D1 dùng detailed-description textarea thường, không phải rich text. |  |  |
| D1 Tạo support request | IA-03-01 | Đạt | User menu có `Events`, `Calendar`, `Saved Events`, `User guide`, `Support requests`, profile và notifications. | Có entry support phù hợp vai trò user. | E-D1-001 |  |
| D1 Tạo support request | IA-03-02 | Đạt | H1 `Create support request`, page title và URL `/complaints/new` xác định vị trí hiện tại. | Người dùng biết đang ở màn hình tạo request. | E-D1-001 |  |
| D1 Tạo support request | IA-03-03 | Không áp dụng | Checklist item nói về việc giữ filter khi đi từ event list sang detail. | D1 không phải luồng duyệt event list/detail. |  |  |
| D1 Tạo support request | IA-03-04 | Đạt | Nhãn điều hướng/hành động cụ thể: `Back`, `Cancel`, `Submit request`, `Create request`. | Không thấy nhãn mơ hồ kiểu `Click here`. | E-D1-001 |  |
| D1 Tạo support request | IA-03-05 | Đạt | User account truy cập được trang support phía user; chức năng quản trị support không lộ trong flow user. | Không thấy sai quyền trong D1. | E-D1-001 |  |
| D1 Tạo support request | IA-03-06 | Không áp dụng | Search/filter thuộc support list D2, không phải create form D1. | Không áp dụng cho D1 form. |  |  |
| D1 Tạo support request | IA-03-07 | Không áp dụng | Pagination thuộc support list D2, không phải create form D1. | Không áp dụng cho D1 form. |  |  |
| D1 Tạo support request | IA-03-08 | Không áp dụng | D1 là form một trang, không phải registration/checkout nhiều bước. | Không cần stepper. |  |  |
| D1 Tạo support request | IA-03-09 | Không đạt | `Cancel` thoát khỏi form đã điền mà không cảnh báo hoặc cho khôi phục. | Điều hướng có thể làm mất dữ liệu chưa lưu. | F-D1-003 | F-D1-003 |
| D1 Tạo support request | IA-03-10 | Đạt | Ở viewport mobile, navigation thu gọn vào menu và không che hành động chính của form. | D1 vẫn dùng được trên phone width. | E-D1-003 |  |
| D1 Tạo support request | IA-03-11 | Đạt | `Submit request` và `Cancel` nằm cuối form, gần nội dung đã nhập. | Hành động đặt đúng ngữ cảnh form. | E-D1-001 |  |
| D1 Tạo support request | IA-03-12 | Không áp dụng | Recovery cho route 404/event đã xóa không liên quan đến form tạo D1. | Không áp dụng. |  |  |
| D1 Tạo support request | IA-04-01 | Không đạt | Submit thành công có redirect và tạo pending request, nhưng không thấy success toast/banner rõ; API success message lại nói về event review. | Người dùng có closure yếu và backend message sai ngữ cảnh support request. | E-D1-004 | F-D1-004 |
| D1 Tạo support request | IA-04-02 | Đạt | Submit hoàn tất nhanh; preview upload xuất hiện sau khi chọn file. | Không cần long loading state trong lần chạy này. | E-D1-002, E-D1-004 |  |
| D1 Tạo support request | IA-04-03 | Đạt | Trong lần submit thành công quan sát được, chỉ có một request được tạo. | Không thấy duplicate request trong danh sách cuối. | E-D1-004 |  |
| D1 Tạo support request | IA-04-04 | Không đạt | API category error trả `400`; recovery trên UI còn hạn chế và chưa giải thích rõ vì sao payload category invalid. | Lỗi kỹ thuật chưa được chuyển thành hướng dẫn dễ hiểu cho người dùng. | F-D1-002 | F-D1-002 |
| D1 Tạo support request | IA-04-05 | Không đạt | Alert form rỗng và alert category invalid xuất hiện gần cuối form; trong trạng thái form dài/scroll, người dùng có thể bỏ lỡ ngữ cảnh field. | Alert thấy được nhưng không nằm gần field lỗi. | F-D1-001, E-D1-003 | F-D1-001 |
| D1 Tạo support request | IA-04-06 | Đạt | Request mới xuất hiện trạng thái `Pending` và có category text trong support list sau submit. | Trạng thái dùng text nhìn thấy được. | E-D1-004 |  |
| D1 Tạo support request | IA-04-07 | Không áp dụng | Empty state thuộc support list, không phải create form D1. | Không áp dụng trong lần D1 này vì list đã có request. |  |  |
| D1 Tạo support request | IA-04-08 | Không áp dụng | D1 không có hành động nguy hiểm phía server như delete/cancel submitted request. | Cancel form chưa lưu đã được cover bởi IA-02-11 và IA-03-09. |  |  |
| D1 Tạo support request | IA-04-09 | Không đạt | Không có undo hoặc recovery sau khi `Cancel` bỏ form đã điền. | Người dùng không thể khôi phục nội dung support request chưa lưu. | F-D1-003 | F-D1-003 |
| D1 Tạo support request | IA-04-10 | Không áp dụng | Không kích hoạt trạng thái session expired trong lần chạy D1 này. | Cần test riêng cho long-session/expired-token. |  |  |
| D1 Tạo support request | IA-04-11 | Không áp dụng | Form tạo D1 không hiển thị dữ liệu động như capacity/status sự kiện. | Không áp dụng. |  |  |
| D1 Tạo support request | IA-04-12 | Đạt | Form có hướng dẫn ngắn và ví dụ cụ thể cho issue và detailed description. | Hướng dẫn inline giúp người dùng viết request rõ hơn. | E-D1-001 |  |
| D1 Tạo support request | IA-04-13 | Không đạt | Luồng kết thúc bằng redirect về list và hiển thị row `Pending` mới, nhưng không có confirmation message rõ; API success body nói `Event review saved successfully`. | Có closure qua list update nhưng message sai ngữ cảnh/không rõ. | E-D1-004 | F-D1-004 |

## 6. Tóm tắt

| Chỉ số | Số lượng |
| --- | ---: |
| Tổng checklist items | 51 |
| Đạt | 27 |
| Không đạt | 12 |
| Không áp dụng | 12 |
| Cần submit Google Form | 4 findings |

## 7. Draft finding cho Bug & Usability Log

| ID | Kịch bản/Màn hình | Loại | Mô tả | Bước/Heuristic | Kỳ vọng | Thực tế | Mức độ nghiêm trọng | Đề xuất sửa | Ảnh tham chiếu | Thời điểm submit Form |
| --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- |
| F-D1-001 | D1 Tạo support request | Usability | Validation field bắt buộc chưa được ngăn sớm và hiển thị bằng alert chung thay vì message cạnh từng field. | IA-02-04, IA-02-05, IA-02-09, IA-04-05. Steps: mở `/complaints/new`; để trống các required fields; bấm `Submit request`. | Submit nên bị disable cho đến khi field bắt buộc hợp lệ, hoặc mỗi field invalid cần có message inline cạnh field đó. | Submit vẫn bật; một alert chung hiển thị `Request type, issue requiring support and detailed description are required.` | 2 | Disable submit cho đến khi required fields hợp lệ và thêm inline errors cạnh request type, issue, description. | `submission/screenshots/checklist-failures/F-D1-001_validation-not-inline.png` | `[Điền thủ công sau khi submit Google Form]` |
| F-D1-002 | D1 Tạo support request | Bug | Request type trông như đã có default/example value, nhưng category thật có thể vẫn rỗng hoặc invalid và submit trả `400`. | IA-01-04, IA-02-05, IA-02-10, IA-04-04. Steps: mở `/complaints/new`; quan sát request type hiển thị `For example: Support`; điền issue/description/upload ảnh; submit mà không chọn rõ một option hợp lệ, hoặc rơi vào trạng thái select lỗi. | Giá trị request type hiển thị và category gửi lên phải khớp một giá trị hợp lệ: `SUPPORT`, `COMPLAINT`, `CONTACT`, hoặc `OTHER`; người dùng cần hướng dẫn recovery rõ. | Network trả `POST /api/complaints => 400` với `category must be one of the following values: SUPPORT, COMPLAINT, CONTACT, OTHER`; console warning ghi `Select: Keys "S" passed to "selectedKeys" are not present in the collection.` | 3 | Sửa mapping state của select, phân biệt placeholder với giá trị thật, và validate category trước khi submit API. | `submission/screenshots/checklist-failures/F-D1-002_category-submit-400-no-clear-ui-error.png` | `[Điền thủ công sau khi submit Google Form]` |
| F-D1-003 | D1 Tạo support request | Usability | `Cancel` bỏ support request đang nhập mà không xác nhận hoặc cho khôi phục. | IA-02-11, IA-03-09, IA-04-09. Steps: nhập issue/description, attach ảnh, bấm `Cancel`. | Nếu có dữ liệu chưa lưu, hệ thống nên xác nhận trước khi rời trang hoặc giữ draft khi quay lại. | Trang chuyển ngay về `/complaints`; không thấy confirmation, undo hoặc draft recovery. | 2 | Thêm xác nhận unsaved changes cho `Cancel`/`Back`, hoặc lưu draft local cho đến khi submit/cancel được xác nhận. | `submission/screenshots/checklist-failures/F-D1-003_cancel-discards-without-confirmation.png` | `[Điền thủ công sau khi submit Google Form]` |
| F-D1-004 | D1 Tạo support request | Bug | Submit D1 thành công nhưng success semantics sai và visible closure yếu. | IA-04-01, IA-04-13. Steps: chọn category bằng keyboard, nhập issue/description hợp lệ, upload PNG, submit. | UI nên hiển thị thông báo tạo support request thành công rõ ràng, ví dụ `Support request created successfully`, rồi hiển thị request mới ở trạng thái pending. | Redirect tới `/complaints?created=1` và request mới xuất hiện, nhưng không thấy success toast/banner rõ; API response body ghi `UPSERT_EVENT_REVIEW_SUCCESS` và `Event review saved successfully.` | 3 | Trả support-specific success code/message và hiển thị success toast/banner rõ sau khi tạo request. | `submission/screenshots/D1/D1_submit_success_redirect.png` | `[Điền thủ công sau khi submit Google Form]` |

## 8. Ghi chú hoàn tất

- Lần thực thi checklist D1 dùng checklist shared từ `submission/group/gui_usability_checklist_final.md` và không sửa file này.
- Playwright MCP đã được dùng để tương tác EMS thật, chụp screenshot, kiểm tra responsive, console và network.
- Chrome DevTools MCP đã được thử nhưng không khởi động được trong môi trường hiện tại vì tool báo thiếu X server cho headful browser startup.
- Một request test thật đã được tạo bằng tài khoản user của Kiên: `/complaints/56`, hiển thị trạng thái `Pending` sau submit thành công.
- Các findings ở trên là draft. Kiên cần review screenshot, submit các finding đã xác nhận lên Google Form, rồi điền giá trị `Form-submission timestamp`.
