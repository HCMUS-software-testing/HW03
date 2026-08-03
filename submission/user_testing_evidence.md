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

> Bạn là cộng tác viên quản trị sự kiện của khoa. Ban tổ chức cần bạn chuẩn bị một sự kiện học thuật mới ở trạng thái bản nháp, cấu hình đăng ký cho sinh viên và một vai trò cộng tác viên bổ sung, sau đó tìm và mở lại sự kiện trong danh sách quản trị để xác nhận dữ liệu đã được lưu. Không xuất bản hoặc xóa sự kiện.

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
| Task success | `Hoàn thành`: có bản nháp, đủ dữ liệu A2/A3 và mở lại xác nhận mà không cần gợi ý. `Một phần`: lưu được bản nháp nhưng thiếu ít nhất một yêu cầu, không xác nhận được hoặc phải nhận gợi ý. `Thất bại`: không tạo được bản nháp dùng được trong 15 phút hoặc để người điều phối làm thay. |
| Time on task | Bắt đầu khi người tham gia nói đã hiểu nhiệm vụ; dừng khi họ mở lại bản nháp và tuyên bố hoàn tất, bỏ cuộc hoặc chạm 15 phút. Ghi `mm:ss`.                                                                                                                                                |
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
| SC-06 | Sau khi mở lại từ A1, dữ liệu A2/A3 vẫn đúng.                               | A1/A2/A3 |

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
| PILOT | Người ngoài P1–P5, phù hợp gần nhóm mục tiêu  | Chưa cung cấp      | Chưa xác nhận |
| P1    | Sinh viên từng tổ chức hoạt động              | Chưa cung cấp      | Chưa xác nhận |
| P2    | Sinh viên từng tổ chức hoạt động              | Chưa cung cấp      | Chưa xác nhận |
| P3    | Sinh viên/người tham dự sự kiện thường xuyên  | Chưa cung cấp      | Chưa xác nhận |
| P4    | Giảng viên/nhân viên                          | Chưa cung cấp      | Chưa xác nhận |
| P5    | Người từng quản trị sự kiện hoặc biểu mẫu web | Chưa cung cấp      | Chưa xác nhận |

## 5. Bảng người tham gia

| ID  | Họ tên hoặc mã hóa   | Hồ sơ phù hợp | Liên hệ đã che       | Ngày giờ phiên | Thiết bị/trình duyệt | Minh chứng ghi hình |
| --- | -------------------- | ------------- | -------------------- | -------------- | -------------------- | ------------------- |
| P1  | Chưa có dữ liệu thật | Chưa xác nhận | Chưa có dữ liệu thật | Chưa xếp lịch  | Chưa ghi nhận        | Chưa ghi nhận       |
| P2  | Chưa có dữ liệu thật | Chưa xác nhận | Chưa có dữ liệu thật | Chưa xếp lịch  | Chưa ghi nhận        | Chưa ghi nhận       |
| P3  | Chưa có dữ liệu thật | Chưa xác nhận | Chưa có dữ liệu thật | Chưa xếp lịch  | Chưa ghi nhận        | Chưa ghi nhận       |
| P4  | Chưa có dữ liệu thật | Chưa xác nhận | Chưa có dữ liệu thật | Chưa xếp lịch  | Chưa ghi nhận        | Chưa ghi nhận       |
| P5  | Chưa có dữ liệu thật | Chưa xác nhận | Chưa có dữ liệu thật | Chưa xếp lịch  | Chưa ghi nhận        | Chưa ghi nhận       |

## 6. Phiên pilot

| Nội dung                        | Ghi chú                                                         |
| ------------------------------- | --------------------------------------------------------------- |
| Trạng thái                      | Chưa thực hiện với người thật; không được ghi là đã hoàn thành. |
| Người pilot                     | Cần 1 người ngoài P1–P5, phù hợp gần nhóm mục tiêu.             |
| Ngày giờ                        | Chưa xếp lịch.                                                  |
| Consent                         | Chưa ghi nhận.                                                  |
| Kết quả/thời gian task          | Chưa ghi nhận.                                                  |
| Vấn đề về câu chữ/dữ liệu/luồng | Chờ quan sát pilot thật.                                        |
| Điều chỉnh sau pilot            | Chỉ ghi thay đổi đã thực hiện sau khi có evidence thật.         |

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
| Kết quả                        | [Hoàn thành/Một phần/Thất bại] |
| Thời gian task                 | [mm:ss]                        |
| Error / Hesitation / Can thiệp | [ ] / [ ] / [ ]                |
| Điểm SUS                       | [ ]                            |

| Mốc thời gian | Quan sát | Loại                 | Minh chứng ảnh/video |
| ------------- | -------- | -------------------- | -------------------- |
| [00:00]       | [ ]      | [Lỗi/Do dự/Nhận xét] | [ ]                  |

### 7.2 Phiên P2

