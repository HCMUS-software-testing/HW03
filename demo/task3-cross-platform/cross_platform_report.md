# Cross-Platform Report Template

## 1. Executive Summary

| Trường | Giá trị |
| --- | --- |
| Target URL | `[Điền URL]` |
| Scope | `[Điền flow hoặc screen]` |
| Test date | `[YYYY-MM-DD]` |
| Tester | `[Điền tên]` |
| Total cells | `5` |
| Pass | `[Điền]` |
| Fail | `[Điền]` |
| Needs review | `[Điền]` |
| Overall assessment | `[Tóm tắt ngắn gọn]` |

## 2. Test Dimensions

| Dimension | Giá trị |
| --- | --- |
| Operating systems | `Windows`, `Linux`, `Android` |
| Browsers | `Edge`, `Opera`, `Firefox`, `Samsung Internet`, `Chrome` |
| Device classes | `Desktop/Laptop`, `Tablet`, `Phone` |

## 3. Method

1. Xác định flow, route hoặc screen cần test.
2. Chạy lần lượt từng cell trong `compatibility_matrix.md`.
3. Quan sát layout, text, interaction, feedback và responsive behavior.
4. Chụp evidence theo `screenshot_protocol.md`.
5. Ghi `Pass`, `Fail` hoặc `Needs review`.
6. Tổng hợp finding và mức độ ưu tiên sửa.

## 4. Result Summary by Cell

| Cell ID | OS | Browser | Device class | Result | Key observation | Screenshot ref |
| --- | --- | --- | --- | --- | --- | --- |
| `CP-01` | `Linux` | `Firefox` | `Desktop/Laptop` | `[Điền]` | `[Điền]` | `[Điền]` |
| `CP-02` | `Windows` | `Edge` | `Desktop/Laptop` | `[Điền]` | `[Điền]` | `[Điền]` |
| `CP-03` | `Windows` | `Opera` | `Desktop/Laptop` | `[Điền]` | `[Điền]` | `[Điền]` |
| `CP-04` | `Android` | `Samsung Internet` | `Tablet` | `[Điền]` | `[Điền]` | `[Điền]` |
| `CP-05` | `Android` | `Chrome` | `Phone` | `[Điền]` | `[Điền]` | `[Điền]` |

## 5. Findings

| Defect ID | Cell ID | Screen / Flow | Type | Description | Severity | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `CP-F-001` | `[Điền]` | `[Điền]` | `Bug / Usability / Visual` | `[Mô tả lỗi]` | `[1-4]` | `[Link/path]` |
| `CP-F-002` | `[Điền]` | `[Điền]` | `Bug / Usability / Visual` | `[Mô tả lỗi]` | `[1-4]` | `[Link/path]` |
| `CP-F-003` | `[Điền]` | `[Điền]` | `Bug / Usability / Visual` | `[Mô tả lỗi]` | `[1-4]` | `[Link/path]` |

## 6. Common Compatibility Patterns

| Pattern | Có xuất hiện không? | Ghi chú |
| --- | --- | --- |
| Layout vỡ trên màn hình hẹp | `[Yes/No]` | `[Điền]` |
| Text bị cắt hoặc quá nhỏ | `[Yes/No]` | `[Điền]` |
| Control khó thao tác trên touch device | `[Yes/No]` | `[Điền]` |
| Modal / drawer vượt viewport | `[Yes/No]` | `[Điền]` |
| Sidebar / sticky element che nội dung | `[Yes/No]` | `[Điền]` |
| Hành vi khác nhau giữa browser | `[Yes/No]` | `[Điền]` |

## 7. Recommendations

| Priority | Recommendation | Lý do |
| --- | --- | --- |
| `High` | `[Điền]` | `[Điền]` |
| `Medium` | `[Điền]` | `[Điền]` |
| `Low` | `[Điền]` | `[Điền]` |

## 8. Conclusion

`[Viết kết luận ngắn về mức độ tương thích hiện tại, khu vực rủi ro cao nhất và thứ tự ưu tiên sửa.]`
