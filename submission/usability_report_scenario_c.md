# Task 2 - Báo cáo tính khả dụng & Minh chứng kiểm thử người dùng (Usability Report & User-Testing Evidence)

**Sinh viên:** Lâm Hữu Khánh - 23127205
**Kịch bản:** C - Admin quản lý người dùng
**Màn hình kiểm thử:** C1 Danh sách người dùng; C2 Gán vai trò / chỉnh sửa người dùng; C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu
**Hệ thống kiểm thử (SUT):** EMS - Event Management System (`https://prod-dev.ems-fitus.cloud/dashboard`)
**Thang đo:** SUS, mức hoàn thành nhiệm vụ, thời gian thực hiện, số lỗi, số lần do dự, số lần trợ giúp
**Thư mục minh chứng ảnh:** `submission/screenshots/checklist-failures/`
**Video minh chứng:** `submission/demo-videos.md` (`evidence/task2_scenario_c/`)

---

## 1. Mục tiêu kiểm thử (Test Objective)

Phiên kiểm thử tính khả dụng này đánh giá liệu một admin EMS mới hoặc thỉnh thoảng sử dụng có thể tìm kiếm người dùng mục tiêu, hiểu rõ trạng thái và vai trò của người dùng, thực hiện các thao tác vai trò/trạng thái/mật khẩu, và xác nhận hệ thống hoàn tất thao tác một cách chính xác hay không.

Nội dung kiểm thử tập trung vào:

- Độ rõ ràng của Danh sách người dùng, bộ lọc, các cột vai trò/trạng thái và hành vi tìm kiếm.
- Mức độ tự tin và khả năng phòng ngừa lỗi trong các thao tác Gán vai trò / Chỉnh sửa người dùng.
- Chất lượng xác nhận, khả năng phục hồi lỗi và độ tin cậy trong các hộp thoại Chặn / Bỏ chặn và Đặt lại mật khẩu.
- Cảm nhận tính khả dụng của người dùng được đo bằng thang điểm SUS sau nhiệm vụ.

---

## 2. Kịch bản nhiệm vụ (Task Scenario)

```text
Bạn là admin của EMS. Hãy tìm một người dùng mục tiêu, kiểm tra trạng thái tài khoản, thay đổi vai trò nếu cần, thử thao tác chặn/bỏ chặn hoặc reset mật khẩu theo yêu cầu được giao, rồi xác nhận xem hệ thống đã hoàn tất thao tác hay chưa.
```

Người tham gia nhận được mục tiêu mở ở trên, không phải là hướng dẫn chi tiết từng cú click. Người điều phối có thể làm rõ ngữ cảnh vai trò nhưng không được chỉ trực tiếp vào nút, menu, bộ lọc hay hộp thoại nào trừ khi người tham gia hoàn toàn bị tắc và sự can thiệp được tính là trợ giúp (Assistance).

---

## 3. Bảng 5 người tham gia phỏng vấn (Table of 5 Participants - Masked Contacts)

Người tham gia là 5 người thật ngoài lớp học. Số Zalo/điện thoại được che trong báo cáo bằng cách ẩn 4 chữ số giữa, danh sách liên hệ gốc chưa che được sinh viên lưu trữ riêng để đối chiếu khi TA xác minh.

| Mã ID | Họ và tên            | Hồ sơ     | Tuổi | Mức quen thuộc EMS/admin | Zalo/SĐT đã che | Đồng ý tham gia | Video ghi hình YouTube                                                                | Ghi chú                               |
| ----- | -------------------- | --------- | ---: | ------------------------ | --------------- | --------------- | ------------------------------------------------------------------------------------- | ------------------------------------- |
| Pilot | Thới Đặng Trường Thọ | Sinh viên |   21 | Trung bình               | 037\*\*\*\*6252 | Đồng ý          | https://youtu.be/lpxRwuFYGBM                                                          | Phiên thử nghiệm kịch bản pilot       |
| P01   | Trần Hữu Lộc         | Sinh viên |   21 | Trung bình               | 084\*\*\*\*3053 | Đồng ý          | https://youtu.be/Qg45dvZBvzo                                                          | Người dùng ngoài lớp (Edge / Windows) |
| P02   | Lê Minh Đức          | Sinh viên |   21 | Trung bình               | 038\*\*\*\*4909 | Đồng ý          | https://youtu.be/MnQzUx25SYI                                                          | Người dùng ngoài lớp (Edge / Windows) |
| P03   | Phùng Ngọc Tuấn      | Sinh viên |   21 | Trung bình               | 093\*\*\*\*2285 | Đồng ý          | https://youtu.be/5hYpKizmWhA                                                          | Người dùng ngoài lớp (Edge / Windows) |
| P04   | Lê Tuấn Anh          | Sinh viên |   21 | Trung bình               | 084\*\*\*\*1688 | Đồng ý          | https://drive.google.com/file/d/1hon0elJEEtFcuhF9n13mTz2mttJw3a5T/view?usp=sharing \* | Người dùng ngoài lớp (Edge / Windows) |
| P05   | Vũ Thế Anh           | Sinh viên |   21 | Trung bình               | 094\*\*\*\*5183 | Đồng ý          | https://youtu.be/ysRW-LvCq_M                                                          | Người dùng ngoài lớp (Edge / Windows) |

