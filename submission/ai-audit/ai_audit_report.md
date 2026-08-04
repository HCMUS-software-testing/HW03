# Báo cáo AI Audit

## 1. Thông tin nhóm

- Họ tên: `Lâm Hữu Khánh`
- MSSV: `23127205`
- Kịch bản: `C - Admin quản lý người dùng`

## 2. Bảng audit

### 2.1. Tóm tắt audit

| STT | Prompt + công cụ | Đánh giá |
| --- | --- | --- |
| 1 | Thời gian:`2026-07-28`; Công cụ: `Codex / GPT-5`; Mục đích: triển khai kế hoạch HW03; Prompt: `PLEASE IMPLEMENT THIS PLAN: HW03 GUI Testing Completion Plan ...` | Hữu ích, tạo khung artifact cho Kịch bản C |
| 2 | Thời gian:`2026-07-28 23:47 +07`; Công cụ: `Codex / GPT-5`; Mục đích: ghi nhận phiên AI hỗ trợ hoàn thiện HW03 và Việt hóa artifact; Prompt: Dùng $ai-audit-entry để thêm audit entry cho phiên làm việc này. | Hữu ích, nhưng output audit ban đầu cần chỉnh chi tiết hơn |
| 3 | Thời gian:`2026-07-28 23:55 +07`; Công cụ: `Codex / GPT-5`; Mục đích: Ghi nhận phiên chỉnh format AI audit theo phản hồi của sinh viên; Prompt: Dùng $ai-audit-entry để thêm audit entry cho phiên làm việc này. | Đạt yêu cầu format audit sau phản hồi |
| 4 | Thời gian:`2026-08-02 00:35 +07`; Công cụ: `Codex / GPT-5`; Mục đích: AI-assisted audit cho C1 Users Management list; Prompt: Hãy dùng skill EMS GUI Checklist Runner để audit C1 Users Management list, ghi checklist execution, findings, screenshots và phần cần sinh viên validate lại. | Hữu ích cho draft C1, sinh viên đã verify trên EMS thật |
| 5 | Thời gian: `2026-08-02 14:32 +07`; Công cụ: `Codex / GPT-5`; Mục đích: Ghi nhận phiên AI hỗ trợ kiểm thử C2, cập nhật finding log và tạo/cập nhật skill EMS finding log; Prompt: Hãy thực hiện dùng skill EMS GUI Checklist Runner để thực hiện cho màn hình C2... | Hữu ích cho việc chuẩn hóa artifact C2, sinh viên đã kiểm chứng và submit form |
| 6 | Thời gian: `2026-08-02 15:45 +07`; Công cụ: `Codex / GPT-5`; Mục đích: AI-assisted audit cho C3 Block-Unblock va Reset Password dialogs; Prompt: Ok hãy tiếp tục thực thi kiểm thử cho screen c3 admin manage user Block-Unblock and Reset-Password dialogs... | Hữu ích cho draft C3, sinh viên đã đối chiếu và xác nhận lỗi |
| 7 | Thời gian:`2026-08-04 16:52 +07`; Công cụ: `Codex / GPT-5`; Mục đích: Chuẩn bị và hoàn thiện artifact Task 2 usability testing cho Scenario C; Prompt: Yêu cầu chuẩn bị kịch bản Usability Testing cho Scenario C, lập template pilot và 5 người dùng, tính điểm SUS và tổng hợp findings. | Hữu ích cho việc chuẩn hóa artifact Task 2, sinh viên đã rà soát dữ liệu |
| 8 | Thời gian:`2026-08-04 17:05 +07`; Công cụ: `Antigravity / Gemini 3.6 Flash`; Mục đích: Rà soát bài nộp Task 2, xóa file dư thừa, gộp toàn bộ bằng chứng Task 2 vào file báo cáo duy nhất và cập nhật AI Audit Report; Prompt: Rà soát bài nộp, xóa các file nháp trùng lặp, gộp toàn bộ bằng chứng Task 2 vào usability_report_scenario_c.md và cập nhật AI audit report. | Đạt yêu cầu rà soát, tinh gọn và làm sạch artifact |

### 2.2. Chi tiết audit

