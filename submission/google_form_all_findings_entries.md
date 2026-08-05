# Nội dung submit Google Form cho toàn bộ findings

## Hướng dẫn chung

- Gửi **18 response riêng**, theo thứ tự trong tệp này.
- Luôn chọn `Có` cho câu hỏi có gặp lỗi; usability finding được ghi rõ là `Tính khả dụng` trong phần mô tả.
- Trường upload chỉ nhận một file tối đa 10 MB. Nếu finding cần nhiều ảnh, hãy ghép thành một ảnh trước/sau.
- Sau mỗi response, chụp trang xác nhận, đặt tên `<Finding-ID>-submitted.png` và ghi lại thời gian gửi thực tế.
- Không upload ảnh xác nhận submit vào form; trường upload chỉ dùng cho bằng chứng lỗi.

---

## 1. T1B-A1-01 — Trạng thái tìm kiếm rỗng không có Reset

- **Tốc độ tải trang:** Bình thường
- **Có gặp lỗi:** Có
- **Mô tả lỗi:**

```text
[T1B-A1-01][Task 1B][A1 – Events list][Tính khả dụng][Severity 2]
Steps: Mở Events, nhập truy vấn không khớp sự kiện nào và quan sát trạng thái rỗng.
Expected: Trạng thái rỗng giải thích kết quả và có nút Reset/xóa bộ lọc trực tiếp.
Actual: Hệ thống thông báo không có sự kiện phù hợp nhưng không có hành động xóa truy vấn/bộ lọc.
```

- **File upload:** `submission/screenshots/task1b/a1-f01-empty-no-reset.png`
- **Điều thích nhất:** Chức năng tìm kiếm giúp lọc nhanh danh sách sự kiện.
- **Chưa hài lòng:** Khi không có kết quả, người dùng phải tự xóa nội dung tìm kiếm thay vì có hành động khôi phục rõ ràng.
- **Mong muốn cải thiện:** Thêm nút `Reset filters` trong trạng thái rỗng và trả tiêu điểm về ô tìm kiếm sau khi đặt lại.
- **Timestamp sau khi gửi:** 20:39 ngày 05/08/2026

## 2. T1B-A1-03 — Bảng sự kiện phải cuộn ngang

- **Tốc độ tải trang:** Bình thường
- **Có gặp lỗi:** Có
- **Mô tả lỗi:**

```text
[T1B-A1-03][Task 1B][A1 – Events list][Tính khả dụng][Severity 2]
Steps: Mở Events trong cửa sổ Safari 1171×768 và quan sát bảng.
Expected: Các cột và hành động cốt lõi hiển thị mà không cần cuộn ngang không cần thiết.
Actual: Bảng tràn ngang, che các cột/hành động phía sau cho đến khi người dùng cuộn ngang.
```

- **File upload:** `submission/screenshots/task1b/a1-overview.png`
- **Điều thích nhất:** Danh sách trình bày được nhiều thông tin và trạng thái sự kiện.
- **Chưa hài lòng:** Bảng quá rộng trong cửa sổ desktop gọn, làm các hành động bên phải bị khuất.
- **Mong muốn cải thiện:** Ưu tiên cột cốt lõi, cho phép xuống dòng và chuyển dữ liệu phụ sang phần chi tiết ở chiều rộng hẹp.
- **Timestamp sau khi gửi:** 20:43 ngày 05/08/2026

## 3. T1B-A1-04 — Thông báo trộn ngôn ngữ

- **Tốc độ tải trang:** Bình thường
- **Có gặp lỗi:** Có
- **Mô tả lỗi:**

```text
[T1B-A1-04][Task 1B][A1 – Notifications][Lỗi][Severity 1]
Steps: Giữ giao diện ở English, mở Notifications và đọc nội dung.
Expected: Toàn bộ thông báo dùng ngôn ngữ English đã chọn.
Actual: Bảng hiển thị "Phản hồi khiếu nại" bằng tiếng Việt trong khi phần giao diện xung quanh là tiếng Anh.
```

