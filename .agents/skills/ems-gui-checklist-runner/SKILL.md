---
name: ems-gui-checklist-runner
description: Chạy checklist GUI usability dùng chung của HW03 EMS trên một màn hình EMS được chọn và sinh các dòng execution cho Task 1B. Dùng khi Codex được yêu cầu đánh giá một màn hình EMS, điền kết quả checklist, nối item fail với ảnh/finding, hoặc kiểm tra Scenario A/B/C/D đã có đủ minh chứng Pass/Fail/N/A hay chưa.
---

# EMS GUI Checklist Runner

## Đầu vào

Cần có:

- Mã và tên màn hình, ví dụ `C1 Danh sách người dùng`.
- Nguồn minh chứng: ghi chú quan sát thật, ảnh chụp màn hình hoặc walkthrough thủ công đã hoàn thành.
- Nguồn checklist: `submission/group/gui_usability_checklist_final.md`.

Không đánh dấu kết quả thật bằng suy đoán. Nếu thiếu minh chứng, ghi `Chờ kiểm thử`.

## Quy trình

1. Đọc checklist dùng chung và giữ nguyên mọi ID item.
2. Với màn hình được chọn, đánh giá từng item là `Pass`, `Fail`, `N/A` hoặc `Chờ kiểm thử`.
3. Chỉ dùng `N/A` khi item thật sự không áp dụng cho màn hình đó.
4. Với mỗi `Fail`, bắt buộc có:
   - Lý do cụ thể trong ghi chú.
   - Đường dẫn ảnh chụp màn hình.
   - Mã finding như `C-F001`.
5. Thêm finding tương ứng vào `submission/bug_usability_findings_log.md`.
6. Giữ nguyên wording của checklist nguồn; không viết lại checklist item trong lúc execution.

## Định dạng đầu ra

```markdown
| Màn hình | Checklist ID | Kết quả | Ghi chú | Ảnh minh chứng | Mã finding |
| --- | --- | --- | --- | --- | --- |
| C1 Danh sách người dùng | IA-01-01 | Chờ kiểm thử | Chưa thu thập minh chứng. |  |  |
```

## Trọng tâm Scenario C

- C1 Danh sách người dùng: cột dữ liệu, bộ lọc, tìm kiếm, trạng thái active/role, phân trang, trạng thái rỗng/tải dữ liệu.
- C2 Gán vai trò / chỉnh sửa người dùng: nhãn, control, hợp lệ hóa, hành vi lưu/hủy, phản hồi.
- C3 Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu: nội dung xác nhận, độ rõ của thao tác nguy hiểm, đường hủy thao tác, phản hồi thành công/lỗi, dấu vết audit.
