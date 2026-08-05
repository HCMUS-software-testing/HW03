# Task 3 - Checklist Scope Mapping

Task 3 vẫn dựa trên checklist gốc `submission/group/gui_usability_checklist_final.md`, nhưng mục tiêu chính là cross-browser/cross-platform. Vì vậy, khi chạy trên từng OS/browser/device, ưu tiên các item có khả năng thay đổi theo browser, viewport, input method hoặc render engine.

## 1. Checklist item nên kiểm tra trong Task 3

| Nhóm | Checklist ID | Vì sao liên quan compatibility |
| --- | --- | --- |
| Bố cục và nhất quán | `IA-01-01`, `IA-01-03`, `IA-01-05`, `IA-01-08`, `IA-01-10`, `IA-01-13` | Dễ phát sinh khác biệt theo browser/viewport: spacing, font, contrast, hover/focus, responsive, EN/VI text wrapping. |
| Form và input | `IA-02-01` đến `IA-02-12` | D1 có select, textbox, textarea, upload ảnh; D2/D3 có search/filter/dropdown/date/pagination. Các control này có thể khác trên mobile browser. |
| Điều hướng | `IA-03-01`, `IA-03-02`, `IA-03-05`, `IA-03-06`, `IA-03-09`, `IA-03-10` | Sidebar/menu, tabs, back behavior, filter state và mobile navigation dễ lỗi khi đổi thiết bị. |
| Feedback/trạng thái | `IA-04-01` đến `IA-04-07`, `IA-04-10` | Toast, badge, loading, empty state, session/auth và status render cần ổn định trên các môi trường. |

## 2. Item thường N/A cho Scenario D Task 3

| Checklist ID | Lý do N/A hoặc chỉ kiểm tra khi có màn hình tương ứng |
| --- | --- |
| `IA-02-13` | Rich-text editor thuộc tạo/sửa event hoặc admin detail response nếu có editor; D1-D3 hiện không dùng rich-text editor trong scope đang chọn. |
| `IA-03-08` | Luồng support D1-D3 không phải registration/checkout nhiều bước nên không có stepper. |
| `IA-04-08` | D1-D3 không thực hiện hành động nguy hiểm như delete/cancel server-side trong matrix compatibility. |
| `IA-04-09` | Chỉ áp dụng nếu cell có thao tác mất dữ liệu hoặc có undo/recovery; nếu chỉ xem list/detail thì N/A. |
| `IA-04-11` | Chỉ áp dụng nếu test cập nhật realtime/stale data giữa user và admin cùng lúc; không bắt buộc trong matrix tối thiểu. |
| `IA-04-12`, `IA-04-13` | Áp dụng theo ngữ cảnh: D1 có hướng dẫn/closure sau submit; D2 có response closure; D3 list/filter thường không phải quy trình dài. |

## 3. Cách đánh giá một cell

| Kết quả | Điều kiện |
| --- | --- |
| `Pass` | Màn hình tải được, URL đúng, account đúng, layout không vỡ, nội dung chính đọc được, control chính thao tác được, không có khác biệt browser/device gây cản task. |
| `Fail` | Có lỗi render/hành vi rõ trên cell đó: tràn ngang, sidebar che content, text overlap, nút không bấm được, upload/search/filter/tab không hoạt động, toast che nội dung, modal/lightbox không đóng được, hoặc lỗi chỉ xuất hiện trên môi trường đó. |
| `N/A` | Checklist item không tồn tại trong màn hình/cell đang test, ví dụ rich-text editor ở D1-D3. |
| `Needs review` | Quan sát chưa đủ vì TestingBot/cloud session lỗi, screenshot thiếu URL/overlay/device identity, hoặc chưa thao tác được đủ flow. Không nên nộp trạng thái này trong report cuối. |

## 4. Liên hệ với findings Task 1B

Các lỗi đã thấy ở Task 1B nên được kiểm tra lại trong Task 3 nếu chúng có thể nặng hơn trên thiết bị/browser khác:

| Finding Task 1B | Cần chú ý trong Task 3 |
| --- | --- |
| `F-D1-001` validation không inline | Trên phone/tablet, alert chung có dễ bị khuất hoặc khó thấy không. |
| `F-D1-002` request type/category gây lỗi submit | Select có hoạt động khác nhau trên Safari/iOS, Samsung Internet hoặc Firefox Android không. |
| `F-D1-003` cancel mất dữ liệu | Back/cancel trên mobile browser có dễ bấm nhầm hơn không. |
| `F-D2-001` back mất filter context | Back behavior trên mobile Samsung Internet và tablet Android Chrome có giữ query/history khác desktop không. |
| `F-D2-003` floating social links che pagination | Kiểm tra kỹ trên phone/tablet vì đây là lỗi responsive. |
| `F-D3-003` admin mobile sidebar chiếm ngang | Kiểm tra trên Android phone, iOS phone và tablet; đây có thể là finding compatibility chính của D3. |
