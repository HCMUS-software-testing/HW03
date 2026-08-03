# Task 3 - Compatibility Matrix Template

| Trường | Giá trị |
| --- | --- |
| Scenario | D - User requests Support and Admin resolves it |
| SUT | `https://prod-dev.ems-fitus.cloud` |
| Overlay bắt buộc | `23127075@clc.fitus.edu.vn` |
| Công cụ ưu tiên | BrowserStack Live hoặc LambdaTest |
| Người thực hiện | Lê Trung Kiên - `23127075` |

## Coverage bắt buộc cho mỗi màn hình

Mỗi màn hình D1, D2, D3 phải phủ đủ:

| Dimension | Yêu cầu |
| --- | --- |
| Operating systems | Ít nhất 3 OS, ví dụ Windows, macOS, Android/iOS. |
| Browsers | Ít nhất 5 browser, ví dụ Chrome, Firefox, Safari, Edge, Opera hoặc Samsung Internet. |
| Device classes | Ít nhất 3 loại thiết bị: desktop, tablet, phone. |
| Screenshot | Một ảnh cho mỗi cell, có EMS URL, BrowserStack OS/browser/device identity và overlay email. |

## Matrix đề xuất dùng chung

Matrix 7 cell dưới đây đủ phủ 3 OS, 5 browser và 3 device classes cho từng màn hình.

| Cell | OS | Browser | Device class | Device/profile đề xuất | Lý do chọn |
| --- | --- | --- | --- | --- | --- |
| CP-01 | Windows 11 | Chrome | Desktop | 1920x1080 hoặc BrowserStack Windows desktop | Baseline phổ biến trên desktop. |
| CP-02 | Windows 11 | Edge | Desktop | 1366x768 hoặc BrowserStack Windows desktop | Kiểm tra Chromium Edge và viewport desktop hẹp hơn. |
| CP-03 | macOS | Safari | Desktop | macOS Safari latest | Bắt buộc thực tế để phủ Safari desktop/WebKit. |
| CP-04 | Android | Chrome | Phone | Pixel hoặc Samsung Galaxy phone | Browser mobile phổ biến, kiểm tra responsive và touch. |
| CP-05 | Android | Firefox | Phone | Android phone | Kiểm tra Gecko/mobile browser khác Chromium. |
| CP-06 | iOS | Safari | Phone | iPhone 14/15 | Kiểm tra Safari iOS và viewport phone. |
| CP-07 | Android hoặc iPadOS | Samsung Internet hoặc Opera | Tablet | Samsung Galaxy Tab hoặc iPad/tablet profile | Phủ tablet và browser thứ 5 nếu chưa đủ. |

## D1 - User tạo support request

| Cell | OS | Browser | Device class | Device/profile | Result | Screenshot ref | Checklist focus | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D1-CP-01 | Windows 11 | Chrome | Desktop | 1920x1080 | `[Pass/Fail]` | `submission/task3/screenshots/D1_CP-01_windows_chrome_desktop.png` | Form layout, labels, required markers, upload zone, submit/cancel. | `[Điền sau khi test]` |
| D1-CP-02 | Windows 11 | Edge | Desktop | 1366x768 | `[Pass/Fail]` | `submission/task3/screenshots/D1_CP-02_windows_edge_desktop.png` | Form width, dropdown behavior, button hierarchy. | `[Điền sau khi test]` |
| D1-CP-03 | macOS | Safari | Desktop | macOS Safari latest | `[Pass/Fail]` | `submission/task3/screenshots/D1_CP-03_macos_safari_desktop.png` | Select/category, file upload, textarea, focus state. | `[Điền sau khi test]` |
| D1-CP-04 | Android | Chrome | Phone | Pixel/Galaxy phone | `[Pass/Fail]` | `submission/task3/screenshots/D1_CP-04_android_chrome_phone.png` | Mobile stacking, keyboard input, upload action, alert visibility. | `[Điền sau khi test]` |
| D1-CP-05 | Android | Firefox | Phone | Android phone | `[Pass/Fail]` | `submission/task3/screenshots/D1_CP-05_android_firefox_phone.png` | Textarea/input rendering, upload button, no horizontal overflow. | `[Điền sau khi test]` |
| D1-CP-06 | iOS | Safari | Phone | iPhone | `[Pass/Fail]` | `submission/task3/screenshots/D1_CP-06_ios_safari_phone.png` | iOS Safari upload/select behavior and viewport safe area. | `[Điền sau khi test]` |
| D1-CP-07 | Android/iPadOS | Samsung Internet/Opera | Tablet | Tablet profile | `[Pass/Fail]` | `submission/task3/screenshots/D1_CP-07_tablet_samsung_or_opera.png` | Tablet layout, form readability, action buttons. | `[Điền sau khi test]` |

## D2 - User My Requests list/detail