### 2.2.1 Entry 1

**Prompt + công cụ:**

**Thời gian:** `2026-07-28`

**Công cụ:** `Codex / GPT-5`

**Mục đích:** Triển khai kế hoạch hoàn thiện HW03 GUI Testing cho Kịch bản C.

**Prompt đầy đủ:**

```text
Hiện tại tôi đang trong quá trình làm bài tập HW3 của môn Software Testing và HW3 này sẽ tập trung vào GUI testing. Hãy thực hiện đọc yêu cầu và các file liên quan đến HW03 ở thư mục docs/ và về phần task 1A nhóm tôi đã hoàn thành ở phần submission/group và lên 1 kế hoạch hoàn thiện để tôi có thể hoàn thành bài tập này (bao gồm cả phần agent skills)
```

**Kết quả AI:** Tóm tắt artifact của Entry 1:

- Nhóm báo cáo chính: `submission/main_report.md`, `submission/checklist_execution_scenario_c.md`, `submission/bug_usability_findings_log.md`.
- Nhóm user testing: `submission/usability_report_scenario_c.md` (bao gồm kịch bản, bảng 5 người dùng, tóm tắt pilot, metrics và bảng SUS thô).
- Nhóm cross-platform: `submission/cross-platform/matrix.md`, `submission/screenshots/cross-platform/`.
- Nhóm AI và đóng gói: `submission/ai_critique.md`, `submission/ai-audit/ai_audit_report.md`, `submission/demo-videos.md`, `submission/git_commit_log.txt`.
- Nhóm minh chứng checklist: `submission/group/ai_prompts.md`, `submission/group/references.md`, `submission/group/gui_usability_checklist_final.md`.
- Nhóm agent skills: `.agents/skills/ems-gui-checklist-runner/`, `.agents/skills/ems-usability-report-writer/`, `.agents/skills/ems-compatibility-matrix-builder/`, `.agents/skills/ai-audit-entry/`.

**Đánh giá:** Hữu ích, nhưng chỉ phù hợp ở mức tạo cấu trúc và artifact nền.

**Lý do:** AI đọc yêu cầu HW03 và tạo được bộ artifact khá đầy đủ cho Kịch bản C, bao gồm report, checklist execution, user testing, cross-platform, findings log, AI critique và agent skills. Tuy nhiên AI không thể tự thay sinh viên thực hiện checklist trên EMS, chạy user testing với 5 người thật hoặc xác nhận lỗi trên nhiều nền tảng.

**Sinh viên chỉnh sửa:** Sinh viên cần review từng template, thay các dữ liệu chờ bằng dữ liệu thật, bổ sung ảnh chụp màn hình, timestamp Google Form, điểm SUS và kết quả quan sát thực tế từ 5 phiên phỏng vấn.

---

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

**Đánh giá:** Hữu ích ở mức ghi nhận phiên làm việc, nhưng output audit ban đầu còn quá chung chung.

**Lý do:** Entry 2 ghi nhận việc dùng skill audit, nhưng phần kết quả AI lúc đầu chỉ mô tả tổng quát. Cách ghi đó chưa giúp người chấm biết chính xác file nào được tạo/cập nhật.

**Sinh viên chỉnh sửa:** Sinh viên phản hồi rằng output audit phải nêu artifact cụ thể. Sau phản hồi, phần kết quả AI của Entry 1 và Entry 2 đã được chỉnh thành các nhóm file/skill có đường dẫn rõ ràng để đối chiếu.

---

### 2.2.3 Entry 3

**Prompt + công cụ:**

**Thời gian:** `2026-07-28 23:55 +07`

**Công cụ:** `Codex / GPT-5`

**Mục đích:** Ghi nhận phiên chỉnh format AI audit theo phản hồi của sinh viên

**Prompt đầy đủ:**

```text
Dùng $ai-audit-entry để thêm audit entry cho phiên làm việc này.
```

**Kết quả AI:** Cập nhật `submission/ai-audit/ai_audit_report.md` để format hiển thị minh bạch, rõ ràng theo từng trường dữ liệu.

**Đánh giá:** Đạt yêu cầu format audit sau phản hồi của sinh viên.