| Trường                         | Nội dung                       |
| ------------------------------ | ------------------------------ |
| Kết quả                        | [Hoàn thành/Một phần/Thất bại] |
| Thời gian task                 | [mm:ss]                        |
| Error / Hesitation / Can thiệp | [ ] / [ ] / [ ]                |
| Điểm SUS                       | [ ]                            |

| Mốc thời gian | Quan sát | Loại                 | Minh chứng ảnh/video |
| ------------- | -------- | -------------------- | -------------------- |
| [00:00]       | [ ]      | [Lỗi/Do dự/Nhận xét] | [ ]                  |

### 7.3 Phiên P3

| Trường                         | Nội dung                       |
| ------------------------------ | ------------------------------ |
| Kết quả                        | [Hoàn thành/Một phần/Thất bại] |
| Thời gian task                 | [mm:ss]                        |
| Error / Hesitation / Can thiệp | [ ] / [ ] / [ ]                |
| Điểm SUS                       | [ ]                            |

| Mốc thời gian | Quan sát | Loại                 | Minh chứng ảnh/video |
| ------------- | -------- | -------------------- | -------------------- |
| [00:00]       | [ ]      | [Lỗi/Do dự/Nhận xét] | [ ]                  |

### 7.4 Phiên P4

| Trường                         | Nội dung                       |
| ------------------------------ | ------------------------------ |
| Kết quả                        | [Hoàn thành/Một phần/Thất bại] |
| Thời gian task                 | [mm:ss]                        |
| Error / Hesitation / Can thiệp | [ ] / [ ] / [ ]                |
| Điểm SUS                       | [ ]                            |

| Mốc thời gian | Quan sát | Loại                 | Minh chứng ảnh/video |
| ------------- | -------- | -------------------- | -------------------- |
| [00:00]       | [ ]      | [Lỗi/Do dự/Nhận xét] | [ ]                  |

### 7.5 Phiên P5

| Trường                         | Nội dung                       |
| ------------------------------ | ------------------------------ |
| Kết quả                        | [Hoàn thành/Một phần/Thất bại] |
| Thời gian task                 | [mm:ss]                        |
| Error / Hesitation / Can thiệp | [ ] / [ ] / [ ]                |
| Điểm SUS                       | [ ]                            |

| Mốc thời gian | Quan sát | Loại                 | Minh chứng ảnh/video |
| ------------- | -------- | -------------------- | -------------------- |
| [00:00]       | [ ]      | [Lỗi/Do dự/Nhận xét] | [ ]                  |

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
| P1             |  [ ] |  [ ] |  [ ] |  [ ] |  [ ] |  [ ] |  [ ] |  [ ] |  [ ] |  [ ] |      [ ] |
| P2             |  [ ] |  [ ] |  [ ] |  [ ] |  [ ] |  [ ] |  [ ] |  [ ] |  [ ] |  [ ] |      [ ] |
| P3             |  [ ] |  [ ] |  [ ] |  [ ] |  [ ] |  [ ] |  [ ] |  [ ] |  [ ] |  [ ] |      [ ] |
| P4             |  [ ] |  [ ] |  [ ] |  [ ] |  [ ] |  [ ] |  [ ] |  [ ] |  [ ] |  [ ] |      [ ] |
| P5             |  [ ] |  [ ] |  [ ] |  [ ] |  [ ] |  [ ] |  [ ] |  [ ] |  [ ] |  [ ] |      [ ] |

## 9. Câu hỏi thăm dò sau task

Người điều phối hỏi nguyên văn theo thứ tự, không gợi ý câu trả lời:

1. Phần nào của nhiệm vụ rõ ràng nhất và phần nào khó hiểu nhất? Vì sao?
2. Khi gặp lỗi hoặc kết quả không như mong đợi, bạn đã biết cách tiếp tục hay không? Điều gì đã giúp hoặc cản trở bạn?
3. Cảm nhận của bạn về tốc độ thao tác và phản hồi của hệ thống là gì?
4. Ở thời điểm nào bạn tin hoặc không tin rằng dữ liệu đã được lưu đúng?
5. Nếu chỉ được thay đổi một điều trong luồng này, bạn sẽ thay đổi điều gì trước?

| Câu hỏi                  | P1  | P2  | P3  | P4  | P5  | Chủ đề rút ra |
| ------------------------ | --- | --- | --- | --- | --- | ------------- |
| Rõ ràng/khó hiểu         | [ ] | [ ] | [ ] | [ ] | [ ] | [ ]           |
| Phục hồi khi lỗi         | [ ] | [ ] | [ ] | [ ] | [ ] | [ ]           |
| Tốc độ/phản hồi          | [ ] | [ ] | [ ] | [ ] | [ ] | [ ]           |
| Tin tưởng dữ liệu đã lưu | [ ] | [ ] | [ ] | [ ] | [ ] | [ ]           |
| Thay đổi ưu tiên         | [ ] | [ ] | [ ] | [ ] | [ ] | [ ]           |
