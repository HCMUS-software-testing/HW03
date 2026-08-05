# Minh chứng kiểm thử với người dùng

## 1. Thông tin task

| Trường                            | Nội dung                                                   |
| --------------------------------- | ---------------------------------------------------------- |
| Sinh viên                         | Lê Mai Hoài Bảo                                            |
| MSSV                              | 23127326                                                   |
| Scenario                          | A - Admin creates and manages events                       |
| Màn hình                          | A1 Events list, A2 Add/Edit Event, A3 Registration & Roles |
| Task scenario trong báo cáo chính | `submission/main_report.md`                                |
| Usability Report                  | `submission/usability_report.md`                           |

## 2. Kịch bản điều phối

### 2.1 Lời mở đầu

“Cảm ơn bạn đã tham gia. Hôm nay mình kiểm thử sản phẩm, không kiểm thử bạn. Không có thao tác đúng hay sai về phía bạn; mọi chỗ gây bối rối đều là dữ liệu có ích. Bạn hãy thao tác tự nhiên và nghĩ thành tiếng khi thấy khó hiểu, chậm hoặc không chắc hệ thống đang làm gì. Mình chỉ hỗ trợ nếu bạn hoàn toàn bị kẹt.”

### 2.2 Xác nhận đồng ý

Trước khi bắt đầu, người điều phối đọc và ghi lại câu trả lời cho từng mục:

| Nội dung xác nhận                                                                                | Lựa chọn              |
| ------------------------------------------------------------------------------------------------ | --------------------- |
| Tôi tham gia tự nguyện và có thể dừng bất cứ lúc nào.                                            | Đồng ý / Không đồng ý |
| Tôi đồng ý cho ghi lại màn hình phục vụ bài kiểm thử.                                            | Đồng ý / Không đồng ý |
| Tôi đồng ý cho ghi âm phần think-aloud.                                                          | Đồng ý / Không đồng ý |
| Tôi hiểu bài nộp chỉ hiển thị liên hệ đã che phần giữa, nhưng trợ giảng có thể liên hệ xác minh. | Đồng ý / Không đồng ý |

Nếu không đồng ý ghi âm hoặc ghi màn hình, phiên vẫn có thể tiếp tục bằng ghi chép thủ công. Nếu không đồng ý tham gia/xác minh thì không đưa người đó vào P1–P5.

### 2.3 Task đưa cho người tham gia

> Bạn là cộng tác viên quản trị sự kiện của khoa. Ban tổ chức cần bạn chuẩn bị một sự kiện học thuật mới ở trạng thái bản nháp, cấu hình đăng ký cho sinh viên và một vai trò cộng tác viên bổ sung, sau đó tìm sự kiện trong danh sách quản trị và mở lại ở chế độ chỉnh sửa để xác nhận dữ liệu đã được lưu. Không xuất bản hoặc xóa sự kiện.

Người tham gia nhận bảng dữ liệu nghiệp vụ, không nhận hướng dẫn vị trí nút hoặc chuỗi thao tác:

