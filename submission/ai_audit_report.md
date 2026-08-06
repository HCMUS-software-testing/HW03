# AI Audit Report — HW03 GUI & Usability Testing on EMS

## 1. Khai báo sử dụng AI

`I use AI tools for the following tasks.`

## 2. Nhật ký tương tác AI

### Entry 1

- **Ngày giờ:** 2026-07-28 14:57 +0700
- **Công cụ AI / model:** Codex / GPT-5
- **Prompt:**

```text
Dùng $ems-ai-audit để ghi lại tất cả prompt trong session HW03 này vào AI Audit Report.
```

- **Output AI:** AI đọc skill `ems-ai-audit`, kiểm tra báo cáo đích và ghi prompt nhìn thấy trong transcript hiện tại vào AI Audit Report; không tự tạo lịch sử prompt/output cũ.

### Entry 2

- **Ngày giờ:** 2026-07-28 15:04 +0700
- **Công cụ AI / model:** Codex / GPT-5
- **Prompt:**

```text
Hãy đọc folder docs và tạo các file cần thiết (template định dạng .md) ngôn ngữ tiếng Việt để nộp cho hw này vào folder submission

tôi chọn phương án 1 nhưng đùng để chữ template
```

- **Output AI:** AI đọc tài liệu HW03 trong `docs/`, README và artefact hiện có, sau đó tạo các file Markdown tiếng Việt trong `submission/`, gồm báo cáo chính, checklist execution, usability report, cross-platform matrix, findings log, AI Critique, AI Audit, git log, Agent Skills demo, README và tài liệu nguồn tham khảo/AI prompts.

### Entry 3

- **Ngày giờ:** 2026-07-28 15:21 +0700
- **Công cụ AI / model:** Codex / GPT-5
- **Prompt:**

```text
Hãy đọc lại kĩ file và sửa lại những file cần nộp chính xác nhất cho tôi
```

- **Output AI:** AI đối chiếu Mục 6, 7 và 10–15 của đề, chỉnh `main_report.md` để có scenario, ba màn hình, checklist execution, usability report và cross-platform report; đồng thời cập nhật các artefact liên quan theo danh sách nội dung phải nộp.

### Entry 4

- **Ngày giờ:** 2026-07-28 15:33 +0700
- **Công cụ AI / model:** Codex / GPT-5
- **Prompt:**

```text
PLEASE IMPLEMENT THIS PLAN:
# Kế hoạch tạo Agent Skill cho Task 1B EMS

Tạo Agent Skill mới tên ems-checklist-execution trong submission/skills/ems-checklist-execution/, có SKILL.md, script build_execution_table.py, agents/openai.yaml, cập nhật agent_skills_demo.md và AI Audit Report, rồi validate theo Test Plan.
```

- **Output AI:** AI tạo skill `ems-checklist-execution`, script sinh bảng Task 1B từ checklist nhóm, metadata cho skill và cập nhật tài liệu demo; sau đó kiểm tra cấu trúc cùng số lượng tiêu chí.

### Entry 5

- **Ngày giờ:** 2026-07-28 15:49 +0700
- **Công cụ AI / model:** Codex / GPT-5
- **Prompt:**

```text
Dùng $ems-checklist-execution để chuẩn bị bảng Task 1B cho Scenario A và hướng dẫn tôi ghi kết quả Passed/Failed/N/A.
```

- **Output AI:** AI dùng checklist nhóm để chuẩn bị bảng Task 1B gồm 51 tiêu chí cho A1, A2 và A3, đồng thời thêm hướng dẫn ghi Passed/Failed/N/A, ghi chú và ảnh minh chứng.

### Entry 6

- **Ngày giờ:** 2026-08-02 22:20 +0700
- **Công cụ AI / model:** Codex / GPT-5
- **Prompt:**

```text
# Rebuild Task 1B — Scenario A

Retain Bảo’s assigned screens: A1 Events list, A2 Add/Edit Event, and A3 Registration & Roles. Re-test all 51 checklist items on each screen using the live prod-dev.ems-fitus.cloud deployment. Log in with the provided Admin account, create one uniquely named draft event, capture evidence, update checklist_execution.md, main_report.md, bug_usability_findings_log.md, READMEs, Google-Form-ready entries, and git_commit_log.md.
```

- **Output AI:** AI điều khiển trình duyệt kiểm thử deployment `https://prod-dev.ems-fitus.cloud/`, tạo và giữ lại một sự kiện nháp riêng, chạy lại 51 tiêu chí trên A1/A2/A3, chụp bộ ảnh `submission/screenshots/task1b/` và đồng bộ checklist, báo cáo, findings, README cùng nhật ký commit.

### Entry 7

- **Ngày giờ:** 2026-08-03 00:21 +0700
- **Công cụ AI / model:** Codex / GPT-5
- **Prompt:**

```text
Hãy thực hiện task 2 phase 1 cho tôi
```

- **Output AI:** AI soạn Task 2 Phase 1 cho Kịch bản A, gồm kịch bản kiểm thử, dữ liệu nhiệm vụ, consent, think-aloud, tiêu chí tuyển người, metrics, SUS, câu hỏi probe và kế hoạch pilot; nội dung được đồng bộ vào các artefact Task 2.

### Entry 8

- **Ngày giờ:** 2026-08-04 19:10 +0700
- **Công cụ AI / model:** Codex / GPT-5
- **Prompt:**

```text
Hãy thực hiện task 03, sau đó tôi sẽ review lại kết quả và chỉnh sửa nếu có sai sót
```

- **Output AI:** AI xây dựng báo cáo Cross-Browser/Cross-Platform cho A1, A2 và A3, bao phủ Windows, macOS, Android; Edge, Safari, Firefox, Samsung Internet, Chrome; và ba loại thiết bị desktop, phone, tablet. AI tổng hợp 15 ô kiểm thử, 15 ảnh có overlay email sinh viên/URL/môi trường, kết quả 12 Đạt và 3 Không đạt, đồng thời ghi ba lỗi tương thích CP-BUG-001–03 vào các artefact liên quan.

### Entry 9

- **Ngày giờ:** 2026-08-06 19:46 +0700
- **Công cụ AI / model:** Codex / GPT-5
- **Prompt:**

```text
• Main report (Markdown + PDF): the chosen scenario, the ≥ 3 screens and why, the checklist-execution results per screen, the Usability Report, and the cross-platform report.
• User-testing evidence: the task scenario, the table of 5 participants (masked contacts), per-session observation notes, the SUS / UEQ-S responses, the metrics table, and screen recordings where available.
• Bug & Usability Findings Log (the aggregated §7 file), consistent with your Google-Form submissions.
• Cross-browser / cross-platform screenshots (with the Student-ID overlay).
• AI Critique and AI Audit Report (Markdown + PDF).
• Git commit log (text file).
• Agent Skills + demo-video links.
• A README.md with the self-assessment table and a test summary.

hãy dựa vào đây check xem còn thiếu gì rồi làm dùm (trừ cái xuất pdf và git commit tôi làm sau)
```

- **Output AI:** AI đối chiếu từng artefact với danh sách nộp bài, bổ sung bảng metrics P1–P5 vào user-testing evidence, tách rõ 10 lỗi/8 usability findings/18 findings trong README, chỉnh self-assessment thành 100/100 cho đúng thành viên, nhúng minh chứng phóng lớn ngoài các bảng và kiểm tra lại checklist, SUS, Google Form timestamps, 15 ô tương thích, đường dẫn ảnh cùng cấu trúc Markdown. PDF và commit cuối được giữ lại cho người dùng thực hiện sau.
