---
name: ems-checklist-execution
description: Use when running the HW03 EMS GUI checklist on assigned scenario screens, recording Passed/Failed/N/A results, failed-item notes, screenshots, and Bug & Usability Findings Log entries.
---

# EMS Checklist Execution

## Mục tiêu

Hỗ trợ sinh viên chạy Task 1B của HW03 EMS: áp dụng checklist nhóm lên các màn hình scenario cá nhân, ghi `Passed` / `Failed` / `N/A`, notes cho item fail, screenshot ref và bug report tương ứng.

## Quy tắc bắt buộc

- Không tự tạo kết quả kiểm thử. Chỉ ghi `Passed`, `Failed`, `N/A`, notes, screenshot ref, bug, severity hoặc Google Form timestamp khi sinh viên cung cấp hoặc khi nhìn thấy bằng chứng thật trong session.
- Không tạo giả screenshot, trạng thái EMS, bug count, Form timestamp, BrowserStack/LambdaTest result hoặc participant data.
- Với mỗi item `Failed`, phải có lý do fail trong notes và screenshot thật từ EMS.
- Mọi bug hoặc usability issue phát hiện từ Task 1B phải được ghi ở cả report và `submission/bug_usability_findings_log.md`; sau khi sinh viên submit Google Form, mới điền `Form-submission timestamp`.
- Nội dung hỗ trợ và output dùng tiếng Việt, giữ nguyên các nhãn bắt buộc như `Passed`, `Failed`, `N/A`.

## Workflow Task 1B

1. Đọc checklist nhóm ở `submission/group/gui_usability_checklist_final.md`.
2. Xác nhận scenario và tối thiểu 3 màn hình. Với Hoài Bảo, mặc định dùng:
   - `A1` Events list with status filters and notification dots.
   - `A2` Add/Edit Event form - image upload + Rich-Text + date/time validation.
   - `A3` Registration & Roles configuration panel - Max Slots / Waitlist / additional role.
3. Nếu bảng Task 1B chưa có đủ item, chạy script:

```bash
python3 submission/skills/ems-checklist-execution/scripts/build_execution_table.py
```

Ghi ra file nếu cần:

```bash
python3 submission/skills/ems-checklist-execution/scripts/build_execution_table.py \
  --output /tmp/ems_task1b_table.md
```

4. Hướng dẫn sinh viên mở EMS bằng tài khoản phù hợp và kiểm từng item trên từng màn hình.
5. Điền bảng chi tiết trong `submission/checklist_execution.md`.
6. Tóm tắt số item áp dụng, Passed, Failed, N/A theo màn hình trong `submission/main_report.md`.
7. Với mỗi bug/usability issue thật, thêm dòng vào `submission/bug_usability_findings_log.md` và nhắc sinh viên submit Google Form.

## Cách đánh giá từng item

| Result | Khi dùng | Bằng chứng cần có |
| --- | --- | --- |
| `Passed` | Màn hình đạt item checklist khi quan sát hoặc thao tác thật. | Không bắt buộc screenshot riêng. |
| `Failed` | Màn hình vi phạm item checklist. | Notes nêu lý do fail và screenshot ref thật. |
| `N/A` | Item không áp dụng hợp lý cho màn hình đó. | Notes ngắn nếu dễ gây tranh cãi. |

## Cách ghi bug từ failed item

Mỗi bug report tối thiểu phải có:

| Field | Nội dung |
| --- | --- |
| Screen | `A1`, `A2`, hoặc `A3` |
| Steps to reproduce | Các bước thao tác cụ thể trên EMS |
| Expected | Hành vi/giao diện mong đợi |
| Actual | Hành vi/giao diện thực tế |
| Severity | `0` đến `4` |
| Screenshot ref | Đường dẫn ảnh thật |
| Form timestamp | Chỉ điền sau khi submit Google Form |

## Demo video gợi ý

Một demo end-to-end đủ rõ cho Section 8 nên thể hiện:

1. Gọi `$ems-checklist-execution`.
2. Chạy script sinh bảng Task 1B từ checklist nhóm.
3. Mở một màn hình EMS thật thuộc A1/A2/A3.
4. Điền thử một item `Passed` và một item `Failed` dựa trên bằng chứng thật.
5. Ghi bug tương ứng vào `bug_usability_findings_log.md`.
6. Đọc lại artefact và nói rõ phần nào do sinh viên kiểm chứng thủ công.

## Lỗi thường gặp

| Lỗi | Cách xử lý |
| --- | --- |
| Ghi `Failed` nhưng không có notes | Thêm lý do fail cụ thể, gắn với item checklist. |
| Ghi screenshot ref cho item chưa chụp | Để trống đến khi có ảnh thật. |
| Đánh dấu `N/A` quá rộng | Chỉ dùng khi item thật sự không áp dụng cho màn hình. |
| Bug trong report nhưng thiếu findings log | Thêm cùng bug vào `submission/bug_usability_findings_log.md`. |
| Có timestamp nhưng chưa submit form | Xóa timestamp cho đến khi sinh viên submit thật. |
