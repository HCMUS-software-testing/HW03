# Task 3 - Compatibility Matrix Template

| Trường | Giá trị |
| --- | --- |
| Scenario | D - User requests Support and Admin resolves it |
| SUT | `https://prod-dev.ems-fitus.cloud` |
| Overlay bắt buộc | `23127075@clc.fitus.edu.vn` |
| Công cụ ưu tiên | TestingBot, BrowserStack Live hoặc LambdaTest |
| Người thực hiện | Lê Trung Kiên - `23127075` |

## Coverage bắt buộc cho mỗi màn hình

Mỗi màn hình D1, D2, D3 phải phủ đủ:

| Dimension | Yêu cầu |
| --- | --- |
| Operating systems | Ít nhất 3 OS; matrix này dùng Linux, Windows và Android. |
| Browsers | Ít nhất 5 browser; matrix này dùng Firefox, Opera, Edge, Samsung Internet và Chrome. |
| Device classes | Ít nhất 3 loại thiết bị: desktop, tablet, phone. |
| Screenshot | Một ảnh cho mỗi cell, có EMS URL, TestingBot OS/browser/device identity và overlay email. |

## Matrix đề xuất dùng chung

Matrix `5` cell dưới đây đủ phủ `3 OS`, `5 browser/platform`, và `3 device classes` cho từng màn hình.

| Cell | OS | Browser | Device class | Device/profile đề xuất | Lý do chọn |
| --- | --- | --- | --- | --- | --- |
| CP-01 | Linux | Firefox | Desktop | Linux desktop + Firefox latest | Phủ desktop non-Windows và engine Gecko. |
| CP-02 | Windows 11 | Opera | Desktop | Windows 11 + Opera latest | Phủ desktop Windows với Chromium-based browser khác Edge/Chrome. |
| CP-03 | Windows 11 | Edge | Desktop | Windows 11 + Edge latest | Browser mặc định Windows, dễ đối chiếu layout admin/list. |
| CP-04 | Android | Chrome | Tablet | Samsung Galaxy Tab hoặc tablet Android + Chrome | TestingBot chỉ có Chrome cho tablet; vẫn phủ tablet Android. |
| CP-05 | Android | Samsung Internet | Phone | Samsung Galaxy S series + Samsung Internet | Phủ Samsung Internet trên điện thoại Android. |

## D1 - User tạo support request

| Cell | OS | Browser | Device class | Device/profile | Result | Screenshot ref | Checklist focus | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D1-CP-01 | Linux | Firefox | Desktop | Linux desktop + Firefox latest | `[Pass/Fail]` | `submission/task3/screenshots/D1_CP-01_linux_firefox_desktop.png` | Form width, dropdown behavior, button hierarchy trên desktop non-Windows. | `[Điền sau khi test]` |
| D1-CP-02 | Windows 11 | Opera | Desktop | Windows 11 + Opera latest | `[Pass/Fail]` | `submission/task3/screenshots/D1_CP-02_windows_opera_desktop.png` | Form layout, labels, required markers, upload zone, submit/cancel. | `[Điền sau khi test]` |
| D1-CP-03 | Windows 11 | Edge | Desktop | Windows 11 + Edge latest | `[Pass/Fail]` | `submission/task3/screenshots/D1_CP-03_windows_edge_desktop.png` | Select/category, file upload, textarea, focus state. | `[Điền sau khi test]` |
| D1-CP-04 | Android | Chrome | Tablet | Galaxy Tab hoặc tablet Android + Chrome | `[Pass/Fail]` | `submission/task3/screenshots/D1_CP-04_android_chrome_tablet.png` | Tablet layout, form readability, action buttons. | `[Điền sau khi test]` |
| D1-CP-05 | Android | Samsung Internet | Phone | Samsung Galaxy S series + Samsung Internet | `[Pass/Fail]` | `submission/task3/screenshots/D1_CP-05_android_samsung-internet_phone.png` | Textarea/input rendering, upload button, no horizontal overflow trên phone. | `[Điền sau khi test]` |

