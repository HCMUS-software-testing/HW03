---
name: gui-usability-testing
description: Use when designing, executing, or managing GUI usability testing artifacts (Task 1A, Task 1B, Task 2, Task 3, and Findings Consolidation) for an application like EMS.
---

# GUI Usability Testing Suite

## Overview

The `gui-usability-testing` skill suite provides an end-to-end testing workflow for GUI Usability & Cross-Platform Evaluation. It is organized into 5 dedicated subskills located in subdirectories:

| Subskill Name | Path | Homework Task | Key Output / Purpose |
| --- | --- | --- | --- |
| **`step1-checklist`** | `step1-checklist/SKILL.md` | Task 1A | Generates project UI inventory & >40-item checklist based on Nielsen, Norman, and Shneiderman principles. |
| **`task1b-execution`** | `task1b-execution/SKILL.md` | Task 1B | Generates `test_environment_access.md` template for Playwright MCP login, then executes checklist testing per screen. |
| **`task2-user-testing`** | `task2-user-testing/SKILL.md` | Task 2 | Prepares interview templates (protocol, SUS sheet, notes, participant table) & synthesizes post-interview data into `usability_report.md`. |
| **`task3-cross-platform`** | `task3-cross-platform/SKILL.md` | Task 3 | Takes OS/Browser/Device lists, builds pairwise test matrix, defines email overlay screenshot protocol, and outputs compatibility report. |
| **`findings-consolidation`** | `findings-consolidation/SKILL.md` | Findings | Consolidates all defects into `findings/`, deduplicates screenshots into `defect-screenshots/`, and maps Google Form timestamps. |

---

## Subskill Details & AI Audit Traceability

### 1. `step1-checklist` (Task 1A)
- **Derived from AI Audit Entries 3 & 5.**
- Extracts UI inventory (screens, roles, flows, widgets, dynamic states).
- Maps heuristics to IA-01 (General UI), IA-02 (Forms), IA-03 (Navigation), IA-04 (Feedback).

### 2. `task1b-execution` (Task 1B)
- **Derived from AI Audit Entries 8, 9, 11, and 12.**
- Step 1: Prepares `test_environment_access.md` for URL, credentials, and safety rules.
- Step 2: Uses Playwright MCP & Chrome DevTools MCP to navigate, inspect DOM/console/network, capture screenshot evidence, and produce `task1b_<Screen>.md`.

### 3. `task2-user-testing` (Task 2)
- **Derived from AI Audit Entries 13 & 20.**
- Step 1 (Prep): Generates interview protocol, participant table, session notes template, SUS sheet, and usability report template.
- Step 2 (Synthesis): Processes raw participant notes (P01-P05), calculates SUS scores, ranks severity (0-4), and populates `usability_report.md`.

### 4. `task3-cross-platform` (Task 3)
- **Derived from AI Audit Entries 14, 15, and 16.**
- Takes user inputs for OS, Browsers, and Devices.
- Builds optimal pairwise reduction matrix (e.g. 5 cells for 3 OS x 5 Browsers x 3 Devices), defines screenshot overlay rules (`MSSV@...`), and outputs compatibility report.

### 5. `findings-consolidation` (Findings Directory)
- **Derived from AI Audit Entries 18, 19, and 20.**
- Aggregates all defects into `findings/bug_usability_findings_log.md`.
- Deduplicates images into `findings/defect-screenshots/` (1 representative image per defect).
- Fills exact Google Form submission timestamps.

---

## Invocation Guidance

- To execute a specific task, navigate to or invoke the corresponding subskill:
  - Task 1A Checklist: `gui-usability-testing/step1-checklist`
  - Task 1B Execution: `gui-usability-testing/task1b-execution`
  - Task 2 User Testing: `gui-usability-testing/task2-user-testing`
  - Task 3 Cross-Platform: `gui-usability-testing/task3-cross-platform`
  - Findings Consolidation: `gui-usability-testing/findings-consolidation`
