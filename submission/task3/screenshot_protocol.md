# Task 3 - Screenshot Protocol và Overlay

## 1. Khi nào chụp screenshot

Chụp một screenshot cho mỗi cell trong `matrix_template.md`. Với matrix đang dùng có `5` cell cho mỗi màn hình, tổng số ảnh tối thiểu là `15` ảnh.

| Màn hình | Số cell | Số ảnh tối thiểu |
| --- | ---: | ---: |
| D1 | 5 | 5 |
| D2 | 5 | 5 |
| D3 | 5 | 5 |
| Tổng | 15 | 15 |

## 2. Nội dung screenshot phải có

| Yếu tố | Cách kiểm tra trước khi lưu ảnh |
| --- | --- |
| EMS URL | Thanh địa chỉ hoặc browser frame phải thấy `https://prod-dev.ems-fitus.cloud/...`. |
| Browser/OS/device | Nếu dùng TestingBot/BrowserStack Live, chụp cả vùng toolbar/device label nếu có thể. |
| Overlay sinh viên | Trên trang EMS phải có text `23127075@clc.fitus.edu.vn`. |
| State đúng | D1 là form tạo request; D2 là list/detail user; D3 là admin support list/tab/filter. |
| Lỗi hiển thị | Nếu Fail, ảnh phải cho thấy lỗi, không chỉ chụp màn hình bình thường. |

Playwright local có thể chụp viewport hoặc full page của trang web, nhưng không chụp được toàn bộ giao diện TestingBot/BrowserStack/device/OS. Vì vậy Task 3 nên dùng screenshot của TestingBot Live, BrowserStack Live hoặc công cụ cloud tương đương để evidence có đủ identity môi trường.

## 3. Cách đặt overlay bằng DevTools Console

Mở DevTools/Console trong TestingBot session rồi chạy đoạn JavaScript sau trên trang EMS:

```js
(() => {
  const old = document.getElementById("hw03-student-overlay");
  if (old) old.remove();

  const badge = document.createElement("div");
  badge.id = "hw03-student-overlay";
  badge.textContent = "23127075@clc.fitus.edu.vn";
  badge.style.position = "fixed";
  badge.style.top = "12px";
  badge.style.right = "12px";
  badge.style.zIndex = "999999";
  badge.style.background = "rgba(255, 255, 255, 0.92)";
  badge.style.color = "#111827";
  badge.style.border = "2px solid #111827";
  badge.style.borderRadius = "6px";
  badge.style.padding = "6px 10px";
  badge.style.font = "600 14px Arial, sans-serif";
  badge.style.boxShadow = "0 2px 8px rgba(0,0,0,0.25)";
  document.body.appendChild(badge);
})();
```

Nếu overlay che nội dung quan trọng, chạy thêm một trong hai đoạn sau:

```js
const badge = document.getElementById("hw03-student-overlay");
badge.style.top = "auto";
badge.style.bottom = "12px";
badge.style.right = "12px";
```

```js
const badge = document.getElementById("hw03-student-overlay");
badge.style.left = "12px";
badge.style.right = "auto";
```

Không để overlay che lỗi UI, URL, nút chính, tab, hoặc nội dung dùng làm bằng chứng.

## 4. Naming convention

Lưu ảnh theo đúng tên trong matrix để dễ cross-check:

```text
submission/task3/screenshots/<Screen>_<Cell>_<os>_<browser>_<device>.png
```

Ví dụ:

```text
submission/task3/screenshots/D1_CP-01_linux_firefox_desktop.png
submission/task3/screenshots/D2_CP-04_android_samsung-internet_tablet.png
submission/task3/screenshots/D3_CP-05_android_chrome_phone.png
```

Nếu chụp thêm ảnh cho lỗi cụ thể, đặt tên có finding ID:

```text
submission/task3/screenshots/CP-F-D3-001_android_chrome_sidebar_overflow.png
```

## 5. Checklist trước khi chuyển sang cell tiếp theo

| Câu hỏi | Done? |
| --- | --- |
| Đúng account user/admin chưa? | `[ ]` |
| Đúng URL/màn hình chưa? | `[ ]` |
| Overlay email đã hiện chưa? | `[ ]` |
| Screenshot thấy browser/OS/device identity chưa? | `[ ]` |
| Nếu Fail, screenshot đã chụp đúng lỗi chưa? | `[ ]` |
| Đã ghi result và notes vào `matrix_template.md` chưa? | `[ ]` |
