# Thực thi checklist Scenario C

| Trường             | Giá trị                                             |
| ------------------ | --------------------------------------------------- |
| Sinh viên          | Lâm Hữu Khánh - 23127205                            |
| Kịch bản           | C - Admin quản lý người dùng                        |
| Nguồn checklist    | `submission/group/gui_usability_checklist_final.md` |
| Màn hình           | Xem bảng "Phạm vi màn hình kiểm thử" bên dưới.      |
| Quy ước trạng thái | Pass; Fail                                          |

## Phạm vi màn hình kiểm thử

| Mã màn hình | Tên màn hình                                 | Phạm vi kiểm thử                                                                                                                                                                             |
| ----------- | -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| C1          | Danh sách người dùng / Users Management list | Trang admin quản lý người dùng tại`/dashboard/admin/users`, gồm search, bộ lọc Vai trò/Trạng thái, bảng user, nút Export/Add User, action Edit/Delete và phân trang.                         |
| C2          | Gán vai trò / chỉnh sửa người dùng           | Màn hình hoặc form mở từ action Edit/Add User để xem và cập nhật thông tin người dùng, vai trò, trạng thái và các nút Lưu/Hủy.                                                               |
| C3          | Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu   | Dialog/confirmation liên quan thao tác nhạy cảm trên user như chặn/bỏ chặn tài khoản hoặc đặt lại mật khẩu; chỉ kiểm thử sau khi xác nhận không gây thay đổi dữ liệu nguy hiểm ngoài ý muốn. |

## C1 - Danh sách người dùng / Users Management list

