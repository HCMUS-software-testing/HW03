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
| CP-04 | Android | Samsung Internet | Tablet | Samsung Galaxy Tab A + Samsung Internet | Phủ tablet Samsung với browser Samsung Internet. |
| CP-05 | Android | Chrome | Phone | Samsung Galaxy A54 + Chrome | Phủ điện thoại Android Samsung với Chrome. |

## D1 - User tạo support request

| Cell | OS | Browser | Device class | Device/profile | Result | Screenshot ref | Checklist focus | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D1-CP-01 | Linux | Firefox | Desktop | Linux desktop + Firefox latest | `Fail` | `submission/task3/screenshots/defects/D1/D1_CP-01_linux_firefox_desktop/` | Form width, dropdown behavior, button hierarchy trên desktop non-Windows. | Đã có ảnh `F-D1-001`, `F-D1-002`, `F-D1-003`. |
| D1-CP-02 | Windows 11 | Opera | Desktop | Windows 11 + Opera latest | `[Pass/Fail]` | `submission/task3/screenshots/D1_CP-02_windows_opera_desktop.png` | Form layout, labels, required markers, upload zone, submit/cancel. | `[Điền sau khi test]` |
| D1-CP-03 | Windows 11 | Edge | Desktop | Windows 11 + Edge latest | `[Pass/Fail]` | `submission/task3/screenshots/D1_CP-03_windows_edge_desktop.png` | Select/category, file upload, textarea, focus state. | `[Điền sau khi test]` |
| D1-CP-04 | Android | Samsung Internet | Tablet | Samsung Galaxy Tab A + Samsung Internet | `Fail` | `submission/task3/screenshots/defects/D1/D1_CP-04_android_samsung-internet_tablet/` | Tablet layout, form readability, action buttons. | Đã có ảnh `F-D1-001`, `F-D1-002`, `F-D1-003`, `F-D1-004`. |
| D1-CP-05 | Android | Chrome | Phone | Samsung Galaxy A54 + Chrome | `Fail` | `submission/task3/screenshots/defects/D1/D1_CP-05_android_chrome_phone/` | Textarea/input rendering, upload button, no horizontal overflow trên phone. | Đã có ảnh `F-D1-001`, `F-D1-003`, `F-D1-004`. |

## D2 - User My Requests list/detail

| Cell | OS | Browser | Device class | Device/profile | Result | Screenshot ref | Checklist focus | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D2-CP-01 | Linux | Firefox | Desktop | Linux desktop + Firefox latest | `Fail` | `submission/task3/screenshots/defects/D2/D2_CP-01_linux_firefox_desktop/` | List density, filter row, rows-per-page trên Firefox/Linux. | Đã có ảnh `F-D2-001`, `F-D2-002`. |
| D2-CP-02 | Windows 11 | Opera | Desktop | Windows 11 + Opera latest | `[Pass/Fail]` | `submission/task3/screenshots/D2_CP-02_windows_opera_desktop.png` | List cards, status/category badges, search/filter, pagination. | `[Điền sau khi test]` |
| D2-CP-03 | Windows 11 | Edge | Desktop | Windows 11 + Edge latest | `[Pass/Fail]` | `submission/task3/screenshots/D2_CP-03_windows_edge_desktop.png` | Detail page, attachment thumbnail/lightbox, response section. | `[Điền sau khi test]` |
| D2-CP-04 | Android | Samsung Internet | Tablet | Samsung Galaxy Tab A + Samsung Internet | `Fail` | `submission/task3/screenshots/defects/D2/D2_CP-04_android_samsung-internet_tablet/` | Tablet list/detail layout and filter controls. | Đã có ảnh `F-D2-001`, `F-D2-002`. |
| D2-CP-05 | Android | Chrome | Phone | Samsung Galaxy A54 + Chrome | `Fail` | `submission/task3/screenshots/defects/D2/D2_CP-05_android_chrome_phone/` | Search/filter and card readability on phone. | Đã có ảnh `F-D2-001`, `F-D2-002`. |

## D3 - Admin Support Requests list

| Cell | OS | Browser | Device class | Device/profile | Result | Screenshot ref | Checklist focus | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D3-CP-01 | Linux | Firefox | Desktop | Linux desktop + Firefox latest | `Fail` | `submission/task3/screenshots/defects/D3/D3_CP-01_linux_firefox_desktop/` | Admin sidebar, Pending/Resolved cards, filter wrap trên Firefox/Linux. | Đã có ảnh `F-D3-001`, `F-D3-002`. |
| D3-CP-02 | Windows 11 | Opera | Desktop | Windows 11 + Opera latest | `[Pass/Fail]` | `submission/task3/screenshots/D3_CP-02_windows_opera_desktop.png` | Admin sidebar, Pending tab, filter panel, cards, pagination. | `[Điền sau khi test]` |
| D3-CP-03 | Windows 11 | Edge | Desktop | Windows 11 + Edge latest | `[Pass/Fail]` | `submission/task3/screenshots/D3_CP-03_windows_edge_desktop.png` | Search/member-code/category filter rendering. | `[Điền sau khi test]` |
| D3-CP-04 | Android | Samsung Internet | Tablet | Samsung Galaxy Tab A + Samsung Internet | `Fail` | `submission/task3/screenshots/defects/D3/D3_CP-04_android_samsung-internet_tablet/` | Tablet sidebar/content layout and filter usability. | Đã có ảnh `F-D3-001`, `F-D3-002`. |
| D3-CP-05 | Android | Chrome | Phone | Samsung Galaxy A54 + Chrome | `Fail` | `submission/task3/screenshots/defects/D3/D3_CP-05_android_chrome_phone/` | Mobile admin layout, sidebar/content width, filter usability trên phone. | Đã có ảnh `F-D3-003`. |

## Coverage check sau khi chạy

| Screen | 3 OS covered? | 5 browsers covered? | 3 device classes covered? | Screenshot đủ chưa? | Notes |
| --- | --- | --- | --- | --- | --- |
| D1 | `No` | `No` | `Yes` | `Partial` | Hiện có ảnh defect cho CP-01, CP-04, CP-05; còn thiếu CP-02 Opera và CP-03 Edge. |
| D2 | `No` | `No` | `Yes` | `Partial` | Hiện có ảnh defect cho CP-01, CP-04, CP-05; còn thiếu CP-02 Opera và CP-03 Edge. |
| D3 | `No` | `No` | `Yes` | `Partial` | Hiện có ảnh defect cho CP-01, CP-04, CP-05; còn thiếu CP-02 Opera và CP-03 Edge. |
