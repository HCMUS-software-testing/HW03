# AI Audit Report

## 1. Thông tin nhóm

- Họ tên: `Lê Trung Kiên`
- MSSV: `23127075`
- Nhóm/Lớp: `23CLC01`

## 2. Bảng audit

### 2.1. Tóm tắt audit

| STT | Prompt + Tool | Verdict |
| --- | --- | --- |
| 1 | Time: `2026-07-25 22:04 +07`Tool: `Codex / GPT-5`Prompt: @Superpowers Convert docs/ISTQB_CT-AI_Syllabus_v1.0.pdf sang markdown. | Valid |
| 2 | Time: `2026-07-25 22:14 +07` Tool: `Codex / GPT-5` Prompt: Tôi muốn 2. Bảng audit sẽ có 2 phần: 2.1. chỉ là tóm tắt STT \\\| Prompt + Tool \\\| Verdict Còn 2.2. Sẽ là list các entry đầy đủ các phần | Valid |
| 3 | Time: `2026-07-26 15:23 +07`<br>Tool: `Codex / GPT-5`<br>Prompt:<br>[@superpowers](plugin://superpowers@openai-api-curated) Tạo một danh sách kiểm tra (checklist) tính khả dụng của GUI (GUI usability) để kiểm thử ứng dụng web Hệ thống Quản lý Sự kiện (Event Management System).<br>Danh sách kiểm tra phải có hơn 40 mục và bao gồm:<br><br>- IA-01 Các tiêu chuẩn UI chung,<br>- IA-02 Biểu mẫu,<br>- IA-03 Điều hướng,<br>- IA-04 Phản hồi và trạng thái hệ thống.<br>  Xây dựng danh sách kiểm tra dựa trên các nguyên tắc Heuristic của Nielsen, các nguyên lý của Norman, và 8 quy tắc vàng của Shneiderman.<br>  Trả kết quả dưới dạng bảng Markdown với các cột: ID, Khía cạnh giao diện (Interface Aspect), Mục kiểm tra (Checklist Item), Tiêu chuẩn đối chiếu (Reference), Lý do (Rationale).<br>  Output sẽ nằm trong folder submission. Nhớ trích nguồn tham khảo. | Incompleted |
| 4 | Time: `2026-07-26 15:30 +07`<br>Tool: `Codex / GPT-5`<br>Prompt:<br>Hãy ghi full output của AI vì nó nằm trong cùng 1 file và liên tục (nội dung không bị ngắt quãng). Sau đó sửa skill ai-audit-entry để đảm bảo khi nội dung được tạo bởi AI liên tục, không bị ngắt quãng, có thể trích full được thì hãy trích full | Valid |
| 5 | Time: `2026-07-27 23:33 +07`<br>Tool: `Codex / GPT-5`<br>Prompt:<br>@Superpowers Hãy dựa vào submission/group để viết bước đầu tiên của skill GUI -  Usability Testing là tạo checklist. Bước này, skill sẽ nhận input là các spec của project để tạo ra checklist dựa trên các nguyên tắc Nielsen's 10 heuristics, Norman's 6 principles, Shneiderman's 8 golden rules, and the per-widget checklists. Nguồn để tham khảo các nguyên tắc ấy cũng đã có trong các file markdown trong thư mục submission/group. | Valid |
| 6 | Time: `2026-07-29 00:05 +07`<br>Tool: `Codex / GPT-5`<br>Prompt:<br>Liệu có thể dùng MCP Playwright + Browserstack để hoàn thành bài tập này theo chiến thuật AI-first không? Nếu có thì tạo các docs hướng dẫn tôi làm | Valid |
| 7 | Time: `2026-08-02 22:34 +07`<br>Tool: `Codex / GPT-5`<br>Prompt:<br>cài thêm nó đi | Valid |
| 8 | Time: `2026-08-02 22:39 +07`<br>Tool: `Codex / GPT-5`<br>Prompt:<br>Bạn tạo 1 file để tôi cung cấp link web mới vì link web cũ đã hỏng. Thêm vào đó là account user và admin. Thêm 1 rule là khi vào trang admin nếu có CRUD tài khoản user thì chỉ đuợc làm trên tài khoản của bản thân, tức là tài khoản user tôi cung cấp để tránh ảnh hưởng đến account người khác. | Valid |
| 9 | Time: `2026-08-02 23:26 +07`<br>Tool: `Codex / GPT-5`<br>Prompt:<br>@Superpowers Đọc các file trong folder docs để hiểu bối cảnh bài tập. Thực hiện Task 1B cho Kiên trên Scene D1. Dùng submission/group/gui_usability_checklist_final.md (không thay đổi file này) để làm check list. Tạo 1 file markdown cho task1b_D1.md trong folder submission/task1B cho việc testing dựa trên checklist đó. Hãy tận dụng MCP Playwright và Chrome Devtools trong quá trình test. Thông tin link web, tài khoản admin và user đã được cung cấp trong submission/test_environment_access.md. Tuyệt đối tuân theo rule được ghi trong  submission/test_environment_access.md. Nếu cần thêm gì thì hãy yêu cầu tôi cung cấp. | Valid |
| 10 | Time: `2026-08-02 23:34 +07`<br>Tool: `Codex / GPT-5`<br>Prompt:<br>Dịch submission/task1B/task1b_D1.md sang tiếng Việt. Thêm rule để biết bài nộp ngôn ngữ chính là Tiếng Việt. Sau đó thêm 1 rule trong folder docs và ai-reasoning là chỉ đọc file markdown vì đọc pdf sẽ tốn token hơn. | Valid |
| 11 | Time: `2026-08-03 11:25 +07`<br>Tool: `Codex / GPT-5`<br>Prompt:<br>@Superpowers Đọc các file trong folder docs để hiểu bối cảnh bài tập. Thực hiện Task 1B cho Kiên trên Scene D2. Dùng submission/group/gui_usability_checklist_final.md (không thay đổi file này) để làm check list. Tạo 1 file markdown cho task1b_D2.md trong folder submission/task1B cho việc testing dựa trên checklist đó. Hãy tận dụng MCP Playwright và Chrome Devtools trong quá trình test. Thông tin link web, tài khoản admin và user đã được cung cấp trong submission/test_environment_access.md. Tuyệt đối tuân theo rule được ghi trong  submission/test_environment_access.md. Nếu cần thêm gì thì hãy yêu cầu tôi cung cấp. Format cho output của D2 cũng nên tương tự như D1. | Valid |
| 12 | Time: `2026-08-03 12:06 +07`<br>Tool: `Codex / GPT-5`<br>Prompt:<br>@Superpowers Đọc các file trong folder docs để hiểu bối cảnh bài tập. Thực hiện Task 1B cho Kiên trên Scene D3. Dùng submission/group/gui_usability_checklist_final.md (không thay đổi file này) để làm check list. Tạo 1 file markdown cho task1b_D3.md trong folder submission/task1B cho việc testing dựa trên checklist đó. Hãy tận dụng MCP Playwright và Chrome Devtools trong quá trình test. Thông tin link web, tài khoản admin và user đã được cung cấp trong submission/test_environment_access.md. Tuyệt đối tuân theo rule được ghi trong  submission/test_environment_access.md. Nếu cần thêm gì thì hãy yêu cầu tôi cung cấp. Format cho output của D3 cũng nên tương tự như D1 và D2. | Valid |
| 13 | Time: `2026-08-03 12:33 +07`<br>Tool: `Codex / GPT-5`<br>Prompt:<br>Ghi vào submission/task1B những thứ tiếp theo tôi cần làm với những thứ tạo từ Task1B. Đọc folder docs ghi vào submission/task2 những thứ cần thiết để chuẩn bị interview 5 người, có thể làm trước template. | Valid |
| 14 | Time: `2026-08-03 15:46 +07`<br>Tool: `Codex / GPT-5`<br>Prompt:<br>Đọc folder docs và tạo ra các file cần thiết cho task 3 | Valid |
| 15 | Time: `2026-08-04 10:48 +07`<br>Tool: `Codex / GPT-5`<br>Prompt:<br>@Superpowers Hãy đọc folder docs tạo ra bộ 3 OS x 5 platform x 3 devices hoàn chỉnh kèm theo tổ hợp để phủ tẩ cả chúng. Sau đó viết plan để thực hiện Task 3 với BrowserStack. Lưu ý vì BrowserStack chỉ có 1 phút trial nên phải cap thật nhanh. Test bằng acc email sinh viên. Bạn hãy thử mở BrowserStack đăng nhập xem cần tôi cung cấp gì để đăng nhập. | Valid |
| 16 | Time: `2026-08-06 01:24 +07`<br>Tool: `Codex / GPT-5`<br>Prompt:<br>Với những screenshot downloads và defects tôi cung cấp, hãy điền vào template ma trận ở Task 3 | Valid |
| 17 | Time: `2026-08-06 01:43 +07`<br>Tool: `Codex / GPT-5`<br>Prompt:<br>[@superpowers](plugin://superpowers@openai-api-curated) <br>Đọc folder docs rồi đưa các content từ trong folder submission vào 23127075_HW03_AI_GUIUsability_EMS_100 là folder nộp. Nếu thiếu file nào sẽ tạo template để làm sau. Các task sẽ chia folder riêng biệt. File main-report.md sẽ là nơi tổng hợp và chứa đường dẫn "relative" đến các content tương ứng, chứ không đưa full nội dung vào. Hãy thêm entry mới trong ai audit cho prompt này. | Valid |
| 18 | Time: `2026-08-06 11:43 +07`<br>Tool: `Codex / GPT-5`<br>Prompt:<br>[@superpowers](plugin://superpowers@openai-api-curated) Hiện tại các defects trong 23127075_HW03_AI_GUIUsability_EMS_100 bị lặp khá nhiều. Vì vậy hãy gom ảnh các defects lại vào 1 folder duy nhất trong 23127075_HW03_AI_GUIUsability_EMS_100. Mỗi defects khác nhau để 1 ảnh làm đại diện. Bug report có thể đề cập nó xuất hiện ở cross platform hay ở các task như thế nào nhưng mỗi defects chỉ 1 ảnh thôi. Hãy ghi prompt này vào ai-audit. | Valid |
| 19 | Time: `2026-08-06 12:25 +07`<br>Tool: `Codex / GPT-5`<br>Prompt:<br>Check lại 23127075_HW03_AI_GUIUsability_EMS_100 những file nào có chữ template mà đã được điền thì bỏ chữ template trong tên file | Valid |
| 20 | Time: `2026-08-06 13:46 +07`<br>Tool: `Codex / GPT-5`<br>Prompt:<br>06/08/2026<br>13:24<br>13:25<br>13:26<br>13:26<br>13:27<br>13:28<br>13:29<br>13:29<br>13:30<br>13:31<br>13:31<br>13:32<br>13:32<br>13:33<br>13:34<br>13:34<br>13:35<br>Ở trên là toàn bộ mốc submit form theo thứ tự. Hãy điền vào 23127075_HW03_AI_GUIUsability_EMS_100\\findings\\bug_usability_findings_log.md | Valid |
| 21 | Time: `2026-08-06 14:48 +07`<br>Tool: `Codex / GPT-5`<br>Prompt:<br>Bạn hãy sửa giúp tôi như sau. <br>- .agents/skills/gui-usability-testing đã có step 1A. Hãy giữ nguyên và đóng gói nó thành step1-checklist<br>Sau đó bạn thêm các skill cho các step sau:<br>- Task1B: Dựa vào ai-audit, tạo ra template cho user điền thông tin account để mcp playwright có thể dùng để đăng nhập. Sau đó execute dựa trên prompt trong ai-audit (Tham khảo entry 9, 11, 12).<br>- Task2: Skill sẽ giúp chuẩn bị các template markdown phù hợp cho buổi interview. Skill cũng có hỗ trợ tổng hợp, phân tích, tự điền các template ấy sau khi người dùng phỏng vấn xong<br>- Task3: Ngưòi dùng cung cấp các OS, Browser, Device. Skill sẽ tạo ra ma trận kiểm thử cross platform cho người dùng kèm theo các template cần thiết.<br>- Có một subskill riêng biệt để tổng hợp all lỗi lại để tạo ra folder findings như 23127075_HW03_AI_GUIUsability_EMS_100/findings<br>Lưu ý các subskill phải có folder con trong .agents/skills/gui-usability-testing nằm riêng biệt để user có thể gọi. Hãy đọc lại ai audit để có thể tham khảo trong quá trình viết skill. Hãy điền lần prompt này vào ai-audit | Valid |

### 2.2. Chi tiết audit

### 2.2.1 Entry 1

**Prompt + Tool:** Time: `2026-07-25 22:04 +07`Tool: `Codex / GPT-5`Prompt: @Superpowers Convert docs/ISTQB_CT-AI_Syllabus_v1.0.pdf sang markdown.

**AI Output:** Tạo file docs/ISTQB_CT-AI_Syllabus_v1.0.md từ PDF, loại bỏ header/footer lặp, dựng lại heading theo section numbering, tách Keywords và giữ phần lớn danh sách/mục lục ở dạng Markdown đọc được.

**Verdict:** Valid

**Reasoning:** Theo ISTQB CT-AI mục 7.5, tài liệu rõ ràng giúp tăng transparency và làm test basis cho các hoạt động kiểm thử có AI hỗ trợ. Việc convert PDF sang Markdown là hợp lý vì giữ nội dung syllabus ở dạng dễ đọc, dễ đối chiếu và giảm chi phí token khi AI dùng làm nguồn tham khảo.

**Student Fix:** Sinh viên đã kiểm tra lại file `docs/ISTQB_CT-AI_Syllabus_v1.0.md` đối chiếu với PDF gốc; không sửa vì bản markdown chuyển đổi đạt yêu cầu cho AI đọc để tiết kiệm token.

### 2.2.2 Entry 2

**Prompt + Tool:** Time: `2026-07-25 22:14 +07` Tool: `Codex / GPT-5` Prompt: Tôi muốn 2. Bảng audit sẽ có 2 phần: 2.1. chỉ là tóm tắt STT \| Prompt + Tool \| Verdict Còn 2.2. Sẽ là list các entry đầy đủ các phần

**AI Output:** Cập nhật skill ai-audit-entry để gồm với bảng và với các mục chứa đủ Prompt + Tool, AI Output, Verdict, Reasoning, Student Fix. Script tự migrate format cũ, tự đánh số lại summary rows và detail entries, và test/valid...

**Verdict:** Valid

**Reasoning:** Theo ISTQB CT-AI mục 7.5, log/audit cần mô tả purpose, output, kết quả kiểm thử và cách dùng để hỗ trợ transparency. Việc tách `2.1` tóm tắt và `2.2` chi tiết làm báo cáo dễ kiểm tra hơn, đồng thời vẫn giữ đủ bằng chứng cho human review.

**Student Fix:** Sinh viên đã rà soát lại cấu trúc báo cáo audit, xác nhận định dạng 2 phần (tóm tắt & chi tiết) hỗ trợ việc rà soát nhanh chóng và đầy đủ thông tin.

### 2.2.3 Entry 3

**Prompt + Tool:**

Time: `2026-07-26 15:23 +07`
Tool: `Codex / GPT-5`
Prompt:
[@superpowers](plugin://superpowers@openai-api-curated) Tạo một danh sách kiểm tra (checklist) tính khả dụng của GUI (GUI usability) để kiểm thử ứng dụng web Hệ thống Quản lý Sự kiện (Event Management System).
Danh sách kiểm tra phải có hơn 40 mục và bao gồm:

- IA-01 Các tiêu chuẩn UI chung,
- IA-02 Biểu mẫu,
- IA-03 Điều hướng,
- IA-04 Phản hồi và trạng thái hệ thống.
  Xây dựng danh sách kiểm tra dựa trên các nguyên tắc Heuristic của Nielsen, các nguyên lý của Norman, và 8 quy tắc vàng của Shneiderman.
  Trả kết quả dưới dạng bảng Markdown với các cột: ID, Khía cạnh giao diện (Interface Aspect), Mục kiểm tra (Checklist Item), Tiêu chuẩn đối chiếu (Reference), Lý do (Rationale).
  Output sẽ nằm trong folder submission. Nhớ trích nguồn tham khảo.

**AI Output:**

```markdown
# Task 1A - GUI Usability Checklist for Event Management System

Checklist này dùng để kiểm thử tính khả dụng GUI của ứng dụng web Event Management System. Các mục được xây dựng dựa trên Nielsen's 10 Usability Heuristics, Norman's design principles, và Shneiderman's Eight Golden Rules.

| ID | Khía cạnh giao diện (Interface Aspect) | Mục kiểm tra (Checklist Item) | Tiêu chuẩn đối chiếu (Reference) | Lý do (Rationale) |
| --- | --- | --- | --- | --- |
| IA-01-01 | IA-01 Các tiêu chuẩn UI chung | Các trang chính như dashboard, danh sách sự kiện, chi tiết sự kiện và hồ sơ người dùng có bố cục nhất quán về header, sidebar, font, màu, icon và khoảng cách. | Nielsen: Consistency and standards; Shneiderman: Strive for consistency; Norman: Consistency | Tính nhất quán giúp người dùng không phải học lại cách dùng ở từng trang và giảm lỗi thao tác. |
| IA-01-02 | IA-01 Các tiêu chuẩn UI chung | Thuật ngữ hiển thị nhất quán trên toàn hệ thống, ví dụ không dùng lẫn lộn `Event`, `Program`, `Activity` nếu cùng chỉ một loại dữ liệu. | Nielsen: Match between system and real world; Shneiderman: Consistency | Thuật ngữ ổn định giúp người dùng hiểu đúng đối tượng đang thao tác và tránh nhầm lẫn khi tìm kiếm hoặc đăng ký sự kiện. |
| IA-01-03 | IA-01 Các tiêu chuẩn UI chung | Các nút hành động chính như `Create Event`, `Register`, `Save`, `Cancel`, `Delete` có kiểu dáng và mức nhấn thị giác phù hợp với độ quan trọng. | Nielsen: Recognition rather than recall; Norman: Signifiers, affordances | Người dùng cần nhận ra ngay hành động chính mà không phải suy luận nút nào quan trọng hơn. |
| IA-01-04 | IA-01 Các tiêu chuẩn UI chung | Màu sắc của trạng thái và hành động nguy hiểm được dùng nhất quán, ví dụ xanh cho thành công, đỏ cho lỗi/xóa, xám cho vô hiệu hóa. | Nielsen: Consistency and standards; Shneiderman: Consistency | Mã màu nhất quán giúp người dùng dự đoán ý nghĩa của trạng thái và tránh bấm nhầm hành động rủi ro. |
| IA-01-05 | IA-01 Các tiêu chuẩn UI chung | Độ tương phản giữa chữ và nền đủ dễ đọc trên desktop và mobile, đặc biệt ở label, placeholder, badge trạng thái và nút bị vô hiệu hóa. | Nielsen: Aesthetic and minimalist design; Norman: Visibility | Chữ khó đọc làm giảm khả năng quét thông tin và khiến người dùng bỏ sót trạng thái quan trọng của sự kiện. |
| IA-01-06 | IA-01 Các tiêu chuẩn UI chung | Nội dung trên card hoặc dòng sự kiện hiển thị thông tin thiết yếu trước: tên sự kiện, thời gian, địa điểm, trạng thái và hành động chính. | Nielsen: Aesthetic and minimalist design; Norman: Discoverability | Sắp xếp thông tin theo mức ưu tiên giúp người dùng ra quyết định nhanh khi duyệt nhiều sự kiện. |
| IA-01-07 | IA-01 Các tiêu chuẩn UI chung | Các icon quan trọng có nhãn hoặc tooltip rõ nghĩa, đặc biệt với icon sửa, xóa, xuất dữ liệu, chia sẻ hoặc xem chi tiết. | Nielsen: Recognition rather than recall; Norman: Signifiers | Icon mơ hồ khiến người dùng phải đoán chức năng, nhất là với người dùng mới hoặc trên màn hình nhỏ. |
| IA-01-08 | IA-01 Các tiêu chuẩn UI chung | Các phần tử có thể tương tác thể hiện rõ trạng thái hover, focus, active và disabled. | Nielsen: Visibility of system status; Norman: Feedback, affordances | Trạng thái tương tác rõ ràng giúp người dùng biết phần tử nào có thể bấm và thao tác đã được nhận hay chưa. |
| IA-01-09 | IA-01 Các tiêu chuẩn UI chung | Giao diện không yêu cầu người dùng ghi nhớ thông tin từ trang trước, ví dụ tên sự kiện hoặc mã đăng ký vẫn hiển thị ở bước xác nhận. | Nielsen: Recognition rather than recall; Shneiderman: Reduce short-term memory load | Giảm tải trí nhớ giúp người dùng hoàn tất tác vụ dài như đăng ký, tạo hoặc chỉnh sửa sự kiện ít sai sót hơn. |
| IA-01-10 | IA-01 Các tiêu chuẩn UI chung | Giao diện responsive không làm mất nội dung, che nút, vỡ bảng hoặc buộc cuộn ngang không cần thiết trên mobile/tablet. | Shneiderman: Seek universal usability; Nielsen: Flexibility and efficiency of use | EMS có thể được dùng trên nhiều thiết bị, nên giao diện phải hỗ trợ người dùng trong các ngữ cảnh màn hình khác nhau. |
| IA-01-11 | IA-01 Các tiêu chuẩn UI chung | Nội dung không bị nhồi quá dày; khoảng trắng, nhóm thông tin và tiêu đề phụ hỗ trợ việc quét nhanh. | Nielsen: Aesthetic and minimalist design; Norman: Conceptual model | Bố cục rõ giúp người dùng hiểu cấu trúc trang và tập trung vào thông tin cần xử lý. |
| IA-01-12 | IA-01 Các tiêu chuẩn UI chung | Các thao tác thường dùng có đường tắt hoặc cách truy cập nhanh, ví dụ tìm kiếm nhanh sự kiện, lọc trạng thái, tạo sự kiện từ dashboard. | Nielsen: Flexibility and efficiency of use; Shneiderman: Enable frequent users to use shortcuts | Người dùng thường xuyên cần hoàn thành tác vụ nhanh mà không đi qua quá nhiều bước lặp lại. |
| IA-02-01 | IA-02 Biểu mẫu | Các trường bắt buộc trong form đăng ký/tạo sự kiện được đánh dấu rõ ràng và có giải thích khi cần. | Nielsen: Error prevention; Norman: Signifiers | Người dùng cần biết thông tin nào bắt buộc trước khi gửi form để tránh lỗi ở cuối quy trình. |
| IA-02-02 | IA-02 Biểu mẫu | Label của input rõ ràng, đặt gần trường nhập và không chỉ dựa vào placeholder để giải thích ý nghĩa trường. | Nielsen: Recognition rather than recall; Norman: Visibility | Placeholder biến mất khi nhập liệu, nên label cố định giúp người dùng kiểm tra lại dữ liệu dễ hơn. |
| IA-02-03 | IA-02 Biểu mẫu | Kiểu input phù hợp với dữ liệu, ví dụ date picker cho ngày, time picker cho giờ, number input cho số lượng vé/sức chứa, email input cho email. | Norman: Mapping, constraints; Nielsen: Error prevention | Kiểu input đúng giúp giới hạn dữ liệu sai và làm thao tác nhập nhanh hơn. |
| IA-02-04 | IA-02 Biểu mẫu | Form kiểm tra dữ liệu ngay tại trường nhập hoặc trước khi submit, ví dụ email sai định dạng, ngày kết thúc trước ngày bắt đầu, sức chứa âm. | Nielsen: Error prevention; Shneiderman: Prevent errors | Phát hiện lỗi sớm giúp người dùng sửa tại chỗ thay vì mất công tìm lỗi sau khi gửi. |
| IA-02-05 | IA-02 Biểu mẫu | Thông báo lỗi form chỉ rõ trường nào lỗi, vì sao lỗi và cách sửa cụ thể. | Nielsen: Help users recognize, diagnose, and recover from errors | Lỗi rõ ràng giúp người dùng khôi phục nhanh mà không phải đoán yêu cầu hệ thống. |
| IA-02-06 | IA-02 Biểu mẫu | Dữ liệu người dùng đã nhập không bị mất sau khi submit thất bại hoặc reload do lỗi hợp lệ hóa. | Nielsen: User control and freedom; Shneiderman: Permit easy reversal of actions | Mất dữ liệu làm tăng bực bội và khiến người dùng phải nhập lại form dài. |
| IA-02-07 | IA-02 Biểu mẫu | Form dài được chia nhóm hợp lý, ví dụ thông tin sự kiện, thời gian/địa điểm, vé/sức chứa, mô tả, hình ảnh. | Nielsen: Aesthetic and minimalist design; Norman: Conceptual model | Nhóm trường theo mô hình tinh thần của người dùng giúp form dễ hiểu và dễ hoàn tất. |
| IA-02-08 | IA-02 Biểu mẫu | Thứ tự tab/focus trong form đi theo luồng đọc tự nhiên và không bỏ qua trường quan trọng. | Shneiderman: Seek universal usability; Nielsen: Flexibility and efficiency of use | Điều hướng bằng bàn phím giúp thao tác nhanh hơn và hỗ trợ người dùng có nhu cầu truy cập khác nhau. |
| IA-02-09 | IA-02 Biểu mẫu | Nút `Submit`/`Save` bị vô hiệu hóa hoặc có cảnh báo rõ khi form chưa đủ điều kiện gửi. | Nielsen: Error prevention; Norman: Constraints | Ràng buộc hợp lý ngăn người dùng gửi dữ liệu chưa hợp lệ. |
| IA-02-10 | IA-02 Biểu mẫu | Các giá trị mặc định hoặc gợi ý nhập liệu phù hợp với ngữ cảnh, ví dụ timezone, định dạng ngày, số lượng mặc định, category phổ biến. | Nielsen: Flexibility and efficiency of use; Norman: Knowledge in the world | Mặc định tốt giảm công nhập liệu và giảm lỗi do người dùng phải nhớ quy ước hệ thống. |
| IA-02-11 | IA-02 Biểu mẫu | Hành động hủy, quay lại hoặc reset form có xác nhận nếu có nguy cơ làm mất dữ liệu đã nhập. | Nielsen: User control and freedom; Shneiderman: Permit easy reversal of actions | Người dùng cần có quyền thoát khỏi tác vụ nhưng vẫn được bảo vệ khỏi mất dữ liệu ngoài ý muốn. |
| IA-02-12 | IA-02 Biểu mẫu | Form upload ảnh/tài liệu sự kiện nêu rõ định dạng, kích thước tối đa, tiến trình upload và lỗi upload nếu có. | Nielsen: Visibility of system status; Nielsen: Help and documentation | Upload thường mất thời gian và dễ lỗi, nên người dùng cần biết điều kiện và trạng thái xử lý. |
| IA-03-01 | IA-03 Điều hướng | Menu chính hiển thị các khu vực quan trọng như Dashboard, Events, My Registrations, Reports/Management, Profile theo vai trò người dùng. | Nielsen: Match between system and real world; Norman: Conceptual model | Điều hướng nên phản ánh mô hình công việc thực tế của attendee, organizer và admin. |
| IA-03-02 | IA-03 Điều hướng | Người dùng luôn biết mình đang ở đâu thông qua tiêu đề trang, trạng thái menu active hoặc breadcrumb. | Nielsen: Visibility of system status; Norman: Feedback | Vị trí hiện tại rõ ràng giúp người dùng định hướng trong hệ thống nhiều trang. |
| IA-03-03 | IA-03 Điều hướng | Từ danh sách sự kiện, người dùng có thể dễ dàng mở chi tiết sự kiện và quay lại danh sách với bộ lọc/trang hiện tại được giữ nguyên. | Nielsen: User control and freedom; Shneiderman: Permit easy reversal of actions | Giữ ngữ cảnh giúp người dùng duyệt nhiều sự kiện mà không phải thiết lập lại tìm kiếm. |
| IA-03-04 | IA-03 Điều hướng | Các liên kết/nút điều hướng có tên gọi cụ thể, ví dụ `View Details`, `Manage Attendees`, `Edit Event`, thay vì nhãn chung chung như `Click here`. | Nielsen: Match between system and real world; Norman: Signifiers | Nhãn cụ thể giúp người dùng dự đoán kết quả trước khi bấm. |
| IA-03-05 | IA-03 Điều hướng | Các trang không truy cập được theo vai trò hiển thị thông báo phù hợp hoặc bị ẩn khỏi menu thay vì dẫn tới lỗi khó hiểu. | Nielsen: Error prevention; Norman: Constraints | Giới hạn quyền truy cập rõ ràng giúp tránh nhầm lẫn và tăng cảm giác hệ thống đáng tin cậy. |
| IA-03-06 | IA-03 Điều hướng | Tìm kiếm và bộ lọc sự kiện dễ thấy, dễ reset và phản ánh đúng trạng thái đang áp dụng. | Nielsen: Visibility of system status; Shneiderman: Offer informative feedback | Người dùng cần biết danh sách đang bị lọc theo tiêu chí nào để không hiểu sai kết quả. |
| IA-03-07 | IA-03 Điều hướng | Phân trang hoặc infinite scroll cho danh sách sự kiện có chỉ báo rõ về số trang, số kết quả hoặc trạng thái đã tải hết. | Nielsen: Visibility of system status; Shneiderman: Offer informative feedback | Khi danh sách dài, người dùng cần biết còn dữ liệu hay không và đang xem phạm vi nào. |
| IA-03-08 | IA-03 Điều hướng | Các bước trong luồng đăng ký sự kiện hoặc checkout vé hiển thị tiến trình hiện tại và bước tiếp theo. | Norman: Mapping; Nielsen: Visibility of system status | Tiến trình rõ giúp người dùng hiểu còn bao nhiêu bước và tránh bỏ dở giữa chừng. |
| IA-03-09 | IA-03 Điều hướng | Nút quay lại, breadcrumb hoặc tab không gây mất dữ liệu chưa lưu trong form hoặc bộ lọc quan trọng. | Nielsen: User control and freedom; Shneiderman: Permit easy reversal of actions | Điều hướng phải cho phép sửa sai mà không tạo tổn thất dữ liệu ngoài ý muốn. |
| IA-03-10 | IA-03 Điều hướng | Điều hướng trên mobile dùng pattern quen thuộc và không che nội dung hoặc hành động chính. | Shneiderman: Seek universal usability; Nielsen: Consistency and standards | Người dùng mobile cần truy cập chức năng chính mà không bị menu chiếm mất không gian thao tác. |
| IA-03-11 | IA-03 Điều hướng | Các trang chi tiết có hành động liên quan đặt gần nội dung liên quan, ví dụ `Register` gần thông tin vé, `Edit` gần thông tin sự kiện. | Norman: Mapping; Nielsen: Recognition rather than recall | Đặt hành động đúng ngữ cảnh giúp người dùng hiểu hành động tác động lên phần nào. |
| IA-03-12 | IA-03 Điều hướng | Khi truy cập URL không tồn tại hoặc sự kiện đã bị xóa, hệ thống hiển thị trang 404/empty state có đường dẫn quay về khu vực phù hợp. | Nielsen: Help users recognize, diagnose, and recover from errors | Lỗi điều hướng cần giúp người dùng phục hồi thay vì rơi vào ngõ cụt. |
| IA-04-01 | IA-04 Phản hồi và trạng thái hệ thống | Sau mỗi hành động quan trọng như tạo sự kiện, đăng ký, hủy đăng ký, lưu thay đổi, hệ thống hiển thị phản hồi thành công hoặc thất bại rõ ràng. | Nielsen: Visibility of system status; Shneiderman: Offer informative feedback; Norman: Feedback | Phản hồi giúp người dùng biết thao tác đã được xử lý và có cần làm gì tiếp hay không. |
| IA-04-02 | IA-04 Phản hồi và trạng thái hệ thống | Các thao tác mất thời gian như tải danh sách, upload ảnh, gửi đăng ký hoặc xuất báo cáo có loading indicator/progress phù hợp. | Nielsen: Visibility of system status; Norman: Feedback | Không có trạng thái tải khiến người dùng tưởng hệ thống đứng hoặc bấm lặp lại. |
| IA-04-03 | IA-04 Phản hồi và trạng thái hệ thống | Nút submit bị khóa hoặc có trạng thái đang xử lý sau khi người dùng bấm để tránh gửi trùng. | Nielsen: Error prevention; Shneiderman: Prevent errors | Tránh thao tác lặp gây đăng ký trùng, tạo bản ghi trùng hoặc gửi yêu cầu nhiều lần. |
| IA-04-04 | IA-04 Phản hồi và trạng thái hệ thống | Thông báo lỗi hệ thống dùng ngôn ngữ dễ hiểu, không chỉ hiển thị mã lỗi kỹ thuật hoặc stack trace. | Nielsen: Help users recognize, diagnose, and recover from errors; Norman: Human-centered design | Người dùng cần biết ý nghĩa lỗi và cách xử lý, không cần chi tiết kỹ thuật nội bộ. |
| IA-04-05 | IA-04 Phản hồi và trạng thái hệ thống | Thông báo toast/banner đủ nổi bật nhưng không che mất nút hoặc dữ liệu quan trọng. | Nielsen: Aesthetic and minimalist design; Shneiderman: Offer informative feedback | Phản hồi phải dễ thấy nhưng không cản trở tác vụ tiếp theo. |
| IA-04-06 | IA-04 Phản hồi và trạng thái hệ thống | Trạng thái sự kiện như Draft, Published, Closed, Cancelled, Full hiển thị rõ bằng text và màu/badge nhất quán. | Nielsen: Visibility of system status; Shneiderman: Consistency | Người dùng cần phân biệt nhanh sự kiện còn đăng ký được hay không. |
| IA-04-07 | IA-04 Phản hồi và trạng thái hệ thống | Empty state của danh sách sự kiện, đăng ký hoặc kết quả tìm kiếm giải thích ngắn gọn và đưa ra hành động tiếp theo. | Nielsen: Help and documentation; Norman: Discoverability | Empty state tốt giúp người dùng hiểu vì sao không có dữ liệu và có thể tiếp tục tác vụ. |
| IA-04-08 | IA-04 Phản hồi và trạng thái hệ thống | Các hành động nguy hiểm như xóa sự kiện, hủy sự kiện hoặc hủy đăng ký có hộp xác nhận nêu rõ hậu quả. | Nielsen: Error prevention; Shneiderman: Prevent errors | Xác nhận trước hành động rủi ro giúp giảm lỗi không thể phục hồi. |
| IA-04-09 | IA-04 Phản hồi và trạng thái hệ thống | Nếu có thể hoàn tác, hệ thống cung cấp `Undo` hoặc cách khôi phục sau thao tác như xóa nháp, hủy lọc, hủy thay đổi. | Nielsen: User control and freedom; Shneiderman: Permit easy reversal of actions | Khả năng hoàn tác tăng cảm giác kiểm soát và giảm lo lắng khi thao tác. |
| IA-04-10 | IA-04 Phản hồi và trạng thái hệ thống | Trạng thái quyền truy cập hoặc phiên đăng nhập hết hạn được thông báo rõ và dẫn người dùng tới bước đăng nhập lại. | Nielsen: Help users recognize, diagnose, and recover from errors | Khi phiên hết hạn, người dùng cần đường phục hồi rõ thay vì mất tác vụ hoặc gặp lỗi mơ hồ. |
| IA-04-11 | IA-04 Phản hồi và trạng thái hệ thống | Dữ liệu thay đổi theo thời gian như số chỗ còn lại, trạng thái đăng ký hoặc danh sách attendee được cập nhật hoặc cảnh báo khi đã cũ. | Nielsen: Visibility of system status; Norman: Feedback | EMS có dữ liệu động; trạng thái lỗi thời có thể làm người dùng đăng ký nhầm hoặc tin vào thông tin sai. |
| IA-04-12 | IA-04 Phản hồi và trạng thái hệ thống | Hệ thống cung cấp hướng dẫn ngắn hoặc liên kết trợ giúp đúng ngữ cảnh cho tác vụ phức tạp như tạo sự kiện, cấu hình vé hoặc xuất báo cáo. | Nielsen: Help and documentation; Shneiderman: Reduce short-term memory load | Trợ giúp đúng lúc hỗ trợ người dùng mới mà không làm quá tải giao diện chính. |

## Nguồn tham khảo

- Jakob Nielsen, "10 Usability Heuristics for User Interface Design", Nielsen Norman Group: https://www.nngroup.com/articles/ten-usability-heuristics/
- Ben Shneiderman, "The Eight Golden Rules of Interface Design", University of Maryland: https://www.cs.umd.edu/users/ben/goldenrules.html
- Don Norman, *The Design of Everyday Things, Revised and Expanded Edition*, JND.org: https://jnd.org/books/the-design-of-everyday-things-revised-and-expanded-edition/
- Basic Books/Hachette Book Group, bibliographic page for Don Norman's *The Design of Everyday Things*: https://www.hachettebookgroup.com/titles/don-norman/the-design-of-everyday-things/9780465050659/
```

**Verdict:** Incompleted

**Reasoning:** Theo ISTQB CT-AI mục 11.6, AI có thể hỗ trợ kiểm thử GUI bằng heuristic/visual review, nhưng mục 11.1 cũng nhấn mạnh một số việc như hiểu nhu cầu người dùng và đề xuất cải thiện UX vẫn cần con người xác nhận. Entry này bị đánh `Incompleted` vì checklist AI tạo ban đầu cần nhóm rà soát, chỉnh theo EMS thật và thống nhất lại trong folder `submission/group`.

**Student Fix:** Cả nhóm đã họp rà soát và điều chỉnh lại checklist, loại bỏ các mục trùng lặp và thống nhất bản checklist chuẩn nằm trong `submission/group/gui_usability_checklist_final.md`.

### 2.2.4 Entry 4

**Prompt + Tool:**

Time: `2026-07-26 15:30 +07`
Tool: `Codex / GPT-5`
Prompt:
Hãy ghi full output của AI vì nó nằm trong cùng 1 file và liên tục (nội dung không bị ngắt quãng). Sau đó sửa skill ai-audit-entry để đảm bảo khi nội dung được tạo bởi AI liên tục, không bị ngắt quãng, có thể trích full được thì hãy trích full

**AI Output:** Đã cập nhật submission/ai-audit/ai_audit_report.md để Entry 3 chứa full nội dung checklist; sửa .agents/skills/ai-audit-entry/SKILL.md và script append_ai_audit_entry.py để --output-file ghi nguyên văn artifact liên t...

**Verdict:** Valid

**Reasoning:** Theo ISTQB CT-AI mục 7.5, tài liệu kiểm thử cần đủ thông tin để truy vết test basis, approach và result. Ghi full output cho artifact liên tục giúp audit minh bạch hơn, nhất là khi checklist là sản phẩm chính cần được người chấm/human reviewer đối chiếu.

**Student Fix:** Sinh viên xác nhận output của AI ghi full thành công ở Entry 3 và script `append_ai_audit_entry.py` hoạt động như kỳ vọng nên không cần chỉnh sửa thêm.

### 2.2.5 Entry 5

**Prompt + Tool:**

Time: `2026-07-27 23:33 +07`
Tool: `Codex / GPT-5`
Prompt:
@Superpowers Hãy dựa vào submission/group để viết bước đầu tiên của skill GUI -  Usability Testing là tạo checklist. Bước này, skill sẽ nhận input là các spec của project để tạo ra checklist dựa trên các nguyên tắc Nielsen's 10 heuristics, Norman's 6 principles, Shneiderman's 8 golden rules, and the per-widget checklists. Nguồn để tham khảo các nguyên tắc ấy cũng đã có trong các file markdown trong thư mục submission/group.

**AI Output:** Đã tạo .agents/skills/gui-usability-testing/SKILL.md mô tả Step 1 - Create Checklist và cập nhật .gitignore để skill mới không bị ignore. Đã kiểm tra file tồn tại, marker nội dung chính, artifact scan và git status.

**Verdict:** Valid

**Reasoning:** Theo ISTQB CT-AI mục 11.6, AI hỗ trợ hiệu quả trong việc thiết lập khung kiểm thử GUI và đối chiếu các chuẩn UI (Nielsen Heuristics, Norman Principles, Shneiderman Rules). Skill `gui-usability-testing` tự động hóa quy trình đọc spec, lập inventory và map các nguyên tắc usability, đồng thời yêu cầu rà soát thủ công để đảm bảo tính phù hợp với bối cảnh EMS.

**Student Fix:** Sinh viên đã kiểm tra lại file `.agents/skills/gui-usability-testing/SKILL.md`, đối chiếu với các tiêu chuẩn trong `submission/group` và giữ workflow ở mức hỗ trợ tạo checklist, yêu cầu kiểm tra lại bằng tay trước khi chốt.

### 2.2.6 Entry 6

**Prompt + Tool:**

Time: `2026-07-29 00:05 +07`
Tool: `Codex / GPT-5`
Prompt:
Liệu có thể dùng MCP Playwright + Browserstack để hoàn thành bài tập này theo chiến thuật AI-first không? Nếu có thì tạo các docs hướng dẫn tôi làm

**AI Output:** Đã tạo submission/ai_first_playwright_browserstack_strategy.md và submission/ai_first_playwright_browserstack_templates.md, giải thích chiến thuật AI-first với Playwright MCP, BrowserStack Live/MCP/Automate, workflow...

**Verdict:** Valid

**Reasoning:** Theo ISTQB CT-AI mục 10.2, virtual test environments giúp tăng controllability, observability và khả năng chạy nhiều môi trường; mục 11.6 cũng nêu AI/tooling có thể hỗ trợ GUI compatibility trên nhiều browser/device/platform. Tài liệu chiến thuật AI-first với Playwright MCP và BrowserStack phù hợp với yêu cầu bài Task 3.

**Student Fix:** Sinh viên đã đọc lại các file tài liệu hướng dẫn `submission/ai_first_playwright_browserstack_strategy.md`, bổ sung thông tin tài khoản và điều chỉnh danh sách thiết bị/browser phù hợp với pool được cấp.

### 2.2.7 Entry 7

**Prompt + Tool:**

Time: `2026-08-02 22:34 +07`
Tool: `Codex / GPT-5`
Prompt:
cài thêm nó đi

**AI Output:** Đã thêm MCP server chrome-devtools bằng lệnh codex mcp add và xác nhận server enabled trong danh sách MCP.

**Verdict:** Valid

**Reasoning:** Theo ISTQB CT-AI mục 11.6.1, kiểm thử qua GUI mô phỏng tương tác người dùng và có thể dùng tool để xác định widget/quan sát UI ổn định hơn. Việc cài Chrome DevTools MCP bổ sung công cụ quan sát console/network/snapshot cho Playwright, giúp bằng chứng kiểm thử đầy đủ hơn.

**Student Fix:** Sinh viên đã kiểm tra danh sách MCP server đã active, xác nhận Chrome DevTools MCP hoạt động như công cụ hỗ trợ và ghi rõ hạn chế môi trường (headless/headful) trong các báo cáo nếu có.

### 2.2.8 Entry 8

**Prompt + Tool:**

Time: `2026-08-02 22:39 +07`
Tool: `Codex / GPT-5`
Prompt:
Bạn tạo 1 file để tôi cung cấp link web mới vì link web cũ đã hỏng. Thêm vào đó là account user và admin. Thêm 1 rule là khi vào trang admin nếu có CRUD tài khoản user thì chỉ đuợc làm trên tài khoản của bản thân, tức là tài khoản user tôi cung cấp để tránh ảnh hưởng đến account người khác.

**AI Output:**

```markdown
# Test Environment Access

File này dùng để lưu thông tin truy cập EMS cho các task AI-first/manual testing. Chỉ dùng tài khoản test hoặc mật khẩu tạm; không commit thông tin nhạy cảm nếu repository được chia sẻ công khai.

## Web URL

| Field | Value |
| --- | --- |
| EMS URL mới | `[Điền link web mới tại đây]` |
| Ghi chú môi trường | `[Ví dụ: ngrok mới, staging, production-like, thời điểm link được cấp]` |

## Accounts

### User Account

Tài khoản này dùng cho Scenario D màn hình `D1` và `D2`.

| Field | Value |
| --- | --- |
| Email / Username / MSSV | `[Điền tài khoản user của Kiên]` |
| Password | `[Điền password user]` |
| Role | `User` |
| Ghi chú | `Chỉ dùng để tạo support request và kiểm tra My Requests của chính tài khoản này.` |

### Admin Account

Tài khoản này dùng cho Scenario D màn hình `D3`.

| Field | Value |
| --- | --- |
| Email / Username | `[Điền tài khoản admin]` |
| Password | `[Điền password admin]` |
| Role | `Admin` |
| Ghi chú | `Chỉ dùng để xem/xử lý support request phục vụ kiểm thử.` |

## Testing Rules

1. Khi test trang admin, nếu có thao tác CRUD tài khoản user, chỉ được thao tác trên tài khoản user của Kiên được cung cấp trong file này.
2. Không sửa, khóa, reset mật khẩu, xóa, đổi role hoặc thay đổi dữ liệu cá nhân của tài khoản người khác.
3. Nếu cần dữ liệu để test admin, ưu tiên tạo dữ liệu mới bằng tài khoản user của Kiên rồi xử lý bằng tài khoản admin.
4. Trước mọi thao tác có thể ảnh hưởng dữ liệu thật, ghi rõ mục đích test và chụp/sao lưu bằng chứng trạng thái trước khi thao tác.
5. Nếu không chắc một thao tác có ảnh hưởng tới tài khoản người khác hay không, dừng lại và hỏi lại trước khi thực hiện.

## Scenario D Scope

| ID | Screen | Role | Intended Use |
| --- | --- | --- | --- |
| D1 | User - create support request form with image attachment | User | Tạo support request test bằng tài khoản user của Kiên. |
| D2 | User - My Requests list/detail with response | User | Kiểm tra danh sách, chi tiết, trạng thái và phản hồi chính thức của request thuộc tài khoản Kiên. |
| D3 | Admin - Support Requests list, Pending/Resolved tabs, search | Admin | Tìm và xử lý support request test do tài khoản Kiên tạo; không thao tác dữ liệu người khác. |
```

**Verdict:** Valid

**Reasoning:** Theo ISTQB CT-AI mục 7.5, test basis và môi trường vận hành cần được tài liệu hóa rõ để hỗ trợ kiểm thử; mục 10.1 cũng nhấn mạnh test environment phải đại diện đúng bối cảnh vận hành. File access tách URL, account, role và rule dữ liệu giúp AI/human tester chạy đúng phạm vi mà không ảnh hưởng tài khoản khác.

**Student Fix:** Sinh viên đã điền đầy đủ URL môi trường EMS thật, thông tin tài khoản user/admin của Kiên và kiểm tra việc tuân thủ các quy tắc an toàn dữ liệu trên file `submission/test_environment_access.md`.

### 2.2.9 Entry 9

**Prompt + Tool:**

Time: `2026-08-02 23:26 +07`
Tool: `Codex / GPT-5`
Prompt:
@Superpowers Đọc các file trong folder docs để hiểu bối cảnh bài tập. Thực hiện Task 1B cho Kiên trên Scene D1. Dùng submission/group/gui_usability_checklist_final.md (không thay đổi file này) để làm check list. Tạo 1 file markdown cho task1b_D1.md trong folder submission/task1B cho việc testing dựa trên checklist đó. Hãy tận dụng MCP Playwright và Chrome Devtools trong quá trình test. Thông tin link web, tài khoản admin và user đã được cung cấp trong submission/test_environment_access.md. Tuyệt đối tuân theo rule được ghi trong  submission/test_environment_access.md. Nếu cần thêm gì thì hãy yêu cầu tôi cung cấp.

**AI Output:** Báo cáo kiểm thử Task 1B D1 chi tiết kèm nhật ký execution, danh mục giao diện, bằng chứng ảnh chụp và danh sách lỗi phát hiện.

**Verdict:** Valid

**Reasoning:** Theo ISTQB CT-AI mục 11.6.1, testing through the GUI là cách mô phỏng tương tác người dùng và phù hợp để kiểm tra form, upload, validation và trạng thái submit. D1 có log thao tác, screenshot, network observation và limitation rõ, nên output hữu ích; phần final vẫn cần sinh viên review lại bằng trình duyệt thật.

**Student Fix:** Sinh viên đã rà soát báo cáo D1 (`submission/task1B/task1b_D1.md`), mở lại các screenshot trong `submission/screenshots/D1` để xác nhận kết quả kiểm thử trên trình duyệt thật.

### 2.2.10 Entry 10

**Prompt + Tool:**

Time: `2026-08-02 23:34 +07`
Tool: `Codex / GPT-5`
Prompt:
Dịch submission/task1B/task1b_D1.md sang tiếng Việt. Thêm rule để biết bài nộp ngôn ngữ chính là Tiếng Việt. Sau đó thêm 1 rule trong folder docs và ai-reasoning là chỉ đọc file markdown vì đọc pdf sẽ tốn token hơn.

**AI Output:** Đã dịch submission/task1B/task1b_D1.md sang tiếng Việt; thêm rule ngôn ngữ chính tiếng Việt trong submission/AGENTS.md; thêm rule ưu tiên đọc Markdown, tránh PDF khi có bản Markdown trong docs/AGENTS.md và ai-reasoning/AGENTS.md.

**Verdict:** Valid

**Reasoning:** Theo ISTQB CT-AI mục 7.5, tài liệu và test basis phải rõ ràng để người kiểm thử hiểu yêu cầu, phạm vi và bằng chứng. Dịch báo cáo D1 sang tiếng Việt và thêm rule ưu tiên Markdown giúp artifact thống nhất với yêu cầu nộp bài, đồng thời giảm rủi ro AI đọc PDF sai/hao token.

**Student Fix:** Sinh viên đã đọc lại bản báo cáo D1 tiếng Việt, giữ nguyên các English UI labels nguyên bản từ hệ thống EMS làm bằng chứng và hiệu chỉnh nhẹ thuật ngữ cho mượt mà.

### 2.2.11 Entry 11

**Prompt + Tool:**

Time: `2026-08-03 11:25 +07`
Tool: `Codex / GPT-5`
Prompt:
@Superpowers Đọc các file trong folder docs để hiểu bối cảnh bài tập. Thực hiện Task 1B cho Kiên trên Scene D2. Dùng submission/group/gui_usability_checklist_final.md (không thay đổi file này) để làm check list. Tạo 1 file markdown cho task1b_D2.md trong folder submission/task1B cho việc testing dựa trên checklist đó. Hãy tận dụng MCP Playwright và Chrome Devtools trong quá trình test. Thông tin link web, tài khoản admin và user đã được cung cấp trong submission/test_environment_access.md. Tuyệt đối tuân theo rule được ghi trong  submission/test_environment_access.md. Nếu cần thêm gì thì hãy yêu cầu tôi cung cấp. Format cho output của D2 cũng nên tương tự như D1.

**AI Output:** Báo cáo thực thi checklist cho màn hình D2 chi tiết kèm nhật ký, danh mục UI, bằng chứng screenshot và các lỗi phát hiện.

**Verdict:** Valid

**Reasoning:** Theo ISTQB CT-AI mục 11.6.1, testing through the GUI cho phép kiểm thử hiển thị danh sách, bộ lọc và chi tiết phản hồi người dùng. Output D2 có đầy đủ log thao tác, screenshot evidence và defect log, đáp ứng yêu cầu kiểm thử usability trên màn hình D2.

**Student Fix:** Sinh viên đối chiếu ảnh chụp D2 trên Playwright MCP với trình duyệt thực tế, kiểm tra lại các lỗi về filter context và empty state trước khi ghi nhận vào bug log.

### 2.2.12 Entry 12

**Prompt + Tool:**

Time: `2026-08-03 12:06 +07`
Tool: `Codex / GPT-5`
Prompt:
@Superpowers Đọc các file trong folder docs để hiểu bối cảnh bài tập. Thực hiện Task 1B cho Kiên trên Scene D3. Dùng submission/group/gui_usability_checklist_final.md (không thay đổi file này) để làm check list. Tạo 1 file markdown cho task1b_D3.md trong folder submission/task1B cho việc testing dựa trên checklist đó. Hãy tận dụng MCP Playwright và Chrome Devtools trong quá trình test. Thông tin link web, tài khoản admin và user đã được cung cấp trong submission/test_environment_access.md. Tuyệt đối tuân theo rule được ghi trong  submission/test_environment_access.md. Nếu cần thêm gì thì hãy yêu cầu tôi cung cấp. Format cho output của D3 cũng nên tương tự như D1 và D2.

**AI Output:** Báo cáo thực thi checklist màn hình D3 Admin Support Requests chi tiết kèm theo log, danh mục giao diện, bằng chứng hình ảnh và phát hiện lỗi.

**Verdict:** Valid

**Reasoning:** Theo ISTQB CT-AI mục 11.6, AI có thể hỗ trợ kiểm tra GUI và phát hiện vấn đề hiển thị/khả dụng; D3 còn liên quan đến role admin và filter/search nên cần evidence rõ. Output có log, checklist execution và defects cho admin list, nhưng vẫn dựa trên human verification để tránh automation bias.

**Student Fix:** Sinh viên đã kiểm tra lại file `submission/task1B/task1b_D3.md`, xác nhận dữ liệu kiểm thử an toàn được tạo từ tài khoản Kiên và rà soát các screenshot lỗi layout admin trên mobile viewport.

### 2.2.13 Entry 13

**Prompt + Tool:**

Time: `2026-08-03 12:33 +07`
Tool: `Codex / GPT-5`
Prompt:
Ghi vào submission/task1B những thứ tiếp theo tôi cần làm với những thứ tạo từ Task1B. Đọc folder docs ghi vào submission/task2 những thứ cần thiết để chuẩn bị interview 5 người, có thể làm trước template.

**AI Output:** Đã thêm next_steps_after_task1b.md trong submission/task1B và bộ template Task 2 trong submission/task2 gồm README, protocol chuẩn bị, participant table, session notes template, SUS score sheet, usability report template...

**Verdict:** Valid

**Reasoning:** Theo ISTQB CT-AI mục 11.1, AI chưa thay thế tốt các hoạt động hiểu nhu cầu người dùng, làm rõ ambiguity và đánh giá UX thực tế; vì vậy chuẩn bị protocol, participant table, notes và SUS template cho interview là hướng đúng. AI tạo khung tài liệu, còn sinh viên/participant cung cấp dữ liệu thực.

**Student Fix:** Sinh viên đã chuẩn bị đầy đủ bộ tài liệu Task 2 trong `submission/task2/`, cập nhật thông tin môi trường test để sẵn sàng cho buổi phỏng vấn 5 người dùng thật.

### 2.2.14 Entry 14

**Prompt + Tool:**

Time: `2026-08-03 15:46 +07`
Tool: `Codex / GPT-5`
Prompt:
Đọc folder docs và tạo ra các file cần thiết cho task 3

**AI Output:** Đã đọc docs và tạo submission/task3 gồm README, checklist scope mapping, matrix template D1-D2-D3, screenshot protocol với overlay, cross-platform report template, findings log template và screenshots README.

**Verdict:** Valid

**Reasoning:** Theo ISTQB CT-AI mục 10.2, virtual test environments hỗ trợ tạo và lặp lại nhiều môi trường khó có sẵn ngoài thực tế; mục 11.6.2 cũng nói công cụ AI/visual comparison có thể hỗ trợ GUI compatibility trên browser/device/platform khác nhau. Các template Task 3 tạo matrix, protocol screenshot và findings log phù hợp với bài cross-platform.

**Student Fix:** Sinh viên đã kiểm tra các file template Task 3 trong `submission/task3/`, bổ sung quy định ghi nhận bằng chứng overlay và đảm bảo cấu trúc sẵn sàng cho việc nộp bài.

### 2.2.15 Entry 15

**Prompt + Tool:**

Time: `2026-08-04 10:48 +07`
Tool: `Codex / GPT-5`
Prompt:
@Superpowers Hãy đọc folder docs tạo ra bộ 3 OS x 5 platform x 3 devices hoàn chỉnh kèm theo tổ hợp để phủ tẩ cả chúng. Sau đó viết plan để thực hiện Task 3 với BrowserStack. Lưu ý vì BrowserStack chỉ có 1 phút trial nên phải cap thật nhanh. Test bằng acc email sinh viên. Bạn hãy thử mở BrowserStack đăng nhập xem cần tôi cung cấp gì để đăng nhập.

**AI Output:** Đã đọc lại yêu cầu Task 3 và artifact hiện có, kiểm tra reachability của EMS/BrowserStack qua HTTP, xác nhận không có screenshot thật sẵn trong submission/task3/screenshots. Đã cập nhật các template Task 3 sang matrix...

**Verdict:** Valid

**Reasoning:** Theo ISTQB CT-AI mục 10.2, cloud/virtual test environments cho phép chạy nhiều môi trường song song và tăng observability; mục 9.2 về pairwise/combinatorial testing ủng hộ việc chọn tổ hợp để phủ nhiều chiều khi số môi trường bị giới hạn. Plan BrowserStack/TestingBot 3 OS x 5 browser x 3 device phù hợp với ràng buộc thời gian trial và coverage của Task 3.

**Student Fix:** Sinh viên đối chiếu lại pool thiết bị/browser có sẵn trên dịch vụ thực tế TestingBot, chốt tổ hợp 5 cell phủ đủ 3 OS x 5 browsers x 3 devices và chuẩn bị kịch bản chụp nhanh.

### 2.2.16 Entry 16

**Prompt + Tool:**

Time: `2026-08-06 01:24 +07`
Tool: `Codex / GPT-5`
Prompt:
Với những screenshot downloads và defects tôi cung cấp, hãy điền vào template ma trận ở Task 3

**AI Output:** Báo cáo ma trận compatibility và báo cáo cross-platform Task 3 đã được điền chi tiết từ các ảnh screenshot thực tế.

**Verdict:** Valid

**Reasoning:** Theo ISTQB CT-AI mục 11.6.2, screenshot/visual comparison có thể dùng để hỗ trợ kiểm tra GUI trên nhiều browser, device và platform; mục 7.5 cũng yêu cầu test result và environment được tài liệu hóa. Việc điền matrix từ screenshot/defect evidence giúp kết quả Task 3 truy vết được từ cell đến ảnh và finding.

**Student Fix:** Sinh viên đã rà soát file ma trận `submission/task3/compatibility_matrix.md`, xác nhận đường dẫn 15 screenshot downloads và các thư mục defect tương ứng cho từng cell.

### 2.2.17 Entry 17

**Prompt + Tool:**

Time: `2026-08-06 01:43 +07`
Tool: `Codex / GPT-5`
Prompt:
[@superpowers](plugin://superpowers@openai-api-curated) 
Đọc folder docs rồi đưa các content từ trong folder submission vào 23127075_HW03_AI_GUIUsability_EMS_100 là folder nộp. Nếu thiếu file nào sẽ tạo template để làm sau. Các task sẽ chia folder riêng biệt. File main-report.md sẽ là nơi tổng hợp và chứa đường dẫn "relative" đến các content tương ứng, chứ không đưa full nội dung vào. Hãy thêm entry mới trong ai audit cho prompt này.

**AI Output:** Đã đọc docs, đối chiếu submission, tạo/cập nhật folder nộp 23127075_HW03_AI_GUIUsability_EMS_100 theo từng task; copy các artifact sẵn có từ submission; tạo main-report.md với relative links và các template còn thiếu...

**Verdict:** Valid

**Reasoning:** Theo ISTQB CT-AI mục 7.5, tài liệu kiểm thử cần rõ purpose, usage, environment, test results và approach để người đọc truy vết. Việc gom nội dung submission vào folder nộp theo task và tạo main-report.md dùng relative links giúp artifact cuối cùng dễ kiểm tra mà không nhân bản full nội dung quá dài.

**Student Fix:** Sinh viên đã mở kiểm tra cây thư mục nộp `23127075_HW03_AI_GUIUsability_EMS_100`, thử nghiệm các relative links trong `main-report.md` đảm bảo điều hướng chính xác.

### 2.2.18 Entry 18

**Prompt + Tool:**

Time: `2026-08-06 11:43 +07`
Tool: `Codex / GPT-5`
Prompt:
[@superpowers](plugin://superpowers@openai-api-curated) Hiện tại các defects trong 23127075_HW03_AI_GUIUsability_EMS_100 bị lặp khá nhiều. Vì vậy hãy gom ảnh các defects lại vào 1 folder duy nhất trong 23127075_HW03_AI_GUIUsability_EMS_100. Mỗi defects khác nhau để 1 ảnh làm đại diện. Bug report có thể đề cập nó xuất hiện ở cross platform hay ở các task như thế nào nhưng mỗi defects chỉ 1 ảnh thôi. Hãy ghi prompt này vào ai-audit.

**AI Output:** Đã tạo thư mục findings/defect-screenshots với ảnh đại diện cho từng finding, cập nhật Task 1B/Task 2/Task 3 và findings log để trỏ về ảnh đại diện, đồng thời ghi rõ các task/CP nơi finding xuất hiện...

**Verdict:** Valid

**Reasoning:** Theo ISTQB CT-AI mục 11.2, AI có thể hỗ trợ phân tích defect bằng cách nhận diện category, duplicate hoặc finding tương tự; mục 7.5 yêu cầu kết quả test và bằng chứng được tài liệu hóa rõ. Gom ảnh đại diện cho defect giúp giảm trùng lặp nhưng vẫn giữ traceability từ bug report đến nơi lỗi xuất hiện.

**Student Fix:** Sinh viên kiểm tra thư mục `findings/defect-screenshots/`, xác nhận mỗi defect có 1 ảnh đại diện tiêu biểu và thông tin phản ánh đúng các platform xuất hiện lỗi.

### 2.2.19 Entry 19

**Prompt + Tool:**

Time: `2026-08-06 12:25 +07`
Tool: `Codex / GPT-5`
Prompt:
Check lại 23127075_HW03_AI_GUIUsability_EMS_100 những file nào có chữ template mà đã được điền thì bỏ chữ template trong tên file

**AI Output:** Đã đổi tên usability_report_template.md thành usability_report.md, matrix_template.md thành compatibility_matrix.md, cross_platform_report_template.md thành cross_platform_report.md; cập nhật main-report.md và relative links...

**Verdict:** Valid

**Reasoning:** Theo ISTQB CT-AI mục 7.5, việc đặt tên tài liệu nhất quán và phản ánh đúng trạng thái hoàn tất giúp tăng khả năng truy vết và độ tin cậy của bộ hồ sơ kiểm thử. Loại bỏ hậu tố `template` sau khi đã hoàn thiện nội dung giúp phân biệt rõ giữa khung tài liệu nháp và báo cáo chính thức.

**Student Fix:** Sinh viên đã rà soát lại tên các file trong thư mục bài nộp `23127075_HW03_AI_GUIUsability_EMS_100`, xác nhận không còn chữ `template` ở các file báo cáo đã được điền dữ liệu thật.

### 2.2.20 Entry 20

**Prompt + Tool:**

Time: `2026-08-06 13:46 +07`
Tool: `Codex / GPT-5`
Prompt:
06/08/2026
13:24
13:25
13:26
13:26
13:27
13:28
13:29
13:29
13:30
13:31
13:31
13:32
13:32
13:33
13:34
13:34
13:35
Ở trên là toàn bộ mốc submit form theo thứ tự. Hãy điền vào 23127075_HW03_AI_GUIUsability_EMS_100\findings\bug_usability_findings_log.md

**AI Output:** Đã điền 17 timestamp submit form vào findings/bug_usability_findings_log.md theo đúng thứ tự người dùng cung cấp, tick các checklist liên quan submit form, và xác nhận không còn placeholder [Điền sau] trong file.

**Verdict:** Valid

**Reasoning:** Theo ISTQB CT-AI mục 7.5, báo cáo defect và bằng chứng thử nghiệm cần ghi nhận chính xác thời mốc thực thi để đảm bảo tính minh bạch và khả năng kiểm tra lại (traceability/auditability). Việc ghi nhận timestamp nộp Google Form đảm bảo tính toàn vẹn dữ liệu thử nghiệm của sinh viên.

**Student Fix:** Sinh viên đã kiểm tra lại toàn bộ 17 mốc timestamp trong `findings/bug_usability_findings_log.md` đối chiếu với nhật ký gửi Google Form thực tế và xác nhận tính chính xác.

### 2.2.21 Entry 21

**Prompt + Tool:**

Time: `2026-08-06 14:48 +07`
Tool: `Codex / GPT-5`
Prompt:
Bạn hãy sửa giúp tôi như sau. 
- .agents/skills/gui-usability-testing đã có step 1A. Hãy giữ nguyên và đóng gói nó thành step1-checklist
Sau đó bạn thêm các skill cho các step sau:
- Task1B: Dựa vào ai-audit, tạo ra template cho user điền thông tin account để mcp playwright có thể dùng để đăng nhập. Sau đó execute dựa trên prompt trong ai-audit (Tham khảo entry 9, 11, 12).
- Task2: Skill sẽ giúp chuẩn bị các template markdown phù hợp cho buổi interview. Skill cũng có hỗ trợ tổng hợp, phân tích, tự điền các template ấy sau khi người dùng phỏng vấn xong
- Task3: Ngưòi dùng cung cấp các OS, Browser, Device. Skill sẽ tạo ra ma trận kiểm thử cross platform cho người dùng kèm theo các template cần thiết.
- Có một subskill riêng biệt để tổng hợp all lỗi lại để tạo ra folder findings như 23127075_HW03_AI_GUIUsability_EMS_100/findings
Lưu ý các subskill phải có folder con trong .agents/skills/gui-usability-testing nằm riêng biệt để user có thể gọi. Hãy đọc lại ai audit để có thể tham khảo trong quá trình viết skill. Hãy điền lần prompt này vào ai-audit

**AI Output:** Đã đóng gói Step 1A thành subskill `step1-checklist`, tạo thêm 4 subskill mới trong các thư mục con tương ứng (`task1b-execution`, `task2-user-testing`, `task3-cross-platform`, `findings-consolidation`) dưới `.agents/skills/gui-usability-testing/`, cập nhật main `SKILL.md` và đồng bộ sang `23127075_HW03_AI_GUIUsability_EMS_100/agent-skills/`.

**Verdict:** Valid

**Reasoning:** Theo ISTQB CT-AI mục 11.6, thiết lập và mô đun hóa các quy trình test qua AI (Modular Agent Skills) giúp tăng tính tái sử dụng, minh bạch và khả năng truy vết của toàn bộ hoạt động kiểm thử GUI Usability.

**Student Fix:** Sinh viên đã rà soát và chỉnh lại bộ skill `.agents/skills/gui-usability-testing/` để các subskill độc lập, đóng gói, portable cho bất kỳ website nào. Sau khi chỉnh, sinh viên xác nhận skill đã yêu cầu cung cấp `target_url`, hỏi đúng loại account/role và credential khi cần đăng nhập, đồng thời bắt buộc dùng MCP Playwright thật cho live testing; MCP Playwright cũng đã được cài/enable trong Codex để tránh mô phỏng kết quả từ artifact tĩnh.

## 3. Tổng kết độ chính xác AI

- Các nội dung AI tạo đã được rà soát với yêu cầu bài làm: Sinh viên đã đối chiếu 100% các artifact do AI tạo (checklist, test log, bug report, ma trận compatibility) với ứng dụng EMS thật và yêu cầu bài tập HW03.
- Mức độ chính xác/độ hữu ích tổng quan: Đạt khoảng 85-90%. AI hỗ trợ tạo khung tài liệu, lập dàn ý checklist, tự động hóa tương tác Playwright MCP và ghi nhận defect nhanh chóng.
- Giới hạn hoặc rủi ro còn lại: AI có rủi ro tạo thông tin giả lập nếu không có môi trường thực (đã bị chặn bằng rule không bịa evidence), một số hình ảnh mobile screenshot qua Playwright bị lệch sticky header và các đánh giá cảm nhận UX thực tế vẫn cần con người trải nghiệm.

## 4. Kết luận

Việc ứng dụng AI theo chiến thuật AI-first (kết hợp Codex/GPT-5, Playwright MCP, TestingBot và các quy tắc kiểm thử ISTQB CT-AI) đã giúp tối ưu hóa thời gian lập kế hoạch, thiết kế checklist và thực thi kiểm thử GUI Usability. Sự giám sát trực tiếp của sinh viên (Human-in-the-loop) đảm bảo tính chính xác, minh bạch và toàn vẹn của kết quả kiểm thử.

## 5. Disclosure

Báo cáo này được thực hiện với sự hỗ trợ của các công cụ AI (Codex, GPT-5, Playwright MCP) dưới sự chỉ đạo và rà soát thủ công của sinh viên Lê Trung Kiên (MSSV: 23127075). Toàn bộ bằng chứng thử nghiệm, screenshot và đánh giá cuối cùng đều dựa trên hệ thống EMS thật.
