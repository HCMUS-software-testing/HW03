---
name: ems-usability-report-writer
description: Tạo hoặc review báo cáo usability HW03 EMS từ ghi chú user testing thật, điểm SUS, quan sát, quote và severity. Dùng khi Codex được yêu cầu tổng hợp 5 phiên người tham gia, tính SUS, xếp hạng usability findings hoặc soạn đề xuất cải thiện cho Scenario A/B/C/D.
---

# EMS Usability Report Writer

## Đầu vào

Cần có bằng chứng thật:

- Bảng 5 người tham gia chính thức.
- Ghi chú pilot.
- Quan sát từng phiên.
- Điểm SUS raw.
- Ảnh chụp hoặc recording nếu có.

Nếu thiếu bằng chứng, giữ kết quả là `Chờ điền`; không tạo giả hành vi người tham gia.

## Quy trình

1. Xác nhận có 5 người tham gia chính thức ngoài lớp.
2. Tính SUS:
   - Câu lẻ: `score - 1`.
   - Câu chẵn: `5 - score`.
   - Điểm cuối: cộng các điểm đóng góp và nhân `2.5`.
3. Tóm tắt task success, thời gian, lỗi, do dự và quote.
4. Chuyển các điểm ma sát lặp lại thành findings.
5. Xếp hạng findings theo severity 0-4:
   - 0: không phải vấn đề.
   - 1: lỗi thẩm mỹ hoặc khó chịu nhẹ.
   - 2: vấn đề nhỏ, có workaround.
   - 3: gây chậm, nhầm lẫn hoặc lỗi đáng kể.
   - 4: chặn nhiệm vụ hoặc có rủi ro mất dữ liệu/bảo mật.
6. Viết recommendation cụ thể gắn với bằng chứng quan sát được.
7. Đưa mọi finding vào log tổng hợp và quy trình tracking Google Form.

## Định dạng đầu ra

```markdown
## Usability findings

| ID | Minh chứng | Severity | Recommendation |
| --- | --- | ---: | --- |
| C-U001 | P02 và P04 do dự trước khi xác nhận reset mật khẩu. | 3 | Hiển thị rõ hậu quả thao tác và tên người dùng mục tiêu trong nội dung dialog. |
```

## Prompt Scenario C

Dùng nhiệm vụ dạng mục tiêu:

```text
Bạn là admin của EMS. Hãy tìm một người dùng mục tiêu, kiểm tra trạng thái tài khoản, thay đổi vai trò nếu cần, chặn/bỏ chặn người dùng hoặc đặt lại mật khẩu, rồi xác nhận xem hệ thống đã hoàn tất thao tác hay chưa.
```
