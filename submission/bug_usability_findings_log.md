# Log tổng hợp bug và usability findings

| Trường      | Giá trị                             |
| ----------- | ----------------------------------- |
| Sinh viên   | Lâm Hữu Khánh - 23127205            |
| Kịch bản    | C - Admin quản lý người dùng        |
| Google Form | https://forms.gle/CJQFQCAXcsDbXDMM9 |

Mọi defect hoặc đề xuất cải thiện tính khả dụng từ checklist execution, user testing và cross-platform testing phải xuất hiện ở cả file này và Google Form. Cột `Timestamp form` là khóa đối chiếu.

## Bảng tổng hợp finding

| ID     | Màn hình                              | Loại      | Mức độ | Tóm tắt                                                                                   | Timestamp form       |
| ------ | ------------------------------------- | --------- | ------ | ----------------------------------------------------------------------------------------- | -------------------- |
| C-F001 | C1 Danh sách người dùng               | Usability | 3      | Layout Users Management không responsive tốt trên mobile/tablet.                          | Chờ sinh viên submit |
| C-F002 | C1 Danh sách người dùng               | Usability | 2      | Empty state search thiếu hành động phục hồi.                                              | Chờ sinh viên submit |
| C-F003 | C2 Gán vai trò / chỉnh sửa người dùng | Usability | 3      | Dialog Edit User/admin layout không responsive tốt trên mobile/tablet.                    | Chờ sinh viên submit |
| C-F004 | C2 Gán vai trò / chỉnh sửa người dùng | Usability | 2      | Add User form đảo placeholder/thông báo lỗi First Name và Last Name.                      | Chờ sinh viên submit |
| C-F005 | C2 Gán vai trò / chỉnh sửa người dùng | Usability | 2      | Password validation không nhất quán và lỗi tiếng Anh khi đang ở VI.                       | Chờ sinh viên submit |
| C-F006 | C2 Gán vai trò / chỉnh sửa người dùng | Bug       | 3      | Email validation cho phép submit email không hợp lệ dạng`@g`.                             | Chờ sinh viên submit |
| C-F007 | C2 Gán vai trò / chỉnh sửa người dùng | Usability | 2      | Phone Number thiếu gợi ý quy tắc 10 số bắt đầu bằng 0.                                    | Chờ sinh viên submit |
| C-F008 | C2 Gán vai trò / chỉnh sửa người dùng | Usability | 2      | Phone Number cho nhập chữ, chỉ báo lỗi sau submit.                                        | Chờ sinh viên submit |
| C-F009 | C2 Gán vai trò / chỉnh sửa người dùng | Usability | 2      | Role dropdown cho chọn placeholder như option thật rồi mới báo lỗi.                       | Chờ sinh viên submit |
| C-F010 | C2 Gán vai trò / chỉnh sửa người dùng | Usability | 3      | Xóa user rồi tạo lại email cũ báo`email already use` bằng tiếng Anh.                      | Chờ sinh viên submit |
| C-F011 | C2 Gán vai trò / chỉnh sửa người dùng | Usability | 2      | Member Code trùng được chặn đúng nhưng lỗi hiển thị tiếng Anh khi đang ở VI.              | Chờ sinh viên submit |
| C-F012 | C3 Block/Unblock và Reset Password    | Usability | 3      | Block/Unblock bị biểu diễn mơ hồ qua Active/Inactive và không thấy Reset Password action. | Chờ sinh viên submit |
| C-F013 | C3 Block/Unblock và Reset Password    | Usability | 3      | Đổi trạng thái Active/Inactive thiếu xác nhận nguy hiểm riêng.                            | Chờ sinh viên submit |

## Chi tiết finding

### C-F001 - Layout Users Management không responsive tốt

**Nguồn:** Checklist execution C1

**Màn hình:** C1 Danh sách người dùng

**Loại:** Usability

**Mức độ:** 3

**Mô tả:** Layout Users Management không responsive tốt trên mobile 375x667 và iPad Pro 1024x1366.

**Bước tái hiện / minh chứng:**

1. Đăng nhập admin.
2. Mở Users Management trên viewport 375x667 hoặc iPad Pro 1024x1366.
3. Quan sát sidebar, header, table và pagination.

**Kết quả mong đợi:**

