# Reference Sources và AI Prompts dùng để xây dựng GUI Checklist

Tài liệu độc lập này tổng hợp danh sách nguồn tham khảo, prompt AI thật và quá trình hoàn thiện checklist GUI usability cho EMS. Tất cả thông tin cần nộp được trình bày trực tiếp trong tệp, không phụ thuộc vào artefact ở thư mục khác.

## 1. Danh sách nguồn tham khảo

| ID     | Nguồn                                                                              | Nội dung được dùng trong checklist                                                                                                                                                                    | Liên kết/artefact                                                                                                    |
| ------ | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| REF-01 | Jakob Nielsen, *10 Usability Heuristics for User Interface Design*                 | Visibility of system status; match with the real world; user control; consistency; error prevention/recovery; recognition rather than recall; flexibility; minimalist design; help and documentation. | [Nielsen Norman Group](https://www.nngroup.com/articles/ten-usability-heuristics/)                                   |
| REF-02 | Ben Shneiderman, *The Eight Golden Rules of Interface Design*                      | Consistency; shortcuts; informative feedback; dialog closure; error prevention; easy reversal; user control; giảm tải trí nhớ ngắn hạn.                                                               | [University of Maryland](https://www.cs.umd.edu/users/ben/goldenrules.html)                                          |
| REF-03 | Don Norman, *The Design of Everyday Things, Revised and Expanded Edition*          | Signifiers, affordances, mapping, constraints, feedback và conceptual model.                                                                                                                          | [JND.org](https://jnd.org/books/the-design-of-every-things-revised-and-expanded-edition/)                            |
| REF-04 | Basic Books/Hachette Book Group, trang thư mục của *The Design of Everyday Things* | Đối chiếu thông tin xuất bản của tài liệu Norman được dùng làm nền tảng lý thuyết.                                                                                                                    | [Hachette Book Group](https://www.hachettebookgroup.com/titles/don-norman/the-design-of-every-things/9780465050659/) |
| REF-05 | UX Magazine, *Understanding Don Norman's Principles of Interaction*                | Diễn giải bổ sung về signifiers, mapping, feedback và các nguyên lý tương tác của Norman.                                                                                                             | [UX Magazine](https://uxmag.com/articles/understanding-don-normans-principles-of-interaction)                        |
| REF-06 | Đề HW03 GUI & Usability Testing on EMS                                             | Yêu cầu checklist lớn hơn 40 mục, bao phủ IA-01 đến IA-04, có nguồn tham khảo, prompt AI và phần bổ sung/review thủ công.                                                                             | `2026.HW03.GUI Usability EMS_En.md`                                                                                  |
| REF-07 | Tài liệu giới thiệu EMS                                                            | Các nhóm chức năng, vai trò và luồng nghiệp vụ EMS dùng để làm checklist cụ thể hơn cho hệ thống.                                                                                                     | `HW03_EMS_Intro_EN.md`                                                                                                |

Chỉ các nguồn có liên kết hoặc artefact kiểm chứng được mới được ghi ở trên. Không đưa “course slides” vào danh sách vì hai tệp nguồn không cung cấp tên hoặc đường dẫn slide cụ thể.

## 2. Prompt AI đã dùng để tạo checklist

| Trường          | Nội dung                                                |
| --------------- | ------------------------------------------------------- |
| Prompt ID       | PROMPT-01                                               |
| Công cụ/model   | Codex / GPT-5, sử dụng Superpowers plugin               |
| Ngày giờ        | 2026-07-26 15:23 +0700                                  |
| Nguồn đối chiếu | Prompt nguyên văn được lưu trực tiếp trong tài liệu này |

```text
[@superpowers](plugin://superpowers@openai-api-curated) Tạo một danh sách kiểm tra (checklist) tính khả dụng của GUI (GUI usability) để kiểm thử ứng dụng web Hệ thống Quản lý Sự kiện (Event Management System).
Danh sách kiểm tra phải có hơn 40 mục và bao gồm:
- IA-01 Các tiêu chuẩn UI chung,
- IA-02 Biểu mẫu,
- IA-03 Điều hướng,
- IA-04 Phản hồi và trạng thái hệ thống.
Xây dựng danh sách kiểm tra dựa trên các nguyên tắc Heuristic của Nielsen, các nguyên lý của Norman, và 8 quy tắc vàng của Shneiderman.
Trả kết quả dưới dạng bảng Markdown với các cột: ID, Khía cạnh giao diện (Interface Aspect), Mục kiểm tra (Checklist Item), Tiêu chuẩn đối chiếu (Reference), Lý do (Rationale).
Output sẽ nằm trong folder submission. Nhớ trích nguồn tham khảo.
```

Không có PROMPT-02 trong dữ liệu nguồn. Vì vậy tài liệu này không tạo thêm prompt thay thế cho placeholder cũ.

## 3. Output AI và kết quả sau khi review

| Giai đoạn                 | IA-01 | IA-02 | IA-03 | IA-04 | Tổng |
| ------------------------- | ----: | ----: | ----: | ----: | ---: |
| Bản nháp do AI tạo        |    12 |    12 |    12 |    12 |   48 |
| Checklist cuối sau review |    13 |    13 |    12 |    13 |   51 |

Output AI ban đầu là bảng Markdown 48 mục, bao phủ đủ bốn khía cạnh và có các cột ID, Interface Aspect, Checklist Item, Reference và Rationale. Output được dùng làm bản nháp; sau bước review thủ công, ba mục đặc thù được bổ sung và các reference chưa chính xác được sửa để tạo bản checklist cuối gồm 51 mục.

## 4. Các mục được bổ sung ngoài output AI

| Checklist ID | Mục bổ sung                                                                                             | Lý do AI bỏ sót                                                                                         | Liên hệ đặc thù EMS                                                                                         |
| ------------ | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| IA-01-13     | Kiểm tra chuyển đổi ngôn ngữ EN/VI đồng bộ, không còn văn bản chưa dịch và không làm vỡ bố cục.         | Prompt chỉ yêu cầu bốn nhóm tiêu chí tổng quát, chưa yêu cầu kiểm tra i18n hoặc language switch cụ thể. | EMS có nút chuyển đổi EN/VI; lỗi dịch thiếu hoặc thay đổi độ dài văn bản có thể làm sai nội dung và bố cục. |
| IA-02-13     | Kiểm tra Rich-Text editor khi định dạng, dán nội dung và xem lại, tránh mất định dạng hoặc lộ HTML thô. | AI có đề cập form và upload nhưng chưa bao phủ rủi ro riêng của trình soạn thảo Rich-Text.              | Màn hình tạo/sửa sự kiện của EMS có Rich-Text editor cho phần mô tả.                                        |
| IA-04-13     | Kiểm tra điểm kết thúc rõ ràng cho quy trình dài, kèm kết quả và gợi ý bước tiếp theo.                  | Output ban đầu tập trung vào toast và trạng thái cục bộ, chưa nhấn mạnh closure của toàn bộ quy trình.  | Các luồng tạo sự kiện, đăng ký hoặc mua vé cần xác nhận rõ để người dùng biết tác vụ đã hoàn tất.           |

## 5. Các chỉnh sửa reference sau khi review

| Checklist ID | Chỉnh sửa trong bản cuối                                         | Lý do                                                                                                         |
| ------------ | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| IA-01-02     | Giữ và nhấn mạnh tính nhất quán của thuật ngữ miền nghiệp vụ.    | EMS có nhiều nhãn nghiệp vụ và nhóm người dùng; thuật ngữ cần được dùng ổn định.                              |
| IA-01-04     | Bổ sung `Nielsen: Visibility of system status`.                  | Màu trạng thái vừa liên quan đến consistency vừa giúp trạng thái hiện tại dễ nhận biết.                       |
| IA-01-06     | Đổi `Norman: Discoverability` thành `Norman: Conceptual model`.  | Thứ tự ưu tiên thông tin phản ánh cách người dùng hiểu cấu trúc nội dung hơn là khả năng phát hiện chức năng. |
| IA-02-10     | Đổi `Norman: Knowledge in the world` thành `Norman: Signifiers`. | Default và gợi ý nhập liệu đóng vai trò tín hiệu hướng dẫn thao tác.                                          |
| IA-04-04     | Bỏ `Norman: Human-centered design`, chỉ giữ Nielsen.             | Đây không phải một nguyên lý Norman cụ thể trong bộ reference được sử dụng.                                   |
| IA-04-07     | Bỏ `Norman: Discoverability`, chỉ giữ Nielsen.                   | Empty state phù hợp trực tiếp hơn với help/documentation và phục hồi ngữ cảnh.                                |
