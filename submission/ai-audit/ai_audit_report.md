# Báo cáo AI Audit

## 1. Thông tin nhóm

- Họ tên: `Lâm Hữu Khánh`
- MSSV: `23127205`
- Kịch bản: `C - Admin quản lý người dùng`

## 2. Bảng audit

### 2.1. Tóm tắt audit

| STT | Prompt + công cụ                                                                                                                                                                                                                                                                            | Đánh giá                                                     |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| 1   | Thời gian:`2026-07-28`; Công cụ: `Codex / GPT-5`; Mục đích: triển khai kế hoạch HW03; Prompt: `PLEASE IMPLEMENT THIS PLAN: HW03 GUI Testing Completion Plan ...`                                                                                                                            | Hữu ích, cần sinh viên kiểm chứng bằng dữ liệu thật          |
| 2   | Thời gian:`2026-07-28 23:47 +07`; Công cụ: `Codex / GPT-5`; Mục đích: ghi nhận phiên AI hỗ trợ hoàn thiện HW03 và Việt hóa artifact; Prompt: Dùng $ai-audit-entry để thêm audit entry cho phiên làm việc này.                                                                               | Hữu ích, nhưng output audit ban đầu cần chỉnh chi tiết hơn   |
| 3   | Thời gian:`2026-07-28 23:55 +07`; Công cụ: `Codex / GPT-5`; Mục đích: Ghi nhận phiên chỉnh format AI audit theo phản hồi của sinh viên; Prompt: Dùng $ai-audit-entry để thêm audit entry cho phiên làm việc này.                                                                            | Đạt yêu cầu format audit sau phản hồi                        |
| 4   | Thời gian:`2026-08-02 00:35 +07`; Công cụ: `Codex / GPT-5`; Mục đích: AI-assisted audit cho C1 Users Management list; Prompt: Hãy dùng skill EMS GUI Checklist Runner để audit C1 Users Management list, ghi checklist execution, findings, screenshots và phần cần sinh viên validate lại. | Hữu ích cho draft C1, cần sinh viên verify lại bằng EMS thật |
| 5 | Thời gian: `2026-08-02 14:32 +07`; Công cụ: `Codex / GPT-5`; Mục đích: Ghi nhận phiên AI hỗ trợ kiểm thử C2, cập nhật finding log và tạo/cập nhật skill EMS finding log; Prompt: Hãy thực hiện dùng skill EMS GUI Checklist Runner để thực hiện cho màn hình C2; cập nhật domain https://prod-dev.ems-fitus.cloud/dashboard; dùng Playwright đã có sẵn để check sc... | Hữu ích cho việc chuẩn hóa artifact C2, cần sinh viên kiểm chứng và submit form |
| 6 | Thời gian: `2026-08-02 15:45 +07`; Công cụ: `Codex / GPT-5`; Mục đích: AI-assisted audit cho C3 Block-Unblock va Reset Password dialogs; Prompt: Ok hãy tiếp tục thực thi kiểm thử cho screen c3 admin manage user Block-Unblock and Reset-Password dialogs — confirmation + audit; Sau đó sinh viên phản biện: C-F014 không có bằ... | Hữu ích cho draft C3, cần sinh viên đối chiếu lại ảnh và submit form |

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

### 2.2.4 Entry 4

**Prompt + công cụ:**

**Thời gian:** `2026-08-02 00:35 +07`

**Công cụ:** `Codex / GPT-5`

**Mục đích:** AI-assisted audit cho C1 Users Management list

**Prompt đầy đủ:**

```text
Hãy dùng skill EMS GUI Checklist Runner để thực hiện AI-assisted audit cho màn hình C1 Users Management list trên EMS `https://prod-dev.ems-fitus.cloud/dashboard`. Dùng Playwright/browser automation để đăng nhập bằng admin account trong đề, quan sát màn hình Users list, chụp screenshot working evidence và chỉ lưu screenshot fail thật vào `submission/screenshots/checklist-failures/`.

Đọc checklist nguồn `submission/group/gui_usability_checklist_final.md`, điền phần C1 trong `submission/checklist_execution_scenario_c.md` theo đúng yêu cầu đề: chỉ dùng `Pass` hoặc `Fail`, không dùng `N/A` cho bản final. Với item không có form/control trực tiếp trên C1 thì đánh `Pass` kèm ghi chú rằng không phát hiện lỗi trong phạm vi C1 hoặc sẽ kiểm sâu ở C2/C3 nếu liên quan.