- **File upload:** `submission/screenshots/task1b/a1-f04-notification-mixed-language.png`
- **Điều thích nhất:** Khu vực Notifications tập trung các thông báo gần đây ở một vị trí dễ truy cập.
- **Chưa hài lòng:** Ngôn ngữ không nhất quán làm giao diện thiếu chuyên nghiệp và gây khó hiểu.
- **Mong muốn cải thiện:** Đưa mọi mẫu thông báo qua cùng tài nguyên bản địa hóa và kiểm thử hồi quy EN/VI.
- **Timestamp sau khi gửi:** 21:05 ngày 05/08/2026

## 4. T1B-A1-05 — Icon không có tooltip khi focus

- **Tốc độ tải trang:** Bình thường
- **Có gặp lỗi:** Có
- **Mô tả lỗi:**

```text
[T1B-A1-05][Task 1B][A1 – Events list][Tính khả dụng][Severity 2]
Steps: Di chuyển focus bàn phím tới hành động chỉ có icon và dừng tại phần tử.
Expected: Icon hiển thị nhãn hoặc tooltip rõ khi hover và khi có focus.
Actual: Icon Delete có viền focus nhưng không hiển thị nhãn/tooltip.
```

- **File upload:** `submission/screenshots/task1b/a1-f05-action-focus-no-tooltip.png`
- **Điều thích nhất:** Các hành động sự kiện được đặt gọn trong từng dòng danh sách.
- **Chưa hài lòng:** Icon không có nhãn buộc người dùng phải đoán chức năng, đặc biệt khi dùng bàn phím.
- **Mong muốn cải thiện:** Thêm accessible name và tooltip kích hoạt bằng cả hover lẫn focus bàn phím.
- **Timestamp sau khi gửi:** 21:08 ngày 05/08/2026

## 5. T1B-A1-06 — Mất trạng thái tìm kiếm khi quay lại

- **Tốc độ tải trang:** Bình thường
- **Có gặp lỗi:** Có
- **Mô tả lỗi:**

```text
[T1B-A1-06][Task 1B][A1 – Events list][Lỗi][Severity 2]
Steps: Tìm một bản nháp có tên duy nhất, mở chi tiết rồi dùng Back của trình duyệt.
Expected: Danh sách khôi phục truy vấn, kết quả đã lọc và vị trí trước đó.
Actual: Danh sách hiển thị lại toàn bộ và ô tìm kiếm bị xóa.
```

- **File upload:** `submission/screenshots/task1b/a1-f06-filter-not-retained.png` (nên ghép với ảnh trước thao tác nếu có)
- **Điều thích nhất:** Việc mở sự kiện từ danh sách nhanh và trực tiếp.
- **Chưa hài lòng:** Mất bộ lọc khi quay lại làm người dùng phải tìm kiếm lại từ đầu.
- **Mong muốn cải thiện:** Lưu truy vấn, bộ lọc và trang trong URL hoặc navigation state, sau đó khôi phục khi quay lại.
- **Timestamp sau khi gửi:** 21:48 ngày 05/08/2026

## 6. T1B-A2-01 — Thumbnail chấp nhận file TXT

- **Tốc độ tải trang:** Bình thường
- **Có gặp lỗi:** Có
- **Mô tả lỗi:**

```text
[T1B-A2-01][Task 1B][A2 – Add/Edit Event][Lỗi][Severity 2]
Steps: Mở form Add/Edit Event và chọn file upload_invalid.txt cho Thumbnail.
Expected: File không phải ảnh bị từ chối với thông báo validation cụ thể.
Actual: File .txt được chấp nhận và phần preview ảnh bị hỏng mà không có thông báo lỗi.
```

- **File upload:** `submission/screenshots/task1b/a2-f01-invalid-thumbnail-accepted.png`
- **Điều thích nhất:** Form cho phép xem trước Thumbnail ngay trong trang tạo sự kiện.
- **Chưa hài lòng:** Hệ thống không chặn file sai định dạng, dẫn đến preview bị hỏng.
- **Mong muốn cải thiện:** Giới hạn file picker và kiểm tra MIME, chữ ký file, phần mở rộng và dung lượng trước khi preview.
- **Timestamp sau khi gửi:** 22:16 ngày 05/08/2026

## 7. T1B-A2-02 — Rời form không cảnh báo thay đổi chưa lưu