> _\* Ghi chú cho P04 (Lê Tuấn Anh): Do chính sách quyền riêng tư và bảo mật thông tin cá nhân của YouTube chặn công khai video phỏng vấn cá nhân, video của P04 được lưu trữ trực tiếp trên Google Drive (đã có sự xin phép và đồng ý của người tham gia)._

---

## 4. Tóm tắt phiên Pilot (Pilot Summary)

| Trường                           | Kết quả                                                                                                                               |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Người tham gia pilot             | Thới Đặng Trường Thọ, 21 tuổi, 037\*\*\*\*6252                                                                                        |
| Ngày/giờ                         | 2026-08-04 10:57                                                                                                                      |
| Thiết bị/trình duyệt             | Chrome trên laptop Windows                                                                                                            |
| Link Video YouTube ghi hình      | https://youtu.be/lpxRwuFYGBM                                                                                                          |
| Ảnh/video minh chứng             | `submission/screenshots/checklist-failures/C-F005.png`                                                                                |
| Điểm chưa rõ chính phát hiện     | Quy tắc mật khẩu chưa đủ rõ trong lúc nhập; người tham gia nhập mật khẩu bị báo lỗi.                                                  |
| Điều chỉnh trước các phiên chính | Bổ sung danh mục quan sát của người điều phối tập trung vào gợi ý mật khẩu và các nút Block/Reset Password không thấy trên giao diện. |
| Kết luận phiên pilot             | Luồng nhiệm vụ chạy được, giữ nguyên kịch bản mở cho 5 phiên chính thức P01-P05.                                                      |

---

## 5. Quy trình phiên kiểm thử (Session Protocol & Rules)

Lời mở đầu:

```text
Mình đang kiểm thử sản phẩm, không phải kiểm tra bạn. Nếu thấy khó hiểu, bạn cứ nói ra suy nghĩ của mình. Mình sẽ quan sát cách hệ thống hỗ trợ bạn thực hiện nhiệm vụ.
```

Quy tắc quan sát:

- Bắt đầu tính giờ sau khi người tham gia đọc xong nhiệm vụ.
- Đếm **1 Lỗi (Error)** khi người tham gia bấm nhầm điều khiển, chọn sai người dùng, hiểu sai vai trò/trạng thái, gửi thao tác ngoài ý muốn, hoặc nhập tìm kiếm/bộ lọc không hiệu quả.
- Đếm **1 Lần do dự (Hesitation)** khi người tham gia dừng lại hơn 3 giây, hỏi ý nghĩa điều khiển, đọc lại dialog lâu, hoặc di chuyển liên tục giữa các màn hình mà không tiến triển.
- Đếm **1 Lần trợ giúp (Assistance)** mỗi khi người điều phối đưa ra gợi ý vượt quá việc nhắc lại mục tiêu ban đầu.
- Dừng tính giờ khi người tham gia báo hoàn thành, bỏ cuộc, hoặc đạt mốc dừng do người điều phối quy định.

Các câu hỏi phỏng vấn sau nhiệm vụ (Probe questions):

```text
1. Phần nào trên Users list khiến bạn dễ hoặc khó tìm đúng người dùng?
2. Khi đổi role hoặc chỉnh user, bạn có thấy hệ thống giải thích đủ rõ hậu quả thao tác không?
3. Dialog block/unblock/reset password có làm bạn đủ tin tưởng trước khi xác nhận không?
4. Nếu thao tác sai, bạn có biết cách phục hồi hoặc quay lại không?
5. Bạn muốn thay đổi điều gì đầu tiên để thao tác nhanh hơn?
```

---

## 6. Chỉ số nhiệm vụ tổng hợp (Task Metrics Table)

