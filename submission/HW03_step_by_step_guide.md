# Hướng Dẫn Từng Bước Hoàn Thành HW03

Tài liệu này tổng hợp từ các file Markdown trong `docs/`, ngoại trừ tài liệu ISTQB. Mục tiêu là biến đề bài HW03 thành một quy trình thực hiện cụ thể để nhóm và từng thành viên có thể theo dõi đến lúc nộp ZIP.

## 1. Tóm tắt yêu cầu

| Hạng mục | Phạm vi | Điểm | Người chịu trách nhiệm |
| --- | --- | ---: | --- |
| Task 1A | Shared GUI checklist `> 40` items, bao phủ `IA-01` đến `IA-04`, kèm nguồn tham khảo và AI prompts | 15 | Nhóm |
| Task 1B | Chạy checklist trên ít nhất `3` màn hình của scenario cá nhân, ghi Pass/Fail/Notes, screenshot lỗi, bug report | 15 | Cá nhân |
| Task 2 | User testing với `5` người thật, có pilot, metrics, SUS hoặc UEQ-S, Usability Report | 25 | Cá nhân |
| Task 3 | Cross-browser/cross-platform matrix cho từng màn hình cá nhân | 25 | Cá nhân |
| Task 4 | Submit findings vào Google Form và tổng hợp vào Bug & Usability Findings Log | 10 | Cá nhân |
| Task 5 | Agent Skills và demo video | 10 | Cá nhân |

SUT: `https://promoter-starboard-prude.ngrok-free.dev/`

Admin account: `admin@gmail.com` / `Admin@123`

Findings Google Form: `https://forms.gle/CJQFQCAXcsDbXDMM9`

Lưu ý quan trọng: EMS chạy qua ngrok và dữ liệu có thể reset. Chụp screenshot, quay video, lưu bằng chứng ngay khi test.

## 2. Chuẩn bị repository và thư mục làm bài

Tạo cấu trúc nộp bài ngay từ đầu để tránh thất lạc bằng chứng:

```text
submission/
  README.md
  main_report.md
  bug_usability_findings_log.md
  git_commit_log.txt
  ai-audit/
    ai_audit_report.md
  ai_critique.md
  group/
    shared_gui_checklist.md
    references.md
    ai_prompts.md
  user-testing/
    pilot_notes.md
    participant_table.md
    session_notes/
    raw_scores/
  cross-platform/
    matrix.md
    screenshots/
  screenshots/
    checklist-failures/
    usability-findings/
  agent-skills/
  demo-videos.md
```

Sau mỗi giai đoạn lớn, commit một lần. Đề yêu cầu có Git commit log theo từng bước testing procedure, ví dụ checklist design, checklist execution, bug logging, usability evaluation, và từng cross-platform run.

## 3. Chia nhóm và chọn scenario

Mỗi thành viên chọn đúng một scenario:

| Scenario | Tên | Phạm vi |
| --- | --- | --- |
| A | Admin creates and manages events | Vòng đời sự kiện phía admin |
| B | User registers to attend an event | Trải nghiệm người tham gia |
| C | Admin manages users | Quản trị người dùng |
| D | User requests Support and Admin resolves it | Luồng support từ user đến admin |

Quy tắc không trùng lặp: trong cùng nhóm, không được có hai thành viên sở hữu cùng scenario và cùng bộ màn hình. Nếu nhóm có hơn bốn người và phải chia sẻ scenario, mỗi người chọn bộ màn hình khác nhau và giải thích lý do.

Chọn ít nhất `3` màn hình. Nên chọn `4` nếu còn thời gian để giảm rủi ro một màn hình bị lỗi hoặc dữ liệu reset.

Gợi ý chọn màn hình:

| Scenario | Bộ màn hình nên chọn |
| --- | --- |
| A | Events list, Add/Edit Event, Registration & Roles config, Participants & Reviews, Check-in |
| B | Home/events listing, Event detail, Registration form, My Registrations/QR ticket, Post-event review |
| C | Users list, Assign Role/edit user, Block/Unblock + Reset Password dialogs, Export to Excel |
| D | User create support request, User My Requests/detail, Admin Support Requests list, Admin request detail/reply |

## 4. Task 1A: Thiết kế shared GUI checklist

Nhóm tạo một checklist dùng chung, nhiều hơn `40` items, bao phủ đủ bốn interface aspects:

