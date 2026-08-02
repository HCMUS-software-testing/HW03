---
name: ems-finding-log-writer
description: Ghi, chỉnh hoặc review `submission/bug_usability_findings_log.md` cho HW03 EMS. Dùng khi Codex cần thêm bug/usability finding, chuẩn hóa mã C-Fxxx, giữ bảng tổng hợp ngắn ở đầu, viết chi tiết từng finding theo từng mục không dùng bảng, gắn ảnh minh chứng trực tiếp, nối checklist fail với finding log, hoặc sửa link/format Markdown bị tràn.
---

# EMS Finding Log Writer

## Mục tiêu

Tạo finding log dễ đọc cho bài HW03 EMS: đầu file có bảng tổng hợp ngắn, phần chi tiết đi từ trên xuống theo từng finding và từng mục, không dùng bảng cho phần chi tiết. Skill này bổ trợ cho `ems-gui-checklist-runner`: checklist execution chỉ trỏ tới mã finding, còn ảnh và mô tả đầy đủ nằm trong bug/usability log.

## Nguồn Cần Đọc

Trước khi sửa log, đọc các file liên quan nếu tồn tại:

- `submission/bug_usability_findings_log.md`
- `submission/checklist_execution_scenario_*.md` tương ứng scenario đang làm
- Ảnh trong `submission/screenshots/checklist-failures/`
- Ghi chú của user trong hội thoại hoặc bằng chứng Playwright/manual test

Không tự bịa kết quả test. Nếu chưa có ảnh hoặc ghi chú đủ mạnh, ghi rõ cần minh chứng thay vì tạo finding final.

## Quy Trình

1. Xác định finding là Bug hay Usability:
   - Bug: chức năng sai, validation sai, dữ liệu sai, lỗi kỹ thuật, trạng thái không nhất quán.
   - Usability: người dùng khó hiểu, thiếu gợi ý, wording không rõ, responsive kém, placeholder/label gây nhầm.
2. Nếu checklist item fail, dùng mã finding dạng `C-F001`, `C-F002`, tăng theo số lớn nhất hiện có trong log.
3. Nếu lỗi mới có cùng nguyên nhân, cùng control và cùng tác động, gộp vào finding cũ và thêm ảnh/ghi chú.
4. Nếu khác rule, khác field, khác tác động hoặc khác bước tái hiện, tạo finding riêng.
5. Cập nhật bảng tổng hợp ở đầu file với cột ngắn gọn.
6. Thêm hoặc chỉnh phần chi tiết bên dưới theo từng finding, mỗi trường là một mục riêng. Không đặt chi tiết finding trong bảng 2 cột.
7. Trong checklist execution, link tới finding bằng file-level link như `[C-F005](bug_usability_findings_log.md)`. Không dùng `:line` trong link vì trình đọc Markdown/IDE có thể báo file không tồn tại.
8. Chạy validator nếu repo có script kiểm tra artifact.
9. Với mục `Bước tái hiện / minh chứng` hoặc `Steps`, mỗi bước phải nằm trên một dòng riêng theo ordered list Markdown. Không gộp nhiều bước như `1. ... 2. ... 3. ...` trên cùng một dòng.

## Format Bắt Buộc

Bảng tổng hợp ở đầu log phải compact:

```markdown
## Bảng tổng hợp finding

| ID | Screen | Type | Severity | Tóm tắt | Evidence |
| --- | --- | --- | --- | --- | --- |
| C-F005 | C2 Add User | Usability | 2 | Password rule inconsistent and English error in VI. | C-F005.png |
```

Chi tiết finding phải là từng section dọc theo từng mục. Không dùng bảng cho phần chi tiết finding:

```markdown
### C-F005 - Password validation inconsistent and English error in VI

**Screen:** C2 Add User

**Type:** Usability

**Severity:** 2

**Steps:**
1. Mở Add User bằng giao diện VI.
2. Nhập password `12345678`.
3. Submit form.

**Expected:** Form phải nói rõ rule trước khi nhập hoặc hiển thị lỗi đúng ngôn ngữ VI.

**Actual:** Ban đầu chỉ thấy yêu cầu 8 ký tự, sau submit hiện lỗi tiếng Anh về uppercase/special characters.

**Evidence:**
<img src="screenshots/checklist-failures/C-F005.png" alt="C-F005 evidence">
```

## Quy Tắc Ảnh

- Đặt ảnh trong `submission/screenshots/checklist-failures/`.
- Đặt tên ảnh theo mã finding: `C-F005.png`; nếu nhiều ảnh dùng `C-F005-01.png`, `C-F005-02.png`.
- Hiển thị ảnh trực tiếp trong detail bằng HTML `<img>` ở kích thước tự nhiên/bình thường của file ảnh. Không thêm `width`, `height` hoặc style resize nếu user không yêu cầu.
- Không nhúng ảnh vào checklist execution table.

## Severity

Thang severity:

- 1: Cosmetic/minor wording, ít ảnh hưởng hoàn thành task.
- 2: Gây nhầm, tăng lỗi nhập liệu hoặc làm người dùng mất thời gian nhưng vẫn có thể hoàn thành.
- 3: Cản trở task chính, responsive nghiêm trọng, validation/data issue có ảnh hưởng rõ.
- 4: Không thể hoàn thành task quan trọng hoặc có rủi ro dữ liệu nghiêm trọng.

## Các Trường Hợp Hay Gặp Trong Scenario C

- Email sai format vẫn submit thành công: Bug riêng.
- Password hint một đằng nhưng validation một nẻo, hoặc lỗi tiếng Anh trong giao diện VI: Usability riêng.
- Phone thiếu hint rule 10 số/bắt đầu 0: Usability riêng.
- Phone cho nhập chữ nhưng chỉ báo lỗi sau submit: Usability riêng nếu field không chặn/không hướng dẫn ngay.
- Dropdown có placeholder chọn được như option thật rồi báo lỗi: Usability riêng.
- Sau khi xóa user mà email vẫn bị báo already in use: Bug/Usability tùy bằng chứng; nếu đúng policy soft delete thì ghi vấn đề thông báo/khôi phục, nếu không có giải thích thì ghi như lỗi data lifecycle.
- Member code đã được user khác dùng mà bị chặn là đúng; nếu lỗi hiển thị tiếng Anh trong giao diện VI thì chỉ ghi localization/usability, không ghi là validation sai.

## Kiểm Tra Trước Khi Kết Thúc

- Mỗi ID trong bảng tổng hợp phải có section detail tương ứng.
- Mỗi screenshot được nhắc tới phải tồn tại đúng path.
- Không có link dạng `bug_usability_findings_log.md:13`.
- Checklist fail phải link tới mã finding đúng.
- Mục bước tái hiện phải có từng bước xuống dòng riêng, không gộp nhiều số thứ tự trên cùng một dòng.
- File vẫn đọc được ở Markdown preview, không dùng bảng cho phần chi tiết từng finding.
