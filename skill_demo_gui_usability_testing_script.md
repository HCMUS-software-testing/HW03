# Kịch Bản Demo Skill `gui-usability-testing`

## 1. Mục tiêu video

Video này dùng để demo rằng skill `gui-usability-testing` có thể hỗ trợ end-to-end cho bài HW03 trên EMS web hiện tại, theo đúng flow Scenario D:

- `D1`: User tạo support request
- `D2`: User xem danh sách / chi tiết request của mình
- `D3`: Admin tìm và xử lý support requests

Video nên cho thấy 3 ý:

1. Skill hiểu đúng scope, URL, role và artifact output.
2. Skill có thể hướng dẫn hoặc sinh artifact cho từng task.
3. Skill có thể gom findings thành một findings log thống nhất.

---

## 2. Cách quay nên dùng

Nên quay theo kiểu `1 video liên tục`, dài khoảng `8-12 phút`.

Flow khuyến nghị:

1. Mở folder repo ở root.
2. Mở file skill `agent-skills/gui-usability-testing/SKILL.md`.
3. Mở web EMS hiện tại.
4. Chạy lần lượt các prompt demo cho:
   - checklist generation
   - checklist execution
   - user testing artifacts
   - cross-platform artifacts
   - findings consolidation
5. Kết thúc bằng cách mở folder output để chứng minh artifact đã có hoặc đúng format mong muốn.

Nếu không muốn quay quá dài, chỉ cần demo sâu `Task 1B + Findings Consolidation`, rồi lướt nhanh các prompt của Task 2 và Task 3.

---

## 3. Chuẩn bị trước khi quay

Chuẩn bị sẵn các cửa sổ sau:

1. Terminal tại root repo:
   - `/home/tkin/Documents/hcmus/software-testing/HW03`
2. Folder đã nộp:
   - `23127075_HW03_AI_GUIUsability_EMS_100/`
3. Web EMS đang dùng:
   - `https://prod-dev.ems-fitus.cloud`
4. File tham chiếu nên ghim sẵn:
   - `23127075_HW03_AI_GUIUsability_EMS_100/main-report.md`
   - `23127075_HW03_AI_GUIUsability_EMS_100/findings/bug_usability_findings_log.md`
   - `23127075_HW03_AI_GUIUsability_EMS_100/agent-skills/gui-usability-testing/SKILL.md`

Nếu có đăng nhập:

- Không nhập password trong lúc phóng to màn hình nếu không cần.
- Có thể chuẩn bị session đăng nhập sẵn cho `user` và `admin`.
- Nếu cần nhập khi quay, nói rõ rằng credentials được cung cấp trong `submission/test_environment_access.md` hoặc file access notes riêng, không hard-code trong skill.

---

## 4. Cấu trúc lời thoại đề xuất

### 4.1. Mở đầu

Lời thoại gợi ý:

> Đây là video demo skill `gui-usability-testing` mà tôi dùng cho HW03 GUI & Usability Testing trên EMS.  
> Skill này được thiết kế để hỗ trợ 5 phần chính: tạo checklist, chạy checklist trên web thật bằng Playwright, chuẩn bị và tổng hợp user testing, tạo artifact cho cross-platform testing, và cuối cùng là gom toàn bộ findings vào một log thống nhất.

### 4.2. Giới thiệu scope

Lời thoại gợi ý:

> Trong bài này tôi chọn Scenario D với 3 màn hình liền mạch: D1 tạo support request, D2 theo dõi request của user, và D3 để admin xử lý request.  
> Tôi sẽ dùng đúng web EMS hiện tại và demo cách prompt skill để sinh ra các artifact tương ứng.

### 4.3. Kết thúc

Lời thoại gợi ý:

> Như vậy skill này không chỉ hỗ trợ từng task riêng lẻ mà còn giúp chuẩn hóa đầu ra theo cùng một flow kiểm thử và cùng một bộ findings.  
> Phần kết quả cuối cùng được gom vào submission folder để nộp cho HW03.

---

## 5. Prompt demo khuyến nghị

## 5.1. Prompt 1 - Giới thiệu skill tổng quát

Prompt để dán:

```text
Use skill gui-usability-testing.
I am testing the current EMS website at https://prod-dev.ems-fitus.cloud.
My scenario is Scenario D - support request lifecycle.
Target scope is 3 connected screens:
- D1: user creates a support request
- D2: user views My Requests list and request detail
- D3: admin views and processes support requests

Explain briefly how this skill supports Task 1A, Task 1B, Task 2, Task 3, and findings consolidation for this scope.
Map each subskill to the expected output files in a submission folder.
```

Mục đích khi quay:

- Chứng minh skill có cấu trúc rõ ràng.
- Cho thấy skill biết map subskill với deliverables.

Bạn nên nói thêm:

> Ở bước đầu tôi cho agent hiểu URL, scenario, và 3 màn hình thuộc cùng một flow.

---