| Mã ID                  | Mức hoàn thành  | Thời gian thực hiện | Số lỗi (Errors) | Do dự (Hesitations) | Trợ giúp (Assistance) | Điểm SUS | Mã minh chứng lỗi            |
| ---------------------- | --------------- | ------------------: | --------------: | ------------------: | --------------------: | -------: | ---------------------------- |
| P01                    | Completed       |               5m00s |               3 |                   2 |                     2 |     77.5 | `C-F014`, `C-F015`, `C-F016` |
| P02                    | Completed       |               4m30s |               3 |                   1 |                     1 |     87.5 | `C-F016`, `C-U001`           |
| P03                    | Completed       |               3m50s |               2 |                   2 |                     2 |     90.0 | `C-U001`, `C-U002`           |
| P04                    | Completed       |               3m29s |               2 |                   3 |                     3 |     70.0 | `C-U001`, `C-U002`           |
| P05                    | Completed       |               4m00s |               2 |                   1 |                     1 |     90.0 | `C-U001`, `C-U002`           |
| **Trung bình / Tỷ lệ** | 100% hoàn thành |               4m10s |             2.4 |                 1.8 |                   1.8 | **83.0** | -                            |

Tóm tắt tính toán:

- Tỷ lệ thành công: `5 / 5 * 100 = 100%`
- Số phiên thất bại/bán phần: `0`
- Thời gian trung bình: `4m10s` (Trung vị: `4m00s`)
- Số lỗi trung bình: `2.4` lỗi / người
- Số lần do dự trung bình: `1.8` lần / người
- Số lần trợ giúp trung bình: `1.8` lần / người
- Điểm SUS trung bình: **`83.0 / 100`** (Xếp hạng A - Good Usability)

---

## 7. Bảng điểm thô 10 câu SUS & Phương pháp tính (SUS Raw Responses & Scoring)

### 7.1 Thang đo 10 câu SUS

| Câu | Nội dung câu hỏi System Usability Scale                                                  |
| --: | ---------------------------------------------------------------------------------------- |
|   1 | Tôi nghĩ rằng tôi sẽ muốn sử dụng hệ thống này thường xuyên.                             |
|   2 | Tôi thấy hệ thống này phức tạp một cách không cần thiết.                                 |
|   3 | Tôi nghĩ rằng hệ thống này dễ sử dụng.                                                   |
|   4 | Tôi nghĩ rằng tôi sẽ cần sự hỗ trợ của một kỹ thuật viên để có thể sử dụng hệ thống này. |
|   5 | Tôi thấy các chức năng trong hệ thống này được tích hợp tốt.                             |
|   6 | Tôi nghĩ rằng có quá nhiều sự không nhất quán trong hệ thống này.                        |
|   7 | Tôi tưởng tượng rằng hầu hết mọi người sẽ học cách sử dụng hệ thống này rất nhanh.       |
|   8 | Tôi thấy hệ thống này rất cồng kềnh khi sử dụng.                                         |
|   9 | Tôi cảm thấy rất tự tin khi sử dụng hệ thống.                                            |
|  10 | Tôi cần phải học nhiều thứ trước khi có thể bắt đầu sử dụng hệ thống này.                |

### 7.2 Bảng trả lời thô 10 câu hỏi SUS (1 = Rất không đồng ý, 5 = Rất đồng ý)

| Mã ID          |  C1 |  C2 |  C3 |  C4 |  C5 |  C6 |  C7 |  C8 |  C9 | C10 | Tổng điểm đóng góp | Điểm SUS chuẩn |
| -------------- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | -----------------: | -------------: |
| P01            |   4 |   2 |   4 |   2 |   5 |   2 |   4 |   2 |   4 |   2 |                 31 |       **77.5** |
| P02            |   5 |   1 |   4 |   2 |   4 |   2 |   5 |   1 |   5 |   2 |                 35 |       **87.5** |
| P03            |   5 |   2 |   5 |   2 |   5 |   2 |   5 |   2 |   5 |   1 |                 36 |       **90.0** |
| P04            |   4 |   3 |   4 |   2 |   4 |   3 |   4 |   2 |   4 |   2 |                 28 |       **70.0** |
| P05            |   5 |   2 |   5 |   1 |   5 |   2 |   4 |   2 |   5 |   1 |                 36 |       **90.0** |
| **Trung bình** |   - |   - |   - |   - |   - |   - |   - |   - |   - |   - |                  - |       **83.0** |

### 7.3 Công thức tính điểm SUS

Với mỗi người tham gia:

- Câu lẻ (1, 3, 5, 7, 9): điểm đóng góp = điểm thô - 1
- Câu chẵn (2, 4, 6, 8, 10): điểm đóng góp = 5 - điểm thô
- Tổng điểm đóng góp = tổng 10 câu đóng góp
- **Điểm SUS chuẩn = Tổng điểm đóng góp \* 2.5**

Chi tiết tính toán:

- **P01:** Điểm đóng góp (3, 3, 3, 3, 4, 3, 3, 3, 3, 3) = 31; SUS = 31 \* 2.5 = **77.5**
- **P02:** Điểm đóng góp (4, 4, 3, 3, 3, 3, 4, 4, 4, 3) = 35; SUS = 35 \* 2.5 = **87.5**
- **P03:** Điểm đóng góp (4, 3, 4, 3, 4, 3, 4, 3, 4, 4) = 36; SUS = 36 \* 2.5 = **90.0**
- **P04:** Điểm đóng góp (3, 2, 3, 3, 3, 2, 3, 3, 3, 3) = 28; SUS = 28 \* 2.5 = **70.0**
- **P05:** Điểm đóng góp (4, 3, 4, 4, 4, 3, 3, 3, 4, 4) = 36; SUS = 36 \* 2.5 = **90.0**

---

## 8. Nhật ký quan sát thô & Phỏng vấn mở 5 phiên (Per-Session Observation Notes & Probe Answers)

### 8.1 Phiên P01 (Trần Hữu Lộc - 21 tuổi - Edge/Windows)

- **Thời gian:** `2026-08-03 10:39` | **Thời gian thực hiện:** `5m00s` | **Số lỗi:** `3` | **Do dự:** `2` | **Trợ giúp:** `2` | **SUS:** `77.5` | **Video ghi hình:** https://youtu.be/Qg45dvZBvzo

**Mốc thời gian quan sát thô:**

- `0m35s` (C2 Edit User): P01 nhập mật khẩu bị sai do thông báo quy tắc mật khẩu hiển thị từng phần thay vì nêu đủ ngay từ đầu. Finding: `C-U001` / `C-F018`. Ảnh: `submission/screenshots/checklist-failures/C-F005.png`
- `1m45s` (C2/C3 Sửa user & Active status): P01 đổi email và trạng thái Active/Inactive, request `PATCH` cập nhật bị timed out. Finding: `C-F014`. Ảnh: `submission/screenshots/checklist-failures/C-F014.png`
- `2m50s` (C3 Block/Reset Password): P01 không tìm thấy nút Block/Unblock hoặc Reset Password trong luồng test. Finding: `C-U002`. Ảnh: `submission/screenshots/checklist-failures/C-F012-01.png`
- `3m40s` (C2 Edit user; Delete dialog): P01 nhập tên/email quá dài; hệ thống không verify độ dài làm tràn UI danh sách và tràn layout confirmation xóa. Finding: `C-F015`. Ảnh: `submission/screenshots/checklist-failures/C-F015-01.png`
- `4m30s` (C2 Edit/Add user): P01 nhập email rất dài đuôi `@g.com` bị báo lỗi `email must be an email`, email ngắn hơn lại được chấp nhận. Finding: `C-F016`. Ảnh: `submission/screenshots/checklist-failures/C-F016.png`

**Câu trả lời phỏng vấn mở P01:**

1. Users list: Danh sách dễ nhìn nhưng khi tên/email quá dài thì dòng bị tràn nhìn xấu và khó theo dõi.
2. Role/Edit: Đổi vai trò dễ nhưng lúc nhập mật khẩu rất dễ bị lỗi do không hiển thị đủ điều kiện.
3. Dialog trust: Không thấy nút Block hay Reset Password rõ ràng nên không tự tin thao tác tài khoản.
4. Recovery: Khi bị timeout thì không biết dữ liệu đã lưu chưa, phải reload lại trang.
5. Improvement: Thêm thông báo cảnh báo rõ ràng khi đổi quyền và hiển thị đầy đủ gợi ý mật khẩu.

---

### 8.2 Phiên P02 (Lê Minh Đức - 21 tuổi - Edge/Windows)

- **Thời gian:** `2026-08-03 11:39` | **Thời gian thực hiện:** `4m30s` | **Số lỗi:** `3` | **Do dự:** `1` | **Trợ giúp:** `1` | **SUS:** `87.5` | **Video ghi hình:** https://youtu.be/MnQzUx25SYI

**Mốc thời gian quan sát thô:**

- `1m10s` (C2 Edit/Add User): P02 nhập email dài bị báo sai định dạng email, sau đó loay hoay với yêu cầu mật khẩu. Finding: `C-F016` / `C-U001`. Ảnh: `submission/screenshots/checklist-failures/C-F016.png`
- `2m40s` (C3 Block/Reset Password): P02 tìm kiếm nút Block và Reset Password nhưng không thấy nút bấm rõ ràng trên bảng. Finding: `C-U002`. Ảnh: `submission/screenshots/checklist-failures/C-F012-01.png`

**Câu trả lời phỏng vấn mở P02:**

