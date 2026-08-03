# Task 2 - User Session Form Template

## 0. Hướng dẫn cho participant

Bạn sẽ trải nghiệm flow support request trên EMS rồi tự điền file này sau khi làm xong. Mục tiêu là kiểm thử giao diện sản phẩm, không phải kiểm tra năng lực của bạn.

Trong lúc thao tác:

- Hãy đọc scenario, tự tìm cách hoàn tất mục tiêu và nói ra suy nghĩ nếu có người điều phối quan sát.
- Người điều phối sẽ không chỉ từng bước click; chỉ can thiệp khi bạn bị kẹt hoàn toàn.
- Nếu đồng ý ghi màn hình/ghi âm, hãy xác nhận ở mục `Consent` và `Recording`.
- Timer bắt đầu sau khi bạn đọc xong scenario và kết thúc khi bạn xác nhận đã hoàn tất hoặc dừng task.
- Không cần tính `SUS score 0-100`; người kiểm thử sẽ tính sau từ 10 câu SUS bạn chấm.

## 1. Thông tin truy cập EMS

| Hạng mục    | Giá trị                                                         |
| ------------- | ----------------------------------------------------------------- |
| Website EMS   | `https://prod-dev.ems-fitus.cloud`                              |
| Scenario test | D - User requests Support and Admin resolves it                   |
| Màn hình D1 | User tạo support request có image attachment                    |
| Màn hình D2 | User xem My Requests list/detail có response                     |
| Màn hình D3 | Admin xem Support Requests list, Pending/Resolved tabs và search |

### User account cho D1-D2

| Field            | Value                                                          |
| ---------------- | -------------------------------------------------------------- |
| Email / Username | `ltkien23@clc.fitus.edu.vn`                                  |
| Password         | `Nothing2k@5`                                                |
| Role             | `User`                                                       |
| Dùng cho        | Tạo support request ở D1 và xem lại request/response ở D2 |

### Admin account cho D3

| Field            | Value                                  |
| ---------------- | -------------------------------------- |
| Email / Username | `admin@gmail.com`                    |
| Password         | `Admin@123`                          |
| Role             | `Admin`                              |
| Dùng cho        | Tìm request trong màn hình admin D3 |

Lưu ý cho participant:

- Chỉ dùng account trên cho buổi test này.
- Không đổi mật khẩu, email, profile hoặc thông tin tài khoản.
- Không xóa, resolve, sửa dữ liệu không được yêu cầu.
- Nếu thấy dữ liệu của người khác ở màn hình admin, chỉ quan sát/tìm kiếm theo yêu cầu, không chỉnh sửa.

## 2. Thông tin phiên

| Trường             | Giá trị                                       |
| -------------------- | ----------------------------------------------- |
| Participant ID       | `P02`                                         |
| Họ tên               | `[Điền]`                                    |
| Số điện thoại        | `[Điền]`                                    |
| Thiết bị/browser   | `[Điền]`                                    |
| Ngày giờ           | `[Điền]`                                    |
| Người điều phối | Lê Trung Kiên                                 |
| Scenario             | D - User requests Support and Admin resolves it |
| Consent              | `[Yes/No]`                                    |
| Recording            | `[File path hoặc N/A]`                       |

## 3. Task scenario

```text
Bạn đang dùng hệ thống EMS của khoa. Bạn gặp một vấn đề khi tham gia hoặc đăng ký sự kiện và muốn gửi yêu cầu hỗ trợ kèm ảnh minh chứng. Sau khi gửi, hãy kiểm tra lại yêu cầu của mình trong danh sách support requests và cho biết bạn thấy trạng thái/phản hồi ở đâu.
```

Phần D3:

```text
Sau khi trải nghiệm phía user, hãy đăng nhập admin hoặc dùng session admin đã được chuẩn bị. Trong màn hình quản lý support requests, hãy tìm request theo tiêu đề, member code, category hoặc trạng thái và cho biết bạn tìm thấy request ở tab nào.
```

## 4. Participant tự ghi quá trình thực hiện

| Màn hình                              | Bạn đã làm gì? | Có hoàn tất không? | Phần nào khó hiểu/chậm? |
| --------------------------------------- | ------------------- | ---------------------- | ---------------------------- |
| D1 - Create support request             | `[Điền]`        | `[Yes/Partial/No]`   | `[Điền]`                 |
| D2 - My Requests/detail                 | `[Điền]`        | `[Yes/Partial/No]`   | `[Điền]`                 |
| D3 - Admin Support Requests list/search | `[Điền]`        | `[Yes/Partial/No]`   | `[Điền]`                 |

## 5. Timeline/quan sát

Participant có thể tự điền theo trí nhớ sau khi làm xong. Nếu người điều phối quan sát trực tiếp, có thể bổ sung thêm timestamp, error và hesitation.

