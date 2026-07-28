#!/usr/bin/env python3
"""Kiểm tra nhanh scaffold bài nộp HW03 và local skills."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = [
    "ems-gui-checklist-runner",
    "ems-usability-report-writer",
    "ems-compatibility-matrix-builder",
    "ai-audit-entry",
]
REQUIRED_FILES = [
    "submission/main_report.md",
    "submission/checklist_execution_scenario_c.md",
    "submission/bug_usability_findings_log.md",
    "submission/ai-audit/ai_audit_report.md",
    "submission/ai_critique.md",
    "submission/user-testing/protocol.md",
    "submission/user-testing/participant_table.md",
    "submission/user-testing/pilot_notes.md",
    "submission/user-testing/raw_scores/sus_scores.md",
    "submission/cross-platform/matrix.md",
    "submission/agent-skills/skill_inventory.md",
    "submission/demo-videos.md",
    "submission/git_commit_log.txt",
    "submission/group/references.md",
    "submission/group/ai_prompts.md",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validate_required_files() -> None:
    for relative in REQUIRED_FILES:
        path = ROOT / relative
        require(path.exists(), f"Thiếu file bắt buộc: {relative}")
        require(path.stat().st_size > 0, f"File bắt buộc đang rỗng: {relative}")


def validate_checklist() -> None:
    checklist = (ROOT / "submission/group/gui_usability_checklist_final.md").read_text(encoding="utf-8")
    ids = re.findall(r"\| (IA-\d\d-\d\d) \|", checklist)
    require(len(ids) > 40, f"Checklist phải có >40 mục, hiện có {len(ids)}")
    aspects = {item[:5] for item in ids}
    require(aspects == {"IA-01", "IA-02", "IA-03", "IA-04"}, f"Bao phủ IA không đúng: {sorted(aspects)}")

    execution = (ROOT / "submission/checklist_execution_scenario_c.md").read_text(encoding="utf-8")
    for item in ids:
        require(item in execution, f"Bảng thực thi checklist thiếu {item}")


def validate_cross_platform_matrix() -> None:
    matrix = (ROOT / "submission/cross-platform/matrix.md").read_text(encoding="utf-8")
    for screen in ["C1", "C2", "C3"]:
        refs = matrix.count(f"screenshots/{screen}_")
        require(refs >= 6, f"{screen} cần ít nhất 6 đường dẫn ảnh, hiện có {refs}")
    for browser in ["Chrome", "Firefox", "Safari", "Edge", "Opera"]:
        require(browser in matrix, f"Ma trận thiếu trình duyệt: {browser}")
    for device_class in ["Desktop", "Tablet", "Phone"]:
        require(device_class.lower() in matrix.lower(), f"Ma trận thiếu lớp thiết bị: {device_class}")


def validate_skills() -> None:
    for skill in SKILLS:
        skill_file = ROOT / ".agents/skills" / skill / "SKILL.md"
        require(skill_file.exists(), f"Thiếu file skill: {skill}")
        text = skill_file.read_text(encoding="utf-8")
        require(text.startswith("---\n"), f"Skill {skill} thiếu YAML frontmatter")
        frontmatter = text.split("---", 2)[1]
        require(re.search(rf"^name: {re.escape(skill)}$", frontmatter, re.MULTILINE), f"Skill {skill} thiếu name")
        require(re.search(r"^description: .+", frontmatter, re.MULTILINE), f"Skill {skill} thiếu description")
        openai_yaml = ROOT / ".agents/skills" / skill / "agents/openai.yaml"
        require(openai_yaml.exists(), f"Skill {skill} thiếu agents/openai.yaml")


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    validate_required_files()
    validate_checklist()
    validate_cross_platform_matrix()
    validate_skills()
    print("Kiểm tra artifact HW03 đã đạt")


if __name__ == "__main__":
    main()