Mobile/tablet layout không làm mất nội dung, không che nút chính và không buộc cuộn ngang quá mức ngoài vùng bảng hợp lý.

**Kết quả thực tế:**

Trên mobile, sidebar vẫn chiếm phần lớn chiều ngang và nội dung chính bị ép hẹp; trên iPad Pro 1024x1366, layout bảng/sidebar cũng không thích ứng đúng.

**Đề xuất sửa:**

Dùng mobile/tablet drawer hoặc collapsed sidebar mặc định, cho table có responsive card layout hoặc horizontal scroll confined trong vùng bảng, không làm toàn trang tràn ngang.

**Ảnh minh chứng:**

<img src="screenshots/checklist-failures/C-F001-01.png"  alt="C-F001 evidence-1">
<img src="screenshots/checklist-failures/C-F001-02.png"  alt="C-F001 evidence-2">

**Timestamp form:**
Phản ánh lúc 22:43 ngày 02/08/2026
<img src="screenshots/checklist-failures/C-F001-form.png" alt="C-F001 Google Form submission evidence">

### C-F002 - Empty state search thiếu hành động phục hồi

**Nguồn:** Checklist execution C1

**Màn hình:** C1 Danh sách người dùng

**Loại:** Usability

**Mức độ:** 2

**Mô tả:** Empty state khi search không có kết quả thiếu hành động phục hồi rõ ràng.

**Bước tái hiện / minh chứng:**

1. Đăng nhập admin.
2. Vào Users Management.
3. Nhập `zzzz-no-user-23127205` vào Search users.

**Kết quả mong đợi:**

Empty state giải thích ngắn gọn và cung cấp hành động tiếp theo như Clear search hoặc Reset filters.

**Kết quả thực tế:**

Hệ thống hiển thị`No users found matching your filters.` nhưng không có nút Clear/Reset rõ ràng trong empty state.

**Đề xuất sửa:**

Thêm nút`Clear search` hoặc `Reset filters` ngay trong empty state và hiển thị tiêu chí đang áp dụng.

**Ảnh minh chứng:**

<img src="screenshots/checklist-failures/C-F002.png" alt="C-F002 evidence">

**Timestamp form:**
Phản ánh lúc 22:45 ngày 02/08/2026

<img src="screenshots/checklist-failures/C-F002-form.png" alt="C-F002 Google Form submission evidence">

### C-F003 - Dialog Edit User không responsive tốt

**Nguồn:** Checklist execution C2

**Màn hình:** C2 Gán vai trò / chỉnh sửa người dùng

**Loại:** Usability

**Mức độ:** 3

**Mô tả:** Dialog Edit User và admin layout không responsive tốt trên mobile 375x667 và iPad Pro 1024x1366.

**Bước tái hiện / minh chứng:**

1. Đăng nhập admin.
2. Vào Users Management trên viewport 375x667 hoặc iPad Pro 1024x1366.
3. Bấm Edit user ở dòng đầu tiên và quan sát dialog/nền admin.

**Kết quả mong đợi:**

Dialog chỉnh sửa user và nền admin không làm mất nội dung, không che hành động chính và không buộc cuộn ngang toàn trang trên mobile/tablet.

**Kết quả thực tế:**

Trên mobile, Playwright ghi nhận`scrollWidth=1018` trong viewport 375px; trên iPad Pro 1024x1366, layout/dialog cũng không thích ứng đúng.

**Đề xuất sửa:**

Dùng mobile/tablet drawer hoặc collapsed sidebar, giới hạn chiều rộng dialog bằng`max-width: calc(100vw - 32px)`, và cho bảng phía sau scroll trong container thay vì làm toàn trang tràn ngang.

**Ảnh minh chứng:**

<img src="screenshots/checklist-failures/C-F003-01.png" alt="C-F003 evidence-1">
<img src="screenshots/checklist-failures/C-F003-02.png" alt="C-F003 evidence-2">

**Timestamp form:**
Phản ánh lúc 22:49 ngày 02/08/2026
<img src="screenshots/checklist-failures/C-F003-form.png" alt="C-F003 Google Form submission evidence">

### C-F004 - Add User form đảo First Name và Last Name

**Nguồn:** Checklist execution C2

**Màn hình:** C2 Gán vai trò / chỉnh sửa người dùng

**Loại:** Usability

**Mức độ:** 2