| Màn hình                | Checklist ID | Kết quả | Ghi chú                                                                                                                                                                 | Finding                                 |
| ----------------------- | ------------ | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| C1 Danh sách người dùng | IA-01-01     | Pass    | Header, sidebar, font, color, icon và spacing nhất quán trong admin layout.                                                                                             |                                         |
| C1 Danh sách người dùng | IA-01-02     | Pass    | Thuật ngữ trên màn hình nhất quán: Users Management, User, Role, Member Code, Status, Created, Updated.                                                                 |                                         |
| C1 Danh sách người dùng | IA-01-03     | Pass    | Export và Add User có kiểu nút nổi bật; Edit màu xanh và Delete màu đỏ phân biệt mức độ hành động.                                                                      |                                         |
| C1 Danh sách người dùng | IA-01-04     | Pass    | Badge Active dùng xanh, Delete dùng đỏ, Export xanh và Add User xanh dương nhất quán theo ý nghĩa.                                                                      |                                         |
| C1 Danh sách người dùng | IA-01-05     | Pass    | Chữ trong bảng, badge và nút đủ tương phản trên desktop 1440px. Lỗi responsive mobile/tablet được ghi riêng ở IA-01-10.                                                |                                         |
| C1 Danh sách người dùng | IA-01-06     | Pass    | Dòng user ưu tiên tên/email, vai trò, member code, trạng thái và audit timestamps.                                                                                      |                                         |
| C1 Danh sách người dùng | IA-01-07     | Pass    | Icon filter nằm cạnh tiêu đề cột Vai trò/Trạng thái nên ngữ cảnh thao tác lọc đủ rõ; có thể cải thiện thêm bằng tooltip khi hover/focus.                                |                                         |
| C1 Danh sách người dùng | IA-01-08     | Pass    | Nút previous page có trạng thái disabled khi đang ở trang đầu; các icon thao tác có phản hồi hover/focus đủ nhận biết trong phạm vi quan sát.                           |                                         |
| C1 Danh sách người dùng | IA-01-09     | Pass    | Không phát hiện yêu cầu ghi nhớ thông tin từ trang trước trong C1; danh sách hiển thị đủ tên, email, vai trò, mã thành viên và trạng thái trên cùng dòng.               |                                         |
| C1 Danh sách người dùng | IA-01-10     | Fail    | Trên mobile iPhone SE 375x667 và iPad Pro 1024x1366, sidebar/nội dung Users Management không responsive tốt và bị tràn hoặc bố cục bảng không thích ứng đúng.           | [C-F001](bug_usability_findings_log.md) |
| C1 Danh sách người dùng | IA-01-11     | Pass    | Nội dung bảng có khoảng trắng, header cột, card/table container và phân trang giúp quét nhanh.                                                                          |                                         |
| C1 Danh sách người dùng | IA-01-12     | Pass    | Có search nhanh, filter role/status, Export, Add User và phân trang ngay trên màn hình.                                                                                 |                                         |
| C1 Danh sách người dùng | IA-01-13     | Pass    | Giao diện hiển thị ổn ở cả ngôn ngữ EN/VI trong phạm vi C1; không thấy văn bản bị vỡ bố cục trên desktop. Lỗi responsive được ghi riêng ở IA-01-10.                     |                                         |
| C1 Danh sách người dùng | IA-02-01     | Pass    | C1 không có form nhập dữ liệu bắt buộc; search/filter/pagination không yêu cầu trường bắt buộc nên không phát hiện lỗi.                                                 |                                         |
| C1 Danh sách người dùng | IA-02-02     | Pass    | Search và Go to page có placeholder và aria-label; với màn hình list, nhãn ngữ cảnh đủ nhận biết.                                                                       |                                         |
| C1 Danh sách người dùng | IA-02-03     | Pass    | Search dùng text input, Go to page dùng number input, rows per page dùng select/dropdown.                                                                               |                                         |
| C1 Danh sách người dùng | IA-02-04     | Pass    | Search xử lý giá trị không khớp bằng empty state thay vì lỗi kỹ thuật; chưa phát hiện lỗi validation trên control C1.                                                   |                                         |
| C1 Danh sách người dùng | IA-02-05     | Pass    | Không phát sinh lỗi form/control trên C1 trong phạm vi search/filter quan sát được; empty state được đánh giá riêng ở IA-04-07.                                         |                                         |
| C1 Danh sách người dùng | IA-02-06     | Pass    | C1 không có form submit dài; search/filter không làm mất dữ liệu quan trọng khi kết quả rỗng.                                                                           |                                         |
| C1 Danh sách người dùng | IA-02-07     | Pass    | C1 không có form dài; các control danh sách được nhóm gọn phía trên bảng và phân trang phía dưới.                                                                       |                                         |
| C1 Danh sách người dùng | IA-02-08     | Pass    | Các control chính có aria-label/label nhận diện được; không phát hiện bỏ qua trường quan trọng trong phạm vi C1 quan sát được.                                          |                                         |
| C1 Danh sách người dùng | IA-02-09     | Pass    | C1 không có Submit/Save form; không phát hiện trường hợp gửi dữ liệu chưa đủ điều kiện.                                                                                 |                                         |
| C1 Danh sách người dùng | IA-02-10     | Pass    | Rows per page mặc định 5 và placeholder search/go-to-page phù hợp với list view.                                                                                        |                                         |
| C1 Danh sách người dùng | IA-02-11     | Pass    | C1 không có form có nguy cơ mất dữ liệu; search/filter là thao tác có thể sửa lại trực tiếp.                                                                            |                                         |
| C1 Danh sách người dùng | IA-02-12     | Pass    | C1 không có upload ảnh/tài liệu nên không phát hiện lỗi upload trên màn hình này.                                                                                       |                                         |
| C1 Danh sách người dùng | IA-02-13     | Pass    | C1 không có Rich-Text editor nên không phát hiện lỗi rich-text trên màn hình này.                                                                                       |                                         |
| C1 Danh sách người dùng | IA-03-01     | Pass    | Sidebar admin hiển thị các khu vực chính: Users Management, Categories, Academic Years, Campuses, Events Management, Support requests, User Guide, Analytics, Settings. |                                         |
| C1 Danh sách người dùng | IA-03-02     | Pass    | Tiêu đề Users Management rõ và menu Users Management đang active.                                                                                                       |                                         |
| C1 Danh sách người dùng | IA-03-03     | Pass    | C1 là danh sách người dùng; thao tác phân trang/search/filter giữ người dùng trong ngữ cảnh danh sách và không phát hiện mất trạng thái ngay trong màn hình.            |                                         |
| C1 Danh sách người dùng | IA-03-04     | Pass    | Menu và nút chính có nhãn cụ thể như Users Management, Export, Add User; icon Edit hiển thị tooltip`Sửa` khi hover.                                                     |                                         |
| C1 Danh sách người dùng | IA-03-05     | Pass    | Với admin account, trang Users Management hiển thị đúng khu vực theo vai trò; chưa phát hiện lỗi quyền truy cập trên luồng admin C1.                                    |                                         |
| C1 Danh sách người dùng | IA-03-06     | Pass    | Search dễ thấy; filter role/status mở được danh sách All Roles/Admin/Guest/Lecturer/Student và All Status/Active/Inactive; search rỗng có phản hồi.                     |                                         |
| C1 Danh sách người dùng | IA-03-07     | Pass    | Phân trang hiển thị rows per page, phạm vi 1-5 of 83 results, tổng 17 trang và nút trang.                                                                               |                                         |
| C1 Danh sách người dùng | IA-03-08     | Pass    | C1 không có luồng đăng ký/checkout nhiều bước; không phát hiện thiếu chỉ báo tiến trình trên tác vụ danh sách người dùng.                                               |                                         |
| C1 Danh sách người dùng | IA-03-09     | Pass    | Search/filter trên C1 có thể chỉnh lại tại chỗ và không có dữ liệu chưa lưu bị mất trong phạm vi quan sát.                                                              |                                         |
| C1 Danh sách người dùng | IA-03-10     | Fail    | Admin navigation/table không thích ứng tốt trên mobile 375x667 và iPad Pro 1024x1366; sidebar/bảng làm nội dung bị tràn hoặc cần cuộn ngang để xem đầy đủ.              | [C-F001](bug_usability_findings_log.md) |
| C1 Danh sách người dùng | IA-03-11     | Pass    | Edit/Delete nằm trong cột Actions của từng dòng user, gần đúng bản ghi chịu tác động.                                                                                   |                                         |
| C1 Danh sách người dùng | IA-03-12     | Pass    | Không phát hiện lỗi điều hướng/route trên URL Users Management hợp lệ; màn hình tải đúng thay vì rơi vào ngõ cụt.                                                       |                                         |
| C1 Danh sách người dùng | IA-04-01     | Pass    | Search/filter/pagination phản hồi bằng thay đổi danh sách và phạm vi kết quả; các thao tác thay đổi dữ liệu được kiểm ở C2/C3.                                          |                                         |
| C1 Danh sách người dùng | IA-04-02     | Pass    | Danh sách tải thành công và phản hồi search/filter trong thời gian quan sát; không thấy trạng thái treo hoặc bấm lặp.                                                   |                                         |
| C1 Danh sách người dùng | IA-04-03     | Pass    | C1 không có submit form; không phát hiện rủi ro gửi trùng trong thao tác danh sách.                                                                                     |                                         |
| C1 Danh sách người dùng | IA-04-04     | Pass    | Không phát sinh lỗi hệ thống hoặc stack trace khi load C1 và search/filter.                                                                                             |                                         |
| C1 Danh sách người dùng | IA-04-05     | Pass    | Không có toast/banner che mất dữ liệu trong các thao tác quan sát trên C1.                                                                                              |                                         |
| C1 Danh sách người dùng | IA-04-06     | Pass    | Trạng thái tài khoản hiển thị bằng text Active và badge xanh rõ ràng.                                                                                                   |                                         |
| C1 Danh sách người dùng | IA-04-07     | Fail    | Empty state khi search không có kết quả chỉ hiển thị`No users found matching your filters.` nhưng không có hành động reset/clear filter rõ ràng.                        | [C-F002](bug_usability_findings_log.md) |
| C1 Danh sách người dùng | IA-04-08     | Pass    | Delete là hành động nguy hiểm và có icon riêng; chưa thực hiện xóa dữ liệu thật trên C1, không ghi nhận lỗi xác nhận trong phạm vi không phá dữ liệu.                   |                                         |
| C1 Danh sách người dùng | IA-04-09     | Pass    | Search/filter có thể hoàn tác bằng cách xóa nội dung search hoặc chọn lại filter; điểm thiếu nút clear trong empty state được ghi riêng ở IA-04-07.                     |                                         |
| C1 Danh sách người dùng | IA-04-10     | Pass    | Phiên admin hợp lệ dẫn đúng vào Users Management; không phát hiện lỗi session/access trong lượt kiểm C1.                                                                |                                         |
| C1 Danh sách người dùng | IA-04-11     | Pass    | Danh sách hiển thị updated timestamps/audit information; không phát hiện dữ liệu cũ hoặc cảnh báo sai trong lượt quan sát C1.                                           |                                         |
| C1 Danh sách người dùng | IA-04-12     | Pass    | Sidebar có User Guide trong khu vực admin để hỗ trợ tác vụ quản trị.                                                                                                    |                                         |
| C1 Danh sách người dùng | IA-04-13     | Pass    | C1 là màn hình danh sách, không phải quy trình dài; các thao tác search/filter kết thúc bằng danh sách kết quả hoặc empty state rõ.                                     |                                         |

