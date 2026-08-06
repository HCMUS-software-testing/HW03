---
name: findings-consolidation
description: Use when consolidating defect and usability findings from Task 1B, Task 2, and Task 3 into a unified findings directory with deduplicated screenshots and Google Form submission timestamps.
---

# Findings Consolidation Subskill

## Overview

Use this subskill to aggregate, deduplicate, and finalize all bug and usability findings across Task 1B, Task 2, and Task 3 into a standardized `findings` directory (matching `findings/bug_usability_findings_log.md` and `findings/defect-screenshots/`).

## Reference AI Audit Prompts

Derived from AI Audit Entries 18, 19, and 20:
- Consolidates duplicated defect screenshots into one single folder with 1 representative screenshot per defect.
- Maps Google Form submission timestamps to each finding row.
- Verifies relative links and removes temporary `template` suffixes once populated.

---

## Workflow

### Step 1 - Deduplicate Defect Screenshots (`defect-screenshots/`)

1. Scan all defects identified across Task 1B (e.g. `F-D1-*`, `F-D2-*`, `F-D3-*`), Task 2 (`UT-D-*`), and Task 3 (`CP-*`).
2. Identify overlapping or duplicate symptoms observed across multiple environments/tasks.
3. Move/copy exactly **1 representative screenshot** for each unique defect into `findings/defect-screenshots/`.
   - Example naming: `F-D1-001_validation-not-inline.png`
4. Update defect references in all task reports so they point directly to `findings/defect-screenshots/<Filename>`.

### Step 2 - Build Aggregated Findings Log (`bug_usability_findings_log.md`)

Create/update `findings/bug_usability_findings_log.md` with the unified table format:

| ID | Scenario/Màn hình | Loại | Mô tả | Bước thực hiện/Heuristic | Mức độ nghiêm trọng | Đề xuất sửa | Tham chiếu screenshot đại diện | Xuất hiện trong | Thời điểm submit form |
| --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- |

Column Rules:
- `ID`: Standardized prefix (`F-D1-xxx`, `F-D2-xxx`, `F-D3-xxx` for functional/checklist defects; `UT-D-xxx` for user testing findings).
- `Loại`: `Bug` or `Usability`.
- `Mức độ nghiêm trọng`: Integer rating from `1` (cosmetic) to `4` (catastrophe).
- `Tham chiếu screenshot đại diện`: Relative path to `defect-screenshots/<filename>`.
- `Xuất hiện trong`: List all tasks & cross-platform cells where observed (e.g., `Task 1B D1; Task 3 D1-CP-01, D1-CP-02`).
- `Thời điểm submit form`: Exact timestamp of Google Form submission (e.g. `06/08/2026 13:24`).

### Step 3 - Final Audit & Checklist Verification

1. Verify that number of findings in log matches total Google Form submissions.
2. Ensure every finding links to valid relative image paths without broken links.
3. Remove `template` suffixes from file names once content is finalized.
4. Mark completion checklist in `bug_usability_findings_log.md`.
