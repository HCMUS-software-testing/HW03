# Compatibility Matrix Template

## 1. Test Context

| Trường | Giá trị |
| --- | --- |
| Target URL | `[Điền URL hệ thống cần test]` |
| Scope | `[Điền flow, route, screen hoặc scenario cần test]` |
| Authentication required | `Yes / No` |
| Test account / role | `[Điền nếu có]` |
| Tester | `[Điền tên người test]` |
| Test date | `[YYYY-MM-DD]` |
| Evidence watermark | `[Tùy chọn]` |

## 2. Coverage Rules

Matrix này phải bảo đảm:

| Dimension | Coverage bắt buộc |
| --- | --- |
| OS | Có đủ `Windows`, `Linux`, `Android` |
| Browser | Có đủ `Edge`, `Opera`, `Firefox`, `Samsung Internet`, `Chrome` |
| Device class | Có đủ `Desktop/Laptop`, `Tablet`, `Phone` |
| Evidence | Mỗi cell có screenshot hoặc link evidence |
| Result | Mỗi cell có `Pass`, `Fail` hoặc `Needs review` |

## 3. Pairwise Matrix Đề Xuất

| Cell ID | Environment Name | OS | Browser | Device class | Viewport / Device profile | Lý do chọn |
| --- | --- | --- | --- | --- | --- | --- |
| `CP-01` | Linux Firefox Desktop | `Linux` | `Firefox` | `Desktop/Laptop` | `1920x1080` | Phủ Gecko engine trên desktop non-Windows. |
| `CP-02` | Windows Edge Desktop | `Windows` | `Edge` | `Desktop/Laptop` | `1920x1080` | Phủ browser mặc định trên Windows. |
| `CP-03` | Windows Opera Desktop | `Windows` | `Opera` | `Desktop/Laptop` | `1600x900` | Phủ thêm browser Chromium khác Edge/Chrome. |
| `CP-04` | Android Samsung Tablet | `Android` | `Samsung Internet` | `Tablet` | `800x1280` | Phủ tablet Android với browser vendor-specific. |
| `CP-05` | Android Chrome Phone | `Android` | `Chrome` | `Phone` | `390x844` | Phủ mobile Android phổ biến nhất. |

## 4. Execution Table

| Cell ID | Screen / Flow | Preconditions | Result | Screenshot ref | Defect ID | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `CP-01` | `[Điền]` | `[Điền]` | `[Pass/Fail/Needs review]` | `[Điền link/path]` | `[Điền nếu có]` | `[Quan sát chính]` |
| `CP-02` | `[Điền]` | `[Điền]` | `[Pass/Fail/Needs review]` | `[Điền link/path]` | `[Điền nếu có]` | `[Quan sát chính]` |
| `CP-03` | `[Điền]` | `[Điền]` | `[Pass/Fail/Needs review]` | `[Điền link/path]` | `[Điền nếu có]` | `[Quan sát chính]` |
| `CP-04` | `[Điền]` | `[Điền]` | `[Pass/Fail/Needs review]` | `[Điền link/path]` | `[Điền nếu có]` | `[Quan sát chính]` |
| `CP-05` | `[Điền]` | `[Điền]` | `[Pass/Fail/Needs review]` | `[Điền link/path]` | `[Điền nếu có]` | `[Quan sát chính]` |

## 5. Compatibility Checklist Focus

Dùng bảng này để nhắc nhanh các loại vấn đề cần quan sát trong từng cell.

| Nhóm kiểm tra | Câu hỏi |
| --- | --- |
| Layout | Có vỡ layout, overlap, misalignment hoặc khoảng trắng bất thường không? |
| Typography | Text có bị cắt, xuống dòng xấu, quá nhỏ hoặc khó đọc không? |
| Navigation | Menu, tab, breadcrumb, back action có dùng được trên môi trường đó không? |
| Form controls | Input, dropdown, radio, checkbox, datepicker, upload control có thao tác đúng không? |
| Responsive behavior | Sidebar, modal, drawer, sticky header/footer có hiển thị đúng không? |
| Media | Image, icon, preview, attachment, thumbnail có render đúng không? |
| Interaction | Hover, focus, click, tap, scroll, keyboard navigation có ổn định không? |
| Feedback | Validation, loading, empty state, success/error message có dễ hiểu không? |

## 6. Coverage Check Sau Khi Chạy

| Kiểm tra | Trạng thái |
| --- | --- |
| Đã phủ đủ `Windows` | `[ ]` |
| Đã phủ đủ `Linux` | `[ ]` |
| Đã phủ đủ `Android` | `[ ]` |
| Đã phủ đủ `Edge` | `[ ]` |
| Đã phủ đủ `Opera` | `[ ]` |
| Đã phủ đủ `Firefox` | `[ ]` |
| Đã phủ đủ `Samsung Internet` | `[ ]` |
| Đã phủ đủ `Chrome` | `[ ]` |
| Đã phủ đủ `Desktop/Laptop` | `[ ]` |
| Đã phủ đủ `Tablet` | `[ ]` |
| Đã phủ đủ `Phone` | `[ ]` |
| Mỗi cell có evidence | `[ ]` |
| Mỗi fail có defect ID | `[ ]` |