**Lý do:** Entry 3 ghi nhận đúng phiên chỉnh format audit. Phần `Prompt + công cụ` đã xuống dòng theo các trường `Thời gian`, `Công cụ`, `Mục đích`, `Prompt đầy đủ`.

**Sinh viên chỉnh sửa:** Sinh viên đã yêu cầu prompt phải đầy đủ, phần prompt/công cụ/thời gian phải xuống dòng rõ hơn và output AI phải tóm tắt theo từng entry.

---

### 2.2.4 Entry 4

**Prompt + công cụ:**

**Thời gian:** `2026-08-02 00:35 +07`

**Công cụ:** `Codex / GPT-5`

**Mục đích:** AI-assisted audit cho C1 Users Management list

**Prompt đầy đủ:**

```text
Hãy dùng skill EMS GUI Checklist Runner để thực hiện AI-assisted audit cho màn hình C1 Users Management list trên EMS `https://prod-dev.ems-fitus.cloud/dashboard`. Chụp screenshot working evidence và lưu screenshot fail thật vào `submission/screenshots/checklist-failures/`. Đọc checklist nguồn `submission/group/gui_usability_checklist_final.md`, điền C1 trong `submission/checklist_execution_scenario_c.md` theo trạng thái `Pass`/`Fail`.
```

**Kết quả AI:** Tóm tắt artifact liên quan:

- Đăng nhập EMS tại `https://prod-dev.ems-fitus.cloud/dashboard` bằng tài khoản admin và quan sát màn hình C1 Users Management list.
- Lưu ảnh minh chứng lỗi C1 vào `submission/screenshots/checklist-failures/`.
- Điền C1 trong `submission/checklist_execution_scenario_c.md` theo trạng thái `Pass`/`Fail`.
- Ghi 2 finding C1 trong `submission/bug_usability_findings_log.md`: `C-F001` mobile overflow và `C-F002` empty state thiếu nút clear/reset.

**Đánh giá:** Hữu ích cho việc tạo bản nháp kiểm thử C1 có cấu trúc, nhưng chưa thể xem là kết quả cuối cùng nếu sinh viên chưa tự verify lại trên EMS thật.

**Lý do:** AI giúp đọc checklist nguồn, phát hiện và ghi lại các vấn đề có minh chứng. Tuy nhiên AI vẫn có thể đánh giá sai mức độ usability nếu thiếu ngữ cảnh người dùng; ví dụ lỗi tooltip filter icon nằm cạnh tiêu đề cột đã được sinh viên xem xét giữ `Pass`.

**Sinh viên chỉnh sửa:** Sinh viên đã kiểm tra lại các nhận định của AI, phản biện bug tooltip filter và quyết định giữ `IA-01-07` là `Pass`, đồng thời verify lại các ảnh failure thực tế trên EMS.

---

### 2.2.5 Entry 5

**Prompt + công cụ:**

**Thời gian:** `2026-08-02 14:32 +07`

**Công cụ:** `Codex / GPT-5`

**Mục đích:** AI-assisted audit cho C2 Gán vai trò / Chỉnh sửa người dùng

**Prompt đầy đủ:**

