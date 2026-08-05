# Báo cáo tính khả dụng - Kịch bản A

## 1. Thông tin chung

| Trường | Nội dung |
| --- | --- |
| Sinh viên | Lê Mai Hoài Bảo |
| MSSV | 23127326 |
| Scenario | A - Admin creates and manages events |
| Màn hình liên quan | A1 Events list, A2 Add/Edit Event, A3 Registration & Roles |
| Ngày chuẩn bị Phase 1 | 2026-08-03 |
| Ngày chạy 5 phiên | Chưa xếp lịch |
| Video pilot | [23127326-PilotUser](https://youtu.be/RBcwhBtWzQ0) |
| Phương pháp điểm số | System Usability Scale (SUS), thang 0–100 |
| Evidence thô | `submission/user_testing_evidence.md` |

## 2. Kịch bản nhiệm vụ

> Bạn là cộng tác viên quản trị sự kiện của khoa. Ban tổ chức cần bạn chuẩn bị một sự kiện học thuật mới ở trạng thái bản nháp, cấu hình đăng ký cho sinh viên và một vai trò cộng tác viên bổ sung, sau đó tìm sự kiện trong danh sách quản trị và mở lại ở chế độ chỉnh sửa để xác nhận dữ liệu đã được lưu. Không xuất bản hoặc xóa sự kiện.

Dữ liệu nghiệp vụ, tiêu chí hoàn thành, quy tắc quan sát, bộ câu SUS và câu hỏi thăm dò được khóa trong `submission/user_testing_evidence.md` trước khi chạy pilot.

## 3. Trạng thái Giai đoạn 1

| Hạng mục | Trạng thái | Minh chứng |
| --- | --- | --- |
| Kịch bản theo mục tiêu | Đã soạn | Mục 2 và `submission/user_testing_evidence.md` |
| Chỉ số và quy tắc đếm | Đã soạn | Kết quả task, thời gian, lỗi, do dự, can thiệp và SUS |
| Câu hỏi thăm dò | Đã soạn | Clarity, error recovery, speed, trust và ưu tiên thay đổi |
| Tiêu chí tuyển người tham gia | Đã soạn | 5 người chính + 1 pilot, đều ngoài lớp |
| Tuyển đủ 5 người thật | Chưa xác nhận | Không bịa hồ sơ/liên hệ |
| Chạy pilot với 1 người thật | Đã thực hiện | Trần Hữu Lộc (`098****620`), ngoài lớp/P1–P5, đã consent; hoàn thành trong `08:24`, error/hesitation/can thiệp `0/0/0`; không phát hiện vấn đề, không cần điều chỉnh; [video](https://youtu.be/RBcwhBtWzQ0) |

## 4. Tóm tắt người tham gia

| ID | Hồ sơ phù hợp | Liên hệ đã che | Kết quả | Thời gian | Lỗi | Do dự | SUS |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| P1 | Sinh viên ngoài lớp, đã consent | `093****285` | Hoàn thành | `08:42` | `1` | `1` | `60` |
| P2 | Sinh viên ngoài lớp, đã consent | `070****688` | Hoàn thành | `03:29` | `0` | `0` | `80` |
| P3 | Sinh viên ngoài lớp, đã consent | `094****183` | Một phần | `07:33` | `1` | `1` | `77.5` |
| P4 | Sinh viên ngoài lớp, đã consent | `090****520` | Một phần | `06:28` | `1` | `1` | `75` |
| P5 | Sinh viên ngoài lớp, đã consent | `094****445` | Một phần | `11:10` | `1` | `0` | `77.5` |

## 5. Tóm tắt chỉ số

| Chỉ số | Kết quả |
| --- | ---: |
| Tỷ lệ hoàn thành | P1–P5: `40%` hoàn thành (2/5), `60%` một phần (3/5) |
| Thời gian trung bình | P1–P5: `07:28` (làm tròn) |
| Số lỗi trung bình | P1–P5: `0.80` |
| Số lần do dự trung bình | P1–P5: `0.60` |
| Điểm SUS trung bình | P1–P5: `74.0` |

## 6. Phát hiện theo mức độ

Mức độ: 0 = không phải vấn đề, 1 = thẩm mỹ/khó chịu nhỏ, 2 = vấn đề nhỏ có cách xử lý thay thế, 3 = nghiêm trọng, 4 = chặn task hoặc gây mất dữ liệu.

| ID | Màn hình | Phát hiện | Bằng chứng | Mức độ | Minh chứng ảnh/video | Khuyến nghị | Thời gian biểu mẫu |
| --- | --- | --- | --- | ---: | --- | --- | --- |
| UX-001 | A2 – Categories | Nhãn `Academic Context` không đủ rõ để người dùng biết cần chọn ngữ cảnh nào. | P1 do dự tại `07:55` và nói “này là sao”; [video](https://youtu.be/dilkwkxXt0Q?t=475). | 2 | [Video/audio P1 tại 07:55](https://youtu.be/dilkwkxXt0Q?t=475) | Thêm mô tả ngắn/ví dụ dưới nhãn `Academic Context` và làm rõ quan hệ với `Event Types`. | Chờ sinh viên gửi form |
| UX-002 | A2 – Save as Draft/validation | Khi form có trường không hợp lệ, nhấn `Save as Draft` không có phản hồi tổng thể và không đưa người dùng tới trường lỗi. | P3 tại `11:20` nhấn hai lần không thấy thay đổi, phải tự cuộn lên tìm lỗi; P5 cũng cho biết khó hiểu vì không có thông báo lỗi chung dạng pop-up; [video P3](https://youtu.be/mEJQPFBlc64?t=680), [video P5](https://youtu.be/FmSO-TaYQxo). | 2 | [Video P3 tại 11:20](https://youtu.be/mEJQPFBlc64?t=680); [video/audio probe P5](https://youtu.be/FmSO-TaYQxo) | Khi submit thất bại, hiển thị thông báo/tóm tắt validation và tự cuộn, đưa focus tới trường lỗi đầu tiên. | Chờ sinh viên gửi form |
| UX-003 | A2 – Date & Time | Thao tác chọn/chỉnh giờ bằng điều khiển kéo gây khó khăn và mất thời gian. | P3 cho biết phải kéo chuột mạnh, đây là phần phiền nhất và muốn nhập giờ trực tiếp; [video P3](https://youtu.be/mEJQPFBlc64). | 2 | [Video/audio probe P3](https://youtu.be/mEJQPFBlc64) | Cho phép nhập giờ trực tiếp bằng bàn phím, giữ time picker dễ thao tác và gom các trường thời gian liên quan. | Chờ sinh viên gửi form |
| UX-004 | A2 – Categories | Trạng thái đã chọn của `Event Types` không đủ rõ, khiến người dùng không chắc lựa chọn đã được ghi nhận hay chưa. | P4 do dự tại `05:25` khi danh sách `Event Types` đang mở; [video](https://www.youtube.com/watch?v=kyZxvvLCOkE&t=325s). | 2 | [Video P4 tại 05:25](https://www.youtube.com/watch?v=kyZxvvLCOkE&t=325s) | Hiển thị lựa chọn hiện tại rõ ràng trong ô, thêm dấu chọn cho option đã chọn và giữ phản hồi sau khi danh sách đóng. | Chờ sinh viên gửi form |

## 7. Phân tích

### 7.1 Nhóm điểm khó sử dụng

[Nhóm các vấn đề tương tự nhau. Tách bug riêng lẻ khỏi vấn đề thiết kế có tính hệ thống.]

### 7.2 Ảnh hưởng tới trải nghiệm

[Phân tích ảnh hưởng tới clarity, error recovery, speed và trust.]

### 7.3 Khuyến nghị theo độ ưu tiên

| Ưu tiên | Khuyến nghị | Lý do | Phát hiện liên quan |
| --- | --- | --- | --- |
| P0 | [Sửa ngay] | [Ảnh hưởng nghiêm trọng] | [UX-...] |
| P1 | Thêm giải thích/ví dụ cho `Academic Context`. | P1 không hiểu ngay ý nghĩa trường nhưng vẫn hoàn thành task. | UX-001 |
| P1 | Hiển thị validation tổng thể và focus trường lỗi sau khi nhấn `Save as Draft`. | P3 nhấn hai lần không có phản hồi và phải tự tìm lỗi. | UX-002 |
| P1 | Cho phép nhập giờ trực tiếp và cải thiện time picker. | P3 xem đây là phần phiền và mất thời gian nhất. | UX-003 |
| P1 | Làm nổi bật trạng thái đã chọn của `Event Types`. | P4 do dự vì không chắc lựa chọn đã được ghi nhận. | UX-004 |
