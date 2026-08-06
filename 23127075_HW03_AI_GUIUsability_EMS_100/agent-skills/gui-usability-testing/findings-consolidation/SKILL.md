---
name: findings-consolidation
description: Use when consolidating website defect and usability findings from checklist execution, user testing, cross-platform testing, or external submissions into a unified findings directory.
---

# Findings Consolidation Subskill

## Overview

Use this subskill to aggregate, deduplicate, and finalize bug and usability findings from any website testing workflow into a standardized `findings` directory, for example `findings/bug_usability_findings_log.md` and `findings/defect-screenshots/`.

## Inputs

- Source reports from checklist execution, moderated user testing, cross-platform testing, manual QA, issue trackers, or external submission forms.
- Screenshot/evidence directories.
- Optional external tracker IDs, submitter names, or submission timestamps supplied by the user.
- Target URL and target scope when available.

---

## Workflow

### Step 1 - Deduplicate Defect Screenshots (`defect-screenshots/`)

1. Scan all defects identified across source reports, for example checklist findings (`CHK-*`), user testing findings (`UT-*`), cross-platform findings (`CP-*`), or imported issue IDs.
2. Identify overlapping or duplicate symptoms observed across multiple environments, roles, screens, or test methods.
3. Move/copy exactly **1 representative screenshot** for each unique defect into `findings/defect-screenshots/`.
   - Example naming: `CHK-001_validation-not-inline.png`
4. Update defect references in all source reports so they point directly to `findings/defect-screenshots/<Filename>`.

### Step 2 - Build Aggregated Findings Log (`bug_usability_findings_log.md`)

Create/update `findings/bug_usability_findings_log.md` with the unified table format:

| ID | Website/Screen/Flow | Type | Description | Reproduction Steps / Heuristic | Severity | Suggested Fix | Representative Screenshot | Observed In | External Reference / Timestamp |
| --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- |

Column Rules:
- `ID`: Standardized prefix such as `CHK-xxx` for checklist findings, `UT-xxx` for user testing findings, and `CP-xxx` for cross-platform findings. Preserve external issue IDs when needed.
- `Type`: `Bug`, `Usability`, `Compatibility`, or another user-supplied category.
- `Severity`: Integer rating from `1` (cosmetic) to `4` (catastrophe), unless the user's project uses another scale.
- `Representative Screenshot`: Relative path to `defect-screenshots/<filename>`.
- `Observed In`: List all screens, roles, environments, and test methods where observed.
- `External Reference / Timestamp`: Optional tracker link, form timestamp, or submission metadata. Leave blank if not supplied.

### Step 3 - Final Audit & Checklist Verification

1. Verify that number of findings in the log matches the selected source set after deduplication.
2. Ensure every finding links to valid relative image paths without broken links.
3. Preserve source traceability for every merged or deduplicated finding.
4. Mark completion checklist in `bug_usability_findings_log.md`.
