#!/usr/bin/env python3
"""Thêm một entry AI audit có đánh số cho HW03."""

from __future__ import annotations

import argparse
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


DEFAULT_AUDIT_FILE = Path("submission/ai-audit/ai_audit_report.md")
MANUAL = "[Sinh viên tự đánh giá]"
SUMMARY_LIMIT = 180


def table_cell(value: str) -> str:
    return (
        value.strip()
        .replace("\\", "\\\\")
        .replace("|", "\\|")
        .replace("\r\n", "\n")
        .replace("\r", "\n")
        .replace("\n", "<br>")
    )


def summarize(value: str, limit: int = SUMMARY_LIMIT) -> str:
    normalized = re.sub(r"\s+", " ", value.strip())
    if len(normalized) <= limit:
        return normalized
    return normalized[: limit - 3].rstrip() + "..."


def prompt_tool_detail(timestamp: str, tool_model: str, purpose: str, prompt: str) -> str:
    return (
        f"**Thời gian:** `{timestamp}`\n\n"
        f"**Công cụ:** `{tool_model}`\n\n"
        f"**Mục đích:** {purpose.strip()}\n\n"
        f"**Prompt đầy đủ:**\n\n"
        f"```text\n{prompt.strip()}\n```"
    )


def initial_report() -> str:
    return """# Báo cáo AI Audit

## 1. Thông tin nhóm

- Họ tên: `Lâm Hữu Khánh`
- MSSV: `23127205`
- Kịch bản: `C - Admin quản lý người dùng`

## 2. Bảng audit

### 2.1. Tóm tắt audit

| STT | Prompt + công cụ | Đánh giá |
| --- | --- | --- |

### 2.2. Chi tiết audit

## 3. Tổng kết độ chính xác AI

- `[Sinh viên tự đánh giá]`

## 4. Kết luận

`[Sinh viên tự đánh giá]`

## 5. Disclosure

`[Sinh viên tự đánh giá]`
"""


def next_index(text: str) -> int:
    numbers = [int(match) for match in re.findall(r"^### 2\.2\.(\d+) Entry \d+", text, re.MULTILINE)]
    return max(numbers, default=0) + 1


def ensure_report(path: Path) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        return path.read_text(encoding="utf-8")
    return initial_report()


def append_entry(path: Path, purpose: str, prompt: str, output: str, tool_model: str) -> None:
    text = ensure_report(path)
    index = next_index(text)
    timestamp = datetime.now(ZoneInfo("Asia/Ho_Chi_Minh")).strftime("%Y-%m-%d %H:%M %Z")
    prompt_tool_summary = (
        f"Thời gian: `{timestamp}`; Công cụ: `{tool_model}`; "
        f"Mục đích: {summarize(purpose)}; Prompt: {summarize(prompt)}"
    )
    prompt_tool = prompt_tool_detail(timestamp, tool_model, purpose, prompt)

    summary_row = f"| {index} | {table_cell(prompt_tool_summary)} | {MANUAL} |"
    detail = f"""### 2.2.{index} Entry {index}

**Prompt + công cụ:**

{prompt_tool}

**Kết quả AI:** {output.strip()}

**Đánh giá:** {MANUAL}

**Lý do:** {MANUAL}

**Sinh viên chỉnh sửa:** {MANUAL}
"""

    text = insert_before(text, "\n### 2.2. Chi tiết audit", summary_row + "\n")
    text = insert_before(text, "\n## 3. Tổng kết độ chính xác AI", "\n" + detail)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def insert_before(text: str, marker: str, addition: str) -> str:
    position = text.find(marker)
    if position == -1:
        return text.rstrip() + "\n" + addition
    return text[:position].rstrip() + "\n" + addition + text[position:]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audit-file", type=Path, default=DEFAULT_AUDIT_FILE)
    parser.add_argument("--purpose", required=True)
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--tool-model", default="Codex / GPT-5")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    append_entry(args.audit_file, args.purpose, args.prompt, args.output, args.tool_model)


if __name__ == "__main__":
    main()
