# Báo cáo AI Audit

## 1. Thông tin nhóm

- Họ tên: `Lâm Hữu Khánh`
- MSSV: `23127205`
- Kịch bản: `C - Admin quản lý người dùng`

## 2. Bảng audit

### 2.1. Tóm tắt audit

| STT | Prompt + công cụ                                                                                                                                                                                              | Đánh giá                |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| 1   | Thời gian:`2026-07-28`; Công cụ: `Codex / GPT-5`; Mục đích: triển khai kế hoạch HW03; Prompt: `PLEASE IMPLEMENT THIS PLAN: HW03 GUI Testing Completion Plan ...`                                              | Hữu ích, cần sinh viên kiểm chứng bằng dữ liệu thật |
| 2   | Thời gian:`2026-07-28 23:47 +07`; Công cụ: `Codex / GPT-5`; Mục đích: ghi nhận phiên AI hỗ trợ hoàn thiện HW03 và Việt hóa artifact; Prompt: Dùng $ai-audit-entry để thêm audit entry cho phiên làm việc này. | Hữu ích, nhưng output audit ban đầu cần chỉnh chi tiết hơn |
| 3 | Thời gian: `2026-07-28 23:55 +07`; Công cụ: `Codex / GPT-5`; Mục đích: Ghi nhận phiên chỉnh format AI audit theo phản hồi của sinh viên; Prompt: Dùng $ai-audit-entry để thêm audit entry cho phiên làm việc này. | Đạt yêu cầu format audit sau phản hồi |

### 2.2. Chi tiết audit

### 2.2.1 Entry 1

**Prompt + công cụ:**

**Thời gian:** `2026-07-28`

**Công cụ:** `Codex / GPT-5`

**Mục đích:** Triển khai kế hoạch hoàn thiện HW03 GUI Testing cho Kịch bản C.

**Prompt đầy đủ:**

```text
Hiện tại tôi đang trong quá trình làm bài tập HW3 của môn Software Testing và HW3 này sẽ tập trung vào GUI testing. [$superpowers:using-superpowers](C:\\Users\\lamhu\\.codex\\plugins\\cache\\openai-curated-remote\\superpowers\\6.2.0\\skills\\using-superpowers\\SKILL.md) [$skill-creator](C:\\Users\\lamhu\\.codex\\skills\\.system\\skill-creator\\SKILL.md) Hãy thực hiện đọc yêu cầu và các file liên quan đến HW03 ở thư mục docs/ và về phần task 1A nhóm tôi đã hoàn thành ở phần submission/group và lên 1 kế hoạch hoàn thiện để tôi có thể hoàn thành bài tập này (bao gồm cả phần agent skills)
```

**Kết quả AI:** Tóm tắt artifact của Entry 1:

- Nhóm báo cáo chính: `submission/main_report.md`, `submission/checklist_execution_scenario_c.md`, `submission/bug_usability_findings_log.md`.
- Nhóm user testing: `submission/user-testing/protocol.md`, `participant_table.md`, `pilot_notes.md`, `session_notes/session_notes_template.md`, `raw_scores/sus_scores.md`.
- Nhóm cross-platform: `submission/cross-platform/matrix.md`, `submission/cross-platform/screenshots/README.md`.
- Nhóm AI và đóng gói: `submission/ai_critique.md`, `submission/ai-audit/ai_audit_report.md`, `submission/demo-videos.md`, `submission/git_commit_log.txt`, `submission/validate_hw03_artifacts.py`.
- Nhóm minh chứng checklist: `submission/group/ai_prompts.md`, `submission/group/references.md`, cập nhật heading trong `gui_usability_checklist*.md`.
- Nhóm agent skills: `.agents/skills/ems-gui-checklist-runner/`, `.agents/skills/ems-usability-report-writer/`, `.agents/skills/ems-compatibility-matrix-builder/`, `.agents/skills/ai-audit-entry/`.
- Các phần cần bằng chứng thật vẫn được giữ là `Chờ kiểm thử` hoặc `Chờ điền` để sinh viên tự thu thập.

**Đánh giá:** Hữu ích, nhưng chỉ phù hợp ở mức tạo cấu trúc và artifact nền. Các kết quả này chưa thể xem là kết quả kiểm thử cuối cùng vì chưa có quan sát EMS thật, người tham gia thật, ảnh chụp màn hình thật và timestamp Google Form.

**Lý do:** AI đọc yêu cầu HW03 và tạo được bộ artifact khá đầy đủ cho Kịch bản C, bao gồm report, checklist execution, user testing, cross-platform, findings log, AI critique và agent skills. Tuy nhiên AI không thể tự thay sinh viên thực hiện checklist trên EMS, chạy user testing với 5 người thật hoặc xác nhận lỗi trên nhiều nền tảng. Vì vậy các dòng `Chờ kiểm thử` và `Chờ điền` là cần thiết để tránh tạo dữ liệu giả.

**Sinh viên chỉnh sửa:** Sinh viên cần review lại từng template, thay các dòng `Chờ kiểm thử`/`Chờ điền` bằng dữ liệu thật, bổ sung ảnh chụp màn hình, timestamp Google Form, điểm SUS và kết quả quan sát thực tế. Sinh viên cũng đã yêu cầu Việt hóa toàn bộ artifact và chỉnh lại format AI audit để dễ đọc hơn.

