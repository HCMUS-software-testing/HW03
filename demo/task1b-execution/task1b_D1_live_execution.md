# Task 1B - Thực thi checklist live cho D1

| Trường | Giá trị |
| --- | --- |
| Người kiểm thử | Lê Trung Kiên |
| Kịch bản | `D - User asks Support, Admin resolves` |
| Màn hình | `D1 - User tạo support request` |
| Vai trò sử dụng | `User` |
| SUT | `https://prod-dev.ems-fitus.cloud` |
| Ngày kiểm thử | `2026-08-06` |
| Công cụ thực thi | `Playwright MCP` |
| Tài khoản | `ltkien23@clc.fitus.edu.vn` |
| Nguồn access note | `submission/test_environment_access.md` |
| Nguồn checklist | `demo/task1a-checklist/gui_usability_checklist_scenario_d.md` |
| Output folder | `demo/task1b-execution` |

## 1. Phạm vi và xác nhận môi trường

- Đăng nhập live thành công bằng tài khoản user được cung cấp.
- Route danh sách support của user: `/complaints`
- Route form tạo support request: `/complaints/new`
- Route sau submit thành công: `/complaints?created=1`
- Request test mới được tạo trong lần chạy này: `/complaints/105`
- Quy tắc an toàn được giữ nguyên: chỉ dùng tài khoản của Kiên và chỉ tạo request test của chính tài khoản này.

## 2. Nhật ký thực thi

| Bước | Quan sát live |
| --- | --- |
| Mở EMS | Điều hướng tới `https://prod-dev.ems-fitus.cloud`, hệ thống chuyển về trang login. |
| Đăng nhập | Login bằng `ltkien23@clc.fitus.edu.vn` thành công, vào `Dashboard`. |
| Điều hướng D1 | Mở menu user, vào `Support requests`, sau đó bấm `Create request`. |
| Xác nhận D1 | Trang mở đúng `Create support request` tại `/complaints/new`. |
| Submit rỗng | Nút `Submit request` vẫn bấm được; UI chỉ hiện alert chung `Request type, issue requiring support and detailed description are required.` |
| Điền form | Nhập issue, detailed description và upload ảnh PNG thành công; thumbnail preview và nút remove xuất hiện. |
| Kiểm tra request type | Trigger mặc định hiển thị `For example: Support`; console phát sinh nhiều warning `Select: Keys "C" passed to "selectedKeys" are not present in the collection.` khi thao tác chọn `Complaint`. |
| Cancel khi có dữ liệu | Bấm `Cancel` trên form đã nhập dữ liệu, hệ thống quay ngay về `/complaints` mà không hiện xác nhận mất dữ liệu. |
| Submit thành công | Sau khi điền lại form và chọn `Complaint`, `POST /api/complaints` trả `201`; hệ thống redirect về `/complaints?created=1`; request mới lên đầu danh sách với trạng thái `Pending`. |
| Success semantics | Response body của request thành công là `UPSERT_EVENT_REVIEW_SUCCESS` / `Event review saved successfully.`, sai ngữ cảnh so với support request. |
| Responsive mobile | Ở viewport `390x844`, form xếp dọc hợp lý, không thấy tràn ngang khi chụp trạng thái validation. |

## 3. UI Inventory D1

| Nhóm | Thành phần quan sát được |
| --- | --- |
| Header và điều hướng | Logo, nút mở menu, `Back`, menu `Support requests`, `Create request` |
| Form controls | `Request type` custom select, `Issue requiring support`, bộ đếm ký tự, `Detailed description`, upload ảnh |
| Attachment area | Vùng `Add evidence images`, helper text định dạng/tối đa, thumbnail preview, nút remove |
| Actions | `Cancel`, `Submit request` |
| Feedback | Alert validation chung, trạng thái invalid của request type, redirect sau submit, row `Pending` mới trong list |

## 4. Bằng chứng screenshot

