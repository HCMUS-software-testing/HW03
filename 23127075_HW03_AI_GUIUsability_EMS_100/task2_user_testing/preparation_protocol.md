# Task 2 - Preparation Protocol Cho Scenario D

## 1. Mục Tiêu Nghiên Cứu

Đánh giá mức độ dễ hiểu và dễ hoàn tất của luồng hỗ trợ trong EMS, từ lúc người dùng tạo support request, kiểm tra request/response của mình, đến lúc admin hoặc observer tìm đúng request trong danh sách quản trị.

## 2. Phạm Vi Màn Hình

| Mã | Màn hình | Vai trò | Lý do đưa vào Task 2 |
| --- | --- | --- | --- |
| D1 | User tạo support request có image attachment | User | Đây là điểm nhập liệu chính của luồng, có required fields, category, upload ảnh và submit/cancel. |
| D2 | User xem My Requests list/detail có response | User | Đây là nơi người dùng xác nhận request đã được ghi nhận, theo dõi status và đọc phản hồi. |
| D3 | Admin Support Requests list với Pending/Resolved/search/filter | Admin hoặc observer vai trò hỗ trợ | Đây là nơi người xử lý tìm request theo title/member code/category và phân biệt pending/resolved. |

Nếu participant không có quyền admin, phần D3 chạy theo dạng observer task: người kiểm thử đăng nhập admin hoặc chuẩn bị sẵn session, participant tìm request trên màn hình admin dưới giám sát và không chỉnh sửa dữ liệu ngoài phạm vi.

## 3. Chuẩn Bị Account/Session Access

| Phần task | Account/session dùng | Cách cấp cho participant | Ghi chú an toàn |
| --- | --- | --- | --- |
| D1 - tạo support request | User test account của Kiên | Cho participant dùng trình duyệt đã đăng nhập sẵn hoặc cung cấp credential trực tiếp trong phiên | Không dùng account cá nhân thật của participant. |
| D2 - xem My Requests/detail | Cùng user account đã tạo request ở D1 | Giữ nguyên session sau D1 để participant tự tìm lại request | Nếu EMS reset dữ liệu, tạo request mới trong phiên. |
| D3 - admin list/search/filter | Admin session do người kiểm thử đăng nhập sẵn | Participant thao tác dưới giám sát hoặc hướng dẫn người kiểm thử nhập query theo lời participant | Không để participant resolve/delete/sửa request không thuộc phạm vi. |

## 4. Scenario Đọc Cho Participant

```text
Bạn đang dùng hệ thống EMS của khoa. Bạn gặp một vấn đề khi tham gia hoặc đăng ký sự kiện và muốn gửi yêu cầu hỗ trợ kèm ảnh minh chứng. Sau khi gửi, hãy kiểm tra lại yêu cầu của mình trong danh sách support requests và cho biết bạn thấy trạng thái/phản hồi ở đâu.
```

Biến thể có phần admin:

```text
Bạn đang hỗ trợ xử lý yêu cầu của người dùng. Hãy tìm request vừa được tạo bằng tiêu đề, member code hoặc category trong màn hình quản lý support requests, rồi cho biết request đang ở trạng thái nào.
```

Không đọc từng bước click cho participant. Chỉ giải thích mục tiêu và để họ tự tìm đường đi.

## 5. Người Tham Gia

| Tiêu chí | Yêu cầu | Kết quả thực tế |
| --- | --- | --- |
| Số lượng chính | 5 người thật | Đã có P01-P05 trong `participant_table.md`. |
| Pilot | 1 người thêm, không tính vào 5 người chính | Không có file pilot riêng trong `session_notes`; đây là khoảng trống bằng chứng cần ghi trong report. |
| Đối tượng | Người ngoài lớp, có trải nghiệm dùng web quản lý/sự kiện/hỗ trợ | Đã ghi danh sách participant và thiết bị/browser. |
| Consent | Xác nhận đồng ý tham gia | Cả 5 phiên chính ghi `Yes`. |
| Recording | Ghi màn hình/âm thanh nếu có đồng ý | Cả 5 phiên ghi `N/A`. |

## 6. Metrics Cần Đo

| Metric | Cách ghi |
| --- | --- |
| Task success | `Completed`, `Partial`, hoặc `Failed` |
| Time on task | Bắt đầu khi đọc xong scenario, kết thúc khi participant xác nhận đã hoàn tất |
| Errors | Số hành động sai, nhầm luồng, submit lỗi, mất dữ liệu, chọn sai filter |
| Hesitations | Số lần dừng lâu, hỏi lại, quay lại hoặc biểu hiện không chắc chắn |
| SUS score | 0-100, tính từ 10 câu SUS |
| Key friction | Tóm tắt điểm vướng lớn nhất của từng participant |

## 7. Quy Trình Mỗi Session Chính

| Bước | Người kiểm thử làm | Dữ liệu cần ghi |
| ---: | --- | --- |
| 1 | Ghi participant ID, họ tên, số điện thoại, thiết bị/browser. | `participant_table.md` |
| 2 | Đọc consent script và xin đồng ý. | Consent `Yes/No`; recording consent nếu có. |
| 3 | Đọc task scenario. | Không đưa click-by-click instruction. |
| 4 | Bắt đầu timer. | Start time. |
| 5 | Quan sát trung lập, yêu cầu think aloud. | Errors, hesitations, quote, friction. |
| 6 | Chỉ can thiệp nếu participant bị kẹt hoàn toàn. | Ghi intervention nếu có. |
| 7 | Kết thúc timer khi participant hoàn tất hoặc bỏ cuộc. | End time, duration, success. |
| 8 | Cho participant trả lời SUS. | Raw SUS 1-5 từng câu. |
| 9 | Hỏi probe questions. | Câu trả lời ngắn hoặc quote. |
| 10 | Lưu screenshot/recording nếu có. | Evidence path. |

## 8. Probe Questions

| Chủ đề | Câu hỏi |
| --- | --- |
| Clarity | Phần nào của màn hình giúp bạn hiểu đang cần làm gì? Phần nào gây khó hiểu? |
| Error recovery | Nếu nhập sai hoặc muốn quay lại, bạn có thấy cách sửa/khôi phục rõ không? |
| Speed | Bạn thấy bước nào làm chậm nhất? |
| Trust | Sau khi gửi request hoặc xem response, bạn có tin là hệ thống đã ghi nhận/xử lý chưa? Vì sao? |
| Navigation | Bạn có dễ tìm lại request vừa tạo không? |
| Admin search/filter | Nếu phải tìm request để xử lý, bạn sẽ dùng title, member code, category hay status? |
| D3 status | Ở D3, bạn có tìm được đúng request trong Pending/Resolved tab không? |
| Layout | Bạn có nhận thấy vấn đề nào về layout mobile/desktop không? |

## 9. Liên Hệ Với Findings Task 1B

Các vấn đề từ Task 1B chỉ dùng để định hướng quan sát, không nói trước cho participant:

| Finding Task 1B | Quan sát trong Task 2 |
| --- | --- |
| F-D1-001, F-D1-002 | Participant có hiểu required fields/category và recovery khi submit lỗi không. |
| F-D1-003 | Participant có lo ngại hoặc bị mất dữ liệu khi bấm `Cancel`/`Back` không. |
| F-D2-001, F-D2-002 | Participant có hiểu filter/no-result và giữ ngữ cảnh khi quay lại detail không. |
| F-D3-001, F-D3-002 | Participant hoặc admin observer có tìm đúng request bằng search/filter không. |
| F-D2-003, F-D3-003 | Nếu chạy mobile, participant có bị control che hoặc layout làm chậm không. |
