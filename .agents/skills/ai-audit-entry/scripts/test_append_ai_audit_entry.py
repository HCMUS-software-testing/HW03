#!/usr/bin/env python3
"""Regression tests cho append_ai_audit_entry.py."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


SCRIPT = Path(__file__).with_name("append_ai_audit_entry.py")


def run_script(tmp_path: Path, prompt: str = "Tạo template HW03") -> Path:
    audit_file = tmp_path / "submission" / "ai-audit" / "ai_audit_report.md"
    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--audit-file",
            str(audit_file),
            "--purpose",
            "ghi nhận entry test",
            "--prompt",
            prompt,
            "--output",
            "Đã tạo template báo cáo.",
            "--tool-model",
            "Codex / GPT-5",
        ],
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    return audit_file


def test_creates_report_with_required_sections() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        audit_file = run_script(Path(temp_dir))
        text = audit_file.read_text(encoding="utf-8")
        assert "## 1. Thông tin nhóm" in text
        assert "## 2. Bảng audit" in text
        assert "### 2.1. Tóm tắt audit" in text
        assert "### 2.2. Chi tiết audit" in text
        assert "## 3. Tổng kết độ chính xác AI" in text
        assert "## 4. Kết luận" in text
        assert "## 5. Disclosure" in text
        assert "| STT | Prompt + công cụ | Đánh giá |" in text
        assert "| 1 |" in text
        assert "### 2.2.1 Entry 1" in text
        assert "**Thời gian:**" in text
        assert "**Công cụ:**" in text
        assert "**Mục đích:**" in text
        assert "**Prompt đầy đủ:**" in text
        assert "```text\nTạo template HW03\n```" in text


def test_appends_entries_sequentially() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        audit_file = run_script(temp_path, "prompt thứ nhất")
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--audit-file",
                str(audit_file),
                "--purpose",
                "ghi nhận entry thứ hai",
                "--prompt",
                "prompt thứ hai",
                "--output",
                "Đã tạo template thứ hai.",
            ],
            text=True,
            capture_output=True,
            check=False,
        )
        assert result.returncode == 0, result.stderr
        text = audit_file.read_text(encoding="utf-8")
        assert "| 1 |" in text
        assert "| 2 |" in text
        assert "### 2.2.1 Entry 1" in text
        assert "### 2.2.2 Entry 2" in text


def test_escapes_table_cells() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        audit_file = run_script(Path(temp_dir), "A | B\nC")
        text = audit_file.read_text(encoding="utf-8")
        assert "A \\| B C" in text
        assert "```text\nA | B\nC\n```" in text


if __name__ == "__main__":
    test_creates_report_with_required_sections()
    test_appends_entries_sequentially()
    test_escapes_table_cells()