1. Users list: Bảng hiển thị thông tin rõ ràng, tìm kiếm nhanh.
2. Role/Edit: Đổi vai trò nhanh nhưng gợi ý mật khẩu cần hiển thị live checklist ngay khi gõ.
3. Dialog trust: Nên có nút Reset Password trực tiếp tại danh sách thay vì bắt người dùng đi tìm.
4. Recovery: Biết bấm Hủy hoặc F5 để tải lại nếu nhập nhầm.
5. Improvement: Bổ sung hiển thị rõ nút Reset Password và Block tài khoản.

---

### 8.3 Phiên P03 (Phùng Ngọc Tuấn - 21 tuổi - Edge/Windows)

- **Thời gian:** `2026-08-03 22:40` | **Thời gian thực hiện:** `3m50s` | **Số lỗi:** `2` | **Do dự:** `2` | **Trợ giúp:** `2` | **SUS:** `90.0` | **Video ghi hình:** https://youtu.be/5hYpKizmWhA

**Mốc thời gian quan sát thô:**

- `1m05s` (C2 Edit/Add User): P03 nhập mật khẩu tưởng đã đủ 8 ký tự + hoa + đặc biệt nhưng vẫn bị từ chối cho đến khi tự thử thêm chữ số. Finding: `C-U001` / `C-F018`. Ảnh: `submission/screenshots/checklist-failures/C-F005.png`
- `2m25s` (C3 Block/Reset Password): P03 ngơ ngác không thấy nút Block hay Reset Password đâu trên giao diện. Finding: `C-U002`. Ảnh: `submission/screenshots/checklist-failures/C-F012-01.png`

**Câu trả lời phỏng vấn mở P03:**

1. Users list: Giao diện trực quan, bộ lọc phân loại tốt.
2. Role/Edit: Form mở lên nhanh nhưng cảnh báo mật khẩu thiếu thông tin quy tắc chữ số khiến người dùng phải đoán.
3. Dialog trust: Thiếu các nút chức năng quản trị quan trọng như Reset Password.
4. Recovery: Không rõ nếu đổi nhầm vai trò thì có khôi phục lại dễ dàng được không.
5. Improvement: Cập nhật thông báo mật khẩu minh bạch và bổ sung nút Reset Password.

---

### 8.4 Phiên P04 (Lê Tuấn Anh - 21 tuổi - Edge/Windows)

- **Thời gian:** `2026-08-03 23:22` | **Thời gian thực hiện:** `3m29s` | **Số lỗi:** `2` | **Do dự:** `3` | **Trợ giúp:** `3` | **SUS:** `70.0` | **Video ghi hình:** https://drive.google.com/file/d/1hon0elJEEtFcuhF9n13mTz2mttJw3a5T/view?usp=sharing _(Lưu trữ trên Google Drive do chính sách bảo mật thông tin cá nhân của YouTube; đã xin phép người tham gia.)_

**Mốc thời gian quan sát thô:**

- `0m50s` (C2 Edit/Add User): P04 nhập mật khẩu bị sai do điều kiện quy tắc mật khẩu không hiển thị rõ trong lúc điền form. Finding: `C-U001`. Ảnh: `submission/screenshots/checklist-failures/C-F005.png`
- `2m10s` (C3 Block/Reset Password): P04 không thấy nút Block tài khoản, phải hỏi người điều phối và được hướng dẫn dùng công tắc Active/Inactive. Finding: `C-U002`. Ảnh: `submission/screenshots/checklist-failures/C-F012-01.png`

**Câu trả lời phỏng vấn mở P04:**

1. Users list: Bảng hiển thị ổn nhưng các nút chức năng quản trị bị giấu.
2. Role/Edit: Cần hiển thị rõ hậu quả khi thay đổi vai trò của người dùng.
3. Dialog trust: Công tắc Active/Inactive biểu diễn mơ hồ, không giống chữ "Block" thông thường.
4. Recovery: Cần sự trợ giúp từ người điều phối để hiểu quy trình.
5. Improvement: Đặt tên nút bấm đúng với thuật ngữ Block / Unblock và Reset Password.

---

### 8.5 Phiên P05 (Vũ Thế Anh - 21 tuổi - Edge/Windows)

- **Thời gian:** `2026-08-04 10:08` | **Thời gian thực hiện:** `4m00s` | **Số lỗi:** `2` | **Do dự:** `1` | **Trợ giúp:** `1` | **SUS:** `90.0` | **Video ghi hình:** https://youtu.be/ysRW-LvCq_M

**Mốc thời gian quan sát thô:**

