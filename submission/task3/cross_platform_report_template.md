# Task 3 - Cross-Browser / Cross-Platform Report

## 1. Scope

| Trường | Giá trị |
| --- | --- |
| Sinh viên | Lê Trung Kiên |
| MSSV | `23127075` |
| Email overlay | `23127075@clc.fitus.edu.vn` |
| Scenario | D - User requests Support and Admin resolves it |
| SUT | `https://prod-dev.ems-fitus.cloud` |
| Screens | D1, D2, D3 |
| Công cụ | `BrowserStack Live` |
| Ngày test | `[YYYY-MM-DD]` |
| Trạng thái thực thi | `[Chưa chạy thật / Đang chạy / Hoàn tất]` |

## 2. Test Environment

| Cell | OS | Browser | Device class | Device/profile | Tool/session link | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-01 | Linux | Firefox | Desktop | `Linux desktop + Firefox latest` | `[Điền link nếu có]` | Desktop Firefox trên Linux. |
| CP-02 | Windows 11 | Opera | Desktop | `Windows 11 + Opera latest` | `[Điền link nếu có]` | Desktop Opera. |
| CP-03 | Windows 11 | Edge | Desktop | `Windows 11 + Edge latest` | `[Điền link nếu có]` | Desktop Edge. |
| CP-04 | Android | Samsung Internet | Tablet | `Samsung Galaxy Tab S8/S9/A9 + Samsung Internet` | `[Điền link nếu có]` | Tablet coverage. |
| CP-05 | Android | Chrome | Phone | `Samsung Galaxy S23/S24 hoặc Pixel + Chrome` | `[Điền link nếu có]` | Android phone Chrome. |

## 3. Method

1. Đọc yêu cầu Task 3 trong `docs/2026.HW03.GUI Usability EMS_En.md`.
2. Dùng ba màn hình đã test ở Task 1B: D1, D2, D3.
3. Dùng checklist gốc `submission/group/gui_usability_checklist_final.md`, nhưng tập trung vào các item compatibility trong `task3_checklist_scope.md`.
4. Với mỗi cell, mở EMS trên môi trường tương ứng, đăng nhập đúng vai trò, đặt overlay `23127075@clc.fitus.edu.vn`, chụp screenshot và ghi `Pass/Fail`.
5. Với mỗi `Fail`, ghi defect vào Google Form và log tổng hợp.

## 4. Result Summary

| Screen | Cells run | Pass | Fail | Needs review | Compatibility risk summary |
| --- | ---: | ---: | ---: | ---: | --- |
| D1 | 5 | `[ ]` | `[ ]` | `[ ]` | `[Tóm tắt sau khi test]` |
| D2 | 5 | `[ ]` | `[ ]` | `[ ]` | `[Tóm tắt sau khi test]` |
| D3 | 5 | `[ ]` | `[ ]` | `[ ]` | `[Tóm tắt sau khi test]` |
| Total | 15 | `[ ]` | `[ ]` | `[ ]` | `[Tóm tắt sau khi test]` |

## 5. Per-Screen Results

### D1 - User tạo support request

| Cell | OS | Browser | Device class | Result | Screenshot ref | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| D1-CP-01 | Linux | Firefox | Desktop | `[Pass/Fail]` | `submission/task3/screenshots/D1_CP-01_linux_firefox_desktop.png` | `[Điền sau]` |
| D1-CP-02 | Windows 11 | Opera | Desktop | `[Pass/Fail]` | `submission/task3/screenshots/D1_CP-02_windows_opera_desktop.png` | `[Điền sau]` |
| D1-CP-03 | Windows 11 | Edge | Desktop | `[Pass/Fail]` | `submission/task3/screenshots/D1_CP-03_windows_edge_desktop.png` | `[Điền sau]` |
| D1-CP-04 | Android | Samsung Internet | Tablet | `[Pass/Fail]` | `submission/task3/screenshots/D1_CP-04_android_samsung-tablet.png` | `[Điền sau]` |
| D1-CP-05 | Android | Chrome | Phone | `[Pass/Fail]` | `submission/task3/screenshots/D1_CP-05_android_chrome_phone.png` | `[Điền sau]` |

### D2 - User My Requests list/detail

| Cell | OS | Browser | Device class | Result | Screenshot ref | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| D2-CP-01 | Linux | Firefox | Desktop | `[Pass/Fail]` | `submission/task3/screenshots/D2_CP-01_linux_firefox_desktop.png` | `[Điền sau]` |
| D2-CP-02 | Windows 11 | Opera | Desktop | `[Pass/Fail]` | `submission/task3/screenshots/D2_CP-02_windows_opera_desktop.png` | `[Điền sau]` |
| D2-CP-03 | Windows 11 | Edge | Desktop | `[Pass/Fail]` | `submission/task3/screenshots/D2_CP-03_windows_edge_desktop.png` | `[Điền sau]` |
| D2-CP-04 | Android | Samsung Internet | Tablet | `[Pass/Fail]` | `submission/task3/screenshots/D2_CP-04_android_samsung-tablet.png` | `[Điền sau]` |
| D2-CP-05 | Android | Chrome | Phone | `[Pass/Fail]` | `submission/task3/screenshots/D2_CP-05_android_chrome_phone.png` | `[Điền sau]` |

### D3 - Admin Support Requests list

| Cell | OS | Browser | Device class | Result | Screenshot ref | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| D3-CP-01 | Linux | Firefox | Desktop | `[Pass/Fail]` | `submission/task3/screenshots/D3_CP-01_linux_firefox_desktop.png` | `[Điền sau]` |
| D3-CP-02 | Windows 11 | Opera | Desktop | `[Pass/Fail]` | `submission/task3/screenshots/D3_CP-02_windows_opera_desktop.png` | `[Điền sau]` |
| D3-CP-03 | Windows 11 | Edge | Desktop | `[Pass/Fail]` | `submission/task3/screenshots/D3_CP-03_windows_edge_desktop.png` | `[Điền sau]` |
| D3-CP-04 | Android | Samsung Internet | Tablet | `[Pass/Fail]` | `submission/task3/screenshots/D3_CP-04_android_samsung-tablet.png` | `[Điền sau]` |
| D3-CP-05 | Android | Chrome | Phone | `[Pass/Fail]` | `submission/task3/screenshots/D3_CP-05_android_chrome_phone.png` | `[Điền sau]` |

## 6. Compatibility Findings

| ID | Screen | Cell(s) | Type | Description | Severity | Screenshot ref | Google Form timestamp |
| --- | --- | --- | --- | --- | ---: | --- | --- |
| `CP-F-001` | `[D1/D2/D3]` | `[Cell ID]` | `[Bug/Usability]` | `[Mô tả lỗi tương thích]` | `[0-4]` | `[Screenshot path]` | `[Điền sau khi submit form]` |

## 7. Conclusion

`[Viết sau khi chạy thật: nêu màn hình nào ổn định nhất, màn hình nào có rủi ro compatibility cao nhất, browser/device nào tạo lỗi nghiêm trọng nhất, và ưu tiên sửa.]`
