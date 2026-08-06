# Screenshot Protocol

## 1. Mục tiêu

Quy định này giúp screenshot giữa các cell có format nhất quán, dễ đối chiếu và đủ bằng chứng để chứng minh lỗi compatibility.

## 2. Quy tắc bắt buộc cho mỗi screenshot

| Thành phần | Bắt buộc |
| --- | --- |
| URL hoặc route | Phải nhìn thấy URL hoặc có thể suy ra rõ screen đang test. |
| Environment identity | Phải thể hiện được `OS`, `browser`, `device class` hoặc `device profile`. |
| Đúng state | Screenshot phải đúng flow, route hoặc UI state đang đánh giá. |
| Rõ vấn đề | Nếu `Fail`, ảnh phải cho thấy trực tiếp lỗi hoặc hành vi bất thường. |
| Tính truy vết | Tên file hoặc link phải map được về `Cell ID`. |

## 3. Khi nào cần chụp

Chụp tối thiểu `1` ảnh cho mỗi cell.

Nên chụp thêm ảnh nếu:

- Cần tách list và detail thành hai state khác nhau
- Có lỗi chỉ xuất hiện sau thao tác scroll, expand, tab switch hoặc submit
- Có hơn một lỗi quan trọng trong cùng một cell

## 4. Nội dung cần ưu tiên quan sát khi chụp

| Nhóm | Ví dụ cần bắt lại trong ảnh |
| --- | --- |
| Layout issues | Overflow, overlap, broken grid, sidebar che content |
| Text issues | Truncated text, label bị che, font scale không hợp lý |
| Control issues | Nút bấm lệch vị trí, dropdown lỗi, upload khó thao tác |
| Responsive issues | Drawer không đóng, sticky header đè form, modal vượt viewport |
| Visual regressions | Màu sắc sai, icon mất, spacing không nhất quán |

## 5. Naming Convention

Tên file đề xuất:

```text
<flow-or-screen>_<cell-id>_<os>_<browser>_<device>.png
```

Ví dụ:

```text
D1_CP-01_linux_firefox_desktop.png
D1_CP-04_android_samsung-internet_tablet.png
D1_CP-05_android_chrome_phone.png
```

Nếu là ảnh defect cụ thể:

```text
<defect-id>_<cell-id>_<short-description>.png
```

Ví dụ:

```text
CP-F-001_CP-05_sidebar-overflow.png
CP-F-002_CP-02_validation-message-clipped.png
```

## 6. Evidence Folder Structure

Gợi ý cấu trúc lưu file:

```text
demo/task3-cross-platform/
├── compatibility_matrix.md
├── screenshot_protocol.md
├── cross_platform_report.md
└── screenshots/
    ├── baseline/
    └── defects/
```

Trong đó:

- `baseline/` chứa ảnh đại diện của từng cell
- `defects/` chứa ảnh phục vụ cho từng finding

## 7. Checklist trước khi lưu ảnh

| Câu hỏi | Done? |
| --- | --- |
| Đã đúng `Cell ID` chưa? | `[ ]` |
| Đã đúng OS / browser / device chưa? | `[ ]` |
| Đã đúng flow hoặc screen cần test chưa? | `[ ]` |
| Ảnh có đủ rõ để đọc nội dung chính không? | `[ ]` |
| Nếu là `Fail`, ảnh có cho thấy lỗi trực tiếp không? | `[ ]` |
| Tên file đã đúng convention chưa? | `[ ]` |
| Đã ghi ref vào matrix chưa? | `[ ]` |