- `1m15s` (C2 Edit/Add User): P05 nhập mật khẩu bị lỗi do gợi ý quy tắc hiển thị không đầy đủ điều kiện bắt buộc. Finding: `C-U001` / `C-F018`. Ảnh: `submission/screenshots/checklist-failures/C-F005.png`
- `2m50s` (C3 Block/Reset Password): P05 phản ánh không thấy action Reset Password hay Block trên dòng người dùng. Finding: `C-U002`. Ảnh: `submission/screenshots/checklist-failures/C-F012-01.png`

**Câu trả lời phỏng vấn mở P05:**

1. Users list: Tìm kiếm người dùng hoạt động tốt và phản hồi nhanh.
2. Role/Edit: Thao tác gán vai trò đơn giản, nhưng form mật khẩu nên có hướng dẫn trực tiếp.
3. Dialog trust: Cần thêm thông báo xác nhận an toàn trước khi thay đổi trạng thái tài khoản.
4. Recovery: Biết bấm nút Hủy trên dialog để thoát thao tác sai.
5. Improvement: Hiển thị đầy đủ nút chức năng và live checklist quy định mật khẩu.

---

## 9. Kết quả tính khả dụng đã xếp hạng (Ranked Usability Findings)

Dùng mã `C-U001`, `C-U002`, ... cho các vấn đề usability từ kiểm thử người dùng. Các bug phát hiện trong phiên test người dùng giữ nguyên mã log tổng hợp, ví dụ `C-F014`.

### C-F014 - Request PATCH cập nhật user bị timed out khi đổi email và Active/Inactive

- Loại: Bug phát hiện trong kiểm thử người dùng Task 2
- Màn hình: C2/C3 Chỉnh sửa người dùng và trạng thái Active/Inactive
- Minh chứng: Trong phiên test với P01, người tham gia đổi email và trạng thái Active/Inactive, request `PATCH` cập nhật bị timed out. Người dùng ID: P01
- Mức độ nghiêm trọng: 3
- Tác động: Người tham gia/admin không biết thao tác cập nhật đã lưu hay thất bại.
- Đề xuất sửa: Xử lý timeout request với thông báo lỗi rõ ràng, đường dẫn thử lại và trạng thái nút Lưu bị vô hiệu hóa/tải dữ liệu trong lúc gửi request.
- Ảnh minh chứng: `submission/screenshots/checklist-failures/C-F014.png`
- Timestamp Google Form: Phản ánh lúc 11:07 ngày 03/08/2026

### C-F015 - Tên hoặc email quá dài được hệ thống chấp nhận và làm tràn UI

- Loại: Bug phát hiện trong kiểm thử người dùng Task 2
- Màn hình: C2 Gán vai trò / chỉnh sửa người dùng; delete confirmation dialog
- Minh chứng: Trong phiên test P01, người tham gia nhập tên hoặc email quá dài. Hệ thống chấp nhận giá trị mà không kiểm tra độ dài, sau đó văn bản dài tràn UI danh sách người dùng và làm tràn layout xác nhận xóa khi chọn user đó. Người dùng ID: P01
- Mức độ nghiêm trọng: 3
- Tác động: Admin có thể lưu dữ liệu không đọc được; Quản lý người dùng và dialog xác nhận xóa bị khó đọc, tăng rủi ro xác nhận nhầm người dùng mục tiêu.
- Đề xuất sửa: Bổ sung kiểm tra độ dài tối đa cho tên/email ở client và server, hiển thị văn bản dài với cơ chế xuống dòng/rút gọn (truncate) trong bảng, form và dialog xác nhận.
- Ảnh minh chứng: `submission/screenshots/checklist-failures/C-F015-01.png`
- Timestamp Google Form: Phản ánh lúc 19:08 ngày 04/08/2026

### C-F016 - Email dài dạng `@g.com` bị báo lỗi không hợp lệ không nhất quán

- Loại: Bug phát hiện trong kiểm thử người dùng Task 2
- Màn hình: C2 Gán vai trò / chỉnh sửa người dùng
- Minh chứng: Trong phiên test P01/P02, người tham gia gặp lỗi validation với email quá dài. Trong một trường hợp, email rất dài có đuôi `@g.com` báo lỗi `email must be an email`, trong khi email ngắn hơn cùng đuôi `@g.com` lại được chấp nhận. Người dùng ID: P01, P02
- Mức độ nghiêm trọng: 2
- Tác động: Người tham gia/admin không biết nguyên nhân thật là định dạng hay độ dài, làm chậm việc sửa lỗi và khiến quy tắc validation cảm giác không đáng tin.
- Đề xuất sửa: Tách kiểm tra định dạng email và kiểm tra độ dài tối đa; hiển thị thông báo chính xác nguyên nhân khi giá trị quá dài.
- Ảnh minh chứng: `submission/screenshots/checklist-failures/C-F016.png`
- Timestamp Google Form: Phản ánh lúc 19:10 ngày 04/08/2026