**Mô tả:** Add User form đảo placeholder/thông báo lỗi giữa First Name và Last Name.

**Bước tái hiện / minh chứng:**

1. Đăng nhập admin.
2. Vào Users Management.
3. Bấm Add User.
4. Bấm Create User khi form trống trong lượt kiểm Playwright đã abort mọi request ghi dữ liệu.

**Kết quả mong đợi:**

Label, placeholder và validation message của từng trường phải khớp đúng ý nghĩa field để admin biết cần nhập gì và sửa lỗi nào.

**Kết quả thực tế:**

Trường label First Name hiển thị placeholder`Last Name` và lỗi `Last name is required`; trường label Last Name hiển thị placeholder `First Name` và lỗi `First name is required`.

**Đề xuất sửa:**

Sửa mapping label/placeholder/schema validation để First Name dùng placeholder và lỗi First Name, Last Name dùng placeholder và lỗi Last Name; thêm dấu hiệu required trước submit nếu có thể.

**Ảnh minh chứng:**

<img src="screenshots/checklist-failures/C-F004.png" alt="C-F004 evidence">

**Timestamp form:**
Phản ánh lúc 22:50 ngày 02/08/2026
<img src="screenshots/checklist-failures/C-F004-form.png" alt="C-F004 Google Form submission evidence">

### C-F005 - Password validation không nhất quán và chưa đồng bộ ngôn ngữ

**Nguồn:** Checklist execution C2

**Màn hình:** C2 Gán vai trò / chỉnh sửa người dùng

**Loại:** Usability

**Mức độ:** 2

**Mô tả:** Password validation không nhất quán giữa hướng dẫn ban đầu và lỗi sau khi nhập, đồng thời lỗi vẫn hiển thị tiếng Anh khi giao diện đang ở VI.

**Bước tái hiện / minh chứng:**

1. Chuyển giao diện sang VI.
2. Vào Users Management.
3. Bấm Add User.
4. Nhập password `12345678` và submit/ra khỏi trường để kích hoạt validation.

**Kết quả mong đợi:**

Form phải nêu đầy đủ password policy trước khi người dùng nhập và thông báo lỗi phải theo đúng ngôn ngữ đang chọn.

**Kết quả thực tế:**

Ban đầu form chỉ thể hiện yêu cầu tối thiểu 8 ký tự; sau khi nhập`12345678`, hệ thống báo thêm `Password must include uppercase letters and special characters` bằng tiếng Anh dù giao diện đang ở VI.

**Đề xuất sửa:**

Hiển thị helper text password policy đầy đủ ngay dưới trường Password; dịch toàn bộ validation message theo VI/EN đồng bộ với nút đổi ngôn ngữ.

**Ảnh minh chứng:**

<img src="screenshots/checklist-failures/C-F005.png" alt="C-F005 evidence">

**Timestamp form:**
Phản ánh lúc 22:51 ngày 02/08/2026
<img src="screenshots/checklist-failures/C-F005-form.png" alt="C-F005 Google Form submission evidence">

### C-F006 - Email validation cho phép email `@g`

**Nguồn:** Checklist execution C2

**Màn hình:** C2 Gán vai trò / chỉnh sửa người dùng

**Loại:** Bug

**Mức độ:** 3

**Mô tả:** Email validation cho phép submit thành công với email không hợp lệ dạng`@g`.

**Bước tái hiện / minh chứng:**

1. Vào Users Management.
2. Bấm Add User hoặc Edit User.
3. Nhập email `@g` cùng các trường bắt buộc khác hợp lệ.
4. Submit form.

**Kết quả mong đợi:**

Form phải chặn email sai định dạng và hiển thị lỗi rõ ràng trước khi gửi dữ liệu.

**Kết quả thực tế:**

Hệ thống vẫn cho submit thành công dù email chỉ là`@g`, không đủ định dạng email hợp lệ.

**Đề xuất sửa:**

Bổ sung validation email ở cả client và server theo định dạng email hợp lệ; hiển thị thông báo lỗi ngay tại trường Email và không cho lưu khi email không hợp lệ.

**Ảnh minh chứng:**

<img src="screenshots/checklist-failures/C-F006.png" alt="C-F006 evidence">

**Timestamp form:**
Phản ánh lúc 22:54 ngày 02/08/2026
<img src="screenshots/checklist-failures/C-F006-form.png" alt="C-F006 Google Form submission evidence">

