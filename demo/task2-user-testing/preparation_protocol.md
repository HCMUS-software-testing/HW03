# Preparation Protocol - Moderated User Testing cho D1

## 1. Thông tin chung

| Trường | Giá trị |
| --- | --- |
| SUT | `https://prod-dev.ems-fitus.cloud` |
| Scenario | `D1 - Tạo support request` |
| Mục tiêu phiên test | Đánh giá người dùng có tìm được luồng tạo request, hiểu form, điền đúng thông tin, upload minh chứng và hoàn tất submit hay không. |
| Loại nghiên cứu | Moderated usability testing |
| Kỹ thuật | Think-aloud + post-task SUS |
| Số participant mặc định | `5` |
| Người điều phối | `[Điền tên]` |
| Ngày chạy | `[Điền]` |

## 2. Research objectives

- Xác định người dùng có tìm đúng nơi để tạo support request không.
- Đánh giá mức độ rõ ràng của các trường bắt buộc như `Request type`, `Issue requiring support`, `Detailed description`.
- Quan sát mức độ dễ hiểu của upload ảnh minh chứng.
- Đo mức độ tin cậy sau khi người dùng bấm `Submit request`.
- Thu thập pain points về validation, wording, điều hướng và trạng thái hoàn tất.

## 3. Task scenario đọc cho participant

Đọc nguyên văn, không hướng dẫn click-by-click:

```text
Bạn đang dùng hệ thống EMS của khoa và gặp một vấn đề cần được hỗ trợ. Hãy tạo một support request trên hệ thống, điền nội dung theo cách bạn thấy hợp lý, và nếu phù hợp thì đính kèm ảnh minh chứng. Khi bạn nghĩ mình đã hoàn tất, hãy nói cho người điều phối biết.
```

## 4. Success criteria

Một session được xem là `Completed` khi participant:

- Tìm được màn hình tạo support request.
- Chọn được loại request phù hợp.
- Nhập được nội dung vấn đề cần hỗ trợ.
- Nhập được mô tả chi tiết.
- Submit request thành công hoặc đi đến trạng thái mà participant tin là đã gửi thành công.

`Partial` nếu participant hoàn tất một phần nhưng cần can thiệp lớn.

`Failed` nếu participant không thể gửi request hoặc bỏ cuộc.

## 5. Chuẩn bị trước buổi test

| Hạng mục | Việc cần làm | Trạng thái |
| --- | --- | --- |
| Thiết bị | Chuẩn bị laptop hoặc điện thoại của participant. | `[ ]` |
| Trình duyệt | Kiểm tra browser và kết nối mạng ổn định. | `[ ]` |
| Tài khoản test | Đăng nhập sẵn hoặc chuẩn bị credential user test. | `[ ]` |
| Dữ liệu minh chứng | Chuẩn bị sẵn 1-2 ảnh demo nếu participant cần file upload. | `[ ]` |
| Ghi hình/ghi âm | Xin consent trước nếu có recording. | `[ ]` |
| Đồng hồ bấm giờ | Sẵn sàng đo `time on task`. | `[ ]` |
| Form ghi chú | Tạo file note cho participant từ template. | `[ ]` |

## 6. Observer rules

- Không nói participant nên bấm ở đâu.
- Không giải thích ý nghĩa field trước khi participant tự thử.
- Chỉ nhắc participant nghĩ thành tiếng nếu họ im lặng quá lâu.
- Chỉ can thiệp khi participant bị kẹt hoàn toàn hoặc chuẩn bị thao tác ngoài phạm vi an toàn.
- Không đánh giá participant; chỉ ghi nhận hành vi và phát biểu.

## 7. Metrics cần đo

| Metric | Cách ghi |
| --- | --- |
| Task completion | `Completed`, `Partial`, `Failed` |
| Time on task | Từ lúc đọc xong scenario đến khi participant tuyên bố xong |
| Error count | Số lần thao tác sai, submit lỗi, chọn sai control, quay lui do nhầm |
| Hesitation count | Số lần dừng lâu, rê chuột tìm kiếm, hỏi lại mục tiêu |
| Assistance count | Số lần người điều phối phải can thiệp |
| SUS | Điểm 10 câu sau task |

## 8. Probe questions sau task

| Chủ đề | Câu hỏi |
| --- | --- |
| Discoverability | Bạn đã bắt đầu tìm chỗ tạo request từ đâu? |
| Form clarity | Trường nào dễ hiểu nhất? Trường nào khó hiểu nhất? |
| Validation | Nếu nhập thiếu hoặc nhập sai, bạn có hiểu hệ thống đang yêu cầu gì không? |
| Confidence | Sau khi bấm submit, bạn có tin là request đã được gửi thành công không? Vì sao? |
| Attachment | Việc đính kèm ảnh có dễ nhận ra và dễ dùng không? |
| Overall | Nếu sau này cần hỗ trợ thật, bạn có sẵn sàng dùng lại flow này không? |

## 9. Privacy và data constraints

- Không dùng dữ liệu cá nhân thật trong nội dung request nếu không cần.
- Nếu participant dùng ảnh cá nhân, hỏi lại trước khi lưu làm evidence.
- Nếu có recording, chỉ lưu đường dẫn trong report; không nhúng dữ liệu nhạy cảm vào file nộp.
- Nếu hệ thống tạo dữ liệu thật, dùng tiêu đề có tiền tố như `UT Demo` để dễ nhận diện.

## 10. Deliverables sau khi chạy test

- `participant_table.md` đã điền đủ metadata participant.
- `session_notes/<participant_id>_session_notes.md` cho từng người.
- `sus_score_sheet.md` có điểm từng participant và điểm trung bình.
- `usability_report_template.md` được dùng để tổng hợp findings và recommendation.