| Thời điểm | Màn hình | Hành động/quan sát | Có lỗi/nhầm lẫn? | Có do dự?  | Quote/ghi chú |
| ------------ | ---------- | ---------------------- | -------------------- | ------------ | -------------- |
| 00:00        | Start      | Bắt đầu task.       | No                   | No           |                |
| `[Điền]` | D1         | `[Điền]`           | `[Yes/No]`         | `[Yes/No]` |                |
| `[Điền]` | D2         | `[Điền]`           | `[Yes/No]`         | `[Yes/No]` |                |
| `[Điền]` | D3         | `[Điền]`           | `[Yes/No]`         | `[Yes/No]` |                |

## 6. Kết quả task

| Metric        | Giá trị                                |
| ------------- | ---------------------------------------- |
| Success       | `[Completed/Partial/Failed]`           |
| Time on task  | `[mm:ss]`                              |
| Errors        | `[Số]`                                |
| Hesitations   | `[Số]`                                |
| Interventions | `[Không/Có, mô tả]`                |
| Key friction  | `[Điền]`                             |
| Evidence      | `[Screenshot/recording path nếu có]` |

## 7. Câu hỏi sau khi trải nghiệm

| Câu hỏi                                                                                                   | Trả lời    |
| ----------------------------------------------------------------------------------------------------------- | ------------ |
| Phần nào giúp bạn hiểu đang cần làm gì? Phần nào gây khó hiểu?                                | `[Điền]` |
| Nếu nhập sai hoặc muốn quay lại, bạn có thấy cách sửa/khôi phục rõ không?                     | `[Điền]` |
| Bước nào làm bạn chậm nhất?                                                                          | `[Điền]` |
| Sau khi gửi request hoặc xem response, bạn có tin là hệ thống đã ghi nhận/xử lý chưa? Vì sao? | `[Điền]` |
| Bạn có dễ tìm lại request vừa tạo không?                                                            | `[Điền]` |
| Nếu phải tìm request để xử lý, bạn sẽ dùng title, member code, category hay status?               | `[Điền]` |
| Ở D3, bạn có tìm được đúng request trong Pending/Resolved tab không?                              | `[Điền]` |
| Bạn có nhận thấy vấn đề nào về layout mobile/desktop không?                                       | `[Điền]` |

## 8. Bảng SUS - đánh giá mức độ dễ dùng

SUS là `System Usability Scale`, một bảng 10 câu dùng để đánh giá nhanh mức độ dễ dùng của hệ thống sau khi bạn đã trải nghiệm flow. Vui lòng chấm mỗi câu từ `1` đến `5` theo cảm nhận thật của bạn:

| Điểm | Ý nghĩa |
| ---: | --- |
| 1 | Rất không đồng ý |
| 2 | Không đồng ý |
| 3 | Trung lập |
| 4 | Đồng ý |
| 5 | Rất đồng ý |

| Mã | Câu hỏi | Điểm 1-5 |
| --- | --- | ---: |
| SUS-01 | Tôi nghĩ tôi muốn sử dụng hệ thống này thường xuyên nếu có nhu cầu gửi hoặc theo dõi yêu cầu hỗ trợ. |  |
| SUS-02 | Tôi thấy hệ thống này phức tạp không cần thiết. |  |
| SUS-03 | Tôi thấy hệ thống này dễ sử dụng. |  |
| SUS-04 | Tôi nghĩ tôi cần người có kỹ thuật hỗ trợ thì mới dùng được hệ thống này. |  |
| SUS-05 | Tôi thấy các chức năng trong flow support request được liên kết với nhau hợp lý. |  |
| SUS-06 | Tôi thấy hệ thống có quá nhiều điểm không nhất quán. |  |
| SUS-07 | Tôi nghĩ hầu hết mọi người có thể học cách dùng flow này rất nhanh. |  |
| SUS-08 | Tôi thấy hệ thống này rườm rà hoặc bất tiện khi sử dụng. |  |
| SUS-09 | Tôi cảm thấy tự tin khi sử dụng flow support request này. |  |
| SUS-10 | Tôi cần học thêm nhiều thứ trước khi có thể sử dụng flow này thành thạo. |  |
| SUS score 0-100 | Người kiểm thử tính sau, participant không cần điền. |  |

## 9. Candidate findings từ phiên này

| ID tạm    | Screen         | Type                | Description  | Evidence         | Severity 0-4 | Có submit Google Form? |
| ---------- | -------------- | ------------------- | ------------ | ---------------- | -----------: | ----------------------- |
| UT-Pxx-001 | `[D1/D2/D3]` | `[Bug/Usability]` | `[Điền]` | `[Path/quote]` |              | `[Yes/No]`            |