| IA | Aspect | Cần kiểm tra |
| --- | --- | --- |
| `IA-01` | General UI standards | Layout, alignment, typography, color, consistency, EN/VI, empty/loading states |
| `IA-02` | Forms | Labels, validation, error placement, required fields, uploads, rich-text editor |
| `IA-03` | Navigation | Menus, breadcrumbs, tabs, sidebar, drag-and-drop reorder, back actions, deep links |
| `IA-04` | Feedback/state | Toasts, badges, confirmation dialogs, progress bars, status colors, real-time updates |

Quy trình làm:

1. Cả nhóm đọc lại Nielsen's 10 heuristics, Norman's 6 principles, Shneiderman's 8 golden rules, và checklist theo widget từ bài giảng.
2. Dùng AI tạo bản nháp checklist. Không dùng prompt chung chung kiểu "generate GUI checklist". Hãy yêu cầu AI tạo checklist theo từng IA và theo đặc điểm EMS.
3. Review thủ công từng item. Xóa item mơ hồ, trùng lặp, hoặc không test được bằng quan sát.
4. Bổ sung các item AI hay bỏ sót: accessibility, keyboard navigation, EN/VI i18n, mobile layout, upload preview, rich-text validation, dark mode nếu có, empty/loading/error states.
5. Với mỗi item nhóm tự thêm ngoài AI output, ghi lý do AI bỏ sót.
6. Lưu `submission/group/shared_gui_checklist.md`, `submission/group/references.md`, và `submission/group/ai_prompts.md`.

Template checklist nên dùng:

```markdown
| ID | IA | Checklist item | Source | AI/Human | Why added or adjusted |
| --- | --- | --- | --- | --- | --- |
| GUI-001 | IA-01 | Text, spacing, and alignment are visually consistent within the screen. | Nielsen/Shneiderman | AI + reviewed | Refined to be observable per screen |
```

Checklist phải đủ cụ thể để chạy trên từng màn hình. Ví dụ "UI is good" là không đạt; "Primary action button is visually distinct from secondary actions" là kiểm tra được.

## 5. Task 1B: Chạy checklist trên scenario cá nhân

Với mỗi màn hình đã chọn, chạy toàn bộ shared checklist và ghi kết quả.

Quy trình thực hiện:

1. Mở EMS, đăng nhập đúng vai trò cần test.
2. Điều hướng đến màn hình cần test.
3. Chụp screenshot trạng thái ban đầu của màn hình để làm bằng chứng tổng quan.
4. Chạy từng checklist item.
5. Ghi `Pass`, `Fail`, hoặc `N/A`. Chỉ dùng `N/A` khi item thật sự không áp dụng cho màn hình đó.
6. Với mỗi `Fail`, ghi rõ lý do trong `Notes`.
7. Chụp screenshot cho từng failed item. Không cần screenshot cho item pass.
8. Nếu fail là bug hoặc usability issue, thêm vào Bug & Usability Findings Log và submit Google Form.

Template execution table:

```markdown
| Screen | Checklist ID | Result | Notes | Screenshot ref | Finding ID |
| --- | --- | --- | --- | --- | --- |
| A2 Add/Edit Event | GUI-014 | Fail | Error message for invalid end date appears only after submit, not near DateTime field. | screenshots/checklist-failures/A2_GUI-014.png | F-001 |
```

Bug report tối thiểu phải có:

```markdown
| Field | Content |
| --- | --- |
| ID | F-001 |
| Screen | A2 Add/Edit Event |
| Type | Bug |
| Steps to reproduce | 1. Open Add Event. 2. Set end date before start date. 3. Click Save Draft. |
| Expected | The form blocks saving and shows an inline validation message near DateTime. |
| Actual | The error is missing, unclear, or appears in the wrong place. |
| Severity | Major |
| Screenshot | screenshots/checklist-failures/A2_GUI-014.png |
| Suggested fix | Add inline validation near DateTime and keep Save disabled until valid. |
```

## 6. Scenario-specific test hints

### Scenario A: Admin creates and manages events

Ưu tiên kiểm tra các màn hình sau:

1. Events list: status filters, notification dots, search/filter behavior, empty/loading state.
2. Add/Edit Event: thumbnail `4:3`, banner `24:9`, RichTextEditor, date/time validation.
3. Registration & Roles config: student/lecturer/guest toggles, Max Slots, Waitlist, Additional Role.
4. Participants & Reviews: Approve/Reject, role decisions, progress bar, status colors, Export.
5. Check-in: scan states, repeated scan, outside check-in window, real-time log.

Luồng E2E admin trong `docs/Kịch-bản-E2E-Test-Flow-Luồng-Admin.md` là checklist chức năng tốt để tạo dữ liệu và phát hiện bug cho Scenario A, C, D phía admin.

