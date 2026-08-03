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
| Công cụ | `[BrowserStack Live / LambdaTest / thiết bị thật - điền sau]` |
| Ngày test | `[YYYY-MM-DD]` |

## 2. Test Environment

| Cell | OS | Browser | Device class | Device/profile | Tool/session link | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-01 | Windows 11 | Chrome | Desktop | `[Điền device/profile]` | `[Điền link nếu có]` | Baseline desktop. |
| CP-02 | Windows 11 | Edge | Desktop | `[Điền device/profile]` | `[Điền link nếu có]` | Desktop Edge. |
| CP-03 | macOS | Safari | Desktop | `[Điền device/profile]` | `[Điền link nếu có]` | Safari desktop. |
| CP-04 | Android | Chrome | Phone | `[Điền device/profile]` | `[Điền link nếu có]` | Android phone Chrome. |
| CP-05 | Android | Firefox | Phone | `[Điền device/profile]` | `[Điền link nếu có]` | Android phone Firefox. |
| CP-06 | iOS | Safari | Phone | `[Điền device/profile]` | `[Điền link nếu có]` | iOS Safari. |
| CP-07 | Android/iPadOS | Samsung Internet/Opera | Tablet | `[Điền device/profile]` | `[Điền link nếu có]` | Tablet coverage và browser thứ 5. |

## 3. Method

1. Đọc yêu cầu Task 3 trong `docs/2026.HW03.GUI Usability EMS_En.md`.
2. Dùng ba màn hình đã test ở Task 1B: D1, D2, D3.
3. Dùng checklist gốc `submission/group/gui_usability_checklist_final.md`, nhưng tập trung vào các item compatibility trong `task3_checklist_scope.md`.
4. Với mỗi cell, mở EMS trên môi trường tương ứng, đăng nhập đúng vai trò, đặt overlay `23127075@clc.fitus.edu.vn`, chụp screenshot và ghi `Pass/Fail`.
5. Với mỗi `Fail`, ghi defect vào Google Form và log tổng hợp.

## 4. Result Summary

| Screen | Cells run | Pass | Fail | Needs review | Compatibility risk summary |
| --- | ---: | ---: | ---: | ---: | --- |
| D1 | 7 | `[ ]` | `[ ]` | `[ ]` | `[Tóm tắt sau khi test]` |
| D2 | 7 | `[ ]` | `[ ]` | `[ ]` | `[Tóm tắt sau khi test]` |
| D3 | 7 | `[ ]` | `[ ]` | `[ ]` | `[Tóm tắt sau khi test]` |
| Total | 21 | `[ ]` | `[ ]` | `[ ]` | `[Tóm tắt sau khi test]` |

## 5. Per-Screen Results

### D1 - User tạo support request

| Cell | OS | Browser | Device class | Result | Screenshot ref | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| D1-CP-01 | Windows 11 | Chrome | Desktop | `[Pass/Fail]` | `submission/task3/screenshots/D1_CP-01_windows_chrome_desktop.png` | `[Điền sau]` |
| D1-CP-02 | Windows 11 | Edge | Desktop | `[Pass/Fail]` | `submission/task3/screenshots/D1_CP-02_windows_edge_desktop.png` | `[Điền sau]` |
| D1-CP-03 | macOS | Safari | Desktop | `[Pass/Fail]` | `submission/task3/screenshots/D1_CP-03_macos_safari_desktop.png` | `[Điền sau]` |
| D1-CP-04 | Android | Chrome | Phone | `[Pass/Fail]` | `submission/task3/screenshots/D1_CP-04_android_chrome_phone.png` | `[Điền sau]` |
| D1-CP-05 | Android | Firefox | Phone | `[Pass/Fail]` | `submission/task3/screenshots/D1_CP-05_android_firefox_phone.png` | `[Điền sau]` |
| D1-CP-06 | iOS | Safari | Phone | `[Pass/Fail]` | `submission/task3/screenshots/D1_CP-06_ios_safari_phone.png` | `[Điền sau]` |
| D1-CP-07 | Android/iPadOS | Samsung Internet/Opera | Tablet | `[Pass/Fail]` | `submission/task3/screenshots/D1_CP-07_tablet_samsung_or_opera.png` | `[Điền sau]` |

