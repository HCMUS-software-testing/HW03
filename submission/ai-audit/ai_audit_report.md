# AI Audit Report

## 1. Thông tin nhóm
- Họ tên: `Lê Trung Kiên`
- MSSV: `23127075`
- Nhóm/Lớp: `[TODO]`

## 2. Bảng audit

### 2.1. Tóm tắt audit

| STT | Prompt + Tool | Verdict |
| --- | --- | --- |
| 1 | Time: `2026-07-25 22:04 +07`Tool: `Codex / GPT-5`Prompt: @Superpowers Convert docs/ISTQB_CT-AI_Syllabus_v1.0.pdf sang markdown. | Valid |
| 2 | Time: `2026-07-25 22:14 +07` Tool: `Codex / GPT-5` Prompt: Tôi muốn 2. Bảng audit sẽ có 2 phần: 2.1. chỉ là tóm tắt STT \\\| Prompt + Tool \\\| Verdict Còn 2.2. Sẽ là list các entry đầy đủ các phần | Valid |
| 3 | Time: `2026-07-26 15:23 +07`<br>Tool: `Codex / GPT-5`<br>Prompt:<br>[@superpowers](plugin://superpowers@openai-api-curated) Tạo một danh sách kiểm tra (checklist) tính khả dụng của GUI (GUI usability) để kiểm thử ứng dụng web Hệ thống Quản lý Sự kiện (Event Management System).<br>Danh sách kiểm tra phải có hơn 40 mục và bao gồm:<br><br>- IA-01 Các tiêu chuẩn UI chung,<br>- IA-02 Biểu mẫu,<br>- IA-03 Điều hướng,<br>- IA-04 Phản hồi và trạng thái hệ thống.<br>  Xây dựng danh sách kiểm tra dựa trên các nguyên tắc Heuristic của Nielsen, các nguyên lý của Norman, và 8 quy tắc vàng của Shneiderman.<br>  Trả kết quả dưới dạng bảng Markdown với các cột: ID, Khía cạnh giao diện (Interface Aspect), Mục kiểm tra (Checklist Item), Tiêu chuẩn đối chiếu (Reference), Lý do (Rationale).<br>  Output sẽ nằm trong folder submission. Nhớ trích nguồn tham khảo. | Incompleted |
| 4 | Time: `2026-07-26 15:30 +07`<br>Tool: `Codex / GPT-5`<br>Prompt:<br>Hãy ghi full output của AI vì nó nằm trong cùng 1 file và liên tục (nội dung không bị ngắt quãng). Sau đó sửa skill ai-audit-entry để đảm bảo khi nội dung được tạo bởi AI liên tục, không bị ngắt quãng, có thể trích full được thì hãy trích full | [Manual by user] |
| 5 | Time: `2026-07-27 23:33 +07`<br>Tool: `Codex / GPT-5`<br>Prompt:<br>@Superpowers Hãy dựa vào submission/group để viết bước đầu tiên của skill GUI -  Usability Testing là tạo checklist. Bước này, skill sẽ nhận input là các spec của project để tạo ra checklist dựa trên các nguyên tắc Nielsen's 10 heuristics, Norman's 6 principles, Shneiderman's 8 golden rules, and the per-widget checklists. Nguồn để tham khảo các nguyên tắc ấy cũng đã có trong các file markdown trong thư mục submission/group. | [Manual by user] |
| 6 | Time: `2026-07-29 00:05 +07`<br>Tool: `Codex / GPT-5`<br>Prompt:<br>Liệu có thể dùng MCP Playwright + Browserstack để hoàn thành bài tập này theo chiến thuật AI-first không? Nếu có thì tạo các docs hướng dẫn tôi làm | [Manual by user] |
| 7 | Time: `2026-08-02 22:34 +07`<br>Tool: `Codex / GPT-5`<br>Prompt:<br>cài thêm nó đi | [Manual by user] |
| 8 | Time: `2026-08-02 22:39 +07`<br>Tool: `Codex / GPT-5`<br>Prompt:<br>Bạn tạo 1 file để tôi cung cấp link web mới vì link web cũ đã hỏng. Thêm vào đó là account user và admin. Thêm 1 rule là khi vào trang admin nếu có CRUD tài khoản user thì chỉ đuợc làm trên tài khoản của bản thân, tức là tài khoản user tôi cung cấp để tránh ảnh hưởng đến account người khác. | [Manual by user] |
| 9 | Time: `2026-08-02 23:26 +07`<br>Tool: `Codex / GPT-5`<br>Prompt:<br>@Superpowers Đọc các file trong folder docs để hiểu bối cảnh bài tập. Thực hiện Task 1B cho Kiên trên Scene D1. Dùng submission/group/gui_usability_checklist_final.md (không thay đổi file này) để làm check list. Tạo 1 file markdown cho task1b_D1.md trong folder submission/task1B cho việc testing dựa trên checklist đó. Hãy tận dụng MCP Playwright và Chrome Devtools trong quá trình test. Thông tin link web, tài khoản admin và user đã được cung cấp trong submission/test_environment_access.md. Tuyệt đối tuân theo rule được ghi trong  submission/test_environment_access.md. Nếu cần thêm gì thì hãy yêu cầu tôi cung cấp. | [Manual by user] |
| 10 | Time: `2026-08-02 23:34 +07`<br>Tool: `Codex / GPT-5`<br>Prompt:<br>Dịch submission/task1B/task1b_D1.md sang tiếng Việt. Thêm rule để biết bài nộp ngôn ngữ chính là Tiếng Việt. Sau đó thêm 1 rule trong folder docs và ai-reasoning là chỉ đọc file markdown vì đọc pdf sẽ tốn token hơn. | [Manual by user] |
| 11 | Time: `2026-08-03 11:25 +07`<br>Tool: `Codex / GPT-5`<br>Prompt:<br>@Superpowers Đọc các file trong folder docs để hiểu bối cảnh bài tập. Thực hiện Task 1B cho Kiên trên Scene D2. Dùng submission/group/gui_usability_checklist_final.md (không thay đổi file này) để làm check list. Tạo 1 file markdown cho task1b_D2.md trong folder submission/task1B cho việc testing dựa trên checklist đó. Hãy tận dụng MCP Playwright và Chrome Devtools trong quá trình test. Thông tin link web, tài khoản admin và user đã được cung cấp trong submission/test_environment_access.md. Tuyệt đối tuân theo rule được ghi trong  submission/test_environment_access.md. Nếu cần thêm gì thì hãy yêu cầu tôi cung cấp. Format cho output của D2 cũng nên tương tự như D1. | [Manual by user] |

### 2.2. Chi tiết audit

### 2.2.1 Entry 1

**Prompt + Tool:** Time: `2026-07-25 22:04 +07`Tool: `Codex / GPT-5`Prompt: @Superpowers Convert docs/ISTQB_CT-AI_Syllabus_v1.0.pdf sang markdown.

**AI Output:** Tạo file docs/ISTQB_CT-AI_Syllabus_v1.0.md từ PDF, loại bỏ header/footer lặp, dựng lại heading theo section numbering, tách Keywords và giữ phần lớn danh sách/mục lục ở dạng Markdown đọc được.

**Verdict:** Valid

**Reasoning:** [Manual by user]

**Student Fix:** Đã đọc lại nhưng không sửa vì convert sang markdown với mục đích cho AI đọc để đỡ hao Token.

### 2.2.2 Entry 2

**Prompt + Tool:** Time: `2026-07-25 22:14 +07` Tool: `Codex / GPT-5` Prompt: Tôi muốn 2. Bảng audit sẽ có 2 phần: 2.1. chỉ là tóm tắt STT \| Prompt + Tool \| Verdict Còn 2.2. Sẽ là list các entry đầy đủ các phần

**AI Output:** Cập nhật skill ai-audit-entry để gồm với bảng và với các mục chứa đủ Prompt + Tool, AI Output, Verdict, Reasoning, Student Fix. Script tự migrate format cũ, tự đánh số lại summary rows và detail entries, và test/valid...

**Verdict:** Valid

**Reasoning:** [Manual by user]

**Student Fix:** Check lại format ai_audit_report.md đã ổn nên không sửa vì đã phù hợp với nhu cầu ở hiện tại.

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

**Reasoning:** [Manual by user]

**Student Fix:** Cả nhóm đã họp với nhau và sửa. Output được dùng chung và nằm trong folder group.

### 2.2.4 Entry 4

**Prompt + Tool:**

Time: `2026-07-26 15:30 +07`
Tool: `Codex / GPT-5`
Prompt:
Hãy ghi full output của AI vì nó nằm trong cùng 1 file và liên tục (nội dung không bị ngắt quãng). Sau đó sửa skill ai-audit-entry để đảm bảo khi nội dung được tạo bởi AI liên tục, không bị ngắt quãng, có thể trích full được thì hãy trích full

**AI Output:** Đã cập nhật submission/ai-audit/ai_audit_report.md để Entry 3 chứa full nội dung checklist; sửa .agents/skills/ai-audit-entry/SKILL.md và script append_ai_audit_entry.py để --output-file ghi nguyên văn artifact liên t...

**Verdict:** [Manual by user]

**Reasoning:** [Manual by user]

**Student Fix:** Output của AI đã phú hợp với mong muốn. Bằng chứng là ở Entry 3, checklist đã được ghi full. Sinh viên không sửa.

### 2.2.5 Entry 5

**Prompt + Tool:**

Time: `2026-07-27 23:33 +07`
Tool: `Codex / GPT-5`
Prompt:
@Superpowers Hãy dựa vào submission/group để viết bước đầu tiên của skill GUI -  Usability Testing là tạo checklist. Bước này, skill sẽ nhận input là các spec của project để tạo ra checklist dựa trên các nguyên tắc Nielsen's 10 heuristics, Norman's 6 principles, Shneiderman's 8 golden rules, and the per-widget checklists. Nguồn để tham khảo các nguyên tắc ấy cũng đã có trong các file markdown trong thư mục submission/group.

**AI Output:** Đã tạo .agents/skills/gui-usability-testing/SKILL.md mô tả Step 1 - Create Checklist và cập nhật .gitignore để skill mới không bị ignore. Đã kiểm tra file tồn tại, marker nội dung chính, artifact scan và git status.

**Verdict:** [Manual by user]

**Reasoning:** [Manual by user]

**Student Fix:** [Manual by user]

### 2.2.6 Entry 6

**Prompt + Tool:**

Time: `2026-07-29 00:05 +07`
Tool: `Codex / GPT-5`
Prompt:
Liệu có thể dùng MCP Playwright + Browserstack để hoàn thành bài tập này theo chiến thuật AI-first không? Nếu có thì tạo các docs hướng dẫn tôi làm

**AI Output:** Đã tạo submission/ai_first_playwright_browserstack_strategy.md và submission/ai_first_playwright_browserstack_templates.md, giải thích chiến thuật AI-first với Playwright MCP, BrowserStack Live/MCP/Automate, workflow...

**Verdict:** [Manual by user]

**Reasoning:** [Manual by user]

**Student Fix:** Sinh viên sửa lại theo đúng pool của sinh viên.

### 2.2.7 Entry 7

**Prompt + Tool:**

Time: `2026-08-02 22:34 +07`
Tool: `Codex / GPT-5`
Prompt:
cài thêm nó đi

**AI Output:** Đã thêm MCP server chrome-devtools bằng lệnh codex mcp add và xác nhận server enabled trong danh sách MCP.

**Verdict:** [Manual by user]

**Reasoning:** [Manual by user]

**Student Fix:** [Manual by user]

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

**Verdict:** [Manual by user]

**Reasoning:** [Manual by user]

**Student Fix:** Sinh viên điền link web mới, account user, account admin và quy tắc chỉ CRUD trên tài khoản user của bản thân để tránh ảnh hưởng account người khác.

### 2.2.9 Entry 9

**Prompt + Tool:**

Time: `2026-08-02 23:26 +07`
Tool: `Codex / GPT-5`
Prompt:
@Superpowers Đọc các file trong folder docs để hiểu bối cảnh bài tập. Thực hiện Task 1B cho Kiên trên Scene D1. Dùng submission/group/gui_usability_checklist_final.md (không thay đổi file này) để làm check list. Tạo 1 file markdown cho task1b_D1.md trong folder submission/task1B cho việc testing dựa trên checklist đó. Hãy tận dụng MCP Playwright và Chrome Devtools trong quá trình test. Thông tin link web, tài khoản admin và user đã được cung cấp trong submission/test_environment_access.md. Tuyệt đối tuân theo rule được ghi trong  submission/test_environment_access.md. Nếu cần thêm gì thì hãy yêu cầu tôi cung cấp.

**AI Output:**

````markdown
# Task 1B - Checklist Execution for D1

| Field | Value |
| --- | --- |
| Tester | Lê Trung Kiên |
| MSSV | `23127075` |
| Scenario | D - User requests Support and Admin resolves it |
| Screen | D1 - User creates support request form with image attachment |
| Role used | User |
| SUT | `https://prod-dev.ems-fitus.cloud` |
| Test date | 2026-08-02 |
| Checklist source | `submission/group/gui_usability_checklist_final.md` |
| Checklist source modified? | No |

## 1. Full Prompt Used for AI-Assisted D1 Testing

```text
Bạn là QA tester cho HW03 GUI & Usability Testing trên EMS.

Hãy thực hiện Task 1B cho Lê Trung Kiên (MSSV 23127075), Scenario D, màn hình D1: User - create support request form with image attachment.

Nguồn bắt buộc:
- Đọc các tài liệu trong `docs/` để hiểu bối cảnh bài tập, EMS, Scenario D và yêu cầu Task 1B.
- Dùng checklist gốc `submission/group/gui_usability_checklist_final.md` làm checklist thực thi.
- Không sửa `submission/group/gui_usability_checklist_final.md`.
- Dùng thông tin URL/tài khoản trong `submission/test_environment_access.md`.
- Tuyệt đối tuân thủ Testing Rules trong `submission/test_environment_access.md`: chỉ dùng tài khoản user của Kiên cho D1/D2, không thao tác dữ liệu hoặc tài khoản người khác, chỉ tạo support request test của chính tài khoản Kiên nếu cần.

Công cụ:
- Dùng Playwright MCP để đăng nhập, điều hướng, lấy accessibility snapshot, thao tác form, upload ảnh, submit, chụp screenshot evidence và kiểm tra network/console.
- Dùng Chrome DevTools MCP nếu môi trường cho phép để kiểm tra bổ sung snapshot/console/network. Nếu Chrome DevTools MCP không chạy được, ghi rõ limitation và không bịa evidence.

Quy trình D1:
1. Mở EMS tại URL mới trong `submission/test_environment_access.md`.
2. Đăng nhập bằng user account của Kiên.
3. Điều hướng `Support requests -> Create request` hoặc route tương ứng.
4. Ghi lại URL, page title, heading, primary actions và danh sách widget hiển thị.
5. Chụp screenshot tổng quan của màn hình D1.
6. Chạy từng item trong `submission/group/gui_usability_checklist_final.md` trên riêng màn hình D1.
7. Với mỗi item, đánh dấu `Pass`, `Fail`, hoặc `N/A`.
8. Với mỗi `Fail`, ghi lý do cụ thể dựa trên quan sát UI/network/console, user impact, severity 0-4, screenshot ref và suggested fix.
9. Kiểm tra tối thiểu các trạng thái D1: submit rỗng, chọn request type, nhập issue/title, nhập detailed description, character counter, upload ảnh hợp lệ, preview/remove ảnh, submit thành công, cancel/back khi có dữ liệu chưa lưu, desktop và mobile responsive layout.
10. Không submit Google Form tự động. Chỉ tạo finding entries sẵn để sinh viên review và submit thủ công.

Output cần tạo:
- File Markdown `submission/task1B/task1b_D1.md`.
- Nội dung gồm: test scope, test log, UI inventory, bảng checklist execution theo ID checklist gốc, danh sách findings, screenshot evidence và completion notes.
```

## 2. Test Log

| Step | Tool | Observation |
| --- | --- | --- |
| Open EMS | Playwright MCP | Opened `https://prod-dev.ems-fitus.cloud`; existing session was admin, so logged out first. |
| Login as Kiên user | Playwright MCP | Logged in as `ltkien23@clc.fitus.edu.vn`; dashboard loaded successfully. |
| Navigate to Support | Playwright MCP | User menu showed `Support requests` -> `/complaints`. |
| Open D1 | Playwright MCP | `Create request` opened `/complaints/new`; page title `Gửi yêu cầu hỗ trợ \| HCMUS EMS`; visible H1 `Create support request`. |
| Submit empty form | Playwright MCP | Alert displayed: `Request type, issue requiring support and detailed description are required.` |
| Fill/upload form | Playwright MCP | Form accepted title, description and PNG attachment; image thumbnail and remove button appeared. |
| Submit after default/category issue | Playwright MCP | First submit attempt produced `POST /api/complaints => 400`; response body said category must be one of `SUPPORT`, `COMPLAINT`, `CONTACT`, `OTHER`; console warning: `Select: Keys "S" passed to "selectedKeys" are not present in the collection.` |
| Submit after keyboard category selection | Playwright MCP | Keyboard selection changed visible type to `Complaint`; submit returned `POST /api/complaints => 201`; redirected to `/complaints?created=1`; new request appeared as `Pending` with URL `/complaints/56`. |
| Mobile responsive check | Playwright MCP | At `390x844`, form fit without horizontal overflow; fields stacked properly. |
| Chrome DevTools check | Chrome DevTools MCP | Could not start because the environment reported `Missing X server to start the headful browser`; no Chrome DevTools evidence was fabricated. |

## 3. D1 UI Inventory

| Category | Observed D1 Items |
| --- | --- |
| Screen and route | `Support requests` list at `/complaints`; create form at `/complaints/new`. |
| Role | User account for Kiên only. |
| Main flow | Open support requests, create request, choose request type, enter issue and detailed description, attach image, submit. |
| Widgets | Header, user menu, `Back`, H1, request type select, issue textbox, `0/255` counter, detailed description textarea, image upload drop zone, image thumbnail, remove attachment button, `Cancel`, `Submit request`, alert/toast area. |
| Dynamic states | Empty validation alert, category validation error, upload preview/remove state, mobile layout, submit success redirect, API error state. |

## 4. Screenshot Evidence

| Evidence ID | Path | Purpose |
| --- | --- | --- |
| E-D1-001 | `submission/screenshots/D1/D1_create_request_overview.png` | D1 overview before data entry. |
| E-D1-002 | `submission/screenshots/D1/D1_form_filled_with_attachment.png` | Filled form with uploaded image evidence. |
| E-D1-003 | `submission/screenshots/D1/D1_mobile_validation_layout.png` | Mobile layout and validation state at `390x844`. |
| E-D1-004 | `submission/screenshots/D1/D1_submit_success_redirect.png` | Successful submit redirect and new request in list. |
| F-D1-001 | `submission/screenshots/checklist-failures/F-D1-001_validation-not-inline.png` | Required-field validation uses a global alert and submit is enabled while empty. |
| F-D1-002 | `submission/screenshots/checklist-failures/F-D1-002_category-submit-400-no-clear-ui-error.png` | Category/default submit issue with no clear recovery message before retry. |
| F-D1-003 | `submission/screenshots/checklist-failures/F-D1-003_cancel-discards-without-confirmation.png` | Cancel returns to list without confirmation after form data was entered. |

## 5. Checklist Execution Table - D1

| Screen | Checklist ID | Result | Evidence | Notes | Screenshot ref | Finding ID |
| --- | --- | --- | --- | --- | --- | --- |
| D1 Create support request | IA-01-01 | Pass | Header, footer, typography and spacing are consistent with the support list and dashboard. | Layout remains consistent in D1. | E-D1-001 |  |
| D1 Create support request | IA-01-02 | Pass | Terms `Support requests`, `Create support request`, `Request type`, `Complaint`, `Support` are used consistently in visible D1 UI. | Browser title is Vietnamese, but visible UI terms are understandable. | E-D1-001 |  |
| D1 Create support request | IA-01-03 | Pass | Primary `Submit request` button is visually stronger than `Cancel`; `Back` is secondary. | Primary and secondary actions are distinguishable. | E-D1-001 |  |
| D1 Create support request | IA-01-04 | Fail | Request type invalid state and alert are shown, but the category/default selection state is confusing and inconsistent with the visible value. | The UI displays a sample/default-looking value while native validation still treats the select as empty. | F-D1-002 | F-D1-002 |
| D1 Create support request | IA-01-05 | Pass | Labels, placeholder text, buttons and alerts are readable on desktop and mobile. | No unreadable low-contrast text observed during D1 run. | E-D1-001, E-D1-003 |  |
| D1 Create support request | IA-01-06 | N/A | Checklist item is about event cards/lists. | D1 is a support request form, not an event card/list. |  |  |
| D1 Create support request | IA-01-07 | Pass | Attachment remove action has accessible label `Remove D1_create_request_overview.png`. | Icon/action is identifiable through label. | E-D1-002 |  |
| D1 Create support request | IA-01-08 | Pass | Inputs, buttons, upload zone and menu are keyboard/click focusable; invalid select exposes invalid state. | Interaction states are observable. | E-D1-003 |  |
| D1 Create support request | IA-01-09 | Pass | The form keeps entered title, description and attachment after a failed submit. | Data was preserved after API/category failure. | F-D1-002 |  |
| D1 Create support request | IA-01-10 | Pass | At `390x844`, fields stack and no horizontal overflow is visible. | Mobile layout is usable. | E-D1-003 |  |
| D1 Create support request | IA-01-11 | Pass | Form is grouped into request type, issue, description, attachments and actions. | Density is manageable. | E-D1-001 |  |
| D1 Create support request | IA-01-12 | Pass | D1 is reachable quickly from user menu `Support requests -> Create request`. | No unnecessary multi-step navigation observed. | E-D1-001 |  |
| D1 Create support request | IA-01-13 | N/A | Language switching was not part of this D1 run. | Needs a separate EN/VI execution pass if required. |  |  |
| D1 Create support request | IA-02-01 | Pass | Required fields have `*`: request type, issue, detailed description. | Required fields are visible before submit. | E-D1-001 |  |
| D1 Create support request | IA-02-02 | Pass | Labels are visible and placed near their controls; form does not rely only on placeholders. | Placeholders provide examples, not sole field meaning. | E-D1-001 |  |
| D1 Create support request | IA-02-03 | Pass | Request type uses a select; issue uses text input; description uses textarea; attachment uses file input. | Control types fit the data. | E-D1-001 |  |
| D1 Create support request | IA-02-04 | Fail | Submit empty form triggers validation only after submit; submit button is enabled while required fields are empty. | Error prevention is weak because invalid submit is allowed. | F-D1-001 | F-D1-001 |
| D1 Create support request | IA-02-05 | Fail | Empty-form error is a global alert; field-level guidance is incomplete, especially for request type/category recovery. | Users must infer which field to fix and why the displayed category value is invalid. | F-D1-001, F-D1-002 | F-D1-001, F-D1-002 |
| D1 Create support request | IA-02-06 | Pass | Entered title, detailed description and image remained visible after failed submit. | No data loss on validation/API error path. | F-D1-002 |  |
| D1 Create support request | IA-02-07 | Pass | D1 form is short and grouped logically; no unnecessary long sections. | Grouping matches the support request mental model. | E-D1-001 |  |
| D1 Create support request | IA-02-08 | Pass | Keyboard interaction can focus the request type and select an option; tab order follows form order. | Keyboard selection succeeded and allowed final submit. | E-D1-002 |  |
| D1 Create support request | IA-02-09 | Fail | `Submit request` remains enabled when required fields are empty. | User can trigger avoidable validation failure. | F-D1-001 | F-D1-001 |
| D1 Create support request | IA-02-10 | Fail | Request type appears to show `For example: Support`, but actual selected value is empty until user explicitly selects an option. | Default/signifier misleads users and caused `400` category validation. | F-D1-002 | F-D1-002 |
| D1 Create support request | IA-02-11 | Fail | `Cancel` discards a filled form with selected attachment without confirmation. | User can lose unsaved support request content accidentally. | F-D1-003 | F-D1-003 |
| D1 Create support request | IA-02-12 | Pass | Upload area states accepted formats `JPG, PNG, GIF or WEBP`, up to 5 images and 5 MB each; valid PNG upload shows thumbnail and remove button. | Upload constraints and preview are visible. | E-D1-002 |  |
| D1 Create support request | IA-02-13 | N/A | Checklist item is about rich-text editor. | D1 uses a plain detailed-description textarea, not rich text. |  |  |
| D1 Create support request | IA-03-01 | Pass | User menu exposes `Events`, `Calendar`, `Saved Events`, `User guide`, `Support requests`, profile and notifications. | Role-appropriate support entry exists for the user. | E-D1-001 |  |
| D1 Create support request | IA-03-02 | Pass | H1 `Create support request`, page title and URL `/complaints/new` identify the current location. | User can tell they are on the create request screen. | E-D1-001 |  |
| D1 Create support request | IA-03-03 | N/A | Checklist item concerns event list/detail filter preservation. | D1 is not an event list/detail browsing flow. |  |  |
| D1 Create support request | IA-03-04 | Pass | Navigation/action labels are specific: `Back`, `Cancel`, `Submit request`, `Create request`. | No vague `Click here` labels observed. | E-D1-001 |  |
| D1 Create support request | IA-03-05 | Pass | User account can access user support pages; admin-only support management is not exposed in this user flow. | No role mismatch observed for D1. | E-D1-001 |  |
| D1 Create support request | IA-03-06 | N/A | Search/filter belongs to support list D2, not create form D1. | Not applicable to D1 form execution. |  |  |
| D1 Create support request | IA-03-07 | N/A | Pagination belongs to support list D2, not create form D1. | Not applicable to D1 form execution. |  |  |
| D1 Create support request | IA-03-08 | N/A | D1 is a one-page form, not a multi-step registration/checkout flow. | No stepper expected. |  |  |
| D1 Create support request | IA-03-09 | Fail | `Cancel` exits the filled form without warning or recovery. | Navigation can cause unsaved data loss. | F-D1-003 | F-D1-003 |
| D1 Create support request | IA-03-10 | Pass | On mobile viewport, navigation collapses into menu and does not cover the form's primary action. | D1 remains usable on phone width. | E-D1-003 |  |
| D1 Create support request | IA-03-11 | Pass | `Submit request` and `Cancel` are placed at the end of the form near the entered content. | Actions are mapped to the form context. | E-D1-001 |  |
| D1 Create support request | IA-03-12 | N/A | 404/deleted event route recovery was not relevant to D1 create form. | Not applicable. |  |  |
| D1 Create support request | IA-04-01 | Fail | Successful submit redirects and creates a pending request, but no visible success toast/banner was observed; API success message is wrongly about event review. | User gets weak closure and the backend message is wrong for support request creation. | E-D1-004 | F-D1-004 |
| D1 Create support request | IA-04-02 | Pass | Submit completed quickly; upload preview appeared after file selection. | No long loading state was needed in this run. | E-D1-002, E-D1-004 |  |
| D1 Create support request | IA-04-03 | Pass | During the observed successful submit, only one request was created. | No duplicate request was observed in the final list. | E-D1-004 |  |
| D1 Create support request | IA-04-04 | Fail | API category error returned `400`; visible recovery was limited and not clearly mapped to why the category payload was invalid. | Technical validation behavior is not translated into a clear user recovery path. | F-D1-002 | F-D1-002 |
| D1 Create support request | IA-04-05 | Fail | Empty-submit alert and invalid-category alert appear near the bottom of the form; on long form/scroll states users may miss the field context. | Alert is visible but not field-local. | F-D1-001, E-D1-003 | F-D1-001 |
| D1 Create support request | IA-04-06 | Pass | Created request appears as `Pending` with category text in the support list after submit. | Status uses visible text. | E-D1-004 |  |
| D1 Create support request | IA-04-07 | N/A | Empty state is for support list, not D1 create form. | Not applicable in this D1 execution because list had existing requests. |  |  |
| D1 Create support request | IA-04-08 | N/A | D1 has no destructive server-side action such as delete/cancel submitted request. | Cancel on unsaved form is covered by IA-02-11 and IA-03-09. |  |  |
| D1 Create support request | IA-04-09 | Fail | No undo or recovery was offered after `Cancel` discarded the filled form. | User cannot recover unsaved support request content. | F-D1-003 | F-D1-003 |
| D1 Create support request | IA-04-10 | N/A | Session-expired state was not triggered in this D1 run. | Requires separate long-session/expired-token test. |  |  |
| D1 Create support request | IA-04-11 | N/A | D1 create form does not display dynamic event capacity/status data. | Not applicable. |  |  |
| D1 Create support request | IA-04-12 | Pass | Form includes short instructions and concrete examples for issue and detailed description. | Inline guidance helps users write a useful support request. | E-D1-001 |  |
| D1 Create support request | IA-04-13 | Fail | Flow ends by redirecting to list and showing new `Pending` row, but there is no explicit visible confirmation message; API success body says `Event review saved successfully`. | Closure is present through list update but message semantics are wrong/unclear. | E-D1-004 | F-D1-004 |

## 6. Summary

| Metric | Count |
| --- | ---: |
| Checklist items total | 51 |
| Pass | 27 |
| Fail | 12 |
| N/A | 12 |
| Needs Google Form submission | 4 findings |

## 7. Findings Draft for Bug & Usability Log

| ID | Scenario/Screen | Type | Description | Steps/Heuristic | Expected | Actual | Severity | Suggested fix | Screenshot ref | Form-submission timestamp |
| --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- |
| F-D1-001 | D1 Create support request | Usability | Required-field validation is not prevented early and is shown as a global alert instead of field-local messages. | IA-02-04, IA-02-05, IA-02-09, IA-04-05. Steps: open `/complaints/new`; leave required fields empty; click `Submit request`. | Submit should be disabled until required fields are valid, or each invalid field should show an inline message near the field. | Submit remains enabled; one alert says `Request type, issue requiring support and detailed description are required.` | 2 | Disable submit until required fields are satisfied and add inline errors beside request type, issue and description. | `submission/screenshots/checklist-failures/F-D1-001_validation-not-inline.png` | `[Manual after Google Form submit]` |
| F-D1-002 | D1 Create support request | Bug | Request type appears to have a default/example value, but actual category can remain empty or invalid and submit can return `400`. | IA-01-04, IA-02-05, IA-02-10, IA-04-04. Steps: open `/complaints/new`; observe request type showing `For example: Support`; fill issue/description/upload image; submit without explicitly selecting a valid option, or use the problematic select state. | Displayed request type and submitted category should match one valid value: `SUPPORT`, `COMPLAINT`, `CONTACT`, or `OTHER`; user should get clear recovery guidance. | Network returned `POST /api/complaints => 400` with `category must be one of the following values: SUPPORT, COMPLAINT, CONTACT, OTHER`; console warning said `Select: Keys "S" passed to "selectedKeys" are not present in the collection.` | 3 | Fix select state mapping, make placeholder visually distinct from a real value, and validate category before API submit. | `submission/screenshots/checklist-failures/F-D1-002_category-submit-400-no-clear-ui-error.png` | `[Manual after Google Form submit]` |
| F-D1-003 | D1 Create support request | Usability | `Cancel` discards an in-progress support request without confirmation or recovery. | IA-02-11, IA-03-09, IA-04-09. Steps: fill issue/description, attach image, click `Cancel`. | If unsaved data exists, system should confirm before leaving or preserve draft on return. | Page immediately returned to `/complaints`; no confirmation, undo, or draft recovery was observed. | 2 | Add unsaved-changes confirmation for `Cancel`/`Back`, or save draft locally until submit/cancel confirmation. | `submission/screenshots/checklist-failures/F-D1-003_cancel-discards-without-confirmation.png` | `[Manual after Google Form submit]` |
| F-D1-004 | D1 Create support request | Bug | Successful D1 submit has wrong success semantics and weak visible closure. | IA-04-01, IA-04-13. Steps: select category via keyboard, fill valid issue/description, upload PNG, submit. | UI should show a clear support-request success message such as `Support request created successfully`, then show the new pending request. | Redirected to `/complaints?created=1` and new request appeared, but no visible success toast/banner was observed; API response body said `UPSERT_EVENT_REVIEW_SUCCESS` and `Event review saved successfully.` | 3 | Return support-specific success code/message and display a visible success toast/banner after creation. | `submission/screenshots/D1/D1_submit_success_redirect.png` | `[Manual after Google Form submit]` |

## 8. Completion Notes

- The D1 checklist execution used the shared checklist from `submission/group/gui_usability_checklist_final.md` without changing it.
- Playwright MCP was used for live EMS interaction, screenshots, responsive check, console and network evidence.
- Chrome DevTools MCP was attempted but could not start in the current environment because the tool reported a missing X server for headful browser startup.
- One real D1 test request was created under Kiên's user account: `/complaints/56`, visible as `Pending` after successful submit.
- Findings above are drafts. Kiên should review screenshots, submit confirmed findings to the Google Form, then fill the `Form-submission timestamp` values.
````

**Verdict:** [Manual by user]

**Reasoning:** [Manual by user]

**Student Fix:** [Manual by user]

### 2.2.10 Entry 10

**Prompt + Tool:**

Time: `2026-08-02 23:34 +07`
Tool: `Codex / GPT-5`
Prompt:
Dịch submission/task1B/task1b_D1.md sang tiếng Việt. Thêm rule để biết bài nộp ngôn ngữ chính là Tiếng Việt. Sau đó thêm 1 rule trong folder docs và ai-reasoning là chỉ đọc file markdown vì đọc pdf sẽ tốn token hơn.

**AI Output:** Đã dịch submission/task1B/task1b_D1.md sang tiếng Việt; thêm rule ngôn ngữ chính tiếng Việt trong submission/AGENTS.md; thêm rule ưu tiên đọc Markdown, tránh PDF khi có bản Markdown trong docs/AGENTS.md và ai-reasonin...

**Verdict:** [Manual by user]

**Reasoning:** [Manual by user]

**Student Fix:** [Manual by user]

### 2.2.11 Entry 11

**Prompt + Tool:**

Time: `2026-08-03 11:25 +07`
Tool: `Codex / GPT-5`
Prompt:
@Superpowers Đọc các file trong folder docs để hiểu bối cảnh bài tập. Thực hiện Task 1B cho Kiên trên Scene D2. Dùng submission/group/gui_usability_checklist_final.md (không thay đổi file này) để làm check list. Tạo 1 file markdown cho task1b_D2.md trong folder submission/task1B cho việc testing dựa trên checklist đó. Hãy tận dụng MCP Playwright và Chrome Devtools trong quá trình test. Thông tin link web, tài khoản admin và user đã được cung cấp trong submission/test_environment_access.md. Tuyệt đối tuân theo rule được ghi trong  submission/test_environment_access.md. Nếu cần thêm gì thì hãy yêu cầu tôi cung cấp. Format cho output của D2 cũng nên tương tự như D1.

**AI Output:**

````markdown
# Task 1B - Thực thi checklist cho D2

| Trường | Giá trị |
| --- | --- |
| Người kiểm thử | Lê Trung Kiên |
| MSSV | `23127075` |
| Kịch bản | D - Người dùng gửi yêu cầu hỗ trợ và Admin xử lý |
| Màn hình | D2 - User xem My Requests list/detail có phản hồi |
| Vai trò sử dụng | User |
| SUT | `https://prod-dev.ems-fitus.cloud` |
| Ngày kiểm thử | 2026-08-03 |
| Nguồn checklist | `submission/group/gui_usability_checklist_final.md` |
| Có sửa checklist gốc không? | Không |

## 1. Prompt đầy đủ đã dùng để AI hỗ trợ test D2

```text
@Superpowers Đọc các file trong folder docs để hiểu bối cảnh bài tập. Thực hiện Task 1B cho Kiên trên Scene D2. Dùng submission/group/gui_usability_checklist_final.md (không thay đổi file này) để làm check list. Tạo 1 file markdown cho task1b_D2.md trong folder submission/task1B cho việc testing dựa trên checklist đó. Hãy tận dụng MCP Playwright và Chrome Devtools trong quá trình test. Thông tin link web, tài khoản admin và user đã được cung cấp trong submission/test_environment_access.md. Tuyệt đối tuân theo rule được ghi trong  submission/test_environment_access.md. Nếu cần thêm gì thì hãy yêu cầu tôi cung cấp. Format cho output của D2 cũng nên tương tự như D1.
```

## 2. Nhật ký kiểm thử

| Bước | Công cụ | Quan sát |
| --- | --- | --- |
| Đọc bối cảnh HW03 | Shell `rtk` | Đã đọc tài liệu trong `docs/`, `submission/test_environment_access.md`, checklist final và file D1 để giữ đúng phạm vi Scenario D và format báo cáo. |
| Mở EMS | Playwright MCP | Mở `https://prod-dev.ems-fitus.cloud`; session hiện tại đã là user Kiên (`ltkien23@clc.fitus.edu.vn`) tại `/dashboard`. |
| Điều hướng D2 | Playwright MCP | Từ menu user mở `Support requests`; URL `/complaints`; page title `Yêu cầu hỗ trợ \| HCMUS EMS`; H1 `Support requests`. |
| Kiểm tra list My Requests | Playwright MCP | List hiển thị 2 request thuộc tài khoản Kiên: `/complaints/56` và `/complaints/55`, đều có status `Resolved`, category, title/description và submitted time. |
| Kiểm tra detail có response | Playwright MCP | Mở `/complaints/56`; page title `Chi tiết yêu cầu \| HCMUS EMS`; detail có status `Resolved`, category `Complaint`, ID `#56`, submitted time, nội dung request, attachments và mục `Support response`. |
| Kiểm tra official response | Playwright MCP | `Support response` hiển thị nội dung phản hồi chính thức: `[QA TEST - HW03 Task 1B] This is a test response to verify the submit/loading/toast behavior of the response form.` kèm hướng dẫn tạo request mới nếu cần hỗ trợ tiếp. |
| Kiểm tra attachment preview/lightbox | Playwright MCP | Click `Open attachment 1`; modal/lightbox mở ảnh lớn với tiêu đề `attachment_1` và nút `Close`; đóng modal thành công. |
| Kiểm tra search không có kết quả | Playwright MCP | Nhập `not-found-D2-2026`; URL đổi thành `/complaints?search=not-found-D2-2026&page=1`; empty state hiển thị `No requests yet`, chưa phản ánh rõ đây là trạng thái không có kết quả do filter/search. |
| Kiểm tra status filter | Playwright MCP | Dropdown status có `All statuses`, `Pending`, `Resolved`; chọn `Resolved` đổi URL thành `status=RESOLVED` và trả đúng 2 resolved requests. |
| Kiểm tra giữ ngữ cảnh khi quay lại | Playwright MCP | Mở detail từ `/complaints?status=RESOLVED&search=keyboard`; bấm `Back` trong detail đưa về `/complaints`, làm mất search/status filter đang áp dụng. |
| Kiểm tra responsive mobile | Playwright MCP | Ở viewport `390x844`, list và detail xếp dọc, không thấy cuộn ngang; tuy nhiên nút floating social links che sát vùng pagination/list và có thể cản trở thao tác ở mép phải. |
| Kiểm tra network/console | Playwright MCP | D2 APIs chính trả thành công: `GET /api/complaints/me?page=1&limit=10 => 200`, `GET /api/complaints/me/56 => 200`. Console có một lỗi cũ `GET /api/users/me => 401` trước khi D2 ổn định; không thấy lỗi API D2 khi list/detail tải. |
| Kiểm tra bằng Chrome DevTools | Chrome DevTools MCP | Không khởi động được vì môi trường báo `Missing X server to start the headful browser`; không tạo bằng chứng Chrome DevTools giả. |

## 3. Danh mục giao diện D2

| Nhóm | Thành phần D2 quan sát được |
| --- | --- |
| Màn hình và route | List `Support requests` tại `/complaints`; detail request tại `/complaints/56`; lightbox attachment trong detail. |
| Vai trò | Chỉ dùng user account của Kiên để xem requests của chính tài khoản Kiên; không thao tác dữ liệu/tài khoản người khác. |
| Luồng chính | Mở support requests, xem danh sách My Requests, search theo title/description, lọc status, mở detail, xem official response, mở/đóng attachment, quay lại list. |
| Widget | Header, user menu, H1, search textbox, status dropdown, `Create request`, request cards, status/category badges, submitted time, rows-per-page dropdown, pagination, `Back`, attachment thumbnail, lightbox modal, `Close`, floating social links. |
| Trạng thái động | List có dữ liệu, filter resolved, search no-result, detail resolved, response official, attachment lightbox, mobile responsive, API loading qua network. |

## 4. Bằng chứng screenshot

| ID bằng chứng | Đường dẫn | Mục đích |
| --- | --- | --- |
| E-D2-001 | `submission/screenshots/D2/D2_my_requests_overview.png` | Tổng quan D2 list ở desktop với 2 resolved requests của Kiên. |
| E-D2-002 | `submission/screenshots/D2/D2_detail_with_response.png` | Detail request `/complaints/56` có status, nội dung, attachment và `Support response`. |
| E-D2-003 | `submission/screenshots/D2/D2_attachment_lightbox.png` | Attachment mở trong lightbox/modal. |
| E-D2-004 | `submission/screenshots/D2/D2_search_status_filter.png` | Search `keyboard` kết hợp filter `Resolved` trả 1 kết quả. |
| E-D2-005 | `submission/screenshots/D2/D2_mobile_detail_response.png` | Detail và response ở viewport mobile `390x844`. |
| F-D2-001 | `submission/screenshots/D2/D2_back_loses_filter_context.png` | `Back` từ detail làm mất search/status filter. |
| F-D2-002 | `submission/screenshots/D2/D2_search_no_results.png` | Empty state khi search không có kết quả dùng message `No requests yet` và không có reset action rõ. |
| F-D2-003 | `submission/screenshots/D2/D2_mobile_list_layout.png` | Floating social links button chồng sát/che vùng pagination trên mobile list. |

## 5. Bảng thực thi checklist - D2

| Màn hình | Checklist ID | Kết quả | Bằng chứng | Ghi chú | Ảnh tham chiếu | ID finding |
| --- | --- | --- | --- | --- | --- | --- |
| D2 My Requests list/detail | IA-01-01 | Đạt | Header, footer, typography, card style và spacing nhất quán giữa `/complaints` và `/complaints/56`. | Bố cục D2 nhất quán với flow support user. | E-D2-001, E-D2-002 |  |
| D2 My Requests list/detail | IA-01-02 | Đạt | Thuật ngữ `Support requests`, `Resolved`, `Complaint`, `Support`, `Support response` được dùng ổn định trong list/detail. | Không thấy dùng lẫn thuật ngữ khác cho cùng trạng thái support. | E-D2-001, E-D2-002 |  |
| D2 My Requests list/detail | IA-01-03 | Đạt | `Create request` nổi bật ở list; `Back` trong detail là hành động phụ rõ ràng. | Mức nhấn thị giác phân biệt được hành động chính/phụ. | E-D2-001, E-D2-002 |  |
| D2 My Requests list/detail | IA-01-04 | Đạt | Status `Resolved` và category badge hiển thị bằng text + màu nhất quán trên list/detail. | Trạng thái chính dễ nhận biết. | E-D2-001, E-D2-002 |  |
| D2 My Requests list/detail | IA-01-05 | Đạt | Label, title, badge, timestamp và response text đọc được trên desktop/mobile. | Không thấy text tương phản quá thấp trong D2. | E-D2-001, E-D2-005 |  |
| D2 My Requests list/detail | IA-01-06 | Đạt | Card request ưu tiên status/category, title, mô tả ngắn và submitted time. | Thông tin thiết yếu của support request nằm trước. | E-D2-001 |  |
| D2 My Requests list/detail | IA-01-07 | Đạt | Attachment button có tên `Open attachment 1`; lightbox có nút `Close`. | Icon/media action có nhãn nhận diện được qua accessibility snapshot. | E-D2-003 |  |
| D2 My Requests list/detail | IA-01-08 | Đạt | Search, status dropdown, card link, pagination, attachment và close modal đều có thể tương tác. | Trạng thái focus/expanded xuất hiện khi dùng dropdown/lightbox. | E-D2-003, E-D2-004 |  |
| D2 My Requests list/detail | IA-01-09 | Đạt | Detail hiển thị lại title, ID, status, category, submitted time, description, attachment và response. | Người dùng không cần nhớ thông tin từ list khi vào detail. | E-D2-002 |  |
| D2 My Requests list/detail | IA-01-10 | Không đạt | Mobile không cuộn ngang, nhưng floating social links button che sát vùng pagination/right edge của list. | Control nổi có thể cản thao tác pagination hoặc làm người dùng tưởng là action của request. | F-D2-003 | F-D2-003 |
| D2 My Requests list/detail | IA-01-11 | Đạt | List, filters, pagination, detail header, attachments và response được tách nhóm rõ. | Mật độ nội dung vừa phải, dễ quét. | E-D2-001, E-D2-002 |  |
| D2 My Requests list/detail | IA-01-12 | Đạt | Có search, status filter, pagination và link tạo request mới. | Người dùng thường xuyên có cách truy cập nhanh request cần xem. | E-D2-001, E-D2-004 |  |
| D2 My Requests list/detail | IA-01-13 | Không áp dụng | Chưa kiểm tra chuyển đổi EN/VI trong lần chạy D2 này. | Cần lượt test i18n riêng nếu yêu cầu. |  |  |
| D2 My Requests list/detail | IA-02-01 | Không áp dụng | D2 không có form required-field để submit dữ liệu mới. | Search/filter không phải form bắt buộc. |  |  |
| D2 My Requests list/detail | IA-02-02 | Đạt | Search textbox có label `Search title or description` nằm gần input. | Không chỉ dựa vào placeholder. | E-D2-001 |  |
| D2 My Requests list/detail | IA-02-03 | Đạt | Search dùng textbox; status và rows per page dùng combobox/dropdown; page dùng spinbutton. | Kiểu control phù hợp dữ liệu lọc/danh sách. | E-D2-001, E-D2-004 |  |
| D2 My Requests list/detail | IA-02-04 | Không áp dụng | Không có dữ liệu nhập hợp lệ/không hợp lệ cần validate trước submit ở D2. | Search không có rule invalid cụ thể. |  |  |
| D2 My Requests list/detail | IA-02-05 | Không áp dụng | Không phát sinh validation error form trong D2. | Không có field lỗi để kiểm tra error placement. |  |  |
| D2 My Requests list/detail | IA-02-06 | Không áp dụng | D2 không submit form nên không có nhánh submit thất bại cần giữ dữ liệu nhập. | Search/filter preservation được đánh giá ở IA-03. |  |  |
| D2 My Requests list/detail | IA-02-07 | Đạt | Filter/search nằm cùng vùng đầu trang; list kết quả và pagination được gom trong region `My support requests`. | Nhóm control theo nhiệm vụ tìm/xem request. | E-D2-001 |  |
| D2 My Requests list/detail | IA-02-08 | Đạt | Các control chính xuất hiện trong accessibility tree theo thứ tự search, status, create request, list, pagination. | Thứ tự focus dự kiến đi theo luồng đọc tự nhiên. | E-D2-001 |  |
| D2 My Requests list/detail | IA-02-09 | Không áp dụng | D2 không có nút submit/save form. | Không áp dụng cho list/detail read-only. |  |  |
| D2 My Requests list/detail | IA-02-10 | Đạt | Status filter mặc định là `All statuses`, và khi chọn `Resolved` trạng thái đang áp dụng hiển thị ngay trên nút. | Default/filter state dễ hiểu. | E-D2-001, E-D2-004 |  |
| D2 My Requests list/detail | IA-02-11 | Không áp dụng | D2 không có cancel/reset form có nguy cơ mất dữ liệu nhập. | Trường hợp mất filter được đánh giá ở navigation. |  |  |
| D2 My Requests list/detail | IA-02-12 | Đạt | Detail hiển thị attachment thumbnail; click mở lightbox ảnh lớn và đóng được. | Media preview/read path dùng được. | E-D2-002, E-D2-003 |  |
| D2 My Requests list/detail | IA-02-13 | Không áp dụng | D2 không có rich-text editor. | Response chỉ hiển thị read-only text. |  |  |
| D2 My Requests list/detail | IA-03-01 | Đạt | User menu có `Support requests`; không thấy menu admin trong user flow D2. | Điều hướng phản ánh vai trò user. | E-D2-001 |  |
| D2 My Requests list/detail | IA-03-02 | Đạt | H1 `Support requests`, page title và URL `/complaints`/`/complaints/56` cho biết vị trí hiện tại. | Người dùng biết đang ở list hay detail. | E-D2-001, E-D2-002 |  |
| D2 My Requests list/detail | IA-03-03 | Không đạt | Mở detail từ list đang filter `status=RESOLVED&search=keyboard`, sau đó bấm `Back` thì quay về `/complaints` và mất filter. | Người dùng phải thiết lập lại search/status khi quay lại list. | F-D2-001, E-D2-004 | F-D2-001 |
| D2 My Requests list/detail | IA-03-04 | Đạt | Nhãn cụ thể: `Support requests`, `Create request`, `Back`, `Open attachment 1`, `Close`. | Không thấy link/nút mơ hồ kiểu `Click here`. | E-D2-001, E-D2-003 |  |
| D2 My Requests list/detail | IA-03-05 | Đạt | User chỉ thấy và mở requests của chính tài khoản Kiên trong list/detail D2. | Không thấy chức năng admin hoặc dữ liệu người khác trong D2. | E-D2-001 |  |
| D2 My Requests list/detail | IA-03-06 | Không đạt | Search/filter dễ thấy và URL phản ánh criteria, nhưng không có nút clear/reset rõ; khi no-result UI khuyến khích tạo request thay vì sửa/clear filter. | Recovery khỏi trạng thái lọc rỗng chưa đủ rõ. | F-D2-002 | F-D2-002 |
| D2 My Requests list/detail | IA-03-07 | Đạt | Pagination hiển thị `1-2 of 2 results`, rows per page, current page và disabled previous/next khi chỉ có một trang. | Phạm vi kết quả rõ ràng. | E-D2-001 |  |
| D2 My Requests list/detail | IA-03-08 | Không áp dụng | D2 không phải luồng đăng ký/checkout nhiều bước. | Không cần stepper. |  |  |
| D2 My Requests list/detail | IA-03-09 | Không đạt | `Back` từ detail làm mất filter/search đang áp dụng ở list. | Điều hướng quay lại không bảo toàn ngữ cảnh người dùng đang xem. | F-D2-001 | F-D2-001 |
| D2 My Requests list/detail | IA-03-10 | Không đạt | Mobile navigation xếp dọc dùng được, nhưng floating social links button nằm chồng sát pagination/list card. | Control nổi có thể che thao tác ở màn hình nhỏ. | F-D2-003 | F-D2-003 |
| D2 My Requests list/detail | IA-03-11 | Đạt | `Back` đặt đầu detail; attachment action nằm trong section `Attachments`; response nằm trong section `Support response`. | Hành động/nội dung liên quan đặt đúng ngữ cảnh. | E-D2-002, E-D2-003 |  |
| D2 My Requests list/detail | IA-03-12 | Không áp dụng | Không kiểm tra URL không tồn tại hoặc request đã bị xóa trong lần chạy D2. | Cần test riêng để tránh đụng dữ liệu không thuộc tài khoản Kiên. |  |  |
| D2 My Requests list/detail | IA-04-01 | Đạt | List và detail tải thành công; resolved request hiển thị response chính thức rõ. | Người dùng biết request đã được xử lý và nội dung phản hồi là gì. | E-D2-002 |  |
| D2 My Requests list/detail | IA-04-02 | Đạt | Các API list/detail trả `200`; không thấy trạng thái treo trong lần test. | Không phát sinh thao tác lâu cần progress đặc biệt. | E-D2-001, E-D2-002 |  |
| D2 My Requests list/detail | IA-04-03 | Không áp dụng | D2 không có submit action. | Không có nguy cơ gửi trùng trong màn hình read-only. |  |  |
| D2 My Requests list/detail | IA-04-04 | Đạt | `GET /api/complaints/me` và `GET /api/complaints/me/56` trả `200`; UI không hiển thị lỗi kỹ thuật khi tải list/detail. | D2 không lộ mã lỗi cho người dùng trong lần chạy này. | E-D2-001, E-D2-002 |  |
| D2 My Requests list/detail | IA-04-05 | Không áp dụng | Không có toast/banner kết quả trong luồng read-only D2. | Floating social button được đánh giá ở responsive/navigation. |  |  |
| D2 My Requests list/detail | IA-04-06 | Đạt | Status `Resolved` hiển thị bằng badge text/màu trên cả list và detail. | Trạng thái request dễ quét. | E-D2-001, E-D2-002 |  |
| D2 My Requests list/detail | IA-04-07 | Không đạt | Khi search không có kết quả, empty state ghi `No requests yet` dù tài khoản thật sự có requests và chỉ đang bị filter. | Message có thể làm người dùng hiểu nhầm dữ liệu đã mất/chưa từng tạo request. | F-D2-002 | F-D2-002 |
| D2 My Requests list/detail | IA-04-08 | Không áp dụng | D2 không có hành động nguy hiểm như delete/cancel submitted request. | Không có confirmation destructive action cần kiểm tra. |  |  |
| D2 My Requests list/detail | IA-04-09 | Không áp dụng | D2 không có undo cho thao tác destructive; mất filter đã được ghi ở IA-03-03/IA-03-09. | Không áp dụng riêng cho D2 read-only. |  |  |
| D2 My Requests list/detail | IA-04-10 | Không áp dụng | Không kích hoạt trạng thái session expired trong lần chạy D2. | Console có 401 cũ từ `/api/users/me`, nhưng D2 APIs vẫn tải `200`. |  |  |
| D2 My Requests list/detail | IA-04-11 | Không áp dụng | Không kiểm tra cập nhật realtime khi admin đổi trạng thái trong cùng lúc. | D2 hiện chỉ xem resolved data đã có. |  |  |
| D2 My Requests list/detail | IA-04-12 | Đạt | Empty state có hướng dẫn tạo request; detail response có câu hướng dẫn `If you need further assistance, please create a new request.` | Có trợ giúp ngắn đúng ngữ cảnh cơ bản. | E-D2-002, F-D2-002 |  |
| D2 My Requests list/detail | IA-04-13 | Đạt | Request resolved có response chính thức và lời nhắc bước tiếp theo nếu cần hỗ trợ thêm. | Luồng xem phản hồi có closure rõ trong detail. | E-D2-002 |  |

## 6. Tóm tắt

| Chỉ số | Số lượng |
| --- | ---: |
| Tổng checklist items | 51 |
| Đạt | 29 |
| Không đạt | 6 |
| Không áp dụng | 16 |
| Cần submit Google Form | 3 findings |

## 7. Draft finding cho Bug & Usability Log

| ID | Kịch bản/Màn hình | Loại | Mô tả | Bước/Heuristic | Kỳ vọng | Thực tế | Mức độ nghiêm trọng | Đề xuất sửa | Ảnh tham chiếu | Thời điểm submit Form |
| --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- |
| F-D2-001 | D2 My Requests list/detail | Usability | `Back` từ request detail làm mất ngữ cảnh search/status filter của list. | IA-03-03, IA-03-09. Steps: mở `/complaints?status=RESOLVED&search=keyboard`; mở request `/complaints/56`; bấm `Back`. | Quay lại đúng list đã filter, giữ `search=keyboard` và `status=RESOLVED`. | Trang quay về `/complaints`, search textbox rỗng và status trở lại `All statuses`. | 2 | Lưu query trước khi vào detail và để `Back` dùng `router.back()` hoặc link về URL list có query hiện tại. | `submission/screenshots/D2/D2_back_loses_filter_context.png` | `[Điền thủ công sau khi submit Google Form]` |
| F-D2-002 | D2 My Requests list/detail | Usability | Empty state khi search/filter không có kết quả dùng message gây hiểu nhầm là tài khoản chưa có request. | IA-03-06, IA-04-07. Steps: mở `/complaints`; nhập search `not-found-D2-2026`. | Empty state nên nói rõ `No matching requests found`, hiển thị criteria đang áp dụng và có nút `Clear filters`. | UI hiển thị `No requests yet` và `Create a request when you need help.` dù tài khoản vẫn có 2 requests khi bỏ search. | 2 | Tách empty state thật sự chưa có dữ liệu khỏi no-result do filter/search; thêm `Clear search`/`Clear filters`. | `submission/screenshots/D2/D2_search_no_results.png` | `[Điền thủ công sau khi submit Google Form]` |
| F-D2-003 | D2 My Requests list/detail | Usability | Floating social links button chồng sát/che vùng thao tác ở mobile list. | IA-01-10, IA-03-10. Steps: resize viewport `390x844`; mở `/complaints`; quan sát cuối list/pagination. | Floating button nên tránh vùng pagination/card content hoặc tự ẩn/đổi vị trí trên mobile. | Nút social links màu xanh nằm ở mép phải vùng card/pagination, có thể che hoặc gây nhầm với action của request. | 2 | Đặt offset cao hơn pagination, giới hạn trong footer, hoặc ẩn social floating button trên các trang tác vụ có pagination ở mobile. | `submission/screenshots/D2/D2_mobile_list_layout.png` | `[Điền thủ công sau khi submit Google Form]` |

## 8. Ghi chú hoàn tất

- Lần thực thi checklist D2 dùng checklist shared từ `submission/group/gui_usability_checklist_final.md` và không sửa file này.
- Playwright MCP đã được dùng để tương tác EMS thật, lấy accessibility snapshot, kiểm tra search/filter/detail/lightbox/mobile, chụp screenshot, và kiểm tra console/network.
- Chrome DevTools MCP đã được thử nhưng không khởi động được trong môi trường hiện tại vì tool báo thiếu X server cho headful browser startup.
- Không tạo support request mới và không dùng admin account trong lần D2 này vì tài khoản Kiên đã có resolved requests đủ để kiểm tra official response.
- Các findings ở trên là draft. Kiên cần review screenshot, submit các finding đã xác nhận lên Google Form, rồi điền giá trị `Form-submission timestamp`.
````

**Verdict:** [Manual by user]

**Reasoning:** [Manual by user]

**Student Fix:** [Manual by user]

## 3. Tổng kết độ chính xác AI
- Các nội dung AI tạo đã được rà soát với yêu cầu bài làm: `[TODO]`
- Mức độ chính xác/độ hữu ích tổng quan: `[TODO]`
- Giới hạn hoặc rủi ro còn lại: `[TODO]`

## 4. Kết luận
`[TODO]`

## 5. Disclosure
`[TODO]`