### Scenario B: User registers to attend an event

Ưu tiên kiểm tra:

1. Home/events listing: carousel, categories, search/filter, responsive cards.
2. Event detail: banner, schedule, register button, waitlist notice.
3. Registration form: role selection, additional role, required fields, confirmation.
4. My Registrations/ticket: status, QR/barcode, cancel or details behavior nếu có.
5. Post-event review: star rating, validation, duplicate review handling.

Cần tự đăng ký tài khoản user riêng. Không dùng chung một user account trong nhóm.

### Scenario C: Admin manages users

Ưu tiên kiểm tra:

1. Users list: Avatar + Name, Role, Member Code, Active, Audit columns, filters.
2. Assign Role/edit user: role update, validation, feedback.
3. Block/Unblock and Reset Password dialogs: confirmation, cancel path, audit log.
4. Export to Excel: file tải xuống, đủ cột, feedback sau khi export.

Khi test block user, nên dùng tài khoản test riêng để tránh làm gián đoạn thành viên khác.

### Scenario D: User requests Support and Admin resolves it

Ưu tiên kiểm tra:

1. User create support request: category, content, image attachment, validation.
2. User My Requests/detail: status, official response, attachment display.
3. Admin Support Requests list: Pending/Resolved tabs, search by member code/category.
4. Admin request detail: image lightbox, internal note, official response, resolve feedback.

Luồng này cần cả user account cá nhân và admin account.

## 7. Task 2: User testing với 5 người thật

Task 2 không phải là tự đánh giá heuristic. Phải chạy user testing với `5` người thật ngoài lớp, có thông tin liên hệ có thể xác minh.

Quy trình:

1. Viết scenario dạng mục tiêu, không đưa từng cú click. Ví dụ Scenario B: "Bạn muốn đăng ký một workshop sắp diễn ra và mở QR check-in của mình."
2. Chọn metrics tối thiểu: task success, time on task, error/hesitation count, SUS hoặc UEQ-S.
3. Viết bộ câu hỏi sau task về clarity, error recovery, speed, trust.
4. Recruit `5` participant đúng profile. Mask contact, ví dụ số điện thoại `090****123`.
5. Chạy pilot với `1` người ngoài 5 người chính. Sửa wording nếu participant pilot hiểu sai nhiệm vụ.
6. Với mỗi participant chính, xin consent, yêu cầu think aloud, record screen nếu được.
7. Không gợi ý dẫn dắt. Chỉ can thiệp nếu họ bị kẹt hoàn toàn.
8. Ghi observation notes: lỗi, hesitation, friction, quote đáng chú ý.
9. Cho participant điền SUS hoặc UEQ-S.
10. Tính metrics và viết Usability Report.

Template participant table:

```markdown
| ID | Profile | Contact masked | Session date/time | Consent | Notes |
| --- | --- | --- | --- | --- | --- |
| P01 | Student, event participant | Zalo 09****1234 | 2026-..-.. ..:.. | Yes | Completed without hints |
```

Template metrics:

```markdown
| Participant | Success | Time on task | Errors | Hesitations | SUS/UEQ-S | Key friction |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| P01 | Completed | 03:42 | 1 | 2 | 72.5 | Could not identify waitlist status quickly |
```

Severity nên dùng thang `0` đến `4`:

| Severity | Ý nghĩa |
| --- | --- |
| 0 | Không phải vấn đề |
| 1 | Cosmetic hoặc minor annoyance |
| 2 | Minor usability issue, có workaround |
| 3 | Major issue, gây chậm hoặc lỗi đáng kể |
| 4 | Critical issue, chặn task hoặc gây mất dữ liệu |

## 8. Task 3: Cross-browser / cross-platform

Với mỗi màn hình cá nhân, tạo matrix bao phủ:

| Dimension | Bắt buộc |
| --- | --- |
| Operating systems | Ít nhất `3`: ví dụ Windows, macOS, Android hoặc iOS |
| Browsers | Ít nhất `5`: Chrome, Firefox, Safari, Edge, Opera hoặc Samsung Internet |
| Device classes | Ít nhất `3`: desktop, tablet, phone |

Không cần chạy đủ `3 x 5 x 3 = 45` tổ hợp cho mỗi màn hình, nhưng với mỗi màn hình phải bao phủ đủ mọi OS, mọi browser, và mọi device class ít nhất một lần.

