# Demo Task 3 - Cross-Platform Compatibility

## 1. Mục tiêu

Bộ file này là template demo độc lập để chuẩn bị và ghi nhận kiểm thử cross-platform / cross-browser cho một website hoặc web app bất kỳ.

Template này ưu tiên:

- Phủ đủ `OS`, `browser`, `device class` theo input người dùng.
- Dùng matrix rút gọn theo hướng pairwise để giảm số cell cần chạy.
- Tách rõ phần planning, evidence và reporting để dễ dùng lại.

## 2. Input dùng cho bản demo này

| Dimension | Giá trị |
| --- | --- |
| Operating systems | `Windows`, `Linux`, `Android` |
| Browsers | `Edge`, `Opera`, `Firefox`, `Samsung Internet`, `Chrome` |
| Device classes | `Desktop/Laptop`, `Tablet`, `Phone` |

Ghi chú:

- Trong matrix, `Desktop/Laptop` được gom thành một nhóm desktop vì cùng kiểu tương tác chuột/bàn phím và viewport rộng.
- Matrix demo không khóa vào một website cụ thể.
- Khi dùng thật, điền thêm `target_url`, `scope`, `test date`, `tester`, `credentials` nếu flow cần đăng nhập.

## 3. File trong thư mục này

| File | Mục đích |
| --- | --- |
| `compatibility_matrix.md` | Matrix test pairwise và bảng ghi kết quả cho từng cell. |
| `screenshot_protocol.md` | Quy tắc chụp ảnh, naming convention và evidence checklist. |
| `cross_platform_report.md` | Template tổng hợp kết quả, defect và khuyến nghị sau khi chạy test. |

## 4. Chiến lược coverage

Matrix dùng `5` cell để phủ:

- `3 OS`: Windows, Linux, Android
- `5 browsers`: Edge, Opera, Firefox, Samsung Internet, Chrome
- `3 device classes`: Desktop/Laptop, Tablet, Phone

Đây là mức coverage phù hợp cho:

- Demo kỹ năng
- Smoke compatibility check
- Đợt test có thời gian giới hạn

Nếu hệ thống có rủi ro cao hoặc flow quan trọng, có thể mở rộng thêm cell thay vì dùng đúng matrix tối thiểu này.

## 5. Cách dùng đề xuất

1. Điền thông tin hệ thống cần test vào `compatibility_matrix.md`.
2. Chọn flow, route hoặc màn hình cần kiểm tra.
3. Chạy từng cell theo matrix.
4. Chụp screenshot theo `screenshot_protocol.md`.
5. Ghi `Pass`, `Fail` hoặc `Needs review` cho từng cell.
6. Tổng hợp finding vào `cross_platform_report.md`.

## 6. Output mong đợi

Sau khi chạy thật, thư mục này nên chứa:

- Matrix đã điền kết quả
- Screenshot hoặc link evidence cho từng cell
- Report tổng hợp các lỗi compatibility
- Danh sách recommendation theo mức ưu tiên