### D2 - User My Requests list/detail

| Cell | OS | Browser | Device class | Result | Screenshot ref | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| D2-CP-01 | Windows 11 | Chrome | Desktop | `[Pass/Fail]` | `submission/task3/screenshots/D2_CP-01_windows_chrome_desktop.png` | `[Điền sau]` |
| D2-CP-02 | Windows 11 | Edge | Desktop | `[Pass/Fail]` | `submission/task3/screenshots/D2_CP-02_windows_edge_desktop.png` | `[Điền sau]` |
| D2-CP-03 | macOS | Safari | Desktop | `[Pass/Fail]` | `submission/task3/screenshots/D2_CP-03_macos_safari_desktop.png` | `[Điền sau]` |
| D2-CP-04 | Android | Chrome | Phone | `[Pass/Fail]` | `submission/task3/screenshots/D2_CP-04_android_chrome_phone.png` | `[Điền sau]` |
| D2-CP-05 | Android | Firefox | Phone | `[Pass/Fail]` | `submission/task3/screenshots/D2_CP-05_android_firefox_phone.png` | `[Điền sau]` |
| D2-CP-06 | iOS | Safari | Phone | `[Pass/Fail]` | `submission/task3/screenshots/D2_CP-06_ios_safari_phone.png` | `[Điền sau]` |
| D2-CP-07 | Android/iPadOS | Samsung Internet/Opera | Tablet | `[Pass/Fail]` | `submission/task3/screenshots/D2_CP-07_tablet_samsung_or_opera.png` | `[Điền sau]` |

### D3 - Admin Support Requests list

| Cell | OS | Browser | Device class | Result | Screenshot ref | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| D3-CP-01 | Windows 11 | Chrome | Desktop | `[Pass/Fail]` | `submission/task3/screenshots/D3_CP-01_windows_chrome_desktop.png` | `[Điền sau]` |
| D3-CP-02 | Windows 11 | Edge | Desktop | `[Pass/Fail]` | `submission/task3/screenshots/D3_CP-02_windows_edge_desktop.png` | `[Điền sau]` |
| D3-CP-03 | macOS | Safari | Desktop | `[Pass/Fail]` | `submission/task3/screenshots/D3_CP-03_macos_safari_desktop.png` | `[Điền sau]` |
| D3-CP-04 | Android | Chrome | Phone | `[Pass/Fail]` | `submission/task3/screenshots/D3_CP-04_android_chrome_phone.png` | `[Điền sau]` |
| D3-CP-05 | Android | Firefox | Phone | `[Pass/Fail]` | `submission/task3/screenshots/D3_CP-05_android_firefox_phone.png` | `[Điền sau]` |
| D3-CP-06 | iOS | Safari | Phone | `[Pass/Fail]` | `submission/task3/screenshots/D3_CP-06_ios_safari_phone.png` | `[Điền sau]` |
| D3-CP-07 | Android/iPadOS | Samsung Internet/Opera | Tablet | `[Pass/Fail]` | `submission/task3/screenshots/D3_CP-07_tablet_samsung_or_opera.png` | `[Điền sau]` |

## 6. Compatibility Findings

| ID | Screen | Cell(s) | Type | Description | Severity | Screenshot ref | Google Form timestamp |
| --- | --- | --- | --- | --- | ---: | --- | --- |
| `CP-F-001` | `[D1/D2/D3]` | `[Cell ID]` | `[Bug/Usability]` | `[Mô tả lỗi tương thích]` | `[0-4]` | `[Screenshot path]` | `[Điền sau khi submit form]` |

## 7. Conclusion

`[Viết sau khi chạy thật: nêu màn hình nào ổn định nhất, màn hình nào có rủi ro compatibility cao nhất, browser/device nào tạo lỗi nghiêm trọng nhất, và ưu tiên sửa.]`