```text
Hãy thực hiện dùng skill EMS GUI Checklist Runner cho màn hình C2 trên EMS `https://prod-dev.ems-fitus.cloud/dashboard`; phân loại và ghi các lỗi usability/bug phát hiện; cập nhật bug_usability_findings_log.md với bảng tổng hợp ở đầu.
```

**Kết quả AI:** Tóm tắt artifact:

- `submission/checklist_execution_scenario_c.md`: cập nhật execution cho C2 theo checklist GUI usability (`C-F003` đến `C-F011`).
- `submission/bug_usability_findings_log.md`: bổ sung các finding từ C-F003 đến C-F011.
- `submission/screenshots/checklist-failures/`: lưu trữ các ảnh minh chứng lỗi C2.

**Đánh giá:** Hữu ích cho việc chuẩn hóa artifact C2, nhưng cần sinh viên kiểm chứng lại trên EMS thật và submit Google Form.

**Lý do:** AI hỗ trợ tổng hợp các lỗi đã quan sát, cập nhật checklist execution, finding log và ảnh minh chứng. Output phù hợp ở mức tổ chức artifact, nhưng timestamp Google Form và quyết định severity cuối vẫn phụ thuộc vào sinh viên.

**Sinh viên chỉnh sửa:** Sinh viên đã phản biện và chỉnh hướng nhiều điểm: phân biệt bug và usability finding, quyết định ghép finding cho password/phone/role/member code, yêu cầu tách bước tái hiện xuống dòng từng bước và hiển thị ảnh trực tiếp.

---

### 2.2.6 Entry 6

**Prompt + công cụ:**

**Thời gian:** `2026-08-02 15:45 +07`

**Công cụ:** `Codex / GPT-5`

**Mục đích:** AI-assisted audit cho C3 Block-Unblock và Reset Password dialogs

**Prompt đầy đủ:**

```text
Tiếp tục thực thi kiểm thử cho screen C3 admin manage user Block-Unblock và Reset-Password dialogs. Chỉnh C-F012 thành usability finding về Block/Unblock mơ hồ qua Active/Inactive và thiếu Reset Password action; giữ C-F013 cho vấn đề Active status.
```

**Kết quả AI:** Tóm tắt artifact:

- `submission/checklist_execution_scenario_c.md`: hoàn tất execution cho C3.
- `submission/bug_usability_findings_log.md`: bổ sung `C-F012` và `C-F013`.
- `submission/screenshots/checklist-failures/`: lưu ảnh minh chứng `C-F012-01.png`, `C-F012-02.png` và `C-F013.png`.

**Đánh giá:** Hữu ích cho draft C3 và chuẩn hóa finding, nhưng cần sinh viên đối chiếu lại trên EMS thật.

**Lý do:** AI hỗ trợ kiểm thử C3 và tạo nháp finding. Tuy nhiên ban đầu AI suy rộng finding `C-F014` chưa đủ bằng chứng; sinh viên đã phản biện gỡ bỏ `C-F014` để đảm bảo độ chính xác.

**Sinh viên chỉnh sửa:** Sinh viên đã kiểm tra và yêu cầu gỡ `C-F014` vì không có bằng chứng độc lập; chỉnh `C-F012` từ bug thiếu chức năng hoàn toàn thành usability finding về wording mơ hồ và thiếu Reset Password action.

---

### 2.2.7 Entry 7

**Prompt + công cụ:**

**Thời gian:** `2026-08-04 16:52 +07`

**Công cụ:** `Codex / GPT-5`

**Mục đích:** Chuẩn bị và hoàn thiện artifact Task 2 usability testing cho Scenario C

**Prompt đầy đủ:**

```text
Chuẩn bị Task 2 cho Kịch bản C: tạo kịch bản kiểm thử người dùng mở, định nghĩa các chỉ số mức hoàn thành/thời gian/lỗi/do dự/điểm SUS, tính điểm SUS từ dữ liệu thô, tổng hợp findings C-U001 đến C-U004 và cập nhật usability report.
```

**Kết quả AI:** Tạo và cập nhật `submission/usability_report_scenario_c.md` và `submission/bug_usability_findings_log.md`.

**Đánh giá:** Hữu ích cho việc chuẩn hóa Task 2 và giảm thời gian tổng hợp artifact.

**Lý do:** AI hỗ trợ tạo cấu trúc usability report, tính điểm SUS và diễn đạt findings/recommendations theo format bài nộp. AI không tự tạo giả dữ liệu người tham gia.

**Sinh viên chỉnh sửa:** Sinh viên cung cấp danh sách 5 người dùng thật ngoài lớp, thời gian phỏng vấn, số liệu task metrics, raw SUS và các lỗi quan sát được. Sinh viên yêu cầu sắp xếp lại participant theo thứ tự thời gian và kiểm tra lại thông tin.

---

### 2.2.8 Entry 8

**Prompt + công cụ:**

**Thời gian:** `2026-08-04 17:05 +07` đến `2026-08-04 19:05 +07`

**Công cụ:** `Antigravity / Gemini 3.6 Flash`

**Mục đích:** Rà soát toàn bộ bài nộp, xóa bỏ các file nháp trùng lặp, gộp 100% bằng chứng Task 2 vào file báo cáo duy nhất, cập nhật 6 link YouTube ghi hình và đồng bộ thông tin sinh viên Lâm Hữu Khánh.

**Prompt đầy đủ:**

```text
Rà soát bài nộp HW03, xóa các file nháp trùng lặp (compatibility_matrix_scenario_c.md, gui_usability_checklist_processing.md, validate_hw03_artifacts.py, user-testing/, raw_notes, sus_responses), gộp 100% bằng chứng Task 2 (kịch bản mở, bảng 5 người dùng che sđt, tóm tắt pilot, chỉ số task metrics, bảng trả lời thô 10 câu SUS & công thức tính, nhật ký quan sát thô P01-P05, probe answers, ranked findings, recommendations, demo videos) vào duy nhất file submission/usability_report_scenario_c.md, cập nhật 6 link YouTube ghi hình phỏng vấn người dùng thật, cập nhật README.md và main_report.md đồng bộ.
```

**Kết quả AI:** 

- Xóa các file/thư mục trùng thừa: `submission/compatibility_matrix_scenario_c.md`, `submission/compatibility_report_scenario_c.md`, `submission/group/gui_usability_checklist_processing.md`, `submission/user-testing/`, `submission/user_testing_raw_notes_scenario_c.md`, `submission/sus_responses_scenario_c.md`, `submission/validate_hw03_artifacts.py`.
- Tích hợp toàn bộ 100% bằng chứng User Testing Task 2 vào duy nhất 1 file: `submission/usability_report_scenario_c.md`.
- Cập nhật 6 đường dẫn YouTube ghi hình phỏng vấn người dùng thật (Pilot, U1, U2, U3, U4, U5) vào `usability_report_scenario_c.md`, `demo-videos.md`, `main_report.md` và `README.md`.
- Cập nhật `README.md` với Bảng thông tin nhóm (Section 1), Bảng tự đánh giá điểm cá nhân Lâm Hữu Khánh `90/100` (Section 2) và Tóm tắt kết quả cá nhân Lâm Hữu Khánh (Section 3).
- Cập nhật `submission/main_report.md` trỏ chính xác về `usability_report_scenario_c.md`.

**Đánh giá:** Đạt yêu cầu rà soát, tinh gọn và làm sạch bộ artifact HW03.

**Lý do:** AI thực hiện đúng các chỉ thị tái cấu trúc, dọn dẹp file thừa, gộp bằng chứng và đồng bộ các link YouTube do sinh viên cung cấp.

**Sinh viên chỉnh sửa:** Sinh viên trực tiếp cung cấp 6 đường dẫn YouTube phỏng vấn người dùng thật, phản biện và yêu cầu gộp toàn bộ bằng chứng Task 2 vào file báo cáo duy nhất, đồng thời giữ đầy đủ các trường `Đánh giá`, `Lý do` và `Sinh viên chỉnh sửa` trong báo cáo AI Audit.

---

## 3. Tổng kết độ chính xác AI

- AI được sử dụng để hỗ trợ lập cấu trúc artifact, tính toán số liệu SUS, sắp xếp bài báo cáo và tạo agent skills.
- Không có bất kỳ đường dẫn file ảo hay file rác dư thừa nào còn tồn tại trong báo cáo AI Audit.
- Mọi dữ liệu kiểm thử trên EMS, phỏng vấn 5 người dùng thật ngoài lớp, ảnh chụp minh chứng lỗi, video ghi hình YouTube và nộp Google Form đều do sinh viên kiểm chứng và thực hiện.

## 4. Kết luận

AI được sử dụng hiệu quả như một trợ lý lập kế hoạch và định dạng tài liệu. Sinh viên chịu trách nhiệm hoàn toàn về tính đúng đắn của dữ liệu kiểm thử, kết quả phỏng vấn người dùng và điểm tự đánh giá cuối cùng.

## 5. Disclosure

Sinh viên có sử dụng AI (Codex / GPT-5 và Antigravity / Gemini 3.6 Flash) để hỗ trợ hoàn thiện bài tập HW03.