Nên dùng BrowserStack hoặc LambdaTest trial. Nếu không có trial, dùng cloud tool khác hoặc thiết bị thật. Mỗi screenshot phải hiển thị:

1. EMS URL.
2. Browser, OS, device name.
3. Overlay email sinh viên dạng `MSSV@....edu.vn`.
4. Màn hình đang test.

Template matrix:

```markdown
| Screen | OS | Browser | Device class | Device/profile | Result | Screenshot ref | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B2 Event Detail | Windows 11 | Chrome | Desktop | 1920x1080 | Pass | cross-platform/screenshots/B2_win_chrome_desktop.png | No layout issue |
| B2 Event Detail | iOS | Safari | Phone | iPhone 15 | Fail | cross-platform/screenshots/B2_ios_safari_phone.png | Register button overlaps sticky footer |
```

Một matrix tối thiểu hợp lý cho mỗi màn hình có thể gồm `5` đến `7` cells, miễn là bao phủ đủ các dimension. Ví dụ:

| Cell | OS | Browser | Device |
| --- | --- | --- | --- |
| 1 | Windows | Chrome | Desktop |
| 2 | Windows | Edge | Desktop |
| 3 | macOS | Safari | Desktop |
| 4 | Android | Chrome | Phone |
| 5 | Android | Firefox | Phone |
| 6 | iOS hoặc Android tablet | Safari, Opera, hoặc Samsung Internet | Tablet |

Nếu chọn Android thay iOS, Safari sẽ khó bao phủ. Khi có thể, nên dùng macOS hoặc iOS để test Safari.

## 9. Findings: submit form và aggregated log

Mọi defect và usability improvement từ Task 1, Task 2, Task 3 phải được báo cáo hai nơi:

1. Google Form: `https://forms.gle/CJQFQCAXcsDbXDMM9`.
2. File tổng hợp: `submission/bug_usability_findings_log.md`.

Template log:

```markdown
| ID | Scenario/Screen | Type | Description | Steps/Heuristic | Severity | Suggested fix | Screenshot ref | Form-submission timestamp |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F-001 | B2 Event Detail | Usability | Waitlist notice is hard to notice on mobile. | User testing P02/P04 hesitated before registration. | 3 | Move waitlist status near primary register button and use clearer badge color. | screenshots/usability-findings/F-001.png | 2026-..-.. ..:.. |
```

Số lượng findings trong log phải khớp số lượng đã submit vào form vì TA có thể cross-check.

## 10. AI Audit Report và AI Critique

AI Policy là open, nhưng bắt buộc khai báo. Nếu dùng AI, ghi vào `submission/ai-audit/ai_audit_report.md`:

1. AI tool/model.
2. Ngày giờ.
3. Prompt.
4. Output tóm tắt.
5. Verdict, reasoning, và student fix do sinh viên tự đánh giá.

Nếu không dùng AI, phải ghi rõ: `I do not use any AI help in this exercise.`

Ngoài audit report, cần viết `AI Critique` dài `200-300` từ. Nội dung nên trả lời:

1. AI sai, thiên lệch, hoặc thiếu ở đâu?
2. Vì sao AI không bắt được vấn đề đó?
3. Bạn đã sửa hoặc kiểm chứng lại như thế nào?
4. Bạn học được nguyên tắc gì khi cộng tác với AI trong software testing?

Không được nộp raw AI output chưa review.

## 11. Agent Skills và demo video

Đề khuyến khích tạo Agent Skills tái sử dụng cho:

1. Chạy GUI checklist trên một màn hình EMS.
2. Hỗ trợ heuristic/usability evaluation.
3. Sinh hoặc kiểm cross-platform matrix.
4. Tạo AI Audit entry.

Nếu làm phần này, cần nộp skill files và video demo end-to-end. Video nên show rõ:

1. Skill được gọi như thế nào.
2. Input là màn hình hoặc scenario nào.
3. Output được sinh ra ở đâu.
4. Sinh viên review và chỉnh sửa output như thế nào.

## 12. Main report outline

`submission/main_report.md` nên theo cấu trúc:

