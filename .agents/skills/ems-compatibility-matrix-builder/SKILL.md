---
name: ems-compatibility-matrix-builder
description: Tạo hoặc kiểm tra ma trận cross-browser và cross-platform cho HW03 EMS. Dùng khi Codex được yêu cầu lập kế hoạch coverage BrowserStack/LambdaTest, kiểm tra đủ 3 OS/5 browser/3 lớp thiết bị cho từng màn hình EMS, đặt tên ảnh chụp hoặc phát hiện thiếu minh chứng compatibility.
---

# EMS Compatibility Matrix Builder

## Đầu vào

Cần có:

- Danh sách màn hình.
- Các dòng ma trận đã chụp hoặc dự kiến chụp.
- Thư mục ảnh chụp.
- Text overlay sinh viên, ví dụ `23127205@....edu.vn`.

Không đánh dấu một cell là `Pass` hoặc `Fail` nếu chưa có ảnh chụp hoặc ghi chú quan sát.

## Quy tắc coverage

Với mỗi màn hình, bảo đảm:

- Có ít nhất 3 hệ điều hành.
- Có ít nhất 5 trình duyệt.
- Có đủ desktop, tablet và phone.
- Mỗi ảnh chụp hiển thị URL EMS và overlay email sinh viên.

Các cell tối thiểu khuyến nghị:

| Cell | Hệ điều hành | Trình duyệt | Lớp thiết bị |
| --- | --- | --- | --- |
| 1 | Windows | Chrome | Desktop |
| 2 | Windows | Edge | Desktop |
| 3 | macOS hoặc iOS | Safari | Desktop hoặc phone |
| 4 | Android | Chrome | Phone |
| 5 | Android | Firefox | Phone |
| 6 | iOS hoặc Android | Opera | Tablet |

## Quy trình

1. Nhóm các dòng theo màn hình.
2. Đếm số hệ điều hành, trình duyệt và lớp thiết bị khác nhau trên từng màn hình.
3. Ghi rõ coverage còn thiếu.
4. Kiểm tra đường dẫn ảnh theo naming convention:
   - `C1_win_chrome_desktop.png`
   - `C2_macos_safari_desktop.png`
   - `C3_android_firefox_phone.png`
5. Thêm defect compatibility vào `submission/bug_usability_findings_log.md`.

## Định dạng đầu ra

```markdown
| Màn hình | Đủ 3 OS | Đủ 5 browser | Đủ 3 lớp thiết bị | Minh chứng còn thiếu |
| --- | --- | --- | --- | --- |
| C1 | Có | Không | Có | Cần thêm ảnh Opera. |
```
