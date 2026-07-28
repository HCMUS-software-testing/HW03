# AI Audit Report - HW03 EMS

Tài liệu này ghi lại quá trình sinh viên dùng AI trong bài HW03 GUI & Usability Testing on EMS.


## Entry 1

- **Ngày giờ:** 2026-07-28 14:57 +0700
- **Công cụ AI / model:** Codex / GPT-5
- **Tác vụ:** Ghi lại prompt trong session HW03 hiện tại vào AI Audit Report
- **Prompt của sinh viên:**

```text
Dùng $ems-ai-audit để ghi lại tất cả prompt trong session HW03 này vào AI Audit Report.
```

- **Output của AI:**

Tóm tắt: AI đọc skill ems-ai-audit, kiểm tra report đích, dùng script add_ai_audit_entry.py để append entry vào AI Audit Report. AI chỉ ghi prompt nhìn thấy trong transcript hiện tại và không tự tạo lịch sử prompt/output cũ.

- **Nhận xét của sinh viên:** Chấp nhận sau khi sinh viên kiểm tra phạm vi transcript.
- **Lý do đánh giá:** Nội dung phù hợp yêu cầu AI Audit vì có công cụ/model, prompt, output tóm tắt, nhận xét, lý do và artefact; tuy nhiên các prompt cũ ngoài transcript hiện tại cần sinh viên cung cấp thêm nếu muốn ghi tiếp.
- **Phần sinh viên sửa hoặc kiểm chứng:** Sinh viên cần đọc lại report, xác nhận đây là toàn bộ prompt trong transcript hiện tại, và paste transcript HW03 trước đó nếu còn prompt khác cần bổ sung.
- **Artefact liên quan:** `submission/ai-audit/ai_audit_report.md`


## Entry 2

- **Ngày giờ:** 2026-07-28 15:04 +0700
- **Công cụ AI / model:** Codex / GPT-5
- **Tác vụ:** Đọc docs HW03 EMS và tạo các file Markdown tiếng Việt cần thiết để nộp bài
- **Prompt của sinh viên:**

```text
Hãy đọc folder docs và tạo các file cần thiết (template định dạng .md) ngôn ngữ tiếng Việt để nộp cho hw này vào folder submission

tôi chọn phương án 1 nhưng đùng để chữ template
```

- **Output của AI:**

Tóm tắt: AI đọc tài liệu HW03 trong docs, README và artefact submission hiện có; đề xuất các phương án cấu trúc file; sau khi sinh viên chọn phương án 1 và yêu cầu không dùng chữ template, AI tạo các file Markdown tiếng Việt trực tiếp trong submission gồm báo cáo chính, checklist execution, usability report, raw notes, cross-platform matrix, findings log, AI critique, git commit log, agent skills demo, README nộp bài và file nguồn tham khảo/AI prompts cho checklist nhóm.

- **Nhận xét của sinh viên:** Chấp nhận sau khi sinh viên điền dữ liệu thật và kiểm tra lại trước khi nộp.
- **Lý do đánh giá:** Các file bao phủ các deliverable bắt buộc trong đề HW03: Task 1A/1B, Task 2, Task 3, findings log, AI Audit/Critique, git log, skills demo và README self-assessment. AI chỉ tạo khung tài liệu; dữ liệu thật như screenshot, participant, timestamp Google Form và cross-platform evidence phải do sinh viên tự thu thập.
- **Phần sinh viên sửa hoặc kiểm chứng:** Sinh viên cần điền MSSV, scenario, màn hình, kết quả test thật, participant thật, screenshot thật, form timestamp thật, link demo và self-assessed grade; sau đó xuất PDF nếu đề yêu cầu Markdown + PDF.
- **Artefact liên quan:** `submission/main_report.md`, `submission/checklist_execution.md`, `submission/usability_report.md`, `submission/user_testing_raw_notes.md`, `submission/cross_platform_matrix.md`, `submission/bug_usability_findings_log.md`, `submission/ai_critique.md`, `submission/git_commit_log.md`, `submission/agent_skills_demo.md`, `submission/README.md`, `submission/group/reference_sources_and_ai_prompts.md`