- **Tốc độ tải trang:** Bình thường
- **Có gặp lỗi:** Có
- **Mô tả lỗi:**

```text
[T1B-A2-02][Task 1B][A2 – Add/Edit Event][Lỗi][Severity 3]
Steps: Đổi Event Title trong form edit, dùng Back trước khi lưu và quan sát.
Expected: Hệ thống yêu cầu xác nhận trước khi rời trang và giữ thay đổi cho đến khi người dùng xác nhận hủy.
Actual: Trang quay về Events ngay, không có cảnh báo và Event Title chưa lưu bị mất.
```

- **File upload:** Ghép `a2-f02-unsaved-before.png` và `a2-f02-unsaved-after-no-warning.png` thành một ảnh dưới 10 MB.
- **Điều thích nhất:** Form edit giữ các nhóm thông tin sự kiện trong một luồng thống nhất.
- **Chưa hài lòng:** Người dùng có thể mất dữ liệu đã nhập mà không được cảnh báo.
- **Mong muốn cải thiện:** Theo dõi dirty state và hiển thị hộp thoại xác nhận cho cả điều hướng trong ứng dụng lẫn Back của trình duyệt.
- **Timestamp sau khi gửi:** 22:19 ngày 05/08/2026

## 8. T1B-A2-03 — Icon Back/Thumbnail/Banner thiếu tooltip

- **Tốc độ tải trang:** Bình thường
- **Có gặp lỗi:** Có
- **Mô tả lỗi:**

```text
[T1B-A2-03][Task 1B][A2 – Add/Edit Event][Tính khả dụng][Severity 2]
Steps: Hover nút Back và các nút camera; sau đó dùng bàn phím focus nút camera Thumbnail.
Expected: Mọi hành động chỉ có icon hiển thị nhãn/tooltip khi hover và focus.
Actual: Back, Thumbnail và Banner không hiển thị nhãn/tooltip trong các trạng thái đã kiểm thử.
```

- **File upload:** Dùng `submission/screenshots/task1b/a2-icon-keyboard-focus-unlabeled-camera.png` hoặc ghép các ảnh icon thành một ảnh.
- **Điều thích nhất:** Các nút icon giúp form gọn và các icon rich-text có tooltip hữu ích.
- **Chưa hài lòng:** Một số icon camera và Back không có chú giải nên khó đoán chức năng.
- **Mong muốn cải thiện:** Thêm accessible name, tooltip cho hover/focus hoặc nhãn hiển thị cạnh icon.
- **Timestamp sau khi gửi:** 22:23 ngày 05/08/2026

## 9. T1B-A3-01 — Max Slots vẫn hoạt động khi Is Unlimited bật

- **Tốc độ tải trang:** Bình thường
- **Có gặp lỗi:** Có
- **Mô tả lỗi:**

```text
[T1B-A3-01][Task 1B][A3 – Registration & Roles][Lỗi][Severity 2]
Steps: Bật Student Registration, bật Is Unlimited và kiểm tra Max Slots.
Expected: Khi không giới hạn số lượng, Max Slots phải bị vô hiệu hóa, xóa hoặc ẩn.
Actual: Max Slots vẫn hiển thị và chỉnh sửa được khi Is Unlimited đang bật.
```

- **File upload:** `submission/screenshots/task1b/a3-f01-unlimited-max-slots-active.png`
- **Điều thích nhất:** Khu vực Registration & Roles cung cấp nhiều tùy chọn cấu hình chi tiết.
- **Chưa hài lòng:** Hai điều khiển mâu thuẫn cùng hoạt động, làm trạng thái số chỗ không rõ ràng.
- **Mong muốn cải thiện:** Vô hiệu hóa và xóa Max Slots khi bật Is Unlimited; chỉ khôi phục khi tắt Is Unlimited.
- **Timestamp sau khi gửi:** 22:26 ngày 05/08/2026

## 10. T1B-A3-03 — Waitlist vẫn bật khi Student Registration tắt

- **Tốc độ tải trang:** Bình thường
- **Có gặp lỗi:** Có
- **Mô tả lỗi:**