## 5.2. Prompt 2 - Demo Task 1A checklist generation

Prompt để dán:

```text
Use skill gui-usability-testing and subskill step1-checklist.

Target URL: https://prod-dev.ems-fitus.cloud
Target scope:
- D1 create support request
- D2 My Requests list and detail
- D3 Admin Support Requests list

Generate a reusable GUI usability checklist for this EMS scope.
Requirements:
- More than 40 items
- Cover IA-01, IA-02, IA-03, IA-04
- Reference Nielsen, Norman, and Shneiderman
- Output in Vietnamese
- Save the checklist in Markdown format suitable for a homework submission
```

Khi quay màn hình:

1. Mở `agent-skills/gui-usability-testing/step1-checklist/SKILL.md`.
2. Dán prompt.
3. Nhấn mạnh rằng đầu ra mong muốn là checklist Markdown có thể tái sử dụng.

Lời thoại gợi ý:

> Ở Task 1A, skill nhận target scope rồi sinh checklist có hơn 40 items, chia theo 4 interface aspects và gắn heuristic reference rõ ràng.

---

## 5.3. Prompt 3 - Demo Task 1B checklist execution trên web thật

Prompt để dán:

```text
Use skill gui-usability-testing and subskill task1b-execution.

Target URL: https://prod-dev.ems-fitus.cloud
Target scope:
- D1 create support request
- D2 My Requests list and request detail
- D3 Admin Support Requests list

I will use the current live EMS website for demonstration.
Follow the skill rules for live browser execution with MCP Playwright.

For this demo:
- First confirm what account roles and safety rules are needed
- Then describe the live execution flow for D1, D2, and D3
- Then show the expected structure of the Task 1B execution reports and screenshot evidence folders
- Keep the output aligned with a homework submission folder
```

Nếu muốn demo sâu hơn, dùng prompt nối tiếp:

```text
Use skill gui-usability-testing and subskill task1b-execution.

Target URL: https://prod-dev.ems-fitus.cloud
Target scope: D1 create support request

I already have the required account and permission to test.
Please guide the live Playwright execution step by step:
- verify environment access
- navigate the page
- inspect key form behavior
- identify failed checklist items
- propose the report structure and screenshot paths
```

Khi quay:

1. Mở web EMS hiện tại.
2. Cho thấy agent yêu cầu đúng `role`, `credentials`, `safety rules`.
3. Nhấn mạnh rằng skill không được giả lập từ screenshot cũ.

Lời thoại gợi ý:

> Phần quan trọng nhất của Task 1B là skill yêu cầu live browser execution bằng MCP Playwright, chứ không chỉ suy luận từ file tĩnh.  
> Điều này phù hợp với yêu cầu bài vì evidence phải đến từ web thật.

---

## 5.4. Prompt 4 - Demo Task 2 user testing artifacts

Prompt để dán:

```text
Use skill gui-usability-testing and subskill task2-user-testing.

Target URL: https://prod-dev.ems-fitus.cloud
Scenario: Scenario D - support request lifecycle
Target tasks:
- User creates a support request
- User tracks request status and reads the admin response
- Admin searches and reviews support requests

Generate the full set of Task 2 artifacts in Vietnamese:
- preparation protocol
- participant brief
- participant table for 5 real users
- session notes template
- SUS score sheet
- usability report template

Keep the output suitable for a homework submission folder.
```

Prompt tiếp theo nếu muốn demo phase synthesis:

```text
Use skill gui-usability-testing and subskill task2-user-testing.

I already have raw notes from 5 moderated user-testing sessions for the EMS Scenario D flow.
Explain how the skill synthesizes:
- session notes
- SUS scoring
- recurring usability findings
- severity ranking
- final usability report
```

Lời thoại gợi ý:

> Với Task 2, điểm chính là skill tách rõ phần chuẩn bị và phần tổng hợp sau phỏng vấn.  
> Nó không chỉ tạo template mà còn định nghĩa cách tính SUS, cách nhóm pain points và cách xếp severity.

---

## 5.5. Prompt 5 - Demo Task 3 cross-platform artifacts

Prompt để dán:

```text
Use skill gui-usability-testing and subskill task3-cross-platform.

Target URL: https://prod-dev.ems-fitus.cloud
Target scope:
- D1 create support request
- D2 My Requests list and detail
- D3 Admin Support Requests list

Testing dimensions:
- OS: Linux, Windows, Android
- Browsers: Firefox, Opera, Edge, Samsung Internet, Chrome
- Device classes: Desktop, Tablet, Phone

Generate the Task 3 planning artifacts in Vietnamese:
- compatibility matrix
- screenshot protocol
- cross-platform report structure

Use a pairwise-style reduced matrix if full Cartesian coverage is too costly, but keep the output appropriate for homework evidence.
```

Khi quay:

1. Nói rõ bạn vẫn dùng web EMS hiện tại.
2. Nhấn mạnh skill biết sinh `compatibility_matrix`, `screenshot_protocol`, `cross_platform_report`.
3. Nếu cần, mở folder `task3_cross_platform/` để đối chiếu artifact thật.

