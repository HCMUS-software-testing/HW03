# Checklist cap defect cross-platform cho D1-D2-D3

File này dùng để đối chiếu khi chụp lỗi cross-platform trong Task 3. Với mỗi defect, chạy lại trên các cell trong matrix:

- `CP-01`: Linux desktop + Firefox
- `CP-02`: Windows 11 desktop + Opera
- `CP-03`: Windows 11 desktop + Edge
- `CP-04`: Android tablet Samsung Galaxy Tab A + Samsung Internet
- `CP-05`: Android phone Samsung Galaxy A54 + Chrome

## D1 - User tạo support request

- [ ] `F-D1-001` - Validation required fields chưa inline
  - Loại: Usability
  - Cách tái hiện: mở `/complaints/new`, để trống `Request type`, `Issue requiring support`, `Detailed description`, rồi bấm `Submit request`.
  - Cần cap: alert chung `Request type, issue requiring support and detailed description are required.` xuất hiện thay vì lỗi đặt cạnh từng field; trên mobile/tablet cần thấy alert có dễ bị khuất hoặc khó liên hệ với field lỗi không.
  - Ưu tiên cap: `D1-CP-04`, `D1-CP-05`, sau đó `D1-CP-02` hoặc `D1-CP-03`.
  - Tên ảnh gợi ý: `F-D1-001_validation-not-inline.png`

- [ ] `F-D1-002` - Request type/category hiển thị như có giá trị nhưng submit lỗi `400`
  - Loại: Bug
  - Cách tái hiện: mở `/complaints/new`, quan sát request type hiển thị ví dụ/default, điền issue/description/upload ảnh, submit khi chưa chọn rõ option hợp lệ hoặc khi select rơi vào trạng thái lỗi.
  - Cần cap: UI select/category và lỗi submit/API hoặc message recovery không rõ; nếu browser khác render select khác nhau thì cap rõ trạng thái đó.
  - Ưu tiên cap: `D1-CP-03`, `D1-CP-04`, `D1-CP-05`.
  - Tên ảnh gợi ý: `F-D1-002_category-submit-400-no-clear-ui-error.png`

- [ ] `F-D1-003` - `Cancel` bỏ dữ liệu form không có xác nhận
  - Loại: Usability
  - Cách tái hiện: nhập issue/description, attach ảnh, bấm `Cancel`.
  - Cần cap: form đã có dữ liệu trước khi cancel và trạng thái sau khi rời trang không có confirmation/undo/draft recovery.
  - Ưu tiên cap: `D1-CP-04`, `D1-CP-05`, vì mobile/tablet dễ bấm nhầm hơn.
  - Tên ảnh gợi ý: `F-D1-003_cancel-discards-without-confirmation.png`

- [ ] `F-D1-004` - Submit thành công nhưng success message sai ngữ cảnh/closure yếu
  - Loại: Bug
  - Cách tái hiện: chọn category hợp lệ, nhập issue/description, upload PNG, submit.
  - Cần cap: redirect về `/complaints?created=1`, request mới xuất hiện `Pending`, nhưng không có success toast/banner rõ hoặc message backend liên quan `Event review`.
  - Ưu tiên cap: bất kỳ cell nào tái hiện được; nếu không thấy message backend thì cap UI closure yếu.
  - Tên ảnh gợi ý: `F-D1-004_success-semantics-weak-closure.png`

## D2 - User My Requests list/detail

- [ ] `F-D2-001` - `Back` từ detail làm mất search/status filter
  - Loại: Usability
  - Cách tái hiện: mở `/complaints?status=RESOLVED&search=keyboard`, mở request detail `/complaints/56`, bấm `Back`.
  - Cần cap: trước khi mở detail có filter/search đang áp dụng; sau khi back URL về `/complaints`, search rỗng và status về `All statuses`.
  - Ưu tiên cap: `D2-CP-04`, `D2-CP-05`, thêm một desktop cell để so sánh.
  - Tên ảnh gợi ý: `F-D2-001_back-loses-filter-context.png`

- [ ] `F-D2-002` - Empty state khi no-result gây hiểu nhầm
  - Loại: Usability
  - Cách tái hiện: mở `/complaints`, nhập search không có kết quả, ví dụ `not-found-D2-2026`.
  - Cần cap: UI hiển thị `No requests yet` và hướng tạo request dù đây chỉ là trạng thái không khớp search/filter; không có nút `Clear filters` rõ.
  - Ưu tiên cap: `D2-CP-01`, `D2-CP-04`, `D2-CP-05`.
  - Tên ảnh gợi ý: `F-D2-002_search-no-results-misleading-empty-state.png`