Cập nhật file execution theo format tách từng màn hình: thêm phần phạm vi màn hình kiểm thử cho C1/C2/C3, giữ bảng C1 gồm các cột `Màn hình`, `Checklist ID`, `Kết quả`, `Ghi chú`, `Finding`. Cột `Finding` chỉ reference tới bug trong file log bằng relative path từ file execution, ví dụ `[C-F001](bug_usability_findings_log.md)`.

Nếu phát hiện lỗi C1, ghi vào `submission/bug_usability_findings_log.md` với ID `C-F001`, `C-F002`, gồm màn hình, loại lỗi, severity, steps, expected vs actual, suggested fix, screenshot ref và `Timestamp form` để `Chờ sinh viên submit`. Không tự submit Google Form.

Áp dụng các chỉnh sửa đã verify trong phiên: không ghi bug cho icon filter thiếu tooltip nếu icon nằm cạnh tiêu đề cột đủ rõ ngữ cảnh; giữ `IA-01-07` là `Pass`. Ghi nhận hai finding nháp cho C1: mobile overflow trên iPhone SE 375x667 và empty state search không có nút clear/reset. Sau khi sửa, chạy validator để kiểm tra artifact, rồi báo lại để sinh viên tự mở EMS validate Pass/Fail, severity, screenshot và submit form sau.
```

**Kết quả AI:** Tóm tắt artifact liên quan:

- Dùng browser automation/Playwright sau khi sinh viên cài Playwright để đăng nhập EMS tại `https://prod-dev.ems-fitus.cloud/dashboard` bằng tài khoản admin trong đề và quan sát màn hình C1 Users Management list.
- Tạo/thu thập working screenshots cho C1 như overview, role/status filter popover, search result, search empty state và ảnh failure trong `submission/screenshots/checklist-failures/`.
- Dùng `submission/group/gui_usability_checklist_final.md` làm checklist nguồn và điền nháp C1 trong `submission/checklist_execution_scenario_c.md` theo trạng thái `Pass`/`Fail`.
- Cập nhật phần "Phạm vi màn hình kiểm thử" để C1/C2/C3 rõ hơn; riêng C1 mô tả phạm vi gồm search, filter Vai trò/Trạng thái, bảng user, Export/Add User, Edit/Delete và phân trang.
- Sau phản hồi của sinh viên, bỏ `N/A`, giữ `IA-01-07` là `Pass` vì icon filter nằm cạnh tiêu đề cột đủ ngữ cảnh; lỗi tooltip filter chỉ được xem là improvement, không ghi finding.
- Ghi 2 finding nháp cho C1 trong `submission/bug_usability_findings_log.md`: `C-F001` mobile overflow trên iPhone SE 375x667 và `C-F002` empty state thiếu hành động clear/reset.
- Sửa cột `Finding` trong execution thành reference tương đối tới `bug_usability_findings_log.md`, ví dụ `[C-F001](bug_usability_findings_log.md)`.
- Chạy `python submission/validate_hw03_artifacts.py` sau các lần chỉnh; validator báo `Kiểm tra artifact HW03 đã đạt`.
- Các finding C1 vẫn là draft do AI hỗ trợ kiểm thử; sinh viên cần mở EMS, đối chiếu screenshot, xác nhận Pass/Fail/severity và submit Google Form sau, rồi điền timestamp.

**Đánh giá:** Hữu ích cho việc tạo bản nháp kiểm thử C1 có cấu trúc, nhưng chưa thể xem là kết quả cuối cùng nếu sinh viên chưa tự verify lại trên EMS thật.

**Lý do:** AI giúp đọc checklist nguồn, chạy quan sát bằng browser automation, phát hiện và ghi lại các vấn đề có minh chứng như mobile overflow và empty state thiếu hành động clear/reset. AI cũng hỗ trợ chuẩn hóa artifact: tách bảng theo màn hình, bỏ trạng thái `N/A`, nối `Finding` tới bug log bằng relative path và chạy validator. Tuy nhiên AI vẫn có thể đánh giá sai mức độ usability nếu thiếu ngữ cảnh người dùng; ví dụ sinh viên đã phản biện trường hợp icon filter thiếu tooltip và quyết định giữ `IA-01-07` là `Pass`.

**Sinh viên chỉnh sửa:** Sinh viên đã kiểm tra lại các nhận định của AI, yêu cầu chỉ dùng `Pass`/`Fail`, chỉnh cách reference finding, làm rõ phạm vi màn hình C1/C2/C3, phản biện bug tooltip filter và giữ lại các finding phù hợp hơn cho C1. Trước khi nộp, sinh viên cần mở EMS để xác nhận lại C1, đối chiếu ảnh fail, submit Google Form cho từng bug hợp lệ và điền timestamp vào bug log.

