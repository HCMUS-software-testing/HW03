#!/usr/bin/env python3
"""Append các entry AI Audit HW03 EMS bằng tiếng Việt."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


DEFAULT_REPORT = Path("submission/ai_audit_report.md")
REQUIRED_NO_AI_DECLARATION = "I do not use any AI help in this exercise."
REQUIRED_AI_DECLARATION = "I use AI tools for the following tasks."


@dataclass
class AuditEntry:
    tool: str = "Codex"
    model: str = "GPT-5"
    prompt: str = ""
    output: str = ""
    output_summary: str = ""
    timestamp: str = ""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Append entry AI Audit cho HW03 EMS bằng tiếng Việt."
    )
    parser.add_argument("--report", default=str(DEFAULT_REPORT), help="Đường dẫn file AI Audit Report.")
    parser.add_argument("--no-ai", action="store_true", help="Ghi khai báo bắt buộc khi không dùng AI.")
    parser.add_argument("--session-json", help="File JSON chứa danh sách entry audit.")
    parser.add_argument("--timezone", default="Asia/Ho_Chi_Minh", help="Timezone IANA dùng cho timestamp.")
    parser.add_argument("--timestamp", help="Ghi đè timestamp cho các entry tạo từ CLI.")

    parser.add_argument("--tool", default="Codex", help="Tên công cụ AI.")
    parser.add_argument("--model", default="GPT-5", help="Tên model AI.")
    parser.add_argument("--prompt", action="append", help="Nội dung prompt của sinh viên. Lặp lại để ghi nhiều prompt.")
    parser.add_argument("--prompt-file", action="append", help="File chứa prompt của sinh viên.")
    parser.add_argument("--output", action="append", help="Nội dung output của AI. Lặp lại để ghi nhiều prompt.")
    parser.add_argument("--output-file", action="append", help="File chứa output của AI.")
    parser.add_argument("--output-summary", action="append", help="Tóm tắt output của AI. Lặp lại để ghi nhiều prompt.")
    parser.add_argument("--output-summary-file", action="append", help="File chứa tóm tắt output của AI.")
    return parser.parse_args()


def read_text_file(path: str | None) -> str:
    if not path:
        return ""
    return Path(path).read_text(encoding="utf-8").strip()


def pick(values: list[str] | None, index: int, default: str = "") -> str:
    if not values:
        return default
    if index < len(values):
        return values[index]
    return values[-1]


def combine_text_and_file(
    text_values: list[str] | None,
    file_values: list[str] | None,
    index: int,
) -> str:
    text = pick(text_values, index)
    file_path = pick(file_values, index)
    file_text = read_text_file(file_path)
    return file_text or text


def timestamp_now(timezone: str) -> str:
    try:
        zone = ZoneInfo(timezone)
    except Exception as exc:  # pragma: no cover - defensive CLI message
        raise SystemExit(f"Timezone không hợp lệ: {timezone}") from exc
    return datetime.now(zone).strftime("%Y-%m-%d %H:%M %z")


def entries_from_session_json(path: str, fallback_timestamp: str) -> list[AuditEntry]:
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        raise SystemExit("--session-json phải là một mảng JSON.")

    entries: list[AuditEntry] = []
    for index, item in enumerate(raw, start=1):
        if not isinstance(item, dict):
            raise SystemExit(f"Entry JSON thứ {index} phải là object.")
        entry = AuditEntry(
            tool=str(item.get("tool", "Codex")),
            model=str(item.get("model", "GPT-5")),
            prompt=str(item.get("prompt", "")).strip(),
            output=str(item.get("output", "")).strip(),
            output_summary=str(item.get("output_summary", "")).strip(),
            timestamp=str(item.get("timestamp", fallback_timestamp)),
        )
        entries.append(entry)
    return entries


def entries_from_cli(args: argparse.Namespace, fallback_timestamp: str) -> list[AuditEntry]:
    prompt_count = max(len(args.prompt or []), len(args.prompt_file or []))
    output_count = max(len(args.output or []), len(args.output_file or []))
    summary_count = max(len(args.output_summary or []), len(args.output_summary_file or []))
    entry_count = max(
        1,
        prompt_count,
        output_count,
        summary_count,
    )

    entries: list[AuditEntry] = []
    for index in range(entry_count):
        entries.append(
            AuditEntry(
                tool=args.tool,
                model=args.model,
                prompt=combine_text_and_file(args.prompt, args.prompt_file, index).strip(),
                output=combine_text_and_file(args.output, args.output_file, index).strip(),
                output_summary=combine_text_and_file(args.output_summary, args.output_summary_file, index).strip(),
                timestamp=args.timestamp or fallback_timestamp,
            )
        )
    return entries


def ensure_report_header(report_path: Path) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    if not report_path.exists():
        report_path.write_text(
            "# AI Audit Report — HW03 GUI & Usability Testing on EMS\n\n"
            "## 1. Khai báo sử dụng AI\n\n"
            f"`{REQUIRED_AI_DECLARATION}`\n\n"
            "## 2. Nhật ký tương tác AI\n",
            encoding="utf-8",
        )


def next_entry_number(existing_text: str) -> int:
    numbers = [int(match) for match in re.findall(r"^#{2,3} Entry (\d+)\b", existing_text, flags=re.MULTILINE)]
    return max(numbers, default=0) + 1


def fenced_text(text: str) -> str:
    if not text.strip():
        return "_Chưa có dữ liệu trong transcript hiện tại._"
    fence = "```"
    if fence in text:
        fence = "````"
    return f"{fence}text\n{text.strip()}\n{fence}"


def output_block(entry: AuditEntry) -> str:
    if entry.output.strip():
        return fenced_text(entry.output)
    if entry.output_summary.strip():
        return f"Tóm tắt: {entry.output_summary.strip()}"
    return "_Chưa có output trong transcript hiện tại._"


def format_entry(entry_number: int, entry: AuditEntry) -> str:
    return (
        f"\n\n### Entry {entry_number}\n\n"
        f"- **Ngày giờ:** {entry.timestamp}\n"
        f"- **Công cụ AI / model:** {entry.tool} / {entry.model}\n"
        "- **Prompt:**\n\n"
        f"{fenced_text(entry.prompt)}\n\n"
        "- **Output AI:**\n\n"
        f"{output_block(entry)}\n"
    )


def append_no_ai_declaration(report_path: Path) -> None:
    existing = report_path.read_text(encoding="utf-8")
    if REQUIRED_NO_AI_DECLARATION in existing:
        print("Khai báo không dùng AI đã tồn tại trong report.")
        return
    with report_path.open("a", encoding="utf-8") as handle:
        handle.write(
            "\n\n## Khai báo không dùng AI\n\n"
            f"{REQUIRED_NO_AI_DECLARATION}\n"
        )
    print(f"Đã ghi khai báo không dùng AI vào {report_path}.")


def validate_entry(entry: AuditEntry, index: int) -> None:
    if not entry.prompt:
        print(
            f"Cảnh báo: Entry đầu vào thứ {index} chưa có prompt. "
            "Chỉ dùng khi transcript thật sự thiếu và cần người dùng bổ sung.",
            file=sys.stderr,
        )
    if not entry.output and not entry.output_summary:
        print(
            f"Cảnh báo: Entry đầu vào thứ {index} chưa có output hoặc output summary.",
            file=sys.stderr,
        )


def append_entries(report_path: Path, entries: list[AuditEntry]) -> None:
    existing = report_path.read_text(encoding="utf-8")
    entry_number = next_entry_number(existing)
    with report_path.open("a", encoding="utf-8") as handle:
        for offset, entry in enumerate(entries):
            validate_entry(entry, offset + 1)
            handle.write(format_entry(entry_number + offset, entry))
    print(f"Đã append {len(entries)} entry vào {report_path}.")


def main() -> int:
    args = parse_args()
    report_path = Path(args.report)
    ensure_report_header(report_path)

    if args.no_ai:
        append_no_ai_declaration(report_path)
        return 0

    fallback_timestamp = args.timestamp or timestamp_now(args.timezone)
    if args.session_json:
        entries = entries_from_session_json(args.session_json, fallback_timestamp)
    else:
        entries = entries_from_cli(args, fallback_timestamp)

    append_entries(report_path, entries)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
