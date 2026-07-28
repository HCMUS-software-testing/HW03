#!/usr/bin/env python3
"""Build a blank HW03 EMS Task 1B checklist execution table."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


DEFAULT_CHECKLIST = Path("submission/group/gui_usability_checklist_final.md")
DEFAULT_SCREENS = [
    "A1 Events list",
    "A2 Add/Edit Event",
    "A3 Registration & Roles",
]


@dataclass(frozen=True)
class ChecklistItem:
    item_id: str
    aspect: str
    text: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sinh bảng Markdown Task 1B từ checklist GUI usability nhóm."
    )
    parser.add_argument(
        "--checklist",
        default=str(DEFAULT_CHECKLIST),
        help="Đường dẫn checklist nhóm Markdown.",
    )
    parser.add_argument(
        "--output",
        help="File đích. Nếu bỏ trống, bảng được in ra stdout.",
    )
    return parser.parse_args()


def split_markdown_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def parse_checklist(path: Path) -> list[ChecklistItem]:
    if not path.exists():
        raise SystemExit(f"Không tìm thấy checklist: {path}")

    items: list[ChecklistItem] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not re.match(r"^\|\s*IA-\d{2}-\d{2}\s*\|", line):
            continue
        cells = split_markdown_row(line)
        if len(cells) < 3:
            continue
        item_id = cells[0]
        aspect = cells[1].split()[0]
        text = cells[2]
        items.append(ChecklistItem(item_id=item_id, aspect=aspect, text=text))

    if not items:
        raise SystemExit(f"Không parse được checklist item nào từ: {path}")
    return items


def escape_table_cell(value: str) -> str:
    return value.replace("|", r"\|").replace("\n", " ").strip()


def build_table(items: list[ChecklistItem], screens: list[str]) -> str:
    headers = [
        "Checklist ID",
        "Interface Aspect",
        "Nội dung kiểm tra",
        *screens,
        "Notes cho Failed",
        "Screenshot ref",
    ]
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]

    for item in items:
        row = [
            item.item_id,
            item.aspect,
            escape_table_cell(item.text),
            *("[Passed/Failed/N/A]" for _ in screens),
            "[Chỉ ghi khi Failed]",
            "[screenshots/...]",
        ]
        lines.append("| " + " | ".join(row) + " |")

    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    checklist_path = Path(args.checklist)
    items = parse_checklist(checklist_path)
    table = build_table(items, DEFAULT_SCREENS)

    if args.output:
        Path(args.output).write_text(table, encoding="utf-8")
    else:
        print(table, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