## D2 - User My Requests list/detail

| Cell | OS | Browser | Device class | Device/profile | Result | Screenshot ref | Checklist focus | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D2-CP-01 | Linux | Firefox | Desktop | Linux desktop + Firefox latest | `[Pass/Fail]` | `submission/task3/screenshots/D2_CP-01_linux_firefox_desktop.png` | List density, filter row, rows-per-page trên Firefox/Linux. | `[Điền sau khi test]` |
| D2-CP-02 | Windows 11 | Opera | Desktop | Windows 11 + Opera latest | `[Pass/Fail]` | `submission/task3/screenshots/D2_CP-02_windows_opera_desktop.png` | List cards, status/category badges, search/filter, pagination. | `[Điền sau khi test]` |
| D2-CP-03 | Windows 11 | Edge | Desktop | Windows 11 + Edge latest | `[Pass/Fail]` | `submission/task3/screenshots/D2_CP-03_windows_edge_desktop.png` | Detail page, attachment thumbnail/lightbox, response section. | `[Điền sau khi test]` |
| D2-CP-04 | Android | Chrome | Tablet | Galaxy Tab hoặc tablet Android + Chrome | `[Pass/Fail]` | `submission/task3/screenshots/D2_CP-04_android_chrome_tablet.png` | Tablet list/detail layout and filter controls. | `[Điền sau khi test]` |
| D2-CP-05 | Android | Samsung Internet | Phone | Samsung Galaxy S series + Samsung Internet | `[Pass/Fail]` | `submission/task3/screenshots/D2_CP-05_android_samsung-internet_phone.png` | Search/filter and card readability on phone. | `[Điền sau khi test]` |

## D3 - Admin Support Requests list

| Cell | OS | Browser | Device class | Device/profile | Result | Screenshot ref | Checklist focus | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D3-CP-01 | Linux | Firefox | Desktop | Linux desktop + Firefox latest | `[Pass/Fail]` | `submission/task3/screenshots/D3_CP-01_linux_firefox_desktop.png` | Admin sidebar, Pending/Resolved cards, filter wrap trên Firefox/Linux. | `[Điền sau khi test]` |
| D3-CP-02 | Windows 11 | Opera | Desktop | Windows 11 + Opera latest | `[Pass/Fail]` | `submission/task3/screenshots/D3_CP-02_windows_opera_desktop.png` | Admin sidebar, Pending tab, filter panel, cards, pagination. | `[Điền sau khi test]` |
| D3-CP-03 | Windows 11 | Edge | Desktop | Windows 11 + Edge latest | `[Pass/Fail]` | `submission/task3/screenshots/D3_CP-03_windows_edge_desktop.png` | Search/member-code/category filter rendering. | `[Điền sau khi test]` |
| D3-CP-04 | Android | Chrome | Tablet | Galaxy Tab hoặc tablet Android + Chrome | `[Pass/Fail]` | `submission/task3/screenshots/D3_CP-04_android_chrome_tablet.png` | Tablet sidebar/content layout and filter usability. | `[Điền sau khi test]` |
| D3-CP-05 | Android | Samsung Internet | Phone | Samsung Galaxy S series + Samsung Internet | `[Pass/Fail]` | `submission/task3/screenshots/D3_CP-05_android_samsung-internet_phone.png` | Mobile admin layout, sidebar/content width, filter usability trên phone. | `[Điền sau khi test]` |

## Coverage check sau khi chạy

| Screen | 3 OS covered? | 5 browsers covered? | 3 device classes covered? | Screenshot đủ chưa? | Notes |
| --- | --- | --- | --- | --- | --- |
| D1 | `[Yes/No]` | `[Yes/No]` | `[Yes/No]` | `[Yes/No]` | `[Điền sau khi test]` |
| D2 | `[Yes/No]` | `[Yes/No]` | `[Yes/No]` | `[Yes/No]` | `[Điền sau khi test]` |
| D3 | `[Yes/No]` | `[Yes/No]` | `[Yes/No]` | `[Yes/No]` | `[Điền sau khi test]` |
