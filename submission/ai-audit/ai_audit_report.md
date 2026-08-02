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


## Entry 3

- **Ngày giờ:** 2026-07-28 15:21 +0700
- **Công cụ AI / model:** Codex / GPT-5
- **Tác vụ:** Đọc lại kỹ đề HW03 và chỉnh bộ file submission cho khớp yêu cầu nộp
- **Prompt của sinh viên:**

```text
Hãy đọc lại kĩ file và sửa lại những file cần nộp chính xác nhất cho tôi
```

- **Output của AI:**

Tóm tắt: AI đọc lại docs/2026.HW03.GUI Usability EMS_En.md, đối chiếu Section 6, Section 7, Section 10-15 và Assessment Template. AI chỉnh main_report.md thành báo cáo chính chứa đủ scenario, >=3 màn hình, checklist execution results, usability report summary và cross-platform report summary; cá nhân hóa các file cho Lê Mai Hoài Bảo - Scenario A; tạo user_testing_evidence.md theo đúng yêu cầu User-testing evidence; xóa file ghi chú thô cũ dễ gây nhầm; cập nhật checklist_execution.md, usability_report.md, cross_platform_matrix.md, bug_usability_findings_log.md, README.md và guide để khớp tên artefact thực tế.

- **Nhận xét của sinh viên:** Chấp nhận sau khi sinh viên điền dữ liệu kiểm thử thật.
- **Lý do đánh giá:** Các sửa đổi bám sát Required Contents trong đề: main report Markdown/PDF, user-testing evidence, findings log, cross-platform screenshots/matrix, AI Audit/Critique, git commit log, agent skills/demo và README self-assessment. Nội dung vẫn là khung điền; AI không tạo bằng chứng thật.
- **Phần sinh viên sửa hoặc kiểm chứng:** Sinh viên cần chạy EMS thật, điền kết quả checklist, submit Google Form, bổ sung screenshot thật, participant thật, raw SUS/UEQ-S, cross-platform screenshot có email overlay, export PDF và cập nhật self-assessed grade.
- **Artefact liên quan:** `submission/main_report.md`, `submission/checklist_execution.md`, `submission/usability_report.md`, `submission/user_testing_evidence.md`, `submission/cross_platform_matrix.md`, `submission/bug_usability_findings_log.md`, `submission/README.md`, `submission/HW03_step_by_step_guide.md`


## Entry 4

- **Ngày giờ:** 2026-07-28 15:33 +0700
- **Công cụ AI / model:** Codex / GPT-5
- **Tác vụ:** Tạo Agent Skill hỗ trợ Task 1B EMS checklist execution
- **Prompt của sinh viên:**

```text
PLEASE IMPLEMENT THIS PLAN:
# Kế hoạch tạo Agent Skill cho Task 1B EMS

Tạo Agent Skill mới tên ems-checklist-execution trong submission/skills/ems-checklist-execution/, có SKILL.md, script build_execution_table.py, agents/openai.yaml, cập nhật agent_skills_demo.md và AI Audit Report, rồi validate theo Test Plan.
```

- **Output của AI:**

Tóm tắt: AI tạo skill ems-checklist-execution để hỗ trợ chạy GUI checklist HW03 EMS Task 1B cho Scenario A; tạo script build_execution_table.py đọc 51 item từ gui_usability_checklist_final.md và sinh bảng Markdown với cột A1/A2/A3; cập nhật agent_skills_demo.md; chạy quick_validate.py thành công sau khi cài PyYAML tạm vào /tmp; kiểm tra script sinh đủ 51 dòng và đủ IA-01, IA-02, IA-03, IA-04.

- **Nhận xét của sinh viên:** Chấp nhận sau khi sinh viên kiểm tra nội dung skill và dùng trong demo video.
- **Lý do đánh giá:** Skill bám đúng Section 8 vì hỗ trợ checklist execution có thể tái sử dụng và có kịch bản demo end-to-end. Skill không tự tạo bằng chứng EMS, không tự điền kết quả test, screenshot, severity hay Google Form timestamp.
- **Phần sinh viên sửa hoặc kiểm chứng:** Sinh viên cần dùng skill khi làm Task 1B thật, điền Passed/Failed/N/A dựa trên EMS thật, chụp screenshot failed item, submit Google Form và quay demo video thể hiện quá trình dùng skill.
- **Artefact liên quan:** `submission/skills/ems-checklist-execution/SKILL.md`, `submission/skills/ems-checklist-execution/scripts/build_execution_table.py`, `submission/skills/ems-checklist-execution/agents/openai.yaml`, `submission/agent_skills_demo.md`


## Entry 5

- **Ngày giờ:** 2026-07-28 15:49 +0700
- **Công cụ AI / model:** Codex / GPT-5
- **Tác vụ:** Dùng ems-checklist-execution để chuẩn bị bảng Task 1B cho Scenario A
- **Prompt của sinh viên:**

