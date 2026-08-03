# Task 2 - Test Accounts Template

File này dùng để chuẩn bị account/session cho pilot và 5 participant. Không ghi password thật vào file nộp cuối nếu password còn dùng được.

## 1. Nguyên tắc cấp account

- Với D1/D2, ưu tiên dùng user test account riêng hoặc session user đã đăng nhập sẵn.
- Với D3, không đưa admin password cho participant. Người kiểm thử đăng nhập admin trước, giám sát thao tác, rồi đăng xuất sau phiên.
- Nếu cần để participant tự đăng nhập, chỉ dùng credential tạm và đổi/xóa password sau khi test.
- Không để participant thao tác dữ liệu của người khác ngoài phạm vi quan sát/tìm kiếm.
- Ghi alias account trong báo cáo, ví dụ `User test account P01`, thay vì ghi password thật.

## 2. Account/session assignment

| Session | Participant | Role needed | Account/session alias | Credential handling | Data created/used | Cleanup needed | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pilot | `[Điền]` | User / Admin observer | `[Điền]` | `[Logged-in session / temporary credential / researcher-controlled admin]` | `[Điền]` | `[Điền]` |  |
| P01 | `[Điền]` | User / Admin observer | `[Điền]` | `[Logged-in session / temporary credential / researcher-controlled admin]` | `[Điền]` | `[Điền]` |  |
| P02 | `[Điền]` | User / Admin observer | `[Điền]` | `[Logged-in session / temporary credential / researcher-controlled admin]` | `[Điền]` | `[Điền]` |  |
| P03 | `[Điền]` | User / Admin observer | `[Điền]` | `[Logged-in session / temporary credential / researcher-controlled admin]` | `[Điền]` | `[Điền]` |  |
| P04 | `[Điền]` | User / Admin observer | `[Điền]` | `[Logged-in session / temporary credential / researcher-controlled admin]` | `[Điền]` | `[Điền]` |  |
| P05 | `[Điền]` | User / Admin observer | `[Điền]` | `[Logged-in session / temporary credential / researcher-controlled admin]` | `[Điền]` | `[Điền]` |  |

## 3. Session setup checklist

- [ ] Browser đang ở đúng SUT.
- [ ] User session truy cập được D1/D2.
- [ ] Admin session truy cập được D3 nếu phiên có phần admin observer.
- [ ] Không còn dữ liệu nhạy cảm hoặc tab ngoài phạm vi trước khi participant bắt đầu.
- [ ] Recording/screenshot tool sẵn sàng nếu participant consent.
- [ ] Sau phiên đã đăng xuất hoặc đóng session.