- [ ] `F-D2-003` - Floating social links che/sát pagination trên mobile
  - Loại: Usability
  - Cách tái hiện: mở `/complaints` ở viewport phone hoặc tablet, kéo đến cuối list/pagination.
  - Cần cap: nút social links màu xanh nằm sát hoặc che vùng card/pagination/right edge, có thể cản thao tác.
  - Ưu tiên cap: `D2-CP-05`, sau đó `D2-CP-04`. Đây là lỗi responsive nên desktop chỉ dùng để đối chiếu nếu cần.
  - Tên ảnh gợi ý: `F-D2-003_mobile-floating-button-near-pagination.png`

## D3 - Admin Support Requests list

- [ ] `F-D3-001` - Search theo title cụ thể vẫn trả thêm request không liên quan
  - Loại: Usability
  - Cách tái hiện: mở `/dashboard/admin/complaints`, ở Pending tab nhập `QA D3 pending list search test` vào `Search name, email or title`.
  - Cần cap: list có request khớp của Kiên nhưng vẫn có thêm request không có `QA D3` trong title/requester; nếu có highlight/match không rõ thì cap thêm.
  - Ưu tiên cap: `D3-CP-01`, `D3-CP-03`, `D3-CP-04`.
  - Tên ảnh gợi ý: `F-D3-001_search-title-returns-extra-result.png`

- [ ] `F-D3-002` - Đổi Pending/Resolved tab làm mất filter context
  - Loại: Usability
  - Cách tái hiện: filter `Member code = G18D126AA`, chọn category `Support`, bấm tab `Resolved`.
  - Cần cap: trước khi đổi tab có filter đang áp dụng; sau khi đổi sang resolved URL còn `?tab=resolved` nhưng filter fields bị clear và list trở về tất cả resolved requests.
  - Ưu tiên cap: `D3-CP-01`, `D3-CP-04`, `D3-CP-05`.
  - Tên ảnh gợi ý: `F-D3-002_tab-switch-loses-filter-context.png`

- [ ] `F-D3-003` - Admin mobile layout bị vỡ do sidebar fixed chiếm chiều ngang
  - Loại: Bug
  - Cách tái hiện: mở `/dashboard/admin/complaints?tab=pending` trên phone/tablet.
  - Cần cap: sidebar admin vẫn rộng/fixed, content còn rất hẹp, title/card/filter/pagination wrap cực đoan hoặc nằm ngoài vùng nhìn thấy.
  - Ưu tiên cap: `D3-CP-05`, sau đó `D3-CP-04`. Đây là defect cross-platform quan trọng nhất của D3 trên mobile/tablet.
  - Tên ảnh gợi ý: `F-D3-003_mobile-sidebar-overflow.png`

## Candidate usability notes từ session notes

Các điểm dưới đây không phải defect chính trong Task 1B, nhưng có thể ghi thành finding Task 3 nếu tái hiện rõ và ảnh thể hiện được khác biệt trên platform:

- [ ] `D1` - Focus/caret trong field form không rõ ngay sau khi click.
  - Nguồn: `UT-P04-002`.
  - Nên cap nếu trên browser/device cụ thể người dùng khó biết input đã focus.

- [ ] `D2/D3` - `Rows per page` xuất hiện nhưng số dòng mỗi trang bị cố định.
  - Nguồn: `UT-P03-001`.
  - Nên cap nếu control hiển thị như thao tác được nhưng không đổi được số dòng.

- [ ] `D2/D3` - Giao diện màu sắc user/admin chưa đồng nhất.
  - Nguồn: `UT-P05-003`.
  - Cần cap đối chiếu: sidebar user màu sáng, sidebar admin màu tối; dùng khi muốn ghi finding về visual consistency hơn là layout.

- [ ] `D3` - Admin navigation dễ lẫn với luồng user.
  - Nguồn: `UT-P02-001`, `UT-P04-001`, `UT-P05-001`.
  - Cần cap: admin account vẫn thấy mục mang tính user như `User Dashboard`, `Yêu cầu hỗ trợ` hoặc `My support requests`.

- [ ] `D3` - Label/trạng thái `Pending`/`Resolved` chưa đủ giống tab/filter.
  - Nguồn: `UT-P02-002`, `UT-P03-003`, `UT-P05-002`.
  - Cần cap: card/tab status dễ bị hiểu là thống kê tổng quan hoặc không nhận ra có thể click để chuyển trạng thái.

- [ ] `D3` - Bố cục bảng/filter admin khó quét.
  - Nguồn: `UT-P03-002`.
  - Cần cap: cột `REQUEST` quá rộng hoặc date range/filter không được gom hàng hợp lý, làm giảm khả năng đọc/lọc request.