| Cell | OS | Browser | Device class | Device/profile | Result | Screenshot ref | Checklist focus | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D2-CP-01 | Windows 11 | Chrome | Desktop | 1920x1080 | `[Pass/Fail]` | `submission/task3/screenshots/D2_CP-01_windows_chrome_desktop.png` | List cards, status/category badges, search/filter, pagination. | `[Điền sau khi test]` |
| D2-CP-02 | Windows 11 | Edge | Desktop | 1366x768 | `[Pass/Fail]` | `submission/task3/screenshots/D2_CP-02_windows_edge_desktop.png` | List density, filter row, rows-per-page. | `[Điền sau khi test]` |
| D2-CP-03 | macOS | Safari | Desktop | macOS Safari latest | `[Pass/Fail]` | `submission/task3/screenshots/D2_CP-03_macos_safari_desktop.png` | Detail page, attachment thumbnail/lightbox, response section. | `[Điền sau khi test]` |
| D2-CP-04 | Android | Chrome | Phone | Pixel/Galaxy phone | `[Pass/Fail]` | `submission/task3/screenshots/D2_CP-04_android_chrome_phone.png` | Mobile list/detail, floating social links, pagination. | `[Điền sau khi test]` |
| D2-CP-05 | Android | Firefox | Phone | Android phone | `[Pass/Fail]` | `submission/task3/screenshots/D2_CP-05_android_firefox_phone.png` | Search/filter and card readability on phone. | `[Điền sau khi test]` |
| D2-CP-06 | iOS | Safari | Phone | iPhone | `[Pass/Fail]` | `submission/task3/screenshots/D2_CP-06_ios_safari_phone.png` | Back behavior, detail response readability, modal close. | `[Điền sau khi test]` |
| D2-CP-07 | Android/iPadOS | Samsung Internet/Opera | Tablet | Tablet profile | `[Pass/Fail]` | `submission/task3/screenshots/D2_CP-07_tablet_samsung_or_opera.png` | Tablet list/detail layout and filter controls. | `[Điền sau khi test]` |

## D3 - Admin Support Requests list

| Cell | OS | Browser | Device class | Device/profile | Result | Screenshot ref | Checklist focus | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D3-CP-01 | Windows 11 | Chrome | Desktop | 1920x1080 | `[Pass/Fail]` | `submission/task3/screenshots/D3_CP-01_windows_chrome_desktop.png` | Admin sidebar, Pending tab, filter panel, cards, pagination. | `[Điền sau khi test]` |
| D3-CP-02 | Windows 11 | Edge | Desktop | 1366x768 | `[Pass/Fail]` | `submission/task3/screenshots/D3_CP-02_windows_edge_desktop.png` | Desktop hẹp, filter wrap, tab count. | `[Điền sau khi test]` |
| D3-CP-03 | macOS | Safari | Desktop | macOS Safari latest | `[Pass/Fail]` | `submission/task3/screenshots/D3_CP-03_macos_safari_desktop.png` | Search/member-code/category filter rendering. | `[Điền sau khi test]` |
| D3-CP-04 | Android | Chrome | Phone | Pixel/Galaxy phone | `[Pass/Fail]` | `submission/task3/screenshots/D3_CP-04_android_chrome_phone.png` | Admin mobile sidebar/content width; likely risk from Task 1B. | `[Điền sau khi test]` |
| D3-CP-05 | Android | Firefox | Phone | Android phone | `[Pass/Fail]` | `submission/task3/screenshots/D3_CP-05_android_firefox_phone.png` | Same mobile admin layout on Firefox Android. | `[Điền sau khi test]` |
| D3-CP-06 | iOS | Safari | Phone | iPhone | `[Pass/Fail]` | `submission/task3/screenshots/D3_CP-06_ios_safari_phone.png` | Safari iOS layout, sidebar, input zoom/wrapping. | `[Điền sau khi test]` |
| D3-CP-07 | Android/iPadOS | Samsung Internet/Opera | Tablet | Tablet profile | `[Pass/Fail]` | `submission/task3/screenshots/D3_CP-07_tablet_samsung_or_opera.png` | Tablet sidebar/content layout and filter usability. | `[Điền sau khi test]` |

## Coverage check sau khi chạy

| Screen | 3 OS covered? | 5 browsers covered? | 3 device classes covered? | Screenshot đủ chưa? | Notes |
| --- | --- | --- | --- | --- | --- |
| D1 | `[Yes/No]` | `[Yes/No]` | `[Yes/No]` | `[Yes/No]` | `[Điền sau khi test]` |
| D2 | `[Yes/No]` | `[Yes/No]` | `[Yes/No]` | `[Yes/No]` | `[Điền sau khi test]` |
| D3 | `[Yes/No]` | `[Yes/No]` | `[Yes/No]` | `[Yes/No]` | `[Điền sau khi test]` |