### 2.2.2 Entry 2

**Prompt + công cụ:**

**Thời gian:** `2026-07-28 23:47 +07`

**Công cụ:** `Codex / GPT-5`

**Mục đích:** Ghi nhận phiên AI hỗ trợ hoàn thiện HW03 và Việt hóa artifact.

**Prompt đầy đủ:**

```text
Dùng $ai-audit-entry để thêm audit entry cho phiên làm việc này.
```

**Kết quả AI:** Tóm tắt artifact của Entry 2:

- `submission/ai-audit/ai_audit_report.md`: thêm Entry 2 để ghi nhận phiên AI hỗ trợ.
- `.agents/skills/ai-audit-entry/SKILL.md`: cập nhật hướng dẫn audit theo yêu cầu xuống dòng rõ ràng và prompt đầy đủ.
- `.agents/skills/ai-audit-entry/scripts/append_ai_audit_entry.py`: cập nhật script để entry mới lưu `Thời gian`, `Công cụ`, `Mục đích`, `Prompt đầy đủ` theo block nhiều dòng.
- `.agents/skills/ai-audit-entry/scripts/test_append_ai_audit_entry.py`: cập nhật regression test cho format audit mới.
- Những dữ liệu cần kiểm thử thật vẫn chưa được AI tạo thay và phải do sinh viên tự thu thập.

**Đánh giá:** Hữu ích ở mức ghi nhận phiên làm việc, nhưng output audit ban đầu còn quá chung chung và chưa đủ truy vết artifact.

**Lý do:** Entry 2 đã ghi nhận việc dùng `$ai-audit-entry`, nhưng phần `Kết quả AI` lúc đầu chỉ mô tả tổng quát rằng AI đã tạo scaffold, skill và Việt hóa artifact. Cách ghi đó chưa giúp người chấm biết chính xác file nào được tạo/cập nhật, nên cần chỉnh lại thành danh sách artifact liên quan.

**Sinh viên chỉnh sửa:** Sinh viên phản hồi rằng output audit phải nêu artifact cụ thể. Sau phản hồi, phần `Kết quả AI` của Entry 1 và Entry 2 đã được chỉnh thành các nhóm file/skill có đường dẫn rõ ràng để có thể đối chiếu trong repo.

### 2.2.3 Entry 3

**Prompt + công cụ:**

**Thời gian:** `2026-07-28 23:55 +07`

**Công cụ:** `Codex / GPT-5`

**Mục đích:** Ghi nhận phiên chỉnh format AI audit theo phản hồi của sinh viên

**Prompt đầy đủ:**

```text
Dùng $ai-audit-entry để thêm audit entry cho phiên làm việc này.
```

**Kết quả AI:** Tóm tắt artifact liên quan: cập nhật `submission/ai-audit/ai_audit_report.md` để `Prompt + công cụ` xuống dòng rõ ràng và `Kết quả AI` tóm tắt theo từng entry; cập nhật `.agents/skills/ai-audit-entry/SKILL.md` để yêu cầu prompt đầy đủ và output theo artifact; cập nhật `.agents/skills/ai-audit-entry/scripts/append_ai_audit_entry.py` để entry mới sinh đúng format; cập nhật `.agents/skills/ai-audit-entry/scripts/test_append_ai_audit_entry.py` để kiểm tra format mới; chạy lại validation và regression test.

**Đánh giá:** Đạt yêu cầu format audit sau phản hồi của sinh viên.

**Lý do:** Entry 3 ghi nhận đúng phiên chỉnh format audit. Sau lần chỉnh này, phần `Prompt + công cụ` đã xuống dòng theo các trường `Thời gian`, `Công cụ`, `Mục đích`, `Prompt đầy đủ`; phần `Kết quả AI` đã tóm tắt artifact liên quan thay vì chỉ mô tả chung. Skill và script audit cũng được cập nhật để các entry sau sinh ra theo format mới.

**Sinh viên chỉnh sửa:** Sinh viên đã yêu cầu prompt phải đầy đủ, phần prompt/công cụ/thời gian phải xuống dòng rõ hơn và output AI phải tóm tắt theo từng entry. AI đã cập nhật `submission/ai-audit/ai_audit_report.md`, `.agents/skills/ai-audit-entry/SKILL.md`, script append audit và regression test theo yêu cầu đó.

## 3. Tổng kết độ chính xác AI

- Các template do AI tạo cần được đối chiếu lại với đề HW03 trước khi nộp.
- AI không tạo giả dữ liệu người tham gia, ảnh chụp hoặc timestamp Google Form.
- Các dòng `Chờ kiểm thử` và `Chờ điền` phải được thay bằng bằng chứng thật do sinh viên thu thập.

## 4. Kết luận

AI được dùng để hỗ trợ lập cấu trúc artifact HW03 và tạo agent skills tái sử dụng. Sinh viên vẫn chịu trách nhiệm kiểm thử EMS thật, chạy phiên người dùng thật, submit form, quyết định severity và đảm bảo độ chính xác của báo cáo cuối.

## 5. Disclosure

Sinh viên có sử dụng AI để lập kế hoạch, tạo template artifact, soạn khung báo cáo và tạo agent skills cục bộ.