| Nhóm trên EMS | Trường/điều khiển | Giá trị yêu cầu |
| --- | --- | --- |
| Media | `Thumbnail` | Để trống. |
| Media | `Event Banner` | Để trống. |
| Media | `Attachments` | Để trống. |
| `Basic Information` | `Event Title` | `23127326_UT_<mã người tham gia>_<thời điểm>` |
| `Basic Information` | `Sub-description` | `Workshop Kỹ năng nghiên cứu 2026` |
| `Basic Information` | `Description` | `Workshop giúp sinh viên chuẩn bị đề cương nghiên cứu và trình bày kết quả.` |
| `Date & Time` | `Start Date & Time` | 08:00 25/08/2026 |
| `Date & Time` | `End Date & Time` | 11:30 25/08/2026 |
| `Date & Time` | `Check-in Open` | 07:30 25/08/2026 |
| `Date & Time` | `Check-in Close` | 09:00 25/08/2026 |
| `Categories` | `Event Types` | Chọn một giá trị phù hợp trong danh sách EMS đang cung cấp. |
| `Categories` | `Academic Context` | Chọn một giá trị phù hợp trong danh sách EMS đang cung cấp. |
| `Registration` | `Registration Open` | 08:00 10/08/2026 |
| `Registration` | `Registration Close` | 23:00 20/08/2026 |
| `Registration` | `Allow Student Registration` | Bật. |
| `Registration` | `Allow Lecturer Registration` | Tắt. |
| `Registration` | `Allow Guest Registration` | Tắt. |
| `Registration` | `Allow Waitlist` | Bật. |
| `Registration` | `Public Event` | Tắt. |
| `Student Roles` | `Is Unlimited` | Tắt. |
| `Student Roles` | `Max roles per student` | 1 |
| `Student Roles` | `Role Name` | `Student` |
| `Student Roles` | `Max Slots` | 30 |
| `Student Roles` | `Description` | `Sinh viên tham dự workshop` |
| `Location & Organization` | `Location` | `Phòng I.23` |
| `Location & Organization` | `Campus` | `Cho Quan Campus` |
| `Location & Organization` | `Organizing Unit` | `Khoa Công nghệ Thông tin` |
| `Additional Options` | `Album Link` | Để trống. |
| `Additional Options` | `Allow Additional Role` | Bật. |
| `Additional Options` | `Additional Role Name` | `Cộng tác viên` |
| `Additional Options` | `Description` | `Hỗ trợ tổ chức sự kiện` |
| `Additional Options` | `Reminder before hours` | 24 |
| Trạng thái cuối | `Save as Draft` | Lưu dưới dạng `Draft`; không `Publish` và không xóa sự kiện. |

### 2.4 Chuẩn bị môi trường

- Dùng deployment `https://prod-dev.ems-fitus.cloud/`.
- Người điều phối đăng nhập sẵn bằng tài khoản Admin; không đưa mật khẩu cho người tham gia và không ghi mật khẩu vào video.
- Bắt đầu từ trang Events ở kích thước desktop, ngôn ngữ English và không có bộ lọc từ phiên trước.
- Kiểm tra tên `23127326_UT_<mã người tham gia>_<thời điểm>` chưa tồn tại.
- Mở đồng hồ bấm giây và công cụ ghi màn hình sau khi đã xin consent.
- Không xuất bản, không xóa và không chỉnh sửa bản nháp Task 1B ID 80.

### 2.5 Quy tắc quan sát

- Không dẫn dắt participant tới đáp án.
- Chỉ can thiệp khi participant bị kẹt hoàn toàn.
- Dùng câu trung tính như “Bạn đang nghĩ gì?” hoặc “Bạn mong đợi điều gì xảy ra?” khi người tham gia im lặng.
- Ghi lại mốc thời gian, màn hình, lỗi, hesitation, lời nói, điểm bị kẹt và mọi can thiệp.
- Không xác nhận “đúng/sai” trong khi task đang chạy.
- Dừng task khi người tham gia tuyên bố hoàn thành, bỏ cuộc hoặc đạt 15 phút.

## 3. Kế hoạch đo lường

### 3.1 Định nghĩa chỉ số

| Chỉ số       | Cách ghi nhận                                                                                                                                                                                                                                                                             |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Task success | `Hoàn thành`: có bản nháp, đủ dữ liệu A2/A3 và mở lại ở chế độ chỉnh sửa để xác nhận mà không cần gợi ý. `Một phần`: lưu được bản nháp nhưng thiếu ít nhất một yêu cầu, không xác nhận được hoặc phải nhận gợi ý. `Thất bại`: không tạo được bản nháp dùng được trong 15 phút hoặc để người điều phối làm thay. |
| Time on task | Bắt đầu khi người tham gia nói đã hiểu nhiệm vụ; dừng khi họ mở bản nháp ở chế độ chỉnh sửa và tuyên bố hoàn tất, bỏ cuộc hoặc chạm 15 phút. Ghi `mm:ss`.                                                                                                                                                |
| Error        | Tính 1 cho mỗi thao tác tạo kết quả sai, thông báo lỗi, giá trị sai cần sửa hoặc đi sai luồng. Cùng một lỗi liên tiếp chỉ tính lại sau một hành động khác.                                                                                                                                |
| Hesitation   | Tính 1 cho mỗi episode dừng/quét giao diện từ 5 giây, lặp việc tìm kiếm hoặc nói rõ sự không chắc chắn. Episode liên tục chỉ tính một lần.                                                                                                                                                |
| Can thiệp    | Ghi nguyên văn gợi ý và mốc thời gian. Nếu gợi ý tiết lộ vị trí/chức năng cần dùng thì task cao nhất là `Một phần`.                                                                                                                                                                       |
| SUS          | 10 phản hồi từ 1–5 sau task; tính riêng từng người rồi lấy trung bình của P1–P5.                                                                                                                                                                                                          |