### C-F007 - Phone Number thiếu gợi ý định dạng

**Nguồn:** Checklist execution C2

**Màn hình:** C2 Gán vai trò / chỉnh sửa người dùng

**Loại:** Usability

**Mức độ:** 2

**Mô tả:** Phone Number field không giải thích trước quy tắc số điện thoại phải gồm 10 số và bắt đầu bằng 0.

**Bước tái hiện / minh chứng:**

1. Vào Users Management.
2. Bấm Add User hoặc Edit User.
3. Quan sát trường Phone Number trước khi nhập hoặc nhập sai định dạng để thấy rule chỉ xuất hiện muộn/không được gợi ý rõ.

**Kết quả mong đợi:**

Field Phone Number nên nêu rõ định dạng hợp lệ trước khi admin nhập, ví dụ 10 chữ số và bắt đầu bằng 0.

**Kết quả thực tế:**

Placeholder chỉ là`Phone Number`, không có helper text về rule 10 số/bắt đầu bằng 0, khiến admin phải đoán hoặc thử sai.

**Đề xuất sửa:**

Thêm helper text hoặc placeholder cụ thể như`VD: 0912345678 - 10 số, bắt đầu bằng 0`; nếu nhập sai, thông báo lỗi cần nói rõ quy tắc và giữ lại dữ liệu đã nhập.

**Ảnh minh chứng:**

<img src="screenshots/checklist-failures/C-F007.png" alt="C-F007 evidence">

**Timestamp form:**
Phản ánh lúc 22:55 ngày 02/08/2026
<img src="screenshots/checklist-failures/C-F007-form.png" alt="C-F007 Google Form submission evidence">

### C-F008 - Phone Number cho nhập chữ

**Nguồn:** Checklist execution C2

**Màn hình:** C2 Gán vai trò / chỉnh sửa người dùng

**Loại:** Usability

**Mức độ:** 2

**Mô tả:** Phone Number field cho phép nhập ký tự chữ, chỉ báo lỗi sau khi submit.

**Bước tái hiện / minh chứng:**

1. Vào Users Management.
2. Bấm Add User hoặc Edit User.
3. Nhập chữ vào trường Phone Number.
4. Submit form.

**Kết quả mong đợi:**

Trường Phone Number nên hạn chế hoặc cảnh báo sớm khi người dùng nhập ký tự không phải số, trước khi submit.

**Kết quả thực tế:**

Field vẫn nhận ký tự chữ; hệ thống chỉ báo lỗi sau khi submit nên admin phải sửa theo kiểu thử-sai.

**Đề xuất sửa:**

Dùng input mode numeric/tel, lọc ký tự không hợp lệ hoặc validate inline khi blur/typing; vẫn giữ validation server-side khi submit.

**Ảnh minh chứng:**

<img src="screenshots/checklist-failures/C-F008.png" alt="C-F008 evidence">

**Timestamp form:**
Phản ánh lúc 22:57 ngày 02/08/2026
<img src="screenshots/checklist-failures/C-F008-form.png" alt="C-F008 Google Form submission evidence">

### C-F009 - Role dropdown cho chọn placeholder

**Nguồn:** Checklist execution C2

**Màn hình:** C2 Gán vai trò / chỉnh sửa người dùng

**Loại:** Usability

**Mức độ:** 2

**Mô tả:** Role dropdown hiển thị placeholder chọn vai trò cùng cấp với các role thật và cho chọn rồi mới báo lỗi.

**Bước tái hiện / minh chứng:**

1. Vào Users Management.
2. Bấm Add User hoặc Edit User.
3. Mở dropdown Role.
4. Chọn option placeholder như `Phần chọn vai trò`/`Select a Role`.
5. Submit form.

**Kết quả mong đợi:**

Placeholder của dropdown Role chỉ nên là gợi ý không chọn được, hoặc nếu chọn lại thì phải được xử lý như trạng thái rỗng rõ ràng trước submit.

**Kết quả thực tế:**

Placeholder nằm cùng cấp với Admin/Guest/Lecturer/Student hoặc Sinh viên/Giảng viên và có thể chọn; hệ thống chỉ báo lỗi sau khi submit.

**Đề xuất sửa:**