## C2 - Gán vai trò / chỉnh sửa người dùng

| Màn hình                              | Checklist ID | Kết quả | Ghi chú                                                                                                                                                                           | Finding                                 |
| ------------------------------------- | ------------ | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-01-01     | Pass    | Dialog Add/Edit User dùng cùng admin layout với C1: sidebar, header, font, màu, icon và khoảng cách nhất quán trên desktop 1440px.                                                |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-01-02     | Pass    | Thuật ngữ nhất quán trong phạm vi C2: Users Management, Create New User, Edit User, Role, Active, Cancel, Save Changes/Create User.                                               |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-01-03     | Pass    | Nút Save Changes/Create User dùng màu xanh nổi bật; Cancel là nút phụ; nút đóng X nằm ở header dialog.                                                                            |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-01-04     | Pass    | Validation lỗi dùng viền/chữ đỏ, trạng thái Active dùng checkbox xanh và hành động lưu dùng nút xanh nhất quán theo ý nghĩa.                                                      |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-01-05     | Pass    | Label, input, validation text và nút đủ tương phản trên desktop; vấn đề responsive mobile/tablet được ghi riêng ở IA-01-10.                                                       |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-01-06     | Pass    | Form ưu tiên thông tin thiết yếu của user: họ/tên, email, số điện thoại, role, member code, trạng thái Active và hành động lưu/hủy.                                               |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-01-07     | Pass    | Icon Edit/Add trong tiêu đề dialog đi cùng nhãn chữ; nút đóng có aria-label Close; không phát hiện icon quan trọng bị mơ hồ trong phạm vi C2.                                     |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-01-08     | Pass    | Input, dropdown Role, checkbox Active, Cancel và Save/Create thể hiện rõ là phần tử tương tác; validation đổi viền đỏ sau submit rỗng.                                            |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-01-09     | Pass    | Dialog Edit User hiển thị lại dữ liệu user đã chọn như tên, email, role và trạng thái nên admin không phải nhớ thông tin từ dòng bảng trước đó.                                   |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-01-10     | Fail    | Trên viewport mobile 375x667 và iPad Pro 1024x1366, admin layout/dialog Edit User không responsive tốt và bị tràn hoặc bố cục không thích ứng đúng.                              | [C-F003](bug_usability_findings_log.md) |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-01-11     | Pass    | Dialog dùng nhóm trường hai cột, khoảng trắng và footer action rõ ràng trên desktop, giúp quét nhanh các nhóm thông tin.                                                          |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-01-12     | Pass    | Admin có thể mở nhanh Add User từ toolbar hoặc Edit User từ cột Actions; role có dropdown chọn trực tiếp.                                                                         |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-01-13     | Fail    | Khi giao diện đang dùng ngôn ngữ VI, một số lỗi form vẫn hiển thị tiếng Anh như password policy, `email already use` và `this member code is already in use`, làm trải nghiệm đa ngôn ngữ không đồng bộ. | [C-F005](bug_usability_findings_log.md); [C-F010](bug_usability_findings_log.md); [C-F011](bug_usability_findings_log.md) |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-02-01     | Fail    | Các trường bắt buộc chỉ rõ sau khi submit rỗng; trước submit không có dấu hiệu bắt buộc rõ, lỗi First Name/Last Name bị đảo nội dung, và Phone Number không giải thích trước quy tắc 10 số bắt đầu bằng 0. | [C-F004](bug_usability_findings_log.md); [C-F007](bug_usability_findings_log.md) |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-02-02     | Fail    | Add User form có label First Name nhưng placeholder là`Last Name`, label Last Name nhưng placeholder là `First Name`, gây nhầm nghĩa trường nhập.                                 | [C-F004](bug_usability_findings_log.md) |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-02-03     | Fail    | Phone Number là dữ liệu số điện thoại nhưng input vẫn cho nhập ký tự chữ; Role dropdown cũng để placeholder chọn vai trò nằm cùng cấp với các role thật, nên control/constraint chưa phù hợp hoàn toàn. | [C-F008](bug_usability_findings_log.md); [C-F009](bug_usability_findings_log.md) |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-02-04     | Fail    | Email validation chưa chặn đúng định dạng không hợp lệ; Phone Number cho nhập chữ và Role placeholder vẫn chọn được rồi mới báo lỗi khi submit, chưa ngăn lỗi sớm tại trường nhập. | [C-F006](bug_usability_findings_log.md); [C-F008](bug_usability_findings_log.md); [C-F009](bug_usability_findings_log.md) |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-02-05     | Fail    | Thông báo lỗi form có tám vấn đề: First/Last Name bị đảo nội dung, password policy không nhất quán/ngôn ngữ chưa đồng bộ, email dạng `@g` không bị báo lỗi trước khi submit thành công, Phone Number thiếu hướng dẫn định dạng, Phone Number cho nhập chữ, Role placeholder được chọn như option thật, email sau khi xóa user báo `email already use`, và lỗi Member Code trùng hiển thị tiếng Anh dù đang ở VI. | [C-F004](bug_usability_findings_log.md); [C-F005](bug_usability_findings_log.md); [C-F006](bug_usability_findings_log.md); [C-F007](bug_usability_findings_log.md); [C-F008](bug_usability_findings_log.md); [C-F009](bug_usability_findings_log.md); [C-F010](bug_usability_findings_log.md); [C-F011](bug_usability_findings_log.md) |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-02-06     | Pass    | Sau submit rỗng, dialog vẫn giữ nguyên trạng thái và hiển thị lỗi tại chỗ; khi Edit User mở, dữ liệu hiện có của user được prefill.                                               |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-02-07     | Pass    | Form C2 không quá dài và được nhóm hợp lý theo thông tin cá nhân, liên hệ, role/member code, trạng thái và hành động.                                                             |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-02-08     | Pass    | Thứ tự DOM/control quan sát được đi theo luồng đọc tự nhiên: First Name, Last Name, Email, Phone Number, Role, Member Code, Password nếu tạo mới, Active, Cancel, Submit.         |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-02-09     | Pass    | Create User không disabled khi form rỗng nhưng sau submit hiển thị cảnh báo rõ tại các trường bắt buộc; không gửi dữ liệu thật trong lượt kiểm do route ghi bị abort.             |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-02-10     | Fail    | Edit User prefill giá trị hiện có và Active có mặc định phù hợp, nhưng Phone Number thiếu gợi ý định dạng và Role dropdown dùng placeholder như option có thể chọn. | [C-F007](bug_usability_findings_log.md); [C-F009](bug_usability_findings_log.md) |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-02-11     | Pass    | Dialog có Cancel và Close để thoát thao tác; trong lượt kiểm, hủy form quay lại danh sách mà không lưu thay đổi.                                                                  |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-02-12     | Pass    | C2 không có upload ảnh/tài liệu nên không phát hiện lỗi upload trong phạm vi màn hình này.                                                                                        |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-02-13     | Pass    | C2 không có Rich-Text editor nên không phát hiện lỗi rich-text trong phạm vi màn hình này.                                                                                        |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-03-01     | Pass    | Sidebar admin vẫn hiển thị các khu vực chính như Users Management, Categories, Events Management, Support requests, User Guide, Analytics và Settings.                            |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-03-02     | Pass    | Người dùng thấy tiêu đề Users Management và title dialog Create New User/Edit User, cho biết đang ở đúng tác vụ quản lý người dùng.                                               |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-03-03     | Pass    | Sau khi Cancel/Close dialog, admin quay lại danh sách Users Management cùng ngữ cảnh bảng hiện tại.                                                                               |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-03-04     | Pass    | Nút và liên kết điều hướng/hành động dùng tên cụ thể như Add User, Edit User, Cancel, Create User và Save Changes.                                                                |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-03-05     | Pass    | Với admin account, trang Users Management và dialog Add/Edit User truy cập được đúng quyền; không phát hiện lỗi quyền truy cập trong lượt kiểm C2.                                |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-03-06     | Pass    | Search/filter thuộc ngữ cảnh danh sách Users Management vẫn hiển thị phía sau dialog; không phát hiện lỗi reset/filter trong phạm vi mở/hủy C2.                                   |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-03-07     | Pass    | Phân trang của Users Management vẫn hiển thị số kết quả 1-5 of 96 results và trạng thái trang phía sau dialog; không phát hiện mất ngữ cảnh danh sách.                            |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-03-08     | Pass    | C2 không phải luồng đăng ký/checkout nhiều bước; tác vụ tạo/sửa user diễn ra trong một dialog có điểm kết thúc rõ.                                                                |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-03-09     | Pass    | Cancel/Close cho phép thoát dialog và quay lại danh sách; không ghi nhận lưu thay đổi ngoài ý muốn trong lượt kiểm.                                                               |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-03-10     | Fail    | Navigation/table không thích ứng tốt trên mobile 375x667 và iPad Pro 1024x1366 khi mở Edit User; dialog/nền trang bị tràn hoặc cần cuộn ngang để thấy đầy đủ nội dung/action.     | [C-F003](bug_usability_findings_log.md) |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-03-11     | Pass    | Edit User được mở từ nút Edit trong cột Actions của từng dòng user; dialog hiển thị dữ liệu đúng user được chọn.                                                                  |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-03-12     | Pass    | URL`/dashboard/admin/users` hợp lệ tải đúng Users Management và dialog Add/Edit thay vì rơi vào 404 hoặc empty route.                                                             |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-04-01     | Fail    | Phản hồi lỗi sau khi tạo user chưa đủ rõ trong trường hợp email của user đã xóa vẫn bị báo đang dùng mà UI không giải thích hậu quả xóa/soft delete. | [C-F010](bug_usability_findings_log.md) |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-04-02     | Pass    | Danh sách và dialog Add/Edit tải trong thời gian quan sát; không thấy trạng thái treo hoặc thiếu loading kéo dài.                                                                 |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-04-03     | Pass    | Submit rỗng bị giữ lại bằng client validation, không phát sinh request ghi dữ liệu trong lượt kiểm có route abort; chưa ghi nhận rủi ro gửi trùng trong phạm vi C2 an toàn.       |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-04-04     | Fail    | Một số lỗi form dùng thông báo tiếng Anh/mơ hồ trong giao diện VI như `email already use` và `this member code is already in use`, chưa giúp admin hiểu nguyên nhân và cách xử lý. | [C-F010](bug_usability_findings_log.md); [C-F011](bug_usability_findings_log.md) |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-04-05     | Pass    | Validation hiển thị ngay dưới trường lỗi và không che nút Cancel/Create User; không có toast/banner che dữ liệu trong lượt kiểm C2.                                               |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-04-06     | Pass    | Trạng thái tài khoản hiển thị bằng checkbox Active trong form và badge Active trong danh sách phía sau.                                                                           |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-04-07     | Pass    | C2 không có empty state danh sách trong phạm vi Add/Edit dialog; empty state search đã được kiểm ở C1.                                                                            |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-04-08     | Fail    | Luồng xóa user không làm rõ hậu quả email của user đã xóa có còn bị giữ/không được tái sử dụng hay không, dẫn đến lỗi `email already use` khi tạo lại. | [C-F010](bug_usability_findings_log.md) |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-04-09     | Pass    | Admin có thể hoàn tác thao tác chưa lưu bằng Cancel hoặc Close; không lưu dữ liệu khi hủy dialog trong lượt kiểm.                                                                 |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-04-10     | Pass    | Phiên admin hợp lệ truy cập được Users Management và dialog C2; không phát hiện lỗi session/access sau login bằng Playwright.                                                     |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-04-11     | Pass    | Danh sách phía sau dialog hiển thị audit timestamps Created/Updated; không phát hiện cảnh báo dữ liệu cũ trong lượt kiểm mở/hủy C2.                                               |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-04-12     | Pass    | Sidebar có User Guide cho khu vực admin; form C2 đủ ngắn nên không cần trợ giúp dài ngay trong dialog.                                                                            |                                         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-04-13     | Fail    | Quy trình xóa rồi tạo lại user chưa có điểm kết thúc rõ về việc email cũ có thể tái sử dụng hay không. | [C-F010](bug_usability_findings_log.md) |

