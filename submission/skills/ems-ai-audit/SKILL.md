---
name: ems-ai-audit
description: Use when ghi AI Audit Report cho HW03 EMS, ghi lại prompt chat trong session, tổng hợp output AI, hoặc khai báo không dùng AI theo yêu cầu bài GUI & Usability Testing.
---

# EMS AI Audit

## Mục tiêu

Ghi lại quá trình dùng AI cho HW03 EMS thành `submission/ai_audit_report.md` bằng tiếng Việt. Mỗi prompt quan trọng trong session phải thành một entry có đủ thông tin bắt buộc tại Mục 10 của đề bài: công cụ/model, ngày giờ, prompt và output AI.

## Quy tắc bắt buộc

- Chỉ ghi những prompt/output thật sự nhìn thấy trong session hiện tại hoặc transcript người dùng cung cấp.
- Nếu thiếu lịch sử chat, hãy hỏi người dùng paste phần transcript còn thiếu. Không tự đoán prompt, output, thời điểm, hoặc kết quả.
- Không tạo giả bằng chứng EMS: screenshot, participant data, BrowserStack/LambdaTest result, Google Form timestamp, bug count, hoặc trạng thái live EMS.
- Không để raw AI output chưa review thành kết luận cuối.
- Nếu dùng AI, đặt câu khai báo `I use AI tools for the following tasks.` ở đầu báo cáo.
- Prompt tạo checklist nhóm Task 1A phải được ghi trong audit theo Mục 10 của đề.
- Nếu người dùng nói không dùng AI, ghi đúng câu bắt buộc: `I do not use any AI help in this exercise.`
- Toàn bộ nội dung do skill sinh ra dùng tiếng Việt, trừ câu tiếng Anh bắt buộc của đề.

## Workflow

1. Xác định report đích, mặc định là `submission/ai_audit_report.md`.
2. Rà lại session hiện tại và gom các prompt người dùng đã dùng cho HW03 EMS.
3. Với từng prompt, xác định:
   - Tác vụ của prompt.
   - Công cụ AI/model đã dùng.
   - Output AI: ghi nguyên văn nếu ngắn; nếu dài, ghi tóm tắt trung thực bằng tiếng Việt.
4. Nếu có đủ dữ liệu, dùng script `scripts/add_ai_audit_entry.py` để append entry. Nếu thiếu dữ liệu, hỏi người dùng trước.
5. Sau khi ghi, đọc lại phần mới append để kiểm tra entry đủ trường và không chứa dữ liệu bịa.

## Script hỗ trợ

Chạy từ root repo:

```bash
python3 submission/skills/ems-ai-audit/scripts/add_ai_audit_entry.py \
  --tool "Codex" \
  --model "GPT-5" \
  --prompt-file /tmp/prompt.txt \
  --output-summary-file /tmp/output_summary.md
```

Ghi nhiều prompt trong một session bằng cách dùng `--session-json`:

```bash
python3 submission/skills/ems-ai-audit/scripts/add_ai_audit_entry.py \
  --session-json /tmp/ai_audit_session.json
```

File JSON là một mảng object. Bốn trường cốt lõi là `tool`/`model`, `timestamp`, `prompt` và `output` hoặc `output_summary`.

Khai báo không dùng AI:

```bash
python3 submission/skills/ems-ai-audit/scripts/add_ai_audit_entry.py --no-ai
```

## Mẫu entry

````markdown
### Entry 1

- **Ngày giờ:** 2026-07-28 14:30 +07
- **Công cụ AI / model:** Codex / GPT-5
- **Prompt:**

```text
Tạo checklist GUI usability cho EMS...
```

- **Output AI:**

Tóm tắt: AI tạo bảng checklist theo IA-01 đến IA-04.

````

## Lỗi thường gặp

| Lỗi | Cách xử lý |
| --- | --- |
| Chỉ ghi prompt, không ghi output | Thêm output nguyên văn hoặc tóm tắt trung thực. |
| Ghi dữ liệu không có trong transcript | Dừng lại và hỏi người dùng cung cấp transcript. |
| Tự tạo bằng chứng EMS | Loại bỏ ngay; chỉ sinh viên được ghi bằng chứng thật đã thu thập. |
| Dùng tiếng Anh cho toàn bộ report | Chuyển sang tiếng Việt, chỉ giữ câu declaration bắt buộc. |