```text
[T1B-A3-03][Task 1B][A3 – Registration & Roles][Lỗi][Severity 3]
Steps: Bật Student Registration và Waitlist, sau đó tắt Student Registration.
Expected: Waitlist phụ thuộc phải bị vô hiệu hóa hoặc xóa khi tùy chọn cha tắt.
Actual: Các điều khiển Student biến mất nhưng Waitlist vẫn bật.
```

- **File upload:** `submission/screenshots/task1b/a3-f03-waitlist-with-student-off.png`
- **Điều thích nhất:** Các tùy chọn đăng ký được nhóm gần nhau và dễ truy cập.
- **Chưa hài lòng:** Trạng thái Waitlist mâu thuẫn với Student Registration có thể tạo cấu hình không hợp lệ.
- **Mong muốn cải thiện:** Tự động tắt/xóa hoặc vô hiệu hóa Waitlist khi Student Registration tắt và kiểm tra lại khi lưu.
- **Timestamp sau khi gửi:** 22:28 ngày 05/08/2026

## 11. T1B-A3-04 — Mất thay đổi Registration & Roles không cảnh báo

- **Tốc độ tải trang:** Bình thường
- **Có gặp lỗi:** Có
- **Mô tả lỗi:**

```text
[T1B-A3-04][Task 1B][A3 – Registration & Roles][Lỗi][Severity 3]
Steps: Đổi Reminder từ 24 thành 25, dùng Back mà không lưu, sau đó mở lại bản nháp.
Expected: Hệ thống cảnh báo trước khi điều hướng và giữ thay đổi cho đến khi người dùng xác nhận hủy.
Actual: Trang quay về Events ngay; khi mở lại, Reminder vẫn là 24 và giá trị 25 chưa lưu bị mất.
```

- **File upload:** Ghép `a3-unsaved-reminder-25-before-back.png`, `a3-unsaved-back-no-warning-destination.png` và `a3-unsaved-reopen-reminder-24-persisted.png` thành một ảnh.
- **Điều thích nhất:** Các cấu hình vai trò và reminder được đặt trong cùng luồng chỉnh sửa sự kiện.
- **Chưa hài lòng:** Có nguy cơ mất cấu hình đã nhập khi rời trang mà không có cảnh báo.
- **Mong muốn cải thiện:** Dùng cơ chế dirty-state chung cho form và cảnh báo khi rời trang qua cả ứng dụng lẫn trình duyệt.
- **Timestamp sau khi gửi:** 22:31 ngày 05/08/2026

## 12. UX-001 — Academic Context khó hiểu

- **Tốc độ tải trang:** Bình thường
- **Có gặp lỗi:** Có
- **Mô tả lỗi:**

```text
[UX-001][Task 2][A2 – Categories][Tính khả dụng][Severity 2]
Quan sát người dùng P1 tại 07:55: khi chọn Academic Context, người dùng dừng lại và nói "này là sao".
Expected: Người dùng hiểu mục đích và phân biệt Academic Context với Event Types mà không cần suy đoán.
Actual: Nhãn không đủ rõ nghĩa, làm người dùng lúng túng trước khi tiếp tục.
```

- **File upload:** Cắt clip P1 quanh `07:55` từ `https://youtu.be/dilkwkxXt0Q?t=475`, xuất file dưới 10 MB.
- **Điều thích nhất:** Luồng tạo sự kiện nhìn chung rõ ràng và các phần được chia nhóm.
- **Chưa hài lòng:** Thuật ngữ Academic Context không có giải thích hoặc ví dụ, nên khó biết cần chọn gì.
- **Mong muốn cải thiện:** Thêm mô tả ngắn/ví dụ bên dưới Academic Context và làm rõ quan hệ với Event Types.
- **Timestamp sau khi gửi:** 22:37 ngày 05/08/2026

## 13. UX-002 — Save as Draft không có phản hồi lỗi tổng thể

- **Tốc độ tải trang:** Bình thường
- **Có gặp lỗi:** Có
- **Mô tả lỗi:**