```text
Dùng $ems-checklist-execution để chuẩn bị bảng Task 1B cho Scenario A và hướng dẫn tôi ghi kết quả Passed/Failed/N/A.
```

- **Output của AI:**

Tóm tắt: AI đọc skill ems-checklist-execution và các file liên quan, chạy script build_execution_table.py để sinh bảng từ checklist nhóm, sau đó cập nhật submission/checklist_execution.md bằng bảng Task 1B gồm 51 checklist item cho ba màn hình A1 Events list, A2 Add/Edit Event và A3 Registration & Roles. AI cũng thêm hướng dẫn cách đánh dấu Passed/Failed/N/A, yêu cầu mỗi Failed phải có notes và screenshot thật, và không tự điền kết quả kiểm thử khi chưa có bằng chứng EMS thật.

- **Nhận xét của sinh viên:** Chấp nhận để dùng làm khung Task 1B; kết quả từng item cần sinh viên tự kiểm chứng trên EMS thật.
- **Lý do đánh giá:** Output đúng phạm vi hỗ trợ chuẩn bị bảng và hướng dẫn ghi kết quả. AI không tự tạo Passed, Failed, N/A, screenshot, bug count hoặc bằng chứng live EMS.
- **Phần sinh viên sửa hoặc kiểm chứng:** Sinh viên cần mở EMS bằng vai trò Admin, kiểm từng item trên A1/A2/A3, thay placeholder bằng Passed/Failed/N/A dựa trên quan sát thật, chụp screenshot cho từng Failed và ghi bug tương ứng vào findings log nếu có.
- **Artefact liên quan:** `submission/checklist_execution.md`, `submission/group/gui_usability_checklist_final.md`, `submission/skills/ems-checklist-execution/SKILL.md`


## Entry 6

- **Ngày giờ:** 2026-08-02 18:35 +0700
- **Công cụ AI / model:** Codex / GPT-5; Computer Use; Browser skill connectivity check
- **Tác vụ:** AI-assisted rebuild Task 1B Scenario A trên EMS production-development deployment, gồm targeted semantic audit và interaction retests
- **Prompt của sinh viên:**

```text
Rebuild Task 1B — Scenario A: giữ A1 Events list, A2 Add/Edit Event và A3 Registration & Roles; chạy lại toàn bộ 51 checklist item trên từng màn hình bằng live prod-dev.ems-fitus.cloud; tạo evidence mới; đồng bộ checklist, report, findings, README, AI Audit, Google-Form-ready entries và commit log; không submit Google Form nếu chưa được phê duyệt.
```

- **Output của AI:**

AI kiểm tra Browser skill nhưng không có browser endpoint khả dụng, sau đó dùng Computer Use trên trình duyệt cục bộ để đăng nhập Admin và kiểm thử tương tác. Targeted semantic audit và interaction retests được chạy thêm cho icon hover/focus trên A2 và unsaved nested Registration & Roles state trên A3. AI chạy 153 checklist rows (51 × A1/A2/A3), tạo evidence mới trong `submission/screenshots/task1b/`, giữ draft `23127326_TASK1B_20260802_163308` (event ID 80) ở trạng thái chưa publish. Kết quả: A1 18 Passed/7 Failed/26 Not applicable trên 25 tiêu chí áp dụng (72.0%); A2 34/4/13 trên 38 (89.5%); A3 30/3/18 trên 33 (90.9%); aggregate 82 Passed, 14 Failed, 57 Not applicable trên 96 tiêu chí áp dụng (85.4%). Có 11 finding được tương tác xác nhận trong log; Google Form không được submit.

- **Nhận xét của sinh viên:** Chờ Bảo kiểm tra evidence, xác nhận email sinh viên thật và tự submit các entry đã chuẩn bị lên Google Form.
- **Lý do đánh giá:** Việc dùng AI có audit trail, kết quả Failed đều gắn evidence mới, các tiêu chí không phù hợp có rationale riêng theo màn hình, và không suy diễn finding chỉ từ ảnh tĩnh. Endpoint ngrok trong đề trả về 404 nên live test dùng `https://prod-dev.ems-fitus.cloud/`.
- **Phần sinh viên sửa hoặc kiểm chứng:** Bảo cần đối chiếu 153 rows với checklist nhóm, xem từng ảnh Failed, nhập email sinh viên thật, submit 11 finding, rồi đồng bộ timestamp nhận từ Google Form. Task 2, Task 3 và PDF tổng hợp được giữ nguyên/chưa hoàn tất.
- **Artefact liên quan:** `submission/checklist_execution.md`, `submission/main_report.md`, `submission/bug_usability_findings_log.md`, `submission/task1b_google_form_entries.md`, `submission/screenshots/task1b/`
