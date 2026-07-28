# Cross-Browser / Cross-Platform Matrix - Scenario A

## 1. Thông tin chung

| Trường | Nội dung |
| --- | --- |
| Sinh viên | Lê Mai Hoài Bảo |
| MSSV | 23127326 |
| Scenario | A - Admin creates and manages events |
| Màn hình | A1 Events list, A2 Add/Edit Event, A3 Registration & Roles |
| Công cụ | [BrowserStack/LambdaTest/thiết bị thật] |
| Email overlay | [MSSV@....edu.vn] |
| Ngày chạy | [YYYY-MM-DD] |

## 2. Coverage bắt buộc theo đề

Mỗi màn hình phải exercise đủ:

| Dimension | Yêu cầu | Coverage thực tế |
| --- | --- | --- |
| Operating systems | 3 OS | [Windows, macOS, Android/iOS...] |
| Browsers | 5 browsers | [Chrome, Firefox, Safari, Edge, Opera/Samsung Internet...] |
| Device classes | 3 device classes | [Desktop, tablet, phone] |

> Không cần chạy đủ 3 x 5 x 3 combinations, nhưng với mỗi màn hình phải chạm đủ mọi OS, browser và device class đã khai báo. Mỗi cell phải có screenshot.

## 3. Ma trận chi tiết

### 3.1 A1 - Events list with status filters and notification dots

| Cell ID | OS | Browser | Device class | Device/Version | EMS URL visible | Browser/OS/device visible | Email overlay | Result | Screenshot ref | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A1-CP-01 | Windows | Chrome | Desktop | [ ] | [Yes/No] | [Yes/No] | [Yes/No] | [Pass/Fail] | [screenshots/...] | [ ] |
| A1-CP-02 | macOS | Safari | Desktop | [ ] | [Yes/No] | [Yes/No] | [Yes/No] | [Pass/Fail] | [screenshots/...] | [ ] |
| A1-CP-03 | Android/iOS | Chrome/Safari | Phone | [ ] | [Yes/No] | [Yes/No] | [Yes/No] | [Pass/Fail] | [screenshots/...] | [ ] |
| A1-CP-04 | [ ] | Firefox | Tablet | [ ] | [Yes/No] | [Yes/No] | [Yes/No] | [Pass/Fail] | [screenshots/...] | [ ] |
| A1-CP-05 | [ ] | Edge/Opera | [Desktop/Tablet/Phone] | [ ] | [Yes/No] | [Yes/No] | [Yes/No] | [Pass/Fail] | [screenshots/...] | [ ] |

### 3.2 A2 - Add/Edit Event form

| Cell ID | OS | Browser | Device class | Device/Version | EMS URL visible | Browser/OS/device visible | Email overlay | Result | Screenshot ref | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A2-CP-01 | Windows | Chrome | Desktop | [ ] | [Yes/No] | [Yes/No] | [Yes/No] | [Pass/Fail] | [screenshots/...] | [ ] |
| A2-CP-02 | macOS | Safari | Desktop | [ ] | [Yes/No] | [Yes/No] | [Yes/No] | [Pass/Fail] | [screenshots/...] | [ ] |
| A2-CP-03 | Android/iOS | Chrome/Safari | Phone | [ ] | [Yes/No] | [Yes/No] | [Yes/No] | [Pass/Fail] | [screenshots/...] | [ ] |
| A2-CP-04 | [ ] | Firefox | Tablet | [ ] | [Yes/No] | [Yes/No] | [Yes/No] | [Pass/Fail] | [screenshots/...] | [ ] |
| A2-CP-05 | [ ] | Edge/Opera | [Desktop/Tablet/Phone] | [ ] | [Yes/No] | [Yes/No] | [Yes/No] | [Pass/Fail] | [screenshots/...] | [ ] |

### 3.3 A3 - Registration & Roles configuration panel

| Cell ID | OS | Browser | Device class | Device/Version | EMS URL visible | Browser/OS/device visible | Email overlay | Result | Screenshot ref | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A3-CP-01 | Windows | Chrome | Desktop | [ ] | [Yes/No] | [Yes/No] | [Yes/No] | [Pass/Fail] | [screenshots/...] | [ ] |
| A3-CP-02 | macOS | Safari | Desktop | [ ] | [Yes/No] | [Yes/No] | [Yes/No] | [Pass/Fail] | [screenshots/...] | [ ] |
| A3-CP-03 | Android/iOS | Chrome/Safari | Phone | [ ] | [Yes/No] | [Yes/No] | [Yes/No] | [Pass/Fail] | [screenshots/...] | [ ] |
| A3-CP-04 | [ ] | Firefox | Tablet | [ ] | [Yes/No] | [Yes/No] | [Yes/No] | [Pass/Fail] | [screenshots/...] | [ ] |
| A3-CP-05 | [ ] | Edge/Opera | [Desktop/Tablet/Phone] | [ ] | [Yes/No] | [Yes/No] | [Yes/No] | [Pass/Fail] | [screenshots/...] | [ ] |

## 4. Compatibility defects

| ID | Cell ID | Màn hình | Mô tả lỗi | Expected | Actual | Severity | Screenshot ref | Form timestamp |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- |
| CP-BUG-001 | [A1/A2/A3-CP-..] | [A1/A2/A3] | [Overflow/overlap/broken layout/unreadable text/non-responsive control...] | [ ] | [ ] | [0-4] | [screenshots/...] | [YYYY-MM-DD HH:mm] |

## 5. Kết luận compatibility

[Tóm tắt màn hình nào ổn nhất, môi trường nào rủi ro nhất, và khuyến nghị sửa responsive/cross-browser.]
