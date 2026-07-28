---
name: ai-audit-entry
description: Ghi thêm entry AI audit có đánh số cho bài HW03 môn Kiểm thử phần mềm. Dùng trước khi kết thúc các phiên làm việc có AI hỗ trợ trong repo này, đặc biệt khi Codex tạo báo cáo, template, skill, kế hoạch hoặc tóm tắt cần khai báo trong `submission/ai-audit/ai_audit_report.md`.
---

# AI Audit Entry

## Quy trình

1. Hỏi sinh viên có muốn thêm audit entry hay không nếu phiên làm việc có hỗ trợ đáng kể từ AI.
2. Chạy script với prompt gốc đầy đủ, không rút gọn:

```bash
python .agents/skills/ai-audit-entry/scripts/append_ai_audit_entry.py --purpose "Mục đích ngắn" --prompt "Prompt gốc đầy đủ của user" --output "Tóm tắt output theo artifact liên quan" --tool-model "Codex / GPT-5"
```

3. Trong phần chi tiết, `Prompt + công cụ` phải xuống dòng rõ ràng theo format:
   - `Thời gian`
   - `Công cụ`
   - `Mục đích`
   - `Prompt đầy đủ`
4. `Kết quả AI` phải tóm tắt theo từng entry và nêu artifact liên quan, không chỉ ghi mô tả chung chung.
5. Giữ `Đánh giá`, `Lý do` và `Sinh viên chỉnh sửa` là các trường sinh viên tự điền.
6. Không đưa hidden reasoning hoặc log lệnh dài vào audit.
7. Không tạo giả phần review của sinh viên; sinh viên phải tự hoàn thành các trường thủ công.

## Cấu trúc báo cáo

Đường dẫn báo cáo là `submission/ai-audit/ai_audit_report.md`.

Báo cáo phải giữ các section:

- `## 1. Thông tin nhóm`
- `## 2. Bảng audit`
- `### 2.1. Tóm tắt audit`
- `### 2.2. Chi tiết audit`
- `## 3. Tổng kết độ chính xác AI`
- `## 4. Kết luận`
- `## 5. Disclosure`