Đặt placeholder Role thành option disabled/hidden, hiển thị helper text`Chọn một vai trò hợp lệ`, và validate inline khi dropdown quay về giá trị rỗng.

**Ảnh minh chứng:**

<img src="screenshots/checklist-failures/C-F009.png" alt="C-F009 evidence">

**Timestamp form:**
Phản ánh lúc 22:58 ngày 02/08/2026
<img src="screenshots/checklist-failures/C-F009-form.png" alt="C-F009 Google Form submission evidence">

### C-F010 - Email của user đã xóa vẫn báo đang dùng

**Nguồn:** Checklist execution C2

**Màn hình:** C2 Gán vai trò / chỉnh sửa người dùng

**Loại:** Usability

**Mức độ:** 3

**Mô tả:** Sau khi xóa user, tạo user mới bằng email của user đã xóa vẫn báo`email already use` và lỗi hiển thị tiếng Anh khi giao diện đang VI.

**Bước tái hiện / minh chứng:**

1. Chuyển giao diện sang VI.
2. Xóa một user trong Users Management.
3. Bấm Add User.
4. Nhập email của user vừa xóa cùng các trường bắt buộc hợp lệ.
5. Submit form.

**Kết quả mong đợi:**

Nếu email sau khi xóa không được tái sử dụng, UI phải giải thích rõ đây là soft delete/định danh bị giữ; thông báo lỗi phải hiển thị bằng tiếng Việt.

**Kết quả thực tế:**

Hệ thống báo`email already use` bằng tiếng Anh dù giao diện đang ở VI, và không giải thích email của user đã xóa có bị giữ lại hay cách khôi phục.

**Đề xuất sửa:**

Làm rõ hậu quả trong dialog xóa user; nếu giữ email do soft delete, cung cấp đường khôi phục hoặc thông báo tiếng Việt rõ ràng; nếu delete thật, giải phóng email sau khi xóa.

**Ảnh minh chứng:**

<img src="screenshots/checklist-failures/C-F010.png" alt="C-F010 evidence">

**Timestamp form:**
Phản ánh lúc 22:58 ngày 02/08/2026
<img src="screenshots/checklist-failures/C-F010-form.png" alt="C-F010 Google Form submission evidence">

### C-F011 - Member Code trùng báo lỗi tiếng Anh khi đang ở VI

**Nguồn:** Checklist execution C2

**Màn hình:** C2 Gán vai trò / chỉnh sửa người dùng

**Loại:** Usability

**Mức độ:** 2

**Mô tả:** Member Code trùng được chặn đúng, nhưng thông báo lỗi hiển thị tiếng Anh khi giao diện đang VI.

**Bước tái hiện / minh chứng:**

1. Chuyển giao diện sang VI.
2. Vào Users Management.
3. Bấm Add User.
4. Nhập một Member Code đã được user khác dùng cùng các trường bắt buộc hợp lệ.
5. Submit form.

**Kết quả mong đợi:**

Hệ thống nên chặn Member Code đã tồn tại và hiển thị thông báo lỗi theo đúng ngôn ngữ đang chọn.

**Kết quả thực tế:**

Hệ thống chặn đúng Member Code đã tồn tại nhưng hiển thị`this member code is already in use` bằng tiếng Anh dù giao diện đang ở VI.

**Đề xuất sửa:**

Dịch validation message Member Code sang tiếng Việt khi giao diện ở VI, ví dụ`Mã thành viên này đã được sử dụng`; giữ logic chặn trùng ở client/server.

**Ảnh minh chứng:**

<img src="screenshots/checklist-failures/C-F011.png" alt="C-F011 evidence">

**Timestamp form:**
Phản ánh lúc 22:59 ngày 02/08/2026
<img src="screenshots/checklist-failures/C-F011-form.png" alt="C-F011 Google Form submission evidence">

### C-F012 - Block/Unblock mơ hồ qua Active và thiếu Reset Password action

**Nguồn:** Checklist execution C3

**Màn hình:** C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu

**Loại:** Usability

**Mức độ:** 3

**Mô tả:** Theo phạm vi Scenario C, màn hình Users Management cần hỗ trợ Block/Unblock và Reset Password dialogs. Trong lượt kiểm Playwright, UI có trạng thái Active/Inactive và checkbox Active trong Edit User, có thể là cơ chế Block/Unblock hiện tại, nhưng wording không nói rõ điều đó; đồng thời không thấy action Reset Password riêng.

