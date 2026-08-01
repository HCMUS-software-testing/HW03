# Log tổng hợp bug và usability findings

| Trường      | Giá trị                             |
| ----------- | ----------------------------------- |
| Sinh viên   | Lâm Hữu Khánh - 23127205            |
| Kịch bản    | C - Admin quản lý người dùng        |
| Google Form | https://forms.gle/CJQFQCAXcsDbXDMM9 |

Mọi defect hoặc đề xuất cải thiện tính khả dụng từ checklist execution, user testing và cross-platform testing phải xuất hiện ở cả file này và Google Form. Cột `Timestamp form` là khóa đối chiếu.

| ID     | Nguồn                  | Màn hình                | Loại      | Mức độ | Mô tả                                                                     | Bước tái hiện / minh chứng                                                                                               | Kết quả mong đợi                                                                                                   | Kết quả thực tế                                                                                                    | Đề xuất sửa                                                                                                                                                          | Ảnh minh chứng                                         | Timestamp form       |
| ------ | ---------------------- | ----------------------- | --------- | ------ | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | -------------------- |
| C-F001 | Checklist execution C1 | C1 Danh sách người dùng | Usability | 3      | Layout Users Management bị tràn ngang mạnh trên mobile viewport 375px.    | 1. Đăng nhập admin. 2. Mở Users Management trên viewport 375x667.<br />3. Quan sát sidebar, header, table và pagination. | Mobile layout không làm mất nội dung, không che nút chính và không buộc cuộn ngang quá mức ngoài vùng bảng hợp lý. | Sidebar vẫn chiếm phần lớn chiều ngang; nội dung chính bị ép hẹp, bảng chỉ còn thấy một phần cột Actions.          | Dùng mobile drawer/collapsed sidebar mặc định, cho table có responsive card layout hoặc horizontal scroll confined trong vùng bảng, không làm toàn trang tràn ngang. | `submission/screenshots/checklist-failures/C-F001.png` | Chờ sinh viên submit |
| C-F002 | Checklist execution C1 | C1 Danh sách người dùng | Usability | 2      | Empty state khi search không có kết quả thiếu hành động phục hồi rõ ràng. | 1. Đăng nhập admin. 2. Vào Users Management. 3. Nhập`zzzz-no-user-23127205` vào Search users.                            | Empty state giải thích ngắn gọn và cung cấp hành động tiếp theo như Clear search hoặc Reset filters.               | Hệ thống hiển thị`No users found matching your filters.` nhưng không có nút Clear/Reset rõ ràng trong empty state. | Thêm nút`Clear search` hoặc `Reset filters` ngay trong empty state và hiển thị tiêu chí đang áp dụng.                                                                | `submission/screenshots/checklist-failures/C-F002.png` | Chờ sinh viên submit |

## Thang mức độ nghiêm trọng

| Mức độ | Ý nghĩa                                                                         |
| ------ | ------------------------------------------------------------------------------- |
| 1      | Lỗi thẩm mỹ hoặc gây khó chịu nhẹ                                               |
| 2      | Vấn đề usability nhỏ, có workaround                                             |
| 3      | Vấn đề lớn gây chậm, nhầm lẫn hoặc lỗi thao tác đáng kể                         |
| 4      | Vấn đề nghiêm trọng chặn hoàn thành nhiệm vụ hoặc có rủi ro mất dữ liệu/bảo mật |