### 3.2 Tiêu chí xác nhận task

| Mã    | Kết quả cần quan sát                                                        | Màn hình |
| ----- | --------------------------------------------------------------------------- | -------- |
| SC-01 | Bản nháp có `Event Title` duy nhất; đủ `Sub-description`, `Description`, bốn mốc `Date & Time`, `Location`, `Campus` và `Organizing Unit`. | A2 |
| SC-02 | `Allow Student Registration` và `Allow Waitlist` được bật; `Student Roles` không unlimited, `Max roles per student` = 1, `Role Name` = `Student`, `Max Slots` = 30. | A3 |
| SC-03 | `Allow Additional Role` được bật; tên vai trò là `Cộng tác viên` và có mô tả `Hỗ trợ tổ chức sự kiện`. | A3 |
| SC-04 | `Reminder before hours` = 24. | A3 |
| SC-05 | Sự kiện hiển thị ở trạng thái nháp trong danh sách và có thể được tìm thấy. | A1       |
| SC-06 | Sau khi tìm bản nháp ở A1 và mở ở chế độ chỉnh sửa, dữ liệu A2/A3 vẫn đúng. | A1/A2/A3 |

## 4. Kế hoạch tuyển người tham gia

### 4.1 Tiêu chí

- Tuyển 5 người chính và 1 người pilot riêng, tất cả đều ngoài lớp học phần này.
- Từ 18 tuổi và đã từng dùng biểu mẫu web.
- Ưu tiên sinh viên từng tổ chức hoạt động câu lạc bộ, giảng viên/nhân viên hoặc người từng quản trị sự kiện.
- Không tuyển người đã xem trước task, checklist hoặc kết quả Task 1B.
- Phải có liên hệ thật có thể xác minh; chỉ che phần giữa khi đưa vào bài nộp.

### 4.2 Lời mời mẫu

> Mình đang thực hiện bài kiểm thử tính khả dụng của một hệ thống quản lý sự kiện. Mình muốn mời bạn tham gia một phiên 20–25 phút, trong đó bạn thử hoàn thành một nhiệm vụ quản trị và trả lời bộ câu hỏi ngắn. Đây là kiểm thử sản phẩm, không phải kiểm tra bạn. Bài nộp chỉ hiển thị liên hệ đã che phần giữa; trợ giảng có thể liên hệ xác minh việc tham gia. Bạn có sẵn lòng tham gia không?

### 4.3 Danh sách cần xác nhận