### 2.2.5 Entry 5

**Prompt + công cụ:**

**Thời gian:** `2026-08-02 14:32 +07`

**Công cụ:** `Codex / GPT-5`

**Mục đích:** Ghi nhận phiên AI hỗ trợ kiểm thử C2, cập nhật finding log và tạo/cập nhật skill EMS finding log

**Prompt đầy đủ:**

```text
Hãy thực hiện dùng skill EMS GUI Checklist Runner để thực hiện cho màn hình C2; cập nhật domain https://prod-dev.ems-fitus.cloud/dashboard; dùng Playwright đã có sẵn để check screen C2; phân loại và ghi các lỗi usability/bug người dùng phát hiện như password validation tiếng Anh khi đang dùng VI, email @g vẫn thành công, phone thiếu gợi ý/cho nhập chữ, role dropdown chọn placeholder, email đã xóa vẫn báo already use, member code duplicate hiển thị tiếng Anh; chỉnh bug_usability_findings_log.md để có bảng tổng hợp ở đầu, chi tiết từng finding không dùng bảng mà viết từng mục, ảnh hiển thị trực tiếp, bước tái hiện xuống dòng từng bước, ảnh giữ kích thước bình thường; tạo/cập nhật skill ems-finding-log-writer bằng skill-creator.
```

**Kết quả AI:** Tóm tắt artifact hiện hành:

- `submission/checklist_execution_scenario_c.md`: cập nhật execution cho C2 theo checklist GUI usability, dùng `Pass`/`Fail` và link finding về `bug_usability_findings_log.md`.
- `submission/bug_usability_findings_log.md`: cập nhật finding log hiện hành với bảng tổng hợp ở đầu và chi tiết các finding C-F001 đến C-F011 theo từng mục, không dùng bảng chi tiết.
- `submission/screenshots/checklist-failures/`: dùng ảnh minh chứng hiện hành cho C-F001 đến C-F011 và hiển thị trực tiếp trong finding log bằng thẻ `<img>` ở kích thước bình thường.
- `.agents/skills/ems-finding-log-writer/`: tạo và cập nhật skill local để chuẩn hóa cách ghi finding log, quy tắc ảnh, cách tách bước tái hiện và cách nối checklist fail với finding log.
- `.gitignore`: thêm exception để tracking skill `ems-finding-log-writer`.
- `README.md`, `docs/`, `submission/HW03_step_by_step_guide.md`, `submission/main_report.md`: cập nhật URL SUT hiện hành thành `https://prod-dev.ems-fitus.cloud/dashboard`.
- `submission/validate_hw03_artifacts.py`: được chạy lại sau khi chỉnh artifact; validator báo `Kiểm tra artifact HW03 đã đạt`.

**Đánh giá:** Hữu ích cho việc chuẩn hóa artifact C2, nhưng cần sinh viên kiểm chứng lại trên EMS thật và submit Google Form trước khi xem là kết quả cuối.

**Lý do:** AI hỗ trợ tổng hợp các lỗi đã quan sát/thảo luận, cập nhật checklist execution, finding log, ảnh minh chứng và skill tái sử dụng theo format nộp bài. Output phù hợp ở mức tổ chức artifact và diễn đạt finding, nhưng timestamp Google Form, quyết định cuối về severity và tính đúng của từng lỗi vẫn phụ thuộc vào kiểm chứng của sinh viên.

**Sinh viên chỉnh sửa:** Sinh viên đã phản biện và chỉnh hướng nhiều điểm trong phiên: yêu cầu không bịa audit, phân biệt bug và usability finding, quyết định tách/ghép finding cho password/phone/role/member code, yêu cầu bỏ bảng chi tiết finding, tách bước tái hiện xuống dòng từng bước, hiển thị ảnh trực tiếp và giữ ảnh ở kích thước bình thường. Sinh viên vẫn cần tự submit Google Form và điền timestamp tương ứng.

### 2.2.6 Entry 6

**Prompt + công cụ:**

**Thời gian:** `2026-08-02 15:45 +07`

**Công cụ:** `Codex / GPT-5`

**Mục đích:** AI-assisted audit cho C3 Block-Unblock va Reset Password dialogs

**Prompt đầy đủ:**

