# AI Audit Report - HW03 EMS

Tài liệu này ghi lại quá trình em dùng AI trong bài HW03 GUI & Usability Testing on EMS.


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

- **Nhận xét của sinh viên:** Chấp nhận sau khi em kiểm tra phạm vi transcript.
- **Lý do đánh giá:** Nội dung phù hợp yêu cầu AI Audit vì có công cụ/model, prompt, output tóm tắt, nhận xét, lý do và artefact; tuy nhiên các prompt cũ ngoài transcript hiện tại cần em cung cấp thêm nếu muốn ghi tiếp.
- **Phần sinh viên sửa hoặc kiểm chứng:** Em đã đọc lại report và xác nhận phạm vi prompt được ghi theo transcript hiện tại.
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

Tóm tắt: AI đọc tài liệu HW03 trong docs, README và artefact submission hiện có; đề xuất các phương án cấu trúc file; sau khi em chọn phương án 1 và yêu cầu không dùng chữ template, AI tạo các file Markdown tiếng Việt trực tiếp trong submission gồm báo cáo chính, checklist execution, usability report, raw notes, cross-platform matrix, findings log, AI critique, git commit log, agent skills demo, README nộp bài và file nguồn tham khảo/AI prompts cho checklist nhóm.

- **Nhận xét của sinh viên:** Chấp nhận sau khi em điền dữ liệu thật và kiểm tra lại trước khi nộp.
- **Lý do đánh giá:** Các file bao phủ các deliverable bắt buộc trong đề HW03: Task 1A/1B, Task 2, Task 3, findings log, AI Audit/Critique, git log, skills demo và README self-assessment. AI chỉ tạo khung tài liệu; dữ liệu thật như screenshot, participant, timestamp Google Form và cross-platform evidence phải do em tự thu thập.
- **Phần sinh viên sửa hoặc kiểm chứng:** Em đã kiểm tra và bổ sung các thông tin thật cho phần bài làm hiện có, gồm MSSV, scenario, màn hình, kết quả kiểm thử, screenshot và các mục cần đồng bộ trong submission.
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

- **Nhận xét của sinh viên:** Chấp nhận sau khi em điền dữ liệu kiểm thử thật.
- **Lý do đánh giá:** Các sửa đổi bám sát Required Contents trong đề: main report Markdown/PDF, user-testing evidence, findings log, cross-platform screenshots/matrix, AI Audit/Critique, git commit log, agent skills/demo và README self-assessment. Nội dung vẫn là khung điền; AI không tạo bằng chứng thật.
- **Phần sinh viên sửa hoặc kiểm chứng:** Em đã chạy EMS thật cho phần Task 1B, kiểm tra kết quả checklist, bổ sung screenshot thật và rà soát các artefact submission liên quan trước khi nộp.
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

- **Nhận xét của sinh viên:** Chấp nhận sau khi em kiểm tra nội dung skill và dùng trong demo video.
- **Lý do đánh giá:** Skill bám đúng Section 8 vì hỗ trợ checklist execution có thể tái sử dụng và có kịch bản demo end-to-end. Skill không tự tạo bằng chứng EMS, không tự điền kết quả test, screenshot, severity hay Google Form timestamp.
- **Phần sinh viên sửa hoặc kiểm chứng:** Em đã dùng quy trình hỗ trợ Task 1B, điền kết quả dựa trên EMS thật, chụp screenshot cho các mục Failed và kiểm tra lại artefact liên quan.
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

- **Nhận xét của sinh viên:** Chấp nhận để dùng làm khung Task 1B; kết quả từng item cần em tự kiểm chứng trên EMS thật.
- **Lý do đánh giá:** Output đúng phạm vi hỗ trợ chuẩn bị bảng và hướng dẫn ghi kết quả. AI không tự tạo Passed, Failed, N/A, screenshot, bug count hoặc bằng chứng live EMS.
- **Phần sinh viên sửa hoặc kiểm chứng:** Em đã mở EMS bằng vai trò Admin, kiểm từng item trên A1/A2/A3, ghi kết quả Đạt/Không đạt/Không áp dụng dựa trên quan sát thật, chụp screenshot cho từng mục Failed và ghi bug tương ứng vào findings log.
- **Artefact liên quan:** `submission/checklist_execution.md`, `submission/group/gui_usability_checklist_final.md`, `submission/skills/ems-checklist-execution/SKILL.md`


## Entry 6

- **Ngày giờ:** 2026-08-02 22:20 +0700
- **Công cụ AI / model:** Codex / GPT-5
- **Tác vụ:** AI hỗ trợ kiểm thử live Task 1B Scenario A và đồng bộ lại artefact
- **Prompt của sinh viên:**

```text
# Rebuild Task 1B — Scenario A

Retain Bảo’s assigned screens: A1 Events list, A2 Add/Edit Event, and A3 Registration & Roles. Re-test all 51 checklist items on each screen using the live prod-dev.ems-fitus.cloud deployment. Log in with the provided Admin account, create one uniquely named draft event, capture evidence, update checklist_execution.md, main_report.md, bug_usability_findings_log.md, READMEs, Google-Form-ready entries, and git_commit_log.md.

```

- **Output của AI:**

Tóm tắt: AI điều khiển trình duyệt kiểm thử trực tiếp deployment `https://prod-dev.ems-fitus.cloud/`, dùng tài khoản Admin đã cung cấp, tạo và giữ lại draft event `23127326_TASK1B_20260802_163308`, chạy lại 51 checklist item cho từng màn hình A1/A2/A3, chụp bộ ảnh minh chứng mới trong `submission/screenshots/task1b/`, xác nhận 14 phát hiện bằng tương tác thật, cập nhật bảng checklist/report/findings theo tiếng Việt và khôi phục cấu trúc bảng theo commit `d655d24e9dc92adb3b09783d18ec56cb84852189`. Sau phản hồi của em, AI xóa mục audit tạm thời, nhúng ảnh trực tiếp bằng Markdown image trong các artefact Task 1B, rồi kiểm tra lại số dòng, số lượng checklist ID, ảnh tồn tại, bảng render và sự nhất quán giữa checklist, report và findings log.

- **Nhận xét của sinh viên:** Chấp nhận việc AI hỗ trợ kiểm thử nếu kết quả dựa trên EMS live, có screenshot thật, không suy đoán từ ảnh tĩnh và em review lại trước khi nộp.
- **Lý do đánh giá:** Việc dùng AI phù hợp chính sách `AI Policy: Open`; AI được dùng như trợ lý kiểm thử có điều khiển browser. Phần không được phép là tạo giả evidence hoặc tự bịa Passed/Failed. Entry này ghi rõ kết quả dựa trên tương tác live và ảnh thật, còn em vẫn chịu trách nhiệm xác minh cuối cùng.
- **Phần sinh viên sửa hoặc kiểm chứng:** Em đã mở lại các artefact, đối chiếu ảnh failed với mô tả lỗi, xác nhận kết quả dựa trên kiểm thử EMS live và chuẩn bị các phát hiện để gửi/đồng bộ Google Form bằng email trường thật của em.
- **Artefact liên quan:** `submission/checklist_execution.md`, `submission/main_report.md`, `submission/bug_usability_findings_log.md`, `submission/task1b_google_form_entries.md`, `submission/screenshots/task1b/`, `submission/git_commit_log.md`, `README.md`, `submission/README.md`