```text
[UX-002][Task 2][A2 – Save as Draft/validation][Tính khả dụng][Severity 2]
Quan sát P3 tại 11:20: người dùng nhấn Save as Draft hai lần nhưng màn hình không thay đổi, sau đó phải tự cuộn lên tìm trường sai. P5 cũng cho biết cách xử lý khó hiểu vì không có thông báo lỗi chung.
Expected: Khi submit thất bại, hệ thống giải thích nguyên nhân và đưa người dùng tới trường cần sửa.
Actual: Không có phản hồi tổng thể hoặc tự cuộn/focus trường lỗi; người dùng phải tự tìm trên form dài.
```

- **File upload:** Cắt clip P3 quanh `11:20` từ `https://youtu.be/mEJQPFBlc64?t=680`, xuất file dưới 10 MB.
- **Điều thích nhất:** Form giữ lại dữ liệu đã nhập, giúp người dùng có thể tìm và sửa trường sai.
- **Chưa hài lòng:** Nút Save as Draft không cho biết vì sao thao tác thất bại hoặc lỗi nằm ở đâu.
- **Mong muốn cải thiện:** Hiển thị pop-up/tóm tắt validation và tự cuộn, focus trường lỗi đầu tiên.
- **Timestamp sau khi gửi:** 22:38 ngày 05/08/2026

## 14. UX-003 — Điều khiển chọn giờ khó thao tác

- **Tốc độ tải trang:** Bình thường
- **Có gặp lỗi:** Có
- **Mô tả lỗi:**

```text
[UX-003][Task 2][A2 – Date & Time][Tính khả dụng][Severity 2]
Trong phần probe, P3 cho biết điều khiển chọn/chỉnh giờ phải kéo chuột mạnh, gây phiền và mất thời gian. P4 cũng đánh giá thao tác chọn giờ rất chậm.
Expected: Người dùng có thể chọn hoặc nhập giờ nhanh, chính xác bằng chuột hoặc bàn phím.
Actual: Thao tác kéo khó dùng và không có cách nhập giờ trực tiếp thuận tiện.
```

- **File upload:** Cắt đoạn video/audio probe P3 từ `https://youtu.be/mEJQPFBlc64`, xuất file dưới 10 MB.
- **Điều thích nhất:** Các mốc thời gian cần thiết cho sự kiện được cung cấp đầy đủ trong form.
- **Chưa hài lòng:** Thao tác chọn giờ bằng kéo chậm và khó kiểm soát.
- **Mong muốn cải thiện:** Cho phép nhập giờ trực tiếp bằng bàn phím, cải thiện time picker và gom các trường thời gian liên quan.
- **Timestamp sau khi gửi:** 22:41 ngày 05/08/2026

## 15. UX-004 — Trạng thái chọn Event Types không rõ

- **Tốc độ tải trang:** Bình thường
- **Có gặp lỗi:** Có
- **Mô tả lỗi:**

```text
[UX-004][Task 2][A2 – Categories][Tính khả dụng][Severity 2]
Quan sát P4 tại 05:25: người dùng dừng lại khi danh sách Event Types đang mở và có vẻ không chắc giá trị đã được chọn hay chưa.
Expected: Lựa chọn hiện tại được thể hiện rõ trong ô và trong danh sách.
Actual: Trạng thái đã chọn không đủ rõ, làm người dùng dừng lại để kiểm tra.
```

- **File upload:** Cắt clip P4 quanh `05:25` từ `https://youtu.be/kyZxvvLCOkE?t=325`, xuất file dưới 10 MB.
- **Điều thích nhất:** Các nhiệm vụ tạo sự kiện nhìn chung rõ ràng và hệ thống phản hồi nhanh.
- **Chưa hài lòng:** Event Types không cho biết rõ option nào đã được ghi nhận.
- **Mong muốn cải thiện:** Hiển thị giá trị hiện tại rõ ràng, thêm dấu chọn cho option đã chọn và duy trì phản hồi sau khi danh sách đóng.
- **Timestamp sau khi gửi:** 22:43 ngày 05/08/2026

## 16. CP-BUG-001 — A1 không responsive trên Samsung Internet phone

- **Tốc độ tải trang:** Bình thường
- **Có gặp lỗi:** Có
- **Mô tả lỗi:**