| ID | Đường dẫn | Mục đích |
| --- | --- | --- |
| E-D1-001 | `demo/task1b-execution/screenshots/D1/D1_support_list_before_create.png` | Danh sách support trước khi vào D1 |
| E-D1-002 | `demo/task1b-execution/screenshots/D1/D1_create_request_overview.png` | Tổng quan giao diện D1 trước khi nhập dữ liệu |
| E-D1-003 | `demo/task1b-execution/screenshots/D1/D1_form_filled_with_attachment.png` | Form đã điền và có preview ảnh |
| E-D1-004 | `demo/task1b-execution/screenshots/D1/D1_submit_success_redirect.png` | Redirect sau submit thành công, request `#105` ở đầu danh sách |
| E-D1-005 | `demo/task1b-execution/screenshots/D1/D1_mobile_validation_layout.png` | Layout mobile và validation trên `390x844` |
| F-D1-001 | `demo/task1b-execution/screenshots/checklist-failures/F-D1-cancel-before-click.png` | Form đã có dữ liệu ngay trước thao tác `Cancel` |

## 5. Bảng thực thi checklist D1

Chỉ liệt kê các item thuộc checklist Scenario D có áp dụng trực tiếp cho `D1`.

| Checklist ID | Kết quả | Quan sát live | Bằng chứng |
| --- | --- | --- | --- |
| IA-01-01 | Passed | Bố cục D1 nhất quán với support list user: header, spacing, button style và typography đồng bộ. | `E-D1-002` |
| IA-01-02 | Passed | Các nhãn `Support requests`, `Create support request`, `Request type`, `Complaint` nhất quán trong flow D1. | `E-D1-002`, `E-D1-004` |
| IA-01-03 | Passed | `Submit request` nổi bật hơn `Cancel`, hành động chính/phụ phân biệt rõ. | `E-D1-002` |
| IA-01-04 | Failed | `Request type` có signifier gây hiểu nhầm: trigger mặc định hiển thị `For example: Support` dù chưa chọn giá trị thật; khi thao tác chọn `Complaint` console phát sinh warning mapping `selectedKeys`. | `E-D1-003` |
| IA-01-05 | Passed | Nội dung và helper text đọc được trên desktop và mobile trong lần test này. | `E-D1-002`, `E-D1-005` |
| IA-01-07 | Passed | Attachment preview có tên file và nút `Remove D1_create_request_overview.png` rõ ràng. | `E-D1-003` |
| IA-01-08 | Passed | Input, textarea, upload area và submit button đều tương tác được; request type có trạng thái invalid rõ sau submit rỗng. | `E-D1-005` |
| IA-01-10 | Passed | Ở `390x844`, form xếp dọc hợp lý, không thấy tràn ngang. | `E-D1-005` |
| IA-01-11 | Passed | Form được nhóm hợp lý theo request type, issue, description, attachments và actions. | `E-D1-002` |
| IA-02-01 | Passed | `Request type`, `Issue requiring support`, `Detailed description` đều có dấu `*`. | `E-D1-002` |
| IA-02-02 | Passed | Form dùng label gần control, không phụ thuộc hoàn toàn vào placeholder. | `E-D1-002` |
| IA-02-03 | Passed | Dữ liệu dùng đúng widget: select, textbox, textarea, file upload. | `E-D1-002` |
| IA-02-04 | Failed | Hệ thống chỉ phát hiện lỗi sau khi bấm submit; không ngăn sớm khi form còn trống. | `E-D1-005` |
| IA-02-05 | Failed | Validation hiện dưới dạng alert chung thay vì chỉ rõ lỗi cạnh từng field. | `E-D1-005` |
| IA-02-06 | Passed | Dữ liệu nhập và attachment preview còn giữ khi form đang ở trạng thái chưa submit thành công. | `E-D1-003` |
| IA-02-07 | Passed | Thứ tự nhóm field phản ánh đúng mental model của việc gửi support request. | `E-D1-002` |
| IA-02-08 | Passed | Có thể mở request type bằng keyboard (`ArrowDown`) và listbox render đủ option. | Ghi nhận từ Playwright live execution |
| IA-02-09 | Failed | `Submit request` vẫn active ngay cả khi chưa điền required fields. | `E-D1-005` |
| IA-02-10 | Failed | Placeholder/default của request type có thể bị hiểu nhầm là đã chọn giá trị hợp lệ. | `E-D1-002`, `E-D1-003` |
| IA-02-11 | Failed | `Cancel` bỏ form có dữ liệu mà không hiện xác nhận. | `F-D1-001` |
| IA-02-12 | Passed | Vùng upload nêu rõ `JPG, PNG, GIF or WEBP`, tối đa 5 ảnh, 5 MB mỗi ảnh; preview xuất hiện sau upload. | `E-D1-003` |
| IA-03-01 | Passed | Menu user có `Support requests` ở ngữ cảnh hợp lý. | `E-D1-001` |
| IA-03-02 | Passed | URL, heading và page title cho biết rõ người dùng đang ở D1. | `E-D1-002` |
| IA-03-04 | Passed | Nhãn `Create request`, `Cancel`, `Submit request`, `Back` đủ cụ thể. | `E-D1-002` |
| IA-03-05 | Passed | Flow D1 chỉ dùng quyền user; không lộ công cụ admin. | `E-D1-001`, `E-D1-002` |
| IA-03-09 | Failed | Sau `Cancel`, hệ thống quay về list ngay, không có cơ chế recovery cho dữ liệu chưa lưu. | `F-D1-001` |
| IA-03-10 | Passed | Mobile navigation không che hành động chính của form trong lần test này. | `E-D1-005` |
| IA-03-11 | Passed | `Submit request` và `Cancel` nằm cuối form, gần ngữ cảnh thao tác. | `E-D1-002` |
| IA-04-01 | Failed | Submit thành công nhưng semantics phản hồi sai ngữ cảnh: response body là `UPSERT_EVENT_REVIEW_SUCCESS` / `Event review saved successfully.` | `E-D1-004` |
| IA-04-02 | Passed | Upload preview và submit response đều phản hồi trong thời gian ngắn; không thấy treo UI. | `E-D1-003`, network `POST /api/complaints => 201` |
| IA-04-03 | Passed | Trong lần test chỉ tạo một request mới `#105`, không thấy duplicate. | `E-D1-004` |
| IA-04-04 | Failed | Thông tin feedback thành công dùng message kỹ thuật/sai domain, không phải support-specific message. | `E-D1-004` |
| IA-04-05 | Failed | Alert validation đủ thấy nhưng không bám sát từng field lỗi. | `E-D1-005` |
| IA-04-08 | Passed | Sau submit, request mới xuất hiện đúng trạng thái `Pending` trong list user. | `E-D1-004` |
| IA-04-11 | Failed | Luồng kết thúc có redirect và row mới, nhưng thiếu confirmation message đúng ngữ cảnh support nên `closure` còn yếu. | `E-D1-004` |

