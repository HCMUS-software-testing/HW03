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

## 3. Tổng kết độ chính xác AI
- Các nội dung AI tạo đã được rà soát với yêu cầu bài làm: `[TODO]`
- Mức độ chính xác/độ hữu ích tổng quan: `[TODO]`
- Giới hạn hoặc rủi ro còn lại: `[TODO]`

## 4. Kết luận
`[TODO]`

## 5. Disclosure
`[TODO]`
