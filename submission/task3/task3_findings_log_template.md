# Task 3 - Compatibility Findings Log Template

Mọi finding Task 3 cần được submit hai nơi:

1. Google Form: `https://forms.gle/CJQFQCAXcsDbXDMM9`
2. Aggregated log chung của bài nộp.

File này là bản nháp riêng cho Task 3 trước khi copy vào aggregated log chung.

| ID | Scenario/Screen | Cell(s) | Type | Description | Steps/Heuristic | Expected | Actual | Severity | Suggested fix | Screenshot ref | Form-submission timestamp |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- |
| CP-F-D1-001 | D1 User create support request | `[D1-CP-xx]` | `[Bug/Usability]` | `[Mô tả vấn đề]` | `[Các bước trên OS/browser/device + checklist ID liên quan]` | `[Kỳ vọng]` | `[Thực tế quan sát được]` | `[0-4]` | `[Đề xuất sửa]` | `submission/task3/screenshots/...png` | `[Điền sau khi submit Google Form]` |
| CP-F-D2-001 | D2 User My Requests list/detail | `[D2-CP-xx]` | `[Bug/Usability]` | `[Mô tả vấn đề]` | `[Các bước trên OS/browser/device + checklist ID liên quan]` | `[Kỳ vọng]` | `[Thực tế quan sát được]` | `[0-4]` | `[Đề xuất sửa]` | `submission/task3/screenshots/...png` | `[Điền sau khi submit Google Form]` |
| CP-F-D3-001 | D3 Admin Support Requests list | `[D3-CP-xx]` | `[Bug/Usability]` | `[Mô tả vấn đề]` | `[Các bước trên OS/browser/device + checklist ID liên quan]` | `[Kỳ vọng]` | `[Thực tế quan sát được]` | `[0-4]` | `[Đề xuất sửa]` | `submission/task3/screenshots/...png` | `[Điền sau khi submit Google Form]` |

## Severity scale

| Severity | Ý nghĩa |
| --- | --- |
| 0 | Không phải lỗi hoặc không ảnh hưởng đáng kể. |
| 1 | Cosmetic/minor annoyance. |
| 2 | Minor usability issue, có workaround rõ. |
| 3 | Major issue, làm chậm đáng kể hoặc làm người dùng dễ sai. |
| 4 | Critical issue, chặn task hoặc gây mất dữ liệu. |

## Finding candidates cần chú ý khi chạy Task 3

| Candidate | Nguồn | Điều kiện để ghi thành finding Task 3 |
| --- | --- | --- |
| D2 floating social links che pagination trên mobile | Task 1B D2 | Nếu tái hiện trên Android/iOS/tablet BrowserStack và ảnh thấy rõ overlap/cản thao tác. |
| D3 admin sidebar làm content quá hẹp trên mobile | Task 1B D3 | Nếu tái hiện trên phone/tablet BrowserStack và ảnh thấy rõ sidebar/content bị vỡ. |
| D1 select/upload khác nhau trên Safari/iOS | Rủi ro compatibility từ form/upload | Chỉ ghi nếu quan sát được lỗi chọn category, upload ảnh, preview hoặc submit trên môi trường cụ thể. |
| D2 attachment lightbox lỗi trên mobile/Safari | Rủi ro compatibility từ modal/media | Chỉ ghi nếu modal không fit viewport, ảnh bị méo, hoặc nút close không thao tác được. |