## 6. Tóm tắt kết quả

| Chỉ số | Số lượng |
| --- | ---: |
| Tổng item áp dụng cho D1 đã chạy | 35 |
| Passed | 24 |
| Failed | 11 |
| N/A | 0 |

## 7. Danh sách findings chính

| ID | Loại | Mô tả | Mức độ | Heuristic / Checklist |
| --- | --- | --- | ---: | --- |
| F-D1-001 | Usability | Validation required fields chỉ hiện alert chung; submit vẫn active khi form chưa hợp lệ. | 2 | `IA-02-04`, `IA-02-05`, `IA-02-09`, `IA-04-05` |
| F-D1-002 | Bug + Usability | `Request type` dùng placeholder `For example: Support` dễ gây hiểu nhầm; console warning lặp lại `selectedKeys` cho thấy mapping select không sạch. | 3 | `IA-01-04`, `IA-02-10` |
| F-D1-003 | Usability | `Cancel` bỏ dữ liệu chưa lưu mà không có xác nhận hoặc cơ chế recovery. | 2 | `IA-02-11`, `IA-03-09` |
| F-D1-004 | Bug | Submit thành công nhưng response body trả về message thuộc `event review`, sai ngữ cảnh support request. | 3 | `IA-04-01`, `IA-04-04`, `IA-04-11` |

## 8. Network và console evidence

- `POST https://prod-dev.ems-fitus.cloud/api/complaints` trả `201`
- Request mới sau submit: `/complaints/105`
- Response body:

```json
{"code":"UPSERT_EVENT_REVIEW_SUCCESS","message":"Event review saved successfully.","messageVn":"Lưu đánh giá sự kiện thành công."}
```

- Console không có error.
- Console có `19` warning cùng mẫu:

```text
Select: Keys "C" passed to "selectedKeys" are not present in the collection.
```

## 9. Ghi chú hoàn tất

- Đây là lần thực thi live bằng `Playwright MCP`, không dựa vào screenshot cũ hay report cũ để chấm trạng thái.
- Một support request test thật đã được tạo bằng tài khoản của Kiên trong lần chạy này.
- Report này chỉ bao phủ `D1 - User tạo support request`; `D2` và `D3` chưa được chạy trong output này.