```markdown
# HW03 GUI & Usability Testing on EMS

## 1. Student and Scenario
- Student ID:
- Full name:
- Group:
- Scenario:
- Screens selected:
- Rationale:

## 2. Shared GUI Checklist Summary
- Checklist source:
- Number of items:
- IA coverage:
- AI prompts reference:

## 3. Checklist Execution
- Screen list
- Execution tables
- Failed items and screenshots
- Bug reports

## 4. Usability Report
- User-testing scenario
- Pilot result and refinement
- Participant table
- Metrics
- Ranked findings
- Recommendations

## 5. Cross-Browser / Cross-Platform Report
- Matrix design
- Per-screen results
- Screenshots
- Compatibility defects

## 6. Bug & Usability Findings Summary
- Count by type
- Count by severity
- Link to aggregated log

## 7. AI Usage
- AI Audit Report reference
- AI Critique reference

## 8. Git Commit Log
- Commit log file reference

## 9. Appendix
- Screenshots
- Recordings
- Raw notes
```

## 13. README self-assessment

ZIP phải có `README.md` với self-assessment table và test summary.

Template:

```markdown
# HW03 Submission README

## Submission Summary

| Field | Value |
| --- | --- |
| Student ID | |
| Full name | |
| Group | |
| Scenario chosen | |
| Screens tested | |
| Checklist items designed | |
| Checklist executions | |
| Passed / Failed | |
| Bugs found | |
| Usability participants | 5 |
| Usability issues by severity | |
| Compatibility cells covered | |
| Demo video links | |

## Self-Assessment

| No. | Criteria | Grade | Self-Assessed Grade |
| --- | --- | ---: | ---: |
| 1a | Task 1A - Shared checklist + sources + AI prompts | 15 | |
| 1b | Task 1B - Checklist execution + bug reports | 15 | |
| 2 | Task 2 - User testing and Usability Report | 25 | |
| 3 | Task 3 - Cross-browser/platform matrix | 25 | |
| 4 | Findings submission + aggregated log | 10 | |
| 5 | Agent Skills + demo videos | 10 | |
| | Total | 100 | |
```

## 14. Đóng gói nộp bài

Tên ZIP:

```text
<StudentID>_HW03_AI_GUIUsability_EMS_<SelfAssessedGrade>.zip
```

Ví dụ:

```text
25127001_HW03_AI_GUIUsability_EMS_090.zip
```

Checklist trước khi nộp:

1. Có shared GUI checklist `> 40` items, nguồn tham khảo, AI prompts.
2. Có main report Markdown và PDF.
3. Có checklist execution cho ít nhất `3` màn hình.
4. Mỗi failed checklist item có screenshot.
5. Mỗi bug/usability finding đã submit Google Form.
6. Aggregated findings log khớp với Google Form.
7. Có user testing với `5` người thật, contact masked, raw notes, SUS hoặc UEQ-S.
8. Có cross-platform matrix và screenshot cho mọi cell, có overlay `MSSV@....edu.vn`.
9. Có AI Audit Report và AI Critique `200-300` từ.
10. Có Git commit log text file.
11. Có Agent Skills và demo video links nếu làm phần điểm này.
12. Có `README.md` với self-assessment và test summary.
13. Tên ZIP đúng format.

## 15. Lịch làm việc đề xuất

| Buổi | Việc cần hoàn thành | Output |
| --- | --- | --- |
| 1 | Chia scenario, chọn màn hình, tạo cấu trúc submission | Screen list, initial README |
| 2 | Nhóm tạo checklist, references, AI prompts | Shared checklist `> 40` items |
| 3 | Cá nhân chạy checklist trên từng màn hình | Execution tables, screenshots, findings |
| 4 | Thiết kế user testing, chạy pilot | Scenario, metrics, refined protocol |
| 5 | Chạy 5 sessions thật | Raw notes, recordings, SUS/UEQ-S |
| 6 | Phân tích usability và submit findings | Usability Report, Form submissions |
| 7 | Chạy cross-platform matrix | Matrix, screenshots, compatibility findings |
| 8 | Hoàn thiện AI Audit, AI Critique, Git log, PDF, ZIP | Final submission package |

## 16. Thứ tự thao tác khuyến nghị khi bắt đầu ngay

1. Chọn scenario cá nhân và ghi lý do chọn ít nhất `3` màn hình.
2. Đăng nhập EMS và kiểm tra các màn hình có truy cập được không.
3. Nếu scenario cần user side, tạo user account riêng.
4. Cùng nhóm tạo shared checklist.
5. Tạo file log findings trước khi test để không quên timestamp form.
6. Chạy checklist trên màn hình đầu tiên, log bug ngay.
7. Commit sau khi hoàn tất mỗi màn hình.
8. Thiết kế user-testing protocol và chạy pilot.
9. Chạy 5 participant sessions.
10. Chạy cross-platform cho từng màn hình.
11. Tổng hợp main report, README, audit, critique.
12. Export PDF, kiểm tra ZIP, nộp Moodle.
