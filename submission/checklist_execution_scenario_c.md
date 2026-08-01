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
| C1          | Danh sách người dùng / Users Management list | Trang admin quản lý người dùng tại `/dashboard/admin/users`, gồm search, bộ lọc Vai trò/Trạng thái, bảng user, nút Export/Add User, action Edit/Delete và phân trang.                        |
| C2          | Gán vai trò / chỉnh sửa người dùng           | Màn hình hoặc form mở từ action Edit/Add User để xem và cập nhật thông tin người dùng, vai trò, trạng thái và các nút Lưu/Hủy.                                                               |
| C3          | Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu   | Dialog/confirmation liên quan thao tác nhạy cảm trên user như chặn/bỏ chặn tài khoản hoặc đặt lại mật khẩu; chỉ kiểm thử sau khi xác nhận không gây thay đổi dữ liệu nguy hiểm ngoài ý muốn. |

## C1 - Danh sách người dùng / Users Management list

| Màn hình                | Checklist ID | Kết quả | Ghi chú                                                                                                                                                                 | Finding                                    |
| ----------------------- | ------------ | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| C1 Danh sách người dùng | IA-01-01     | Pass    | Header, sidebar, font, color, icon và spacing nhất quán trong admin layout.                                                                                             |                                            |
| C1 Danh sách người dùng | IA-01-02     | Pass    | Thuật ngữ trên màn hình nhất quán: Users Management, User, Role, Member Code, Status, Created, Updated.                                                                 |                                            |
| C1 Danh sách người dùng | IA-01-03     | Pass    | Export và Add User có kiểu nút nổi bật; Edit màu xanh và Delete màu đỏ phân biệt mức độ hành động.                                                                      |                                            |
| C1 Danh sách người dùng | IA-01-04     | Pass    | Badge Active dùng xanh, Delete dùng đỏ, Export xanh và Add User xanh dương nhất quán theo ý nghĩa.                                                                      |                                            |
| C1 Danh sách người dùng | IA-01-05     | Pass    | Chữ trong bảng, badge và nút đủ tương phản trên desktop 1440px. Mobile layout được ghi riêng ở IA-01-10.                                                                |                                            |
| C1 Danh sách người dùng | IA-01-06     | Pass    | Dòng user ưu tiên tên/email, vai trò, member code, trạng thái và audit timestamps.                                                                                      |                                            |
| C1 Danh sách người dùng | IA-01-07     | Pass    | Icon filter nằm cạnh tiêu đề cột Vai trò/Trạng thái nên ngữ cảnh thao tác lọc đủ rõ; có thể cải thiện thêm bằng tooltip khi hover/focus.                                |                                            |
| C1 Danh sách người dùng | IA-01-08     | Pass    | Nút previous page có trạng thái disabled khi đang ở trang đầu; các icon thao tác có phản hồi hover/focus đủ nhận biết trong phạm vi quan sát.                           |                                            |
| C1 Danh sách người dùng | IA-01-09     | Pass    | Không phát hiện yêu cầu ghi nhớ thông tin từ trang trước trong C1; danh sách hiển thị đủ tên, email, vai trò, mã thành viên và trạng thái trên cùng dòng.               |                                            |
| C1 Danh sách người dùng | IA-01-10     | Fail    | Trên màn hình mobile iPhone SE 375x667, sidebar và nội dung admin bị tràn ngang; người dùng phải vuốt ngang mới xem được đầy đủ nội dung.                              | [C-F001](bug_usability_findings_log.md:13) |
| C1 Danh sách người dùng | IA-01-11     | Pass    | Nội dung bảng có khoảng trắng, header cột, card/table container và phân trang giúp quét nhanh.                                                                          |                                            |
| C1 Danh sách người dùng | IA-01-12     | Pass    | Có search nhanh, filter role/status, Export, Add User và phân trang ngay trên màn hình.                                                                                 |                                            |
| C1 Danh sách người dùng | IA-01-13     | Pass    | Giao diện hiển thị ổn ở cả ngôn ngữ EN/VI trong phạm vi C1; không thấy văn bản bị vỡ bố cục trên desktop. Lỗi mobile được ghi riêng ở IA-01-10.                         |                                            |
| C1 Danh sách người dùng | IA-02-01     | Pass    | C1 không có form nhập dữ liệu bắt buộc; search/filter/pagination không yêu cầu trường bắt buộc nên không phát hiện lỗi.                                                 |                                            |
| C1 Danh sách người dùng | IA-02-02     | Pass    | Search và Go to page có placeholder và aria-label; với màn hình list, nhãn ngữ cảnh đủ nhận biết.                                                                       |                                            |
| C1 Danh sách người dùng | IA-02-03     | Pass    | Search dùng text input, Go to page dùng number input, rows per page dùng select/dropdown.                                                                               |                                            |
| C1 Danh sách người dùng | IA-02-04     | Pass    | Search xử lý giá trị không khớp bằng empty state thay vì lỗi kỹ thuật; chưa phát hiện lỗi validation trên control C1.                                                   |                                            |
| C1 Danh sách người dùng | IA-02-05     | Pass    | Không phát sinh lỗi form/control trên C1 trong phạm vi search/filter quan sát được; empty state được đánh giá riêng ở IA-04-07.                                         |                                            |
| C1 Danh sách người dùng | IA-02-06     | Pass    | C1 không có form submit dài; search/filter không làm mất dữ liệu quan trọng khi kết quả rỗng.                                                                           |                                            |
| C1 Danh sách người dùng | IA-02-07     | Pass    | C1 không có form dài; các control danh sách được nhóm gọn phía trên bảng và phân trang phía dưới.                                                                       |                                            |
| C1 Danh sách người dùng | IA-02-08     | Pass    | Các control chính có aria-label/label nhận diện được; không phát hiện bỏ qua trường quan trọng trong phạm vi C1 quan sát được.                                          |                                            |
| C1 Danh sách người dùng | IA-02-09     | Pass    | C1 không có Submit/Save form; không phát hiện trường hợp gửi dữ liệu chưa đủ điều kiện.                                                                                 |                                            |
| C1 Danh sách người dùng | IA-02-10     | Pass    | Rows per page mặc định 5 và placeholder search/go-to-page phù hợp với list view.                                                                                        |                                            |
| C1 Danh sách người dùng | IA-02-11     | Pass    | C1 không có form có nguy cơ mất dữ liệu; search/filter là thao tác có thể sửa lại trực tiếp.                                                                            |                                            |
| C1 Danh sách người dùng | IA-02-12     | Pass    | C1 không có upload ảnh/tài liệu nên không phát hiện lỗi upload trên màn hình này.                                                                                       |                                            |
| C1 Danh sách người dùng | IA-02-13     | Pass    | C1 không có Rich-Text editor nên không phát hiện lỗi rich-text trên màn hình này.                                                                                       |                                            |
| C1 Danh sách người dùng | IA-03-01     | Pass    | Sidebar admin hiển thị các khu vực chính: Users Management, Categories, Academic Years, Campuses, Events Management, Support requests, User Guide, Analytics, Settings. |                                            |
| C1 Danh sách người dùng | IA-03-02     | Pass    | Tiêu đề Users Management rõ và menu Users Management đang active.                                                                                                       |                                            |
| C1 Danh sách người dùng | IA-03-03     | Pass    | C1 là danh sách người dùng; thao tác phân trang/search/filter giữ người dùng trong ngữ cảnh danh sách và không phát hiện mất trạng thái ngay trong màn hình.            |                                            |
| C1 Danh sách người dùng | IA-03-04     | Pass    | Menu và nút chính có nhãn cụ thể như Users Management, Export, Add User; icon Edit hiển thị tooltip `Sửa` khi hover.                                                    |                                            |
| C1 Danh sách người dùng | IA-03-05     | Pass    | Với admin account, trang Users Management hiển thị đúng khu vực theo vai trò; chưa phát hiện lỗi quyền truy cập trên luồng admin C1.                                    |                                            |
| C1 Danh sách người dùng | IA-03-06     | Pass    | Search dễ thấy; filter role/status mở được danh sách All Roles/Admin/Guest/Lecturer/Student và All Status/Active/Inactive; search rỗng có phản hồi.                     |                                            |
| C1 Danh sách người dùng | IA-03-07     | Pass    | Phân trang hiển thị rows per page, phạm vi 1-5 of 83 results, tổng 17 trang và nút trang.                                                                               |                                            |
| C1 Danh sách người dùng | IA-03-08     | Pass    | C1 không có luồng đăng ký/checkout nhiều bước; không phát hiện thiếu chỉ báo tiến trình trên tác vụ danh sách người dùng.                                               |                                            |
| C1 Danh sách người dùng | IA-03-09     | Pass    | Search/filter trên C1 có thể chỉnh lại tại chỗ và không có dữ liệu chưa lưu bị mất trong phạm vi quan sát.                                                              |                                            |
| C1 Danh sách người dùng | IA-03-10     | Fail    | Mobile admin navigation/table không thích ứng tốt; sidebar chiếm gần hết chiều ngang và bảng bị ép còn một phần cột Actions, tạo cuộn ngang lớn.                        | [C-F001](bug_usability_findings_log.md:13) |
| C1 Danh sách người dùng | IA-03-11     | Pass    | Edit/Delete nằm trong cột Actions của từng dòng user, gần đúng bản ghi chịu tác động.                                                                                   |                                            |
| C1 Danh sách người dùng | IA-03-12     | Pass    | Không phát hiện lỗi điều hướng/route trên URL Users Management hợp lệ; màn hình tải đúng thay vì rơi vào ngõ cụt.                                                       |                                            |
| C1 Danh sách người dùng | IA-04-01     | Pass    | Search/filter/pagination phản hồi bằng thay đổi danh sách và phạm vi kết quả; các thao tác thay đổi dữ liệu được kiểm ở C2/C3.                                          |                                            |
| C1 Danh sách người dùng | IA-04-02     | Pass    | Danh sách tải thành công và phản hồi search/filter trong thời gian quan sát; không thấy trạng thái treo hoặc bấm lặp.                                                   |                                            |
| C1 Danh sách người dùng | IA-04-03     | Pass    | C1 không có submit form; không phát hiện rủi ro gửi trùng trong thao tác danh sách.                                                                                     |                                            |
| C1 Danh sách người dùng | IA-04-04     | Pass    | Không phát sinh lỗi hệ thống hoặc stack trace khi load C1 và search/filter.                                                                                             |                                            |
| C1 Danh sách người dùng | IA-04-05     | Pass    | Không có toast/banner che mất dữ liệu trong các thao tác quan sát trên C1.                                                                                              |                                            |
| C1 Danh sách người dùng | IA-04-06     | Pass    | Trạng thái tài khoản hiển thị bằng text Active và badge xanh rõ ràng.                                                                                                   |                                            |
| C1 Danh sách người dùng | IA-04-07     | Fail    | Empty state khi search không có kết quả chỉ hiển thị `No users found matching your filters.` nhưng không có hành động reset/clear filter rõ ràng.                       | [C-F002](bug_usability_findings_log.md:14) |
| C1 Danh sách người dùng | IA-04-08     | Pass    | Delete là hành động nguy hiểm và có icon riêng; chưa thực hiện xóa dữ liệu thật trên C1, không ghi nhận lỗi xác nhận trong phạm vi không phá dữ liệu.                   |                                            |
| C1 Danh sách người dùng | IA-04-09     | Pass    | Search/filter có thể hoàn tác bằng cách xóa nội dung search hoặc chọn lại filter; điểm thiếu nút clear trong empty state được ghi riêng ở IA-04-07.                     |                                            |
| C1 Danh sách người dùng | IA-04-10     | Pass    | Phiên admin hợp lệ dẫn đúng vào Users Management; không phát hiện lỗi session/access trong lượt kiểm C1.                                                                |                                            |
| C1 Danh sách người dùng | IA-04-11     | Pass    | Danh sách hiển thị updated timestamps/audit information; không phát hiện dữ liệu cũ hoặc cảnh báo sai trong lượt quan sát C1.                                           |                                            |
| C1 Danh sách người dùng | IA-04-12     | Pass    | Sidebar có User Guide trong khu vực admin để hỗ trợ tác vụ quản trị.                                                                                                    |                                            |
| C1 Danh sách người dùng | IA-04-13     | Pass    | C1 là màn hình danh sách, không phải quy trình dài; các thao tác search/filter kết thúc bằng danh sách kết quả hoặc empty state rõ.                                     |                                            |

## C2 - Gán vai trò / chỉnh sửa người dùng

| Màn hình                              | Checklist ID | Kết quả      | Ghi chú | Finding |
| ------------------------------------- | ------------ | ------------ | ------- | ------- |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-01-01     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-01-02     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-01-03     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-01-04     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-01-05     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-01-06     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-01-07     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-01-08     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-01-09     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-01-10     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-01-11     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-01-12     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-01-13     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-02-01     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-02-02     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-02-03     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-02-04     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-02-05     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-02-06     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-02-07     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-02-08     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-02-09     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-02-10     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-02-11     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-02-12     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-02-13     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-03-01     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-03-02     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-03-03     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-03-04     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-03-05     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-03-06     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-03-07     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-03-08     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-03-09     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-03-10     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-03-11     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-03-12     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-04-01     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-04-02     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-04-03     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-04-04     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-04-05     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-04-06     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-04-07     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-04-08     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-04-09     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-04-10     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-04-11     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-04-12     | Chờ kiểm thử |         |         |
| C2 Gán vai trò / chỉnh sửa người dùng | IA-04-13     | Chờ kiểm thử |         |         |

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
