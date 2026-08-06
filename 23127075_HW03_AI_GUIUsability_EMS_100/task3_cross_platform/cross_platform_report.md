# Task 3 - Cross-Browser / Cross-Platform Report

> Ghi chú về dung lượng bài nộp: các screenshot defect gốc theo từng cell cross-platform trong `submission\task3\screenshots\defects` không được include đầy đủ trong folder nộp vì số lượng ảnh lớn và làm bài nộp nặng. Folder nộp chỉ giữ ảnh đại diện đã gom ở `../findings/defect-screenshots/`; nếu cần đối chiếu toàn bộ screenshot defect gốc, giảng viên có thể xem repository [HCMUS-software-testing/HW03.git](https://github.com/HCMUS-software-testing/HW03.git), branch `kien`.

## 1. Scope

| Trường | Giá trị |
| --- | --- |
| Sinh viên | Lê Trung Kiên |
| MSSV | `23127075` |
| Email overlay | `23127075@student.hcmus.edu.vn` |
| Scenario | D - User requests Support and Admin resolves it |
| SUT | `https://prod-dev.ems-fitus.cloud` |
| Screens | D1, D2, D3 |
| Công cụ | `TestingBot` |
| Ngày test | `2026-08-06` |
| Trạng thái thực thi | `Hoàn tất` |

## 2. Test Environment

| Cell | OS | Browser | Device class | Device/profile | Tool/session link | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-01 | Linux | Firefox | Desktop | `Linux desktop + Firefox latest` | `Không ghi nhận trong repo` | Desktop Firefox trên Linux, có ảnh D1/D2/D3 trong `screenshots/downloads/CP-01_linux_firefox_desktop/`. |
| CP-02 | Windows 11 | Opera | Desktop | `Windows 11 + Opera latest` | `Không ghi nhận trong repo` | Desktop Opera, có ảnh D1/D2-list/D2-detail/D3 trong `screenshots/downloads/CP-02_windows_opera_desktop/`. |
| CP-03 | Windows 11 | Edge | Desktop | `Windows 11 + Edge latest` | `Không ghi nhận trong repo` | Desktop Edge, có ảnh D1/D2-list/D2-detail/D3 trong `screenshots/downloads/CP-03_windows_edge_desktop/`. |
| CP-04 | Android | Samsung Internet | Tablet | `Samsung Galaxy Tab A + Samsung Internet` | `Không ghi nhận trong repo` | Tablet Samsung chạy Samsung Internet, có ảnh D1/D2-list/D2-detail/D3 trong `screenshots/downloads/CP-04_android_samsung-internet_tablet/`. |
| CP-05 | Android | Chrome | Phone | `Samsung Galaxy A54 + Chrome` | `Không ghi nhận trong repo` | Điện thoại Android Samsung chạy Chrome, có ảnh D1/D2-list/D2-detail/D3 trong `screenshots/downloads/CP-05_android_chrome_phone/`. |

## 3. Method

1. Đọc yêu cầu Task 3 trong `docs/2026.HW03.GUI Usability EMS_En.md`.
2. Dùng ba màn hình đã test ở Task 1B: D1, D2, D3.
3. Dùng checklist gốc `../../task1A_group_checklist/group/gui_usability_checklist_final.md`, nhưng tập trung vào các item compatibility trong `compatibility-focused checklist subset`.
4. Với mỗi cell, mở EMS trên môi trường tương ứng, đăng nhập đúng vai trò, đặt overlay `23127075@student.hcmus.edu.vn`, chụp screenshot và ghi `Pass/Fail`.
5. Với mỗi `Fail`, ghi defect vào Google Form và log tổng hợp.

## 4. Result Summary

| Screen | Cells run | Pass | Fail | Needs review | Compatibility risk summary |
| --- | ---: | ---: | ---: | ---: | --- |
| D1 | 5 | 0 | 5 | 0 | Form tạo support request tái hiện lỗi validation không inline, lỗi category/submit `400`, `Cancel` mất dữ liệu và thông báo success chưa tạo closure rõ trên nhiều browser/device. |
| D2 | 5 | 0 | 5 | 0 | My Requests list/detail tái hiện lỗi mất filter context khi quay lại detail và empty state gây hiểu nhầm trên tất cả cell đã chụp. |
| D3 | 5 | 0 | 5 | 0 | Admin Support Requests có lỗi search trả thêm kết quả không liên quan, đổi tab làm mất filter context trên desktop/tablet, và lỗi sidebar/content nghiêm trọng trên Android phone. |
| Total | 15 | 0 | 15 | 0 | Matrix phủ đủ `3 OS`, `5 browsers/platforms`, `3 device classes`; tất cả cell có ít nhất một defect evidence. |

## 5. Per-Screen Results

### D1 - User tạo support request

| Cell | OS | Browser | Device class | Result | Screenshot ref | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| D1-CP-01 | Linux | Firefox | Desktop | `Fail` | `screenshots/downloads/CP-01_linux_firefox_desktop/D1.png` | Có F-D1-001, F-D1-002, F-D1-003; ảnh đại diện nằm trong `../findings/defect-screenshots/`. |
| D1-CP-02 | Windows 11 | Opera | Desktop | `Fail` | `screenshots/downloads/CP-02_windows_opera_desktop/D1.png` | Có F-D1-001, F-D1-002, F-D1-003, F-D1-004; ảnh đại diện nằm trong `../findings/defect-screenshots/`. |
| D1-CP-03 | Windows 11 | Edge | Desktop | `Fail` | `screenshots/downloads/CP-03_windows_edge_desktop/D1.png` | Có F-D1-001, F-D1-002, F-D1-003, F-D1-004; ảnh đại diện nằm trong `../findings/defect-screenshots/`. |
| D1-CP-04 | Android | Samsung Internet | Tablet | `Fail` | `screenshots/downloads/CP-04_android_samsung-internet_tablet/D1.png` | Có F-D1-001, F-D1-002, F-D1-003, F-D1-004; ảnh đại diện nằm trong `../findings/defect-screenshots/`. |
| D1-CP-05 | Android | Chrome | Phone | `Fail` | `screenshots/downloads/CP-05_android_chrome_phone/D1.png` | Có F-D1-001, F-D1-003, F-D1-004; ảnh đại diện nằm trong `../findings/defect-screenshots/`. |

### D2 - User My Requests list/detail

| Cell | OS | Browser | Device class | Result | Screenshot ref | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| D2-CP-01 | Linux | Firefox | Desktop | `Fail` | `screenshots/downloads/CP-01_linux_firefox_desktop/D2.png` | Có F-D2-001, F-D2-002; ảnh đại diện nằm trong `../findings/defect-screenshots/`. |
| D2-CP-02 | Windows 11 | Opera | Desktop | `Fail` | `screenshots/downloads/CP-02_windows_opera_desktop/D2-list.png`; `screenshots/downloads/CP-02_windows_opera_desktop/D2-detail.png` | Có F-D2-001, F-D2-002; ảnh đại diện nằm trong `../findings/defect-screenshots/`. |
| D2-CP-03 | Windows 11 | Edge | Desktop | `Fail` | `screenshots/downloads/CP-03_windows_edge_desktop/D2-list.png`; `screenshots/downloads/CP-03_windows_edge_desktop/D2-detail.png` | Có F-D2-001, F-D2-002; ảnh đại diện nằm trong `../findings/defect-screenshots/`. |
| D2-CP-04 | Android | Samsung Internet | Tablet | `Fail` | `screenshots/downloads/CP-04_android_samsung-internet_tablet/D2-list.png`; `screenshots/downloads/CP-04_android_samsung-internet_tablet/D2-detail.png` | Có F-D2-001, F-D2-002; ảnh đại diện nằm trong `../findings/defect-screenshots/`. |
| D2-CP-05 | Android | Chrome | Phone | `Fail` | `screenshots/downloads/CP-05_android_chrome_phone/D2-list.png`; `screenshots/downloads/CP-05_android_chrome_phone/D2-detail.png` | Có F-D2-001, F-D2-002; ảnh đại diện nằm trong `../findings/defect-screenshots/`. |

### D3 - Admin Support Requests list

| Cell | OS | Browser | Device class | Result | Screenshot ref | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| D3-CP-01 | Linux | Firefox | Desktop | `Fail` | `screenshots/downloads/CP-01_linux_firefox_desktop/D3.png` | Có F-D3-001, F-D3-002; ảnh đại diện nằm trong `../findings/defect-screenshots/`. |
| D3-CP-02 | Windows 11 | Opera | Desktop | `Fail` | `screenshots/downloads/CP-02_windows_opera_desktop/D3.png` | Có F-D3-001, F-D3-002; ảnh đại diện nằm trong `../findings/defect-screenshots/`. |
| D3-CP-03 | Windows 11 | Edge | Desktop | `Fail` | `screenshots/downloads/CP-03_windows_edge_desktop/D3.png` | Có F-D3-001, F-D3-002; ảnh đại diện nằm trong `../findings/defect-screenshots/`. |
| D3-CP-04 | Android | Samsung Internet | Tablet | `Fail` | `screenshots/downloads/CP-04_android_samsung-internet_tablet/D3.png` | Có F-D3-001, F-D3-002; ảnh đại diện nằm trong `../findings/defect-screenshots/`. |
| D3-CP-05 | Android | Chrome | Phone | `Fail` | `screenshots/downloads/CP-05_android_chrome_phone/D3.png` | Có F-D3-003; ảnh đại diện nằm trong `../findings/defect-screenshots/`. |

## 6. Compatibility Findings

| ID | Screen | Cell(s) | Type | Description | Severity | Screenshot ref | Google Form timestamp |
| --- | --- | --- | --- | --- | ---: | --- | --- |
| `CP-F-D1-001` | D1 | D1-CP-01, D1-CP-02, D1-CP-03, D1-CP-04, D1-CP-05 | Usability | Required-field validation chưa inline theo từng input, làm người dùng khó biết trường nào cần sửa khi tạo support request. | 2 | `../findings/defect-screenshots/F-D1-001_validation-not-inline.png` | `06/08/2026 13:24` |
| `CP-F-D1-002` | D1 | D1-CP-01, D1-CP-02, D1-CP-03, D1-CP-04 | Bug | Request type/category hiển thị như đã có giá trị nhưng submit trả lỗi `400`, UI không chỉ rõ nguyên nhân hoặc cách sửa. | 3 | `../findings/defect-screenshots/F-D1-002_category-submit-400-no-clear-ui-error.png` | `06/08/2026 13:25` |
| `CP-F-D1-003` | D1 | D1-CP-01, D1-CP-02, D1-CP-03, D1-CP-04, D1-CP-05 | Usability | Nút `Cancel` bỏ dữ liệu form đang nhập mà không có xác nhận, tăng rủi ro mất dữ liệu trên cả desktop và mobile. | 3 | `../findings/defect-screenshots/F-D1-003_cancel-discards-without-confirmation.png` | `06/08/2026 13:26` |
| `CP-F-D1-004` | D1 | D1-CP-02, D1-CP-03, D1-CP-04, D1-CP-05 | Usability | Submit thành công nhưng success message chưa nói rõ request đã được tạo, bước tiếp theo hoặc nơi xem trạng thái. | 2 | `../findings/defect-screenshots/F-D1-004_success-semantics-weak-closure.png` | `06/08/2026 13:26` |
| `CP-F-D2-001` | D2 | D2-CP-01, D2-CP-02, D2-CP-03, D2-CP-04, D2-CP-05 | Usability | Khi mở detail rồi `Back` về list, search/status filter bị mất context làm người dùng phải lọc lại. | 2 | `../findings/defect-screenshots/F-D2-001_back-loses-filter-context.png` | `06/08/2026 13:27` |
| `CP-F-D2-002` | D2 | D2-CP-01, D2-CP-02, D2-CP-03, D2-CP-04, D2-CP-05 | Usability | Empty state khi search không có kết quả gây hiểu nhầm vì không nhắc tiêu chí tìm kiếm/filter hiện tại hoặc cách reset. | 2 | `../findings/defect-screenshots/F-D2-002_search-no-results-misleading-empty-state.png` | `06/08/2026 13:28` |
| `CP-F-D3-001` | D3 | D3-CP-01, D3-CP-02, D3-CP-03, D3-CP-04 | Bug | Admin search theo title cụ thể vẫn trả thêm support request không liên quan, làm kết quả lọc thiếu tin cậy. | 3 | `../findings/defect-screenshots/F-D3-001_search-title-returns-extra-result.png` | `06/08/2026 13:29` |
| `CP-F-D3-002` | D3 | D3-CP-01, D3-CP-02, D3-CP-03, D3-CP-04 | Usability | Đổi giữa `Pending` và `Resolved` tab làm mất filter/search context, khiến admin phải nhập lại tiêu chí. | 2 | `../findings/defect-screenshots/F-D3-002_tab-switch-loses-filter-context.png` | `06/08/2026 13:30` |
| `CP-F-D3-003` | D3 | D3-CP-05 | Usability | Trên Android Chrome phone, admin sidebar/content bị vỡ hoặc chiếm chiều ngang, làm vùng nội dung chính khó đọc và khó thao tác. | 3 | `../findings/defect-screenshots/F-D3-003_mobile-sidebar-overflow.png` | `06/08/2026 13:31` |

## 7. Conclusion

Kết quả Task 3 cho thấy cả ba màn hình D1, D2 và D3 đều có lỗi usability/compatibility tái hiện trên nhiều môi trường. D2 có rủi ro thấp hơn vì lỗi chủ yếu ảnh hưởng hiệu quả thao tác khi lọc và quay lại detail. D1 có rủi ro trung bình-cao do liên quan trực tiếp đến tạo support request, validation, submit và khả năng mất dữ liệu form. D3 có rủi ro cao nhất trên mobile vì layout admin bị vỡ ở Android Chrome phone, đồng thời search/filter context chưa ổn định trên desktop/tablet.

Ưu tiên sửa đề xuất: xử lý D3 mobile sidebar/content responsive trước, sau đó sửa D1 category submit `400` và xác nhận `Cancel`, cuối cùng cải thiện giữ filter context/empty state cho D2-D3.