Lời thoại gợi ý:

> Với Task 3, skill hỗ trợ xây ma trận test và quy tắc chụp evidence.  
> Trong bài nộp của tôi, ảnh defect được gom gọn theo representative screenshot để giữ ZIP dưới giới hạn dung lượng.

---

## 5.6. Prompt 6 - Demo findings consolidation

Prompt để dán:

```text
Use skill gui-usability-testing and subskill findings-consolidation.

Target URL: https://prod-dev.ems-fitus.cloud
Target scope: Scenario D support request flow across D1, D2, D3

Source artifacts:
- Task 1B execution reports
- Task 2 usability findings
- Task 3 cross-platform findings

I want one final aggregated findings package for submission.
Please explain and demonstrate the expected output structure:
- findings/bug_usability_findings_log.md
- findings/defect-screenshots/

Use one representative screenshot per unique finding and preserve source traceability.
```

Nếu muốn nối trực tiếp vào file nộp hiện tại:

```text
Use skill gui-usability-testing and subskill findings-consolidation.

Review the current submission-style folder:
23127075_HW03_AI_GUIUsability_EMS_100

Explain how findings from Task 1B, Task 2, and Task 3 are consolidated into:
23127075_HW03_AI_GUIUsability_EMS_100/findings/bug_usability_findings_log.md

Also explain why representative screenshots are enough for the final findings folder.
```

Lời thoại gợi ý:

> Bước cuối cùng là gom findings từ nhiều task vào một log duy nhất, đồng thời giữ đúng một representative screenshot cho mỗi lỗi để tránh trùng lặp và giảm dung lượng.

---

## 6. Prompt ngắn gọn nhất nếu bạn muốn quay nhanh

Nếu bạn muốn quay một clip ngắn hơn, chỉ dùng prompt này:

```text
Use skill gui-usability-testing.

Target URL: https://prod-dev.ems-fitus.cloud
Scenario: Scenario D - support request lifecycle
Target scope:
- D1 create support request
- D2 My Requests list and request detail
- D3 Admin Support Requests list

I want to demonstrate this skill for my HW03 submission.
Please show how the skill supports:
- Task 1A checklist generation
- Task 1B live checklist execution with MCP Playwright
- Task 2 user testing artifacts and synthesis
- Task 3 cross-platform planning artifacts
- findings consolidation

Map each part to expected output files in a submission folder similar to:
23127075_HW03_AI_GUIUsability_EMS_100
```

Cách dùng:

1. Dán một prompt duy nhất.
2. Để agent trả lời tổng quan.
3. Mở các file artifact thật trong folder nộp để chứng minh kết quả tương ứng.

---

## 7. Timeline quay đề xuất

### Cách quay 8-12 phút

1. `00:00 - 01:00`
   - Giới thiệu bài, scope D1-D2-D3, URL EMS hiện tại.
2. `01:00 - 02:30`
   - Mở `SKILL.md`, giải thích 5 subskills.
3. `02:30 - 04:00`
   - Demo prompt Task 1A và Task 1B.
4. `04:00 - 06:00`
   - Mở web EMS, nói về live execution bằng Playwright.
5. `06:00 - 07:30`
   - Demo prompt Task 2 và Task 3.
6. `07:30 - 09:00`
   - Demo findings consolidation.
7. `09:00 - 10:30`
   - Mở `23127075_HW03_AI_GUIUsability_EMS_100/` để show artifact mapping.
8. `10:30 - 12:00`
   - Kết luận.

---

## 8. Những điểm bắt buộc nên nói rõ khi quay

- Skill dùng trên `web EMS hiện tại`, không phải mock data.
- Task 1B yêu cầu `live browser execution` nếu thực thi thật.
- Skill không được tự bịa `credentials`; phải hỏi role, account, và safety rules.
- Task 2 dùng `5 real users` và raw notes thật.
- Task 3 cần evidence theo từng môi trường test.
- Findings consolidation chỉ giữ `1 representative screenshot` cho mỗi lỗi duy nhất nếu mục tiêu là folder nộp gọn.

---

## 9. Những gì nên tránh khi quay

- Không nói skill tự động thay thế hoàn toàn việc test thủ công.
- Không nói Task 1B đã được executed nếu chỉ mới xem file cũ.
- Không quay lộ password hoặc dữ liệu nhạy cảm.
- Không nói mọi artifact đều được skill sinh ra hoàn toàn tự động nếu thực tế có bước chỉnh tay để đúng format nộp.

---

## 10. Kết câu ngắn gọn để dùng trong video

Bạn có thể chốt video bằng câu này:

> Skill `gui-usability-testing` giúp tôi chuẩn hóa toàn bộ workflow của HW03 từ checklist, execution, usability testing, cross-platform đến findings consolidation, sau đó map các đầu ra này vào submission folder để nộp bài.
