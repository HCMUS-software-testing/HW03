---
name: ems-gui-checklist-runner
description: Chạy checklist GUI usability dùng chung của HW03 EMS trên một màn hình EMS được chọn và sinh các dòng execution cho Task 1B. Dùng khi Codex được yêu cầu đánh giá một màn hình EMS, điền kết quả checklist, nối item fail với finding log, hoặc kiểm tra Scenario A/B/C/D đã có đủ minh chứng Pass/Fail hay chưa.
---

# EMS GUI Checklist Runner

## Đầu vào

Cần có:

- Mã và tên màn hình, ví dụ `C1 Danh sách người dùng`.
- Nguồn minh chứng: ghi chú quan sát thật, ảnh chụp màn hình hoặc walkthrough thủ công đã hoàn thành.
- Nguồn checklist: `submission/group/gui_usability_checklist_final.md`.

Không đánh dấu kết quả thật bằng suy đoán. Với bản nộp cuối, mỗi item phải là `Pass` hoặc `Fail`. Nếu chưa có đủ minh chứng để kết luận, để trạng thái tạm là `Chờ kiểm thử` trong draft và không xem là kết quả final.

## Quy trình

1. Đọc checklist dùng chung và giữ nguyên mọi ID item.
2. Với màn hình được chọn, đánh giá từng item trong bản final là `Pass` hoặc `Fail`.
3. Không dùng trạng thái ngoài `Pass`/`Fail` trong bảng final. Nếu checklist item không phát sinh control/luồng tương ứng trên màn hình đang test, ghi `Pass` với note giải thích rằng không phát hiện lỗi trong phạm vi màn hình đó và item sẽ được kiểm sâu ở màn hình liên quan nếu có.
4. Với mỗi `Fail`, bắt buộc có:
   - Lý do cụ thể trong ghi chú.
   - Mã finding như `C-F001`.
5. Thêm finding tương ứng vào `submission/bug_usability_findings_log.md`; đường dẫn ảnh chụp màn hình nằm trong finding log, không đặt thành cột riêng trong bảng execution.
6. Giữ nguyên wording của checklist nguồn; không viết lại checklist item trong lúc execution.
7. Tách execution theo từng màn hình. Mỗi màn hình có một section riêng và một bảng riêng để dễ đọc, thay vì gộp nhiều màn hình thành một bảng ngang.

## Định dạng đầu ra

```markdown
## C1 Danh sách người dùng

| Màn hình | Checklist ID | Kết quả | Ghi chú | Finding |
| --- | --- | --- | --- | --- |
| C1 Danh sách người dùng | IA-01-01 | Pass | Không phát hiện lỗi trong phạm vi màn hình C1. |  |
| C1 Danh sách người dùng | IA-01-10 | Fail | Mobile layout bị tràn ngang trên viewport 390px. | [C-F001](bug_usability_findings_log.md) |
```

## Trọng tâm Scenario C

- C1 Danh sách người dùng: cột dữ liệu, bộ lọc, tìm kiếm, trạng thái active/role, phân trang, trạng thái rỗng/tải dữ liệu.
- C2 Gán vai trò / chỉnh sửa người dùng: nhãn, control, hợp lệ hóa, hành vi lưu/hủy, phản hồi.
- C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu: nội dung xác nhận, độ rõ của thao tác nguy hiểm, đường hủy thao tác, phản hồi thành công/lỗi, dấu vết audit.