### C-U001 / C-F018 - Gợi ý quy tắc Mật khẩu không đầy đủ và ẩn yêu cầu chữ số

- Màn hình: C2 Gán vai trò / chỉnh sửa người dùng
- Minh chứng: Trong phỏng vấn người dùng, người tham gia nhận xét gợi ý cảnh báo mật khẩu chỉ nêu cần 8 ký tự, chữ hoa và ký tự đặc biệt. Nhập đúng theo gợi ý (VD: `Password!`) vẫn bị báo lỗi cho đến khi người dùng tự phát hiện phải có thêm 1 chữ số (VD: `Password1!`).
- Mức độ nghiêm trọng: 2
- Tác động: Admin tốn thời gian sửa mật khẩu dù đã làm đúng theo hướng dẫn hiển thị trên màn hình, gây bối rối và gia tăng ma sát khi tạo người dùng.
- Đề xuất sửa: Hiển thị đầy đủ mọi tiêu chí mật khẩu bắt buộc (độ dài >= 8, chữ hoa, ký tự đặc biệt và chữ số) ngay từ đầu với danh sách kiểm tra hợp lệ thời gian thực.
- Ảnh minh chứng: `submission/screenshots/checklist-failures/C-F005.png`
- Timestamp Google Form: Đã phản ánh lúc 19:15 ngày 04/08/2026

### C-U002 / C-F012 - Chức năng Block và Reset Password khó tìm thấy trong luồng kiểm thử

- Màn hình: C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu
- Minh chứng: Cả 5 người tham gia đều báo cáo họ không thấy hoặc không tìm thấy hành động Block/Reset Password trong hệ thống khi làm nhiệm vụ.
- Mức độ nghiêm trọng: 3
- Tác động: Admin không thể tự tin hoàn thành nhiệm vụ kiểm soát tài khoản nếu các thao tác quan trọng bị ẩn, không khả dụng hoặc không có nhãn phân biệt rõ.
- Đề xuất sửa: Hiển thị hành động Block/Unblock và Reset Password ở vị trí dễ đoán trên bảng danh sách hoặc dòng chi tiết người dùng, giữ nhãn nhất quán với ngôn ngữ nhiệm vụ.
- Ảnh minh chứng: `submission/screenshots/checklist-failures/C-F012-01.png`
- Timestamp Google Form: Phản ánh lúc 23:00 ngày 02/08/2026

### C-U003 - Đường phục hồi sau khi thao tác sai chưa đủ rõ ràng

- Màn hình: C1 Danh sách người dùng; C2 Edit user; C3 dialogs
- Minh chứng: 2 người tham gia nói họ biết cách quay lại hoặc phục hồi sau khi thao tác sai, trong khi 3 người tham gia nói họ không biết rõ cách phục hồi.
- Mức độ nghiêm trọng: 2
- Tác động: Admin có thể do dự trước khi xác nhận thay đổi hoặc phụ thuộc vào sự hỗ trợ của người điều phối khi không chắc thao tác có thể hoàn tác hay không.
- Đề xuất sửa: Bổ sung nút Hủy/Quay lại rõ ràng hơn, thông báo sau thao tác và hướng dẫn phục hồi sau các hành động vai trò/trạng thái/mật khẩu.
- Ảnh minh chứng: `submission/screenshots/checklist-failures/C-F002.png`
- Timestamp Google Form: Phản ánh lúc 22:45 ngày 02/08/2026

### C-U004 / C-F013 - Thay đổi vai trò và Active/Inactive thiếu cảnh báo trước khi xác nhận

- Màn hình: C2 Edit user / Assign Role; C3 status action
- Minh chứng: Người tham gia yêu cầu thông báo cảnh báo rõ ràng hơn khi thay đổi vai trò hoặc trạng thái Active/Inactive.
- Mức độ nghiêm trọng: 2
- Tác động: Admin có thể không hiểu hết ảnh hưởng của việc đổi quyền/trạng thái trước khi lưu, làm tăng rủi ro thay đổi tài khoản ngoài ý muốn.
- Đề xuất sửa: Hiển thị hộp thoại xác nhận ngắn gọn hoặc cảnh báo trực tiếp giải thích hậu quả của việc đổi vai trò và trạng thái Active/Inactive trước khi áp dụng cập nhật.
- Ảnh minh chứng: `submission/screenshots/checklist-failures/C-F013.png`
- Timestamp Google Form: Phản ánh lúc 23:01 ngày 02/08/2026

---

## 10. Thang mức độ nghiêm trọng (Severity Scale)