**Bước tái hiện / minh chứng:**

1. Đăng nhập EMS bằng tài khoản admin.
2. Vào `https://prod-dev.ems-fitus.cloud/dashboard/admin/users`.
3. Quan sát cột Actions của các dòng user.
4. Bấm Edit user ở dòng đầu tiên.
5. Quan sát các control trong dialog Edit User.

**Kết quả mong đợi:**

Admin phải thấy action/label rõ ràng cho Block/Unblock và Reset Password, hoặc UI phải giải thích trực tiếp rằng Active/Inactive tương ứng với trạng thái unblock/block.

**Kết quả thực tế:**

Cột Actions chỉ có Edit/Delete; Edit User có checkbox Active nhưng không giải thích Active/Inactive là Block/Unblock hay hậu quả khi đổi trạng thái. Không thấy Reset Password action.

**Đề xuất sửa:**

Thêm action riêng `Block`/`Unblock` và `Reset Password`, hoặc đổi wording/helper text để Active/Inactive được hiểu rõ là trạng thái block/unblock; Reset Password cần có entry point và confirmation dialog riêng.

**Ảnh minh chứng:**

<img src="screenshots/checklist-failures/C-F012-01.png" alt="C-F012 evidence-1">
<img src="screenshots/checklist-failures/C-F012-02.png" alt="C-F012 evidence-2">

**Timestamp form:**
Phản ánh lúc 23:00 ngày 02/08/2026
<img src="screenshots/checklist-failures/C-F012-form.png" alt="C-F012 Google Form submission evidence">

### C-F013 - Active/Inactive thiếu xác nhận nguy hiểm riêng

**Nguồn:** Checklist execution C3

**Màn hình:** C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu

**Loại:** Usability

**Mức độ:** 3

**Mô tả:** Checkbox Active trong Edit User phản ánh trạng thái tài khoản hiện tại: user Active được tick và user Inactive không được tick. Tuy nhiên thao tác đổi trạng thái Active/Inactive có thể ảnh hưởng quyền truy cập của user nhưng không có confirmation riêng trước khi lưu.

**Bước tái hiện / minh chứng:**

1. Đăng nhập EMS bằng tài khoản admin.
2. Vào Users Management.
3. Lọc Status = Inactive.
4. Bấm Edit user ở một dòng Inactive.
5. Quan sát checkbox Active đang không được tick và nút Save Changes.
6. Không bấm Save trong lượt kiểm an toàn để tránh thay đổi dữ liệu thật.

**Kết quả mong đợi:**

Thao tác đổi trạng thái tài khoản phải có label trực tiếp như `Block user`/`Unblock user` hoặc helper text nêu hậu quả, đồng thời có confirmation dialog trước khi lưu.

**Kết quả thực tế:**

UI chỉ có checkbox `Active` trong Edit User; với user Inactive checkbox không được tick đúng trạng thái, nhưng UI không giải thích trạng thái này ảnh hưởng quyền truy cập thế nào và không có confirmation riêng trước nút Save Changes.

**Đề xuất sửa:**

Tách Block/Unblock khỏi form Edit User thành action riêng hoặc bổ sung confirmation khi checkbox Active thay đổi; dialog cần hiển thị tên/email user, trạng thái trước-sau và hậu quả đăng nhập.

**Ảnh minh chứng:**

<img src="screenshots/checklist-failures/C-F013.png" alt="C-F013 evidence">

**Timestamp form:**
Phản ánh lúc 23:01 ngày 02/08/2026
<img src="screenshots/checklist-failures/C-F013-form.png" alt="C-F013 Google Form submission evidence">

## Thang mức độ nghiêm trọng

| Mức độ | Ý nghĩa                                                                         |
| ------ | ------------------------------------------------------------------------------- |
| 1      | Lỗi thẩm mỹ hoặc gây khó chịu nhẹ                                               |
| 2      | Vấn đề usability nhỏ, có workaround                                             |
| 3      | Vấn đề lớn gây chậm, nhầm lẫn hoặc lỗi thao tác đáng kể                         |
| 4      | Vấn đề nghiêm trọng chặn hoàn thành nhiệm vụ hoặc có rủi ro mất dữ liệu/bảo mật |