## C3 - Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu

| Màn hình                                      | Checklist ID | Kết quả      | Ghi chú | Finding |
| --------------------------------------------- | ------------ | ------------ | ------- | ------- |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-01-01     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-01-02     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-01-03     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-01-04     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-01-05     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-01-06     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-01-07     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-01-08     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-01-09     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-01-10     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-01-11     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-01-12     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-01-13     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-02-01     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-02-02     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-02-03     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-02-04     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-02-05     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-02-06     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-02-07     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-02-08     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-02-09     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-02-10     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-02-11     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-02-12     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-02-13     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-03-01     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-03-02     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-03-03     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-03-04     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-03-05     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-03-06     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-03-07     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-03-08     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-03-09     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-03-10     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-03-11     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-03-12     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-04-01     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-04-02     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-04-03     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-04-04     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-04-05     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-04-06     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-04-07     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-04-08     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-04-09     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-04-10     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-04-11     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-04-12     | Chờ kiểm thử |         |         |
| C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu | IA-04-13     | Chờ kiểm thử |         |         |

## Template chi tiết lỗi

| Trường                | Nội dung                                                      |
| --------------------- | ------------------------------------------------------------- |
| Mã finding            | C-F001                                                        |
| Màn hình              | C1 / C2 / C3                                                  |
| Checklist ID          | IA-..-..                                                      |
| Loại                  | Bug / Usability                                               |
| Các bước tái hiện     | 1. Mở EMS bằng tài khoản admin. 2. Vào màn hình Users. 3. ... |
| Kết quả mong đợi      |                                                               |
| Kết quả thực tế       |                                                               |
| Mức độ nghiêm trọng   | 1 Cosmetic; 2 Minor; 3 Major; 4 Critical                      |
| Ảnh minh chứng        | `submission/screenshots/checklist-failures/C-F001.png`        |
| Timestamp Google Form |                                                               |