| Mức độ | Ý nghĩa                                                |
| -----: | ------------------------------------------------------ |
|      0 | Không phải vấn đề tính khả dụng                        |
|      1 | Lỗi thẩm mỹ hoặc gây khó chịu nhẹ                      |
|      2 | Vấn đề nhỏ, có cách khắc phục tạm thời (workaround)    |
|      3 | Gây chậm trễ đáng kể, bối rối hoặc thao tác nhầm       |
|      4 | Chặn hoàn tất nhiệm vụ hoặc rủi ro mất dữ liệu/bảo mật |

---

## 11. Đề xuất cải tiến ưu tiên (Prioritised Recommendations)

| Ưu tiên | Đề xuất cải tiến cụ thể                                                   | Cơ sở bằng chứng                                                                     | Màn hình mục tiêu                    |
| ------: | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------ |
|       1 | Hiển thị rõ hành động Block/Unblock và Reset Password với nhãn nhất quán. | Cả 5 người tham gia đều không tìm thấy các hành động này trong luồng test.           | C3 dialogs / C1 Danh sách người dùng |
|       2 | Bổ sung gợi ý quy tắc mật khẩu thời gian thực khi điền form.              | Người tham gia bối rối khi quy tắc 8 ký tự theo sau là yêu cầu chữ hoa/chữ số bị ẩn. | C2 Edit/Add user                     |
|       3 | Bổ sung kiểm tra độ dài và bảo vệ layout cho giá trị tên/email dài.       | P01 kích hoạt lỗi tràn chữ tên/email dài, bao gồm cả trong layout xác nhận xóa.      | C2 Edit/Add user; delete dialog      |
|       4 | Hiển thị cảnh báo rõ hơn cho thay đổi vai trò và Active/Inactive.         | Người tham gia yêu cầu phản hồi rõ ràng hơn trước khi thay đổi vai trò/trạng thái.   | C2 Edit user                         |
|       5 | Cải thiện hướng dẫn phục hồi sau thao tác sai.                            | 3 trên 5 người tham gia cho biết họ không biết rõ cách phục hồi lỗi.                 | C1/C2/C3                             |

---

## 12. Ghi hình màn hình & Video minh chứng (Screen Recordings & Demo Videos)

- **Danh mục video demo:** `submission/demo-videos.md`
- **Thư mục minh chứng gốc:** `evidence/task2_scenario_c/`

| Mã phiên     | Người tham gia       | Đường dẫn Video YouTube                                                               |
| ------------ | -------------------- | ------------------------------------------------------------------------------------- |
| **Pilot**    | Thới Đặng Trường Thọ | https://youtu.be/lpxRwuFYGBM                                                          |
| **P01 (U1)** | Trần Hữu Lộc         | https://youtu.be/Qg45dvZBvzo                                                          |
| **P02 (U2)** | Lê Minh Đức          | https://youtu.be/MnQzUx25SYI                                                          |
| **P03 (U3)** | Phùng Ngọc Tuấn      | https://youtu.be/5hYpKizmWhA                                                          |
| **P04 (U4)** | Lê Tuấn Anh          | https://drive.google.com/file/d/1hon0elJEEtFcuhF9n13mTz2mttJw3a5T/view?usp=sharing \* |
| **P05 (U5)** | Vũ Thế Anh           | https://youtu.be/ysRW-LvCq_M                                                          |

---

## 13. Truy vết nộp Bug và Usability Findings (Submission Trace)

Mỗi finding từ Task 2 phải được nộp 2 lần:

1. Google Form: `https://forms.gle/CJQFQCAXcsDbXDMM9`
2. Log tổng hợp: `submission/bug_usability_findings_log.md`

| Mã Finding ID   | Đã nộp Google Form? | Timestamp Google Form                 | Có trong log tổng hợp? |
| --------------- | ------------------- | ------------------------------------- | ---------------------- |
| C-F014          | Có                  | Phản ánh lúc 11:07 ngày 03/08/2026    | Có                     |
| C-F015          | Có                  | Phản ánh lúc 19:08 ngày 04/08/2026    | Có                     |
| C-F016          | Có                  | Phản ánh lúc 19:10 ngày 04/08/2026    | Có                     |
| C-U001 / C-F018 | Có                  | Đã phản ánh lúc 19:15 ngày 04/08/2026 | Có                     |
| C-U002 / C-F012 | Có                  | Phản ánh lúc 23:00 ngày 02/08/2026    | Có                     |
| C-U003 / C-F002 | Có                  | Phản ánh lúc 22:45 ngày 02/08/2026    | Có                     |
| C-U004 / C-F013 | Có                  | Phản ánh lúc 23:01 ngày 02/08/2026    | Có                     |