```text
[CP-BUG-001][Task 3][A1-CP-04][Lỗi tương thích][Severity 3]
Môi trường: Samsung Galaxy S24, Android 14, Samsung Internet 29, Phone.
Expected: Navigation và danh sách vừa viewport hoặc chuyển sang bố cục mobile, không cuộn ngang toàn trang.
Actual: Sidebar chiếm phần lớn chiều rộng, vùng nội dung bên phải bị cắt và page-level horizontal overflow là 664 px.
```

- **File upload:** `submission/screenshots/task3/a1-cp-04-android-samsung-internet-phone.png`
- **Điều thích nhất:** Màn hình tải đủ nội dung và luồng Events hoạt động ổn trên các môi trường desktop/tablet đã kiểm thử.
- **Chưa hài lòng:** Bố cục phone không thu gọn sidebar, làm danh sách bị cắt và buộc cuộn ngang.
- **Mong muốn cải thiện:** Chuyển sidebar thành drawer/hamburger ở breakpoint phone, bỏ fixed/min-width gây tràn và bảo đảm danh sách vừa viewport.
- **Timestamp sau khi gửi:** 22:44 ngày 05/08/2026

## 17. CP-BUG-002 — A2 không responsive trên Samsung Internet phone

- **Tốc độ tải trang:** Bình thường
- **Có gặp lỗi:** Có
- **Mô tả lỗi:**

```text
[CP-BUG-002][Task 3][A2-CP-04][Lỗi tương thích][Severity 3]
Môi trường: Samsung Galaxy S24, Android 14, Samsung Internet 29, Phone.
Expected: Nhãn, trường nhập và khu vực upload co giãn/xuống hàng trong viewport phone.
Actual: Form bị ép hẹp, chữ và điều khiển bị cắt, phải cuộn ngang; page-level horizontal overflow là 156 px.
```

- **File upload:** `submission/screenshots/task3/a2-cp-04-android-samsung-internet-phone.png`
- **Điều thích nhất:** Form có các nhóm thông tin rõ ràng và hiển thị ổn trên Edge, Safari, Firefox desktop và Chrome tablet.
- **Chưa hài lòng:** Trên phone, các cột và khu vực upload không xuống hàng đúng cách nên khó đọc và thao tác.
- **Mong muốn cải thiện:** Đổi form/grid sang một cột ở breakpoint phone, cho text và upload area co giãn theo 100% viewport, đồng thời loại bỏ min-width gây tràn.
- **Timestamp sau khi gửi:** 22:46 ngày 05/08/2026

## 18. CP-BUG-003 — A3 không responsive trên Samsung Internet phone

- **Tốc độ tải trang:** Bình thường
- **Có gặp lỗi:** Có
- **Mô tả lỗi:**

```text
[CP-BUG-003][Task 3][A3-CP-04][Lỗi tương thích][Severity 3]
Môi trường: Samsung Galaxy S24, Android 14, Samsung Internet 29, Phone.
Expected: Panel Registration & Roles và các điều khiển vừa viewport phone, không cuộn ngang toàn trang.
Actual: Panel/form bị cắt và page-level horizontal overflow là 216 px.
```

- **File upload:** `submission/screenshots/task3/a3-cp-04-android-samsung-internet-phone.png`
- **Điều thích nhất:** Các nhóm cấu hình Registration & Roles tải đủ và hoạt động ổn trên các môi trường desktop/tablet đã kiểm thử.
- **Chưa hài lòng:** Trên phone, vùng cấu hình bị cắt và yêu cầu cuộn ngang nên khó đọc, đối chiếu và chỉnh tùy chọn.
- **Mong muốn cải thiện:** Cho panel chuyển sang một cột trên phone, dùng width/max-width responsive và thêm regression test cho breakpoint mobile.
- **Timestamp sau khi gửi:** 22:48 ngày 05/08/2026

---

## Đối soát sau khi gửi

| Nhóm | Số response phải gửi | Số đã gửi | Trạng thái |
| --- | ---: | ---: | --- |
| Task 1B | 11 | 11 | Hoàn tất |
| Task 2 | 4 | 4 | Hoàn tất |
| Task 3 | 3 | 3 | Hoàn tất |
| **Tổng** | **18** | **18** | **Hoàn tất** |
