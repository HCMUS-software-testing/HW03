# Task 3 Screenshots

Thư mục này lưu screenshot cross-browser/cross-platform cho Scenario D.

## Quy ước bắt buộc

Mỗi screenshot phải có:

1. EMS URL `https://prod-dev.ems-fitus.cloud/...`
2. Browser/OS/device identity từ TestingBot, BrowserStack, LambdaTest hoặc thiết bị thật.
3. Overlay `23127075@clc.fitus.edu.vn`.
4. Đúng screen/cell trong `submission/task3/matrix_template.md`.

## Chỗ tải ảnh thô

Tải screenshot gốc từ TestingBot/BrowserStack/LambdaTest/thiết bị thật vào các thư mục staging sau:

```text
submission/task3/screenshots/downloads/CP-01_linux_firefox_desktop/
submission/task3/screenshots/downloads/CP-02_windows_opera_desktop/
submission/task3/screenshots/downloads/CP-03_windows_edge_desktop/
submission/task3/screenshots/downloads/CP-04_android_chrome_tablet/
submission/task3/screenshots/downloads/CP-05_android_samsung-internet_phone/
```

Sau khi chọn ảnh cuối cùng, copy hoặc đổi tên ra root `submission/task3/screenshots/` theo đúng tên bên dưới để khớp report template.

## Tên file cuối cùng

```text
D1_CP-01_linux_firefox_desktop.png
D1_CP-02_windows_opera_desktop.png
D1_CP-03_windows_edge_desktop.png
D1_CP-04_android_chrome_tablet.png
D1_CP-05_android_samsung-internet_phone.png

D2_CP-01_linux_firefox_desktop.png
D2_CP-02_windows_opera_desktop.png
D2_CP-03_windows_edge_desktop.png
D2_CP-04_android_chrome_tablet.png
D2_CP-05_android_samsung-internet_phone.png

D3_CP-01_linux_firefox_desktop.png
D3_CP-02_windows_opera_desktop.png
D3_CP-03_windows_edge_desktop.png
D3_CP-04_android_chrome_tablet.png
D3_CP-05_android_samsung-internet_phone.png
```

Nếu có ảnh defect riêng:

```text
CP-F-D1-001_<short-problem>.png
CP-F-D2-001_<short-problem>.png
CP-F-D3-001_<short-problem>.png
```

Với ảnh failure riêng của D1 trong Task 3, tải ảnh thô vào đúng thư mục theo matrix:

```text
submission/task3/screenshots/defects/D1/D1_CP-01_linux_firefox_desktop/
submission/task3/screenshots/defects/D1/D1_CP-02_windows_opera_desktop/
submission/task3/screenshots/defects/D1/D1_CP-03_windows_edge_desktop/
submission/task3/screenshots/defects/D1/D1_CP-04_android_chrome_tablet/
submission/task3/screenshots/defects/D1/D1_CP-05_android_samsung-internet_phone/

submission/task3/screenshots/defects/D2/D2_CP-01_linux_firefox_desktop/
submission/task3/screenshots/defects/D2/D2_CP-02_windows_opera_desktop/
submission/task3/screenshots/defects/D2/D2_CP-03_windows_edge_desktop/
submission/task3/screenshots/defects/D2/D2_CP-04_android_chrome_tablet/
submission/task3/screenshots/defects/D2/D2_CP-05_android_samsung-internet_phone/

submission/task3/screenshots/defects/D3/D3_CP-01_linux_firefox_desktop/
submission/task3/screenshots/defects/D3/D3_CP-02_windows_opera_desktop/
submission/task3/screenshots/defects/D3/D3_CP-03_windows_edge_desktop/
submission/task3/screenshots/defects/D3/D3_CP-04_android_chrome_tablet/
submission/task3/screenshots/defects/D3/D3_CP-05_android_samsung-internet_phone/
```

Trong mỗi thư mục `D1_CP-*`, đặt file ảnh trực tiếp theo tên defect D1 từ Task 1B:

```text
F-D1-001_validation-not-inline.png
F-D1-002_category-submit-400-no-clear-ui-error.png
F-D1-003_cancel-discards-without-confirmation.png
F-D1-004_success-semantics-weak-closure.png
```

Trong mỗi thư mục `D2_CP-*`, dùng tên:

```text
F-D2-001_back-loses-filter-context.png
F-D2-002_search-no-results-misleading-empty-state.png
F-D2-003_mobile-floating-button-near-pagination.png
```

Trong mỗi thư mục `D3_CP-*`, dùng tên:

```text
F-D3-001_search-title-returns-extra-result.png
F-D3-002_tab-switch-loses-filter-context.png
F-D3-003_mobile-sidebar-overflow.png
```