```text
Ok hãy tiếp tục thực thi kiểm thử cho screen c3 admin manage user Block-Unblock and Reset-Password dialogs — confirmation + audit; Sau đó sinh viên phản biện: C-F014 không có bằng chứng đủ rõ nên gỡ; câu Active mặc định chỉ đúng với user đang Active nên chỉnh lại chưa kết luận user Inactive; Block/Unblock hiện tại có thể là Active/Inactive nên cần chỉnh C-F012 từ thiếu hoàn toàn thành wording/entry point mơ hồ và thiếu Reset Password action; hỏi ảnh C-F012/C-F013 nên chụp gì.
```

**Kết quả AI:** Tóm tắt artifact hiện hành:

- `submission/checklist_execution_scenario_c.md`: cập nhật phần C3 từ `Chờ kiểm thử` sang `Pass`/`Fail`, nối các checklist item fail tới finding hợp lệ trong `bug_usability_findings_log.md`.
- `submission/bug_usability_findings_log.md`: giữ lại `C-F012` và `C-F013` cho C3; chỉnh `C-F012` thành usability finding về Block/Unblock mơ hồ qua Active/Inactive và thiếu Reset Password action; giữ `C-F013` cho vấn đề Active checkbox thiếu giải thích/confirmation riêng.
- `submission/bug_usability_findings_log.md`: gỡ `C-F014` vì sinh viên phản biện rằng chưa có bằng chứng đủ độc lập để tạo finding riêng.
- `submission/screenshots/checklist-failures/`: thêm ảnh minh chứng C3 cho `C-F012-01.png` và `C-F013.png`; ảnh `C-F014.png` không còn được reference trong finding log sau khi gỡ finding.
- `submission/screenshots/`: thêm ảnh quan sát Playwright cho C3 như `c3-users-actions-overview.png`, `c3-edit-dialog-actions.png`, `c3-delete-confirmation.png`.
- `submission/validate_hw03_artifacts.py`: được chạy lại sau các lần chỉnh; validator báo `Kiểm tra artifact HW03 đã đạt`.

**Đánh giá:** Hữu ích cho việc tạo draft C3 và chuẩn hóa finding, nhưng cần sinh viên đối chiếu lại trên EMS thật, chụp đúng ảnh cuối cho C-F012/C-F013 và submit Google Form trước khi xem là kết quả cuối.

**Lý do:** AI hỗ trợ chạy Playwright để quan sát Users Management, mở Edit/Delete dialog, chuyển C3 từ trạng thái chờ sang bảng Pass/Fail và viết finding theo format hiện hành. Tuy nhiên ban đầu AI đã suy rộng một finding audit/ngôn ngữ `C-F014` chưa đủ bằng chứng và khẳng định hơi rộng về Active cho cả user Active/Inactive; các điểm này cần sinh viên phản biện để kết quả chính xác hơn.

**Sinh viên chỉnh sửa:** Sinh viên đã kiểm tra lại và yêu cầu gỡ `C-F014` vì không có lỗi/bằng chứng độc lập; chỉnh câu Active mặc định để chỉ kết luận trên user Active đã quan sát, chưa kết luận user Inactive; làm rõ khả năng Active/Inactive chính là Block/Unblock hiện tại; yêu cầu chỉnh `C-F012` từ bug thiếu chức năng hoàn toàn thành usability finding về wording/entry point mơ hồ và thiếu Reset Password action. Sinh viên cũng xác định ảnh tốt nhất cho `C-F012` là list/Edit dialog thể hiện không có Reset Password và Block/Unblock không gọi tên rõ, còn `C-F013` là Edit dialog khi bỏ tick Active nhưng chưa có warning/confirmation.

## 3. Tổng kết độ chính xác AI

- Các template do AI tạo cần được đối chiếu lại với đề HW03 trước khi nộp.
- AI không tạo giả dữ liệu người tham gia, ảnh chụp hoặc timestamp Google Form.
- Các dòng `Chờ kiểm thử` và `Chờ điền` phải được thay bằng bằng chứng thật do sinh viên thu thập.

## 4. Kết luận

AI được dùng để hỗ trợ lập cấu trúc artifact HW03 và tạo agent skills tái sử dụng. Sinh viên vẫn chịu trách nhiệm kiểm thử EMS thật, chạy phiên người dùng thật, submit form, quyết định severity và đảm bảo độ chính xác của báo cáo cuối.

## 5. Disclosure

Sinh viên có sử dụng AI để lập kế hoạch, tạo template artifact, soạn khung báo cáo và tạo agent skills cục bộ.
