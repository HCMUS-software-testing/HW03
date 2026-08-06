# Task 3 - Compatibility Matrix

> Ghi chú về dung lượng bài nộp: các screenshot defect gốc theo từng cell cross-platform trong `submission\task3\screenshots\defects` không được include đầy đủ trong folder nộp vì số lượng ảnh lớn và làm bài nộp nặng. Folder nộp chỉ giữ ảnh đại diện đã gom ở `../findings/defect-screenshots/`; nếu cần đối chiếu toàn bộ screenshot defect gốc, giảng viên có thể xem repository [HCMUS-software-testing/HW03.git](https://github.com/HCMUS-software-testing/HW03.git), branch `kien`.

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
| D1-CP-01 | Linux | Firefox | Desktop | Linux desktop + Firefox latest | `Fail` | `screenshots/downloads/CP-01_linux_firefox_desktop/D1.png` | Form width, dropdown behavior, button hierarchy trên desktop non-Windows. | Có F-D1-001, F-D1-002, F-D1-003; ảnh đại diện nằm trong `../findings/defect-screenshots/`. |
| D1-CP-02 | Windows 11 | Opera | Desktop | Windows 11 + Opera latest | `Fail` | `screenshots/downloads/CP-02_windows_opera_desktop/D1.png` | Form layout, labels, required markers, upload zone, submit/cancel. | Có F-D1-001, F-D1-002, F-D1-003, F-D1-004; ảnh đại diện nằm trong `../findings/defect-screenshots/`. |
| D1-CP-03 | Windows 11 | Edge | Desktop | Windows 11 + Edge latest | `Fail` | `screenshots/downloads/CP-03_windows_edge_desktop/D1.png` | Select/category, file upload, textarea, focus state. | Có F-D1-001, F-D1-002, F-D1-003, F-D1-004; ảnh đại diện nằm trong `../findings/defect-screenshots/`. |
| D1-CP-04 | Android | Samsung Internet | Tablet | Samsung Galaxy Tab A + Samsung Internet | `Fail` | `screenshots/downloads/CP-04_android_samsung-internet_tablet/D1.png` | Tablet layout, form readability, action buttons. | Có F-D1-001, F-D1-002, F-D1-003, F-D1-004; ảnh đại diện nằm trong `../findings/defect-screenshots/`. |
| D1-CP-05 | Android | Chrome | Phone | Samsung Galaxy A54 + Chrome | `Fail` | `screenshots/downloads/CP-05_android_chrome_phone/D1.png` | Textarea/input rendering, upload button, no horizontal overflow trên phone. | Có F-D1-001, F-D1-003, F-D1-004; ảnh đại diện nằm trong `../findings/defect-screenshots/`. |

## D2 - User My Requests list/detail

| Cell | OS | Browser | Device class | Device/profile | Result | Screenshot ref | Checklist focus | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D2-CP-01 | Linux | Firefox | Desktop | Linux desktop + Firefox latest | `Fail` | `screenshots/downloads/CP-01_linux_firefox_desktop/D2.png` | List density, filter row, rows-per-page trên Firefox/Linux. | Có F-D2-001, F-D2-002; ảnh đại diện nằm trong `../findings/defect-screenshots/`. |
| D2-CP-02 | Windows 11 | Opera | Desktop | Windows 11 + Opera latest | `Fail` | `screenshots/downloads/CP-02_windows_opera_desktop/D2-list.png`; `screenshots/downloads/CP-02_windows_opera_desktop/D2-detail.png` | List cards, status/category badges, search/filter, pagination. | Có F-D2-001, F-D2-002; ảnh đại diện nằm trong `../findings/defect-screenshots/`. |
| D2-CP-03 | Windows 11 | Edge | Desktop | Windows 11 + Edge latest | `Fail` | `screenshots/downloads/CP-03_windows_edge_desktop/D2-list.png`; `screenshots/downloads/CP-03_windows_edge_desktop/D2-detail.png` | Detail page, attachment thumbnail/lightbox, response section. | Có F-D2-001, F-D2-002; ảnh đại diện nằm trong `../findings/defect-screenshots/`. |
| D2-CP-04 | Android | Samsung Internet | Tablet | Samsung Galaxy Tab A + Samsung Internet | `Fail` | `screenshots/downloads/CP-04_android_samsung-internet_tablet/D2-list.png`; `screenshots/downloads/CP-04_android_samsung-internet_tablet/D2-detail.png` | Tablet list/detail layout and filter controls. | Có F-D2-001, F-D2-002; ảnh đại diện nằm trong `../findings/defect-screenshots/`. |
| D2-CP-05 | Android | Chrome | Phone | Samsung Galaxy A54 + Chrome | `Fail` | `screenshots/downloads/CP-05_android_chrome_phone/D2-list.png`; `screenshots/downloads/CP-05_android_chrome_phone/D2-detail.png` | Search/filter and card readability on phone. | Có F-D2-001, F-D2-002; ảnh đại diện nằm trong `../findings/defect-screenshots/`. |

## D3 - Admin Support Requests list

| Cell | OS | Browser | Device class | Device/profile | Result | Screenshot ref | Checklist focus | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D3-CP-01 | Linux | Firefox | Desktop | Linux desktop + Firefox latest | `Fail` | `screenshots/downloads/CP-01_linux_firefox_desktop/D3.png` | Admin sidebar, Pending/Resolved cards, filter wrap trên Firefox/Linux. | Có F-D3-001, F-D3-002; ảnh đại diện nằm trong `../findings/defect-screenshots/`. |
| D3-CP-02 | Windows 11 | Opera | Desktop | Windows 11 + Opera latest | `Fail` | `screenshots/downloads/CP-02_windows_opera_desktop/D3.png` | Admin sidebar, Pending tab, filter panel, cards, pagination. | Có F-D3-001, F-D3-002; ảnh đại diện nằm trong `../findings/defect-screenshots/`. |
| D3-CP-03 | Windows 11 | Edge | Desktop | Windows 11 + Edge latest | `Fail` | `screenshots/downloads/CP-03_windows_edge_desktop/D3.png` | Search/member-code/category filter rendering. | Có F-D3-001, F-D3-002; ảnh đại diện nằm trong `../findings/defect-screenshots/`. |
| D3-CP-04 | Android | Samsung Internet | Tablet | Samsung Galaxy Tab A + Samsung Internet | `Fail` | `screenshots/downloads/CP-04_android_samsung-internet_tablet/D3.png` | Tablet sidebar/content layout and filter usability. | Có F-D3-001, F-D3-002; ảnh đại diện nằm trong `../findings/defect-screenshots/`. |
| D3-CP-05 | Android | Chrome | Phone | Samsung Galaxy A54 + Chrome | `Fail` | `screenshots/downloads/CP-05_android_chrome_phone/D3.png` | Mobile admin layout, sidebar/content width, filter usability trên phone. | Có F-D3-003; ảnh đại diện nằm trong `../findings/defect-screenshots/`. |

## Coverage check sau khi chạy

| Screen | 3 OS covered? | 5 browsers covered? | 3 device classes covered? | Screenshot đủ chưa? | Notes |
| --- | --- | --- | --- | --- | --- |
| D1 | `Yes` | `Yes` | `Yes` | `Complete` | Đã có ảnh baseline cho CP-01 đến CP-05 trong `screenshots/downloads`; tất cả cell có defect evidence tương ứng. |
| D2 | `Yes` | `Yes` | `Yes` | `Complete` | Đã có ảnh baseline cho CP-01 đến CP-05 trong `screenshots/downloads`; CP-02 đến CP-05 có đủ ảnh list/detail, CP-01 có ảnh D2 tổng hợp. |
| D3 | `Yes` | `Yes` | `Yes` | `Complete` | Đã có ảnh baseline cho CP-01 đến CP-05 trong `screenshots/downloads`; tất cả cell có defect evidence tương ứng. |