| ID    | Hồ sơ mục tiêu                                | Hồ sơ/liên hệ thật | Trạng thái    |
| ----- | --------------------------------------------- | ------------------ | ------------- |
| PILOT | Người ngoài P1–P5, phù hợp gần nhóm mục tiêu  | Trần Hữu Lộc; `098****620` | Đã thực hiện; [video pilot](https://youtu.be/RBcwhBtWzQ0) |
| P1    | Sinh viên ngoài lớp | Phùng Ngọc Tuấn; `093****285` | Đã thực hiện; [video P1](https://www.youtube.com/watch?v=dilkwkxXt0Q) |
| P2    | Sinh viên ngoài lớp | Trần Tuấn Kiệt; `070****688` | Đã thực hiện; [video P2](https://youtu.be/ZKvHyMedWX4) |
| P3    | Sinh viên ngoài lớp | Vũ Thế Anh; `094****183` | Đã thực hiện; [video P3](https://youtu.be/mEJQPFBlc64) |
| P4    | Sinh viên ngoài lớp | Hồng Gia Bảo; `090****520` | Đã thực hiện; [video P4](https://www.youtube.com/watch?v=kyZxvvLCOkE) |
| P5    | Sinh viên ngoài lớp | Quách Vĩnh Kỳ; `094****445` | Đã thực hiện; [video P5](https://youtu.be/FmSO-TaYQxo) |

## 5. Bảng người tham gia

| ID  | Họ tên hoặc mã hóa   | Hồ sơ phù hợp | Liên hệ đã che       | Ngày giờ phiên | Thiết bị/trình duyệt | Minh chứng ghi hình |
| --- | -------------------- | ------------- | -------------------- | -------------- | -------------------- | ------------------- |
| P1  | Phùng Ngọc Tuấn | Sinh viên ngoài lớp | `093****285` | 15:30 ngày 03/08/2026 | Lenovo / Google Chrome | [YouTube – 23127326-Tuan](https://www.youtube.com/watch?v=dilkwkxXt0Q) |
| P2  | Trần Tuấn Kiệt | Sinh viên ngoài lớp | `070****688` | 16:05 ngày 03/08/2026 | MacBook Pro M1 Pro / Google Chrome | [YouTube – 23127326-Kiet](https://youtu.be/ZKvHyMedWX4) |
| P3  | Vũ Thế Anh | Sinh viên ngoài lớp | `094****183` | 16:20 ngày 03/08/2026 | Lenovo / Google Chrome | [YouTube – 23127326-TheAnh](https://youtu.be/mEJQPFBlc64) |
| P4  | Hồng Gia Bảo | Sinh viên ngoài lớp | `090****520` | 20:00 ngày 04/08/2026 | ASUS / Microsoft Edge | [YouTube – P4](https://www.youtube.com/watch?v=kyZxvvLCOkE) |
| P5  | Quách Vĩnh Kỳ | Sinh viên ngoài lớp | `094****445` | 22:30 ngày 04/08/2026 | Lenovo ThinkBook / Cốc Cốc | [YouTube – P5](https://youtu.be/FmSO-TaYQxo) |

## 6. Phiên pilot

| Nội dung                        | Ghi chú                                                         |
| ------------------------------- | --------------------------------------------------------------- |
| Trạng thái                      | Đã thực hiện; hoàn thành task trong `08:24`.                         |
| Người pilot                     | Trần Hữu Lộc; liên hệ đã che `098****620`; ngoài lớp và không thuộc P1–P5. |
| Minh chứng video                   | [YouTube – 23127326-PilotUser](https://youtu.be/RBcwhBtWzQ0)                 |
| Ngày giờ                        | 15:00 ngày 03/08/2026.                                           |
| Thiết bị/trình duyệt            | ASUS Zenbook 14 OLED / Microsoft Edge.                              |
| Consent                         | Đã đồng ý tham gia và ghi hình.                                  |
| Kết quả/thời gian task          | Hoàn thành / `08:24`.                                               |
| Error / hesitation / can thiệp    | `0 / 0 / 0`.                                                        |
| Vấn đề về câu chữ/dữ liệu/luồng | Không phát hiện vấn đề.                                          |
| Điều chỉnh sau pilot            | Không cần điều chỉnh.                                              |

### 6.1 Tiêu chí pilot đạt

- Người pilot hiểu mục tiêu và có thể bắt đầu mà không được chỉ vị trí nút.
- Dữ liệu thời gian được EMS chấp nhận và tên sự kiện là duy nhất.
- Luồng có thể đi qua A2, A3 và A1, không bị chặn bởi dữ liệu test hoặc lỗi môi trường.
- Toàn bộ phiên gồm task, SUS và probe có thể hoàn thành trong 20–25 phút.
- Mọi thay đổi sau pilot được khóa trước P1 và áp dụng giống nhau cho P1–P5.

## 7. Ghi chép từng phiên

### 7.1 Phiên P1

| Trường                         | Nội dung                       |
| ------------------------------ | ------------------------------ |
| Kết quả                        | Hoàn thành                     |
| Thời gian task                 | `08:42`                        |
| Error / Hesitation / Can thiệp | `1 / 1 / 0`                    |
| Điểm SUS                       | `60/100`                       |
| Consent                        | Đã đồng ý tham gia và ghi hình |
| Ngày giờ                       | 15:30 ngày 03/08/2026       |
| Video                          | [YouTube – 23127326-Tuan](https://www.youtube.com/watch?v=dilkwkxXt0Q) |

| Mốc thời gian | Quan sát | Loại                 | Minh chứng ảnh/video |
| ------------- | -------- | -------------------- | -------------------- |
| `07:55`       | Khi chọn `Academic Context` trong mục `Categories`, người dùng lúng túng và nói “này là sao”. | Lỗi + do dự | [Video/audio tại 07:55](https://youtu.be/dilkwkxXt0Q?t=475) |

### 7.2 Phiên P2

| Trường                         | Nội dung                       |
| ------------------------------ | ------------------------------ |
| Kết quả                        | Hoàn thành                     |
| Thời gian task                 | `03:29`                        |
| Error / Hesitation / Can thiệp | `0 / 0 / 0`                    |
| Điểm SUS                       | `80/100`                       |
| Consent                        | Đã đồng ý tham gia và ghi hình |
| Ngày giờ                       | 16:05 ngày 03/08/2026       |
| Thiết bị/trình duyệt           | MacBook Pro M1 Pro / Google Chrome |
| Video                          | [YouTube – 23127326-Kiet](https://youtu.be/ZKvHyMedWX4) |

| Mốc thời gian | Quan sát | Loại                 | Minh chứng ảnh/video |
| ------------- | -------- | -------------------- | -------------------- |
| —             | Không ghi nhận lỗi, do dự hoặc can thiệp trong phiên. | Nhận xét | [Video P2](https://youtu.be/ZKvHyMedWX4) |

### 7.3 Phiên P3

| Trường                         | Nội dung                       |
| ------------------------------ | ------------------------------ |
| Kết quả                        | Một phần – nhập sai title       |
| Thời gian task                 | `07:33`                        |
| Error / Hesitation / Can thiệp | `1 / 1 / 0`                    |
| Điểm SUS                       | `77.5/100`                     |
| Consent                        | Đã đồng ý tham gia và ghi hình |
| Ngày giờ                       | 16:20 ngày 03/08/2026       |
| Thiết bị/trình duyệt           | Lenovo / Google Chrome          |
| Video                          | [YouTube – 23127326-TheAnh](https://youtu.be/mEJQPFBlc64) |

| Mốc thời gian | Quan sát | Loại                 | Minh chứng ảnh/video |
| ------------- | -------- | -------------------- | -------------------- |
| `11:20`       | Người dùng nhấn `Save as Draft` hai lần nhưng màn hình không thay đổi và không hiển thị phản hồi; sau đó tự cuộn lên để tìm trường nhập sai. | Lỗi + do dự | [Video P3 tại 11:20](https://youtu.be/mEJQPFBlc64?t=680) |

### 7.4 Phiên P4

| Trường                         | Nội dung                       |
| ------------------------------ | ------------------------------ |
| Kết quả                        | Một phần – bật `Is Unlimited` trái yêu cầu |
| Thời gian task                 | `06:28`                        |
| Error / Hesitation / Can thiệp | `1` / `1` / `0`                |
| Điểm SUS                       | `75/100`                       |
| Consent                        | Đã đồng ý tham gia và ghi hình |
| Ngày giờ                       | 20:00 ngày 04/08/2026          |
| Thiết bị/trình duyệt           | ASUS / Microsoft Edge           |
| Video                          | [YouTube – P4](https://www.youtube.com/watch?v=kyZxvvLCOkE) |

| Mốc thời gian | Quan sát | Loại                 | Minh chứng ảnh/video |
| ------------- | -------- | -------------------- | -------------------- |
| `05:25`       | Người dùng do dự khi thao tác `Event Types`; quan sát cho thấy họ có vẻ không chắc giá trị đã được chọn hay chưa. | Do dự | [Video P4 tại 05:25](https://www.youtube.com/watch?v=kyZxvvLCOkE&t=325s) |
| —             | Người dùng bật `Is Unlimited`, trong khi dữ liệu task yêu cầu tắt; vì vậy phiên chỉ được tính là hoàn thành một phần. | Lỗi | [Video P4](https://www.youtube.com/watch?v=kyZxvvLCOkE) |

### 7.5 Phiên P5

| Trường                         | Nội dung                       |
| ------------------------------ | ------------------------------ |
| Kết quả                        | Một phần – mở nhầm sự kiện của người khác khi xác nhận |
| Thời gian task                 | `11:10`                        |
| Error / Hesitation / Can thiệp | `1` / `0` / `0`                |
| Điểm SUS                       | `77.5/100`                     |
| Consent                        | Đã đồng ý tham gia và ghi hình |
| Ngày giờ                       | 22:30 ngày 04/08/2026          |
| Thiết bị/trình duyệt           | Lenovo ThinkBook / Cốc Cốc     |
| Video                          | [YouTube – P5](https://youtu.be/FmSO-TaYQxo) |

| Mốc thời gian | Quan sát | Loại                 | Minh chứng ảnh/video |
| ------------- | -------- | -------------------- | -------------------- |
| —             | Ở bước cuối, người dùng mở nhầm sự kiện của người khác và cho rằng đó là sự kiện mình vừa tạo; không xác nhận đúng bản nháp theo SC-06. | Lỗi | [Video P5](https://youtu.be/FmSO-TaYQxo) |

## 8. Phiếu SUS sau task

Với mỗi câu, người tham gia chọn một mức: `1 = Hoàn toàn không đồng ý`, `2 = Không đồng ý`, `3 = Trung lập`, `4 = Đồng ý`, `5 = Hoàn toàn đồng ý`.

| Mã  | Mệnh đề                                                      |
| --- | ------------------------------------------------------------ |
| Q1  | Tôi nghĩ mình muốn sử dụng EMS thường xuyên.                 |
| Q2  | Tôi thấy EMS phức tạp một cách không cần thiết.              |
| Q3  | Tôi thấy EMS dễ sử dụng.                                     |
| Q4  | Tôi nghĩ mình sẽ cần người có chuyên môn hỗ trợ để dùng EMS. |
| Q5  | Tôi thấy các chức năng trong EMS được kết hợp tốt.           |
| Q6  | Tôi thấy EMS có quá nhiều điểm thiếu nhất quán.              |
| Q7  | Tôi nghĩ phần lớn mọi người sẽ học cách dùng EMS rất nhanh.  |
| Q8  | Tôi thấy EMS rườm rà khi sử dụng.                            |
| Q9  | Tôi cảm thấy tự tin khi sử dụng EMS.                         |
| Q10 | Tôi cần học nhiều thứ trước khi có thể sử dụng EMS.          |

**Cách tính:** với Q1, Q3, Q5, Q7, Q9, điểm đóng góp = phản hồi - 1. Với Q2, Q4, Q6, Q8, Q10, điểm đóng góp = 5 - phản hồi. Cộng 10 điểm đóng góp và nhân 2,5 để ra SUS 0–100.

Nguồn thang đo: [John Brooke, *SUS: A Quick and Dirty Usability Scale* (1996)](https://www.taylorfrancis.com/chapters/edit/10.1201/9781498710411-35/sus-quick-dirty-usability-scale-john-brooke). Điểm SUS là điểm quy đổi trên thang 0–100, không phải tỷ lệ phần trăm.

| Người tham gia |   Q1 |   Q2 |   Q3 |   Q4 |   Q5 |   Q6 |   Q7 |   Q8 |   Q9 |  Q10 | Điểm SUS |
| -------------- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | -------: |
| P1             |    4 |    2 |    4 |    1 |    3 |    3 |    2 |    2 |    4 |    5 |       60 |
| P2             |    3 |    1 |    4 |    1 |    3 |    1 |    4 |    1 |    3 |    1 |       80 |
| P3             |    4 |    2 |    5 |    2 |    4 |    1 |    3 |    2 |    3 |    1 |     77.5 |
| P4             |    3 |    1 |    5 |    2 |    3 |    3 |    5 |    1 |    4 |    3 |       75 |
| P5             |    3 |    1 |    5 |    3 |    5 |    2 |    5 |    2 |    4 |    3 |     77.5 |

## 9. Câu hỏi thăm dò sau task

Người điều phối hỏi nguyên văn theo thứ tự, không gợi ý câu trả lời:

1. Phần nào của nhiệm vụ rõ ràng nhất và phần nào khó hiểu nhất? Vì sao?
2. Khi gặp lỗi hoặc kết quả không như mong đợi, bạn đã biết cách tiếp tục hay không? Điều gì đã giúp hoặc cản trở bạn?
3. Cảm nhận của bạn về tốc độ thao tác và phản hồi của hệ thống là gì?
4. Ở thời điểm nào bạn tin hoặc không tin rằng dữ liệu đã được lưu đúng?
5. Nếu chỉ được thay đổi một điều trong luồng này, bạn sẽ thay đổi điều gì trước?

| Câu hỏi                  | P1  | P2  | P3  | P4  | P5  | Chủ đề rút ra |
| ------------------------ | --- | --- | --- | --- | --- | ------------- |
| Rõ ràng/khó hiểu         | Việc tạo hoạt động nhìn chung rõ ràng; `Academic Context` là chỗ khó hiểu. | Tạo sự kiện có giao diện trực quan và thông báo lỗi rõ ràng. | Phần lên kế hoạch sự kiện rõ ràng vì có đủ chi tiết thời gian, phân công và mô tả; phần xem log khó hiểu. | Các nhiệm vụ đều rõ ràng; phần tự chọn `Event Types` gây bối rối vì chưa biết nên chọn gì. | Không có phần nào được nêu là đặc biệt rõ ràng hoặc khó hiểu. | Tổng thể trực quan; `Academic Context`, `Event Types` và phần xem log cần giải thích rõ hơn |
| Phục hồi khi lỗi         | Không gặp khó khăn gì. | Có thể tiếp tục vì thông báo lỗi dễ hiểu và dễ sửa. | Không biết cách sửa ngay vì hệ thống không thông báo lỗi nằm ở đâu. | Đọc thông báo lỗi hiển thị trên màn hình và sửa được lỗi. | Biết cách tiếp tục nhưng hơi khó hiểu vì không có thông báo lỗi chung dạng pop-up. | Trải nghiệm phục hồi không nhất quán; P3 và P5 cần phản hồi lỗi tổng thể rõ hơn |
| Tốc độ/phản hồi          | Hệ thống có giật nhẹ tại chỗ thiết lập số lượng student. | Ổn định và nhanh chóng. | Tạm ổn, nhưng thao tác chọn giờ khó dùng, phải kéo chuột mạnh; nên cho phép nhập giờ trực tiếp. | Hệ thống phản hồi nhanh, nhưng thao tác chọn giờ rất chậm. | Khá nhanh. | Phản hồi nhìn chung tốt; điều khiển thời gian gây ma sát thao tác |
| Tin tưởng dữ liệu đã lưu | Sau khi mở lại chế độ chỉnh sửa và thấy dữ liệu đã lưu, người dùng cảm thấy tin tưởng. | Sau khi tạo sự kiện, người dùng xem bản nháp để kiểm tra và tin rằng dữ liệu đã lưu. | Chưa tin ngay sau khi bấm save; chỉ chắc chắn sau khi mở phần xem/chỉnh sửa và thấy dữ liệu. | Tin dữ liệu đã lưu khi submit, nhưng vẫn cần vào kiểm tra lại một lần. | Tin dữ liệu đã lưu khi hệ thống chuyển về trang danh sách. | Phần lớn người dùng dựa vào trang danh sách hoặc kiểm tra lại bản nháp/chỉnh sửa để xác nhận dữ liệu đã lưu |
| Thay đổi ưu tiên         | Gom các trường thiết lập thời gian vào một chỗ. | Không đề xuất thay đổi; cảm thấy hệ thống ổn. | Thay đổi phần chỉnh giờ vì đây là phần phiền và mất thời gian nhất. | Không đề xuất thay đổi. | Thay đổi cách hệ thống xử lý lỗi trường nhập sai. | P1 muốn gom nhóm thời gian; P3 muốn cải thiện cách nhập giờ; P5 muốn cải thiện xử lý lỗi |
