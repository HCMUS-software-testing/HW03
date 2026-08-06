---
name: gui-usability-testing
description: Use when designing, executing, or managing reusable GUI usability testing artifacts for any website or web application.
---

# GUI Usability Testing Suite

## Overview

The `gui-usability-testing` skill suite provides an end-to-end workflow for GUI usability, user testing, cross-platform evaluation, and findings consolidation for any website. It is portable and must not assume a specific assignment, domain, application name, account, or route.

## Required Context

Before using any subskill, obtain or infer:
- `target_url`: the website or web app URL under test. If missing, ask the user for it before browser execution or website-specific checklist generation.
- `target_scope`: screens, routes, user journeys, or features to evaluate.
- `artifact_location`: where reports, checklists, screenshots, and findings should be saved.
- `auth_required`: whether the target website requires login.
- `account_type` and credentials for each required role if login is needed, for example `customer`, `editor`, `admin`, `student`, or any domain-specific role supplied by the user.

If login is required and account data is missing, ask the user for:
- Account type / role name.
- Username or email.
- Password or authentication method.
- Any safety rules for data mutation.

Do not invent credentials, reuse credentials from another project, or attempt login with placeholders.

## Browser Automation Requirement

When a workflow says to execute live browser testing with MCP Playwright:
- Actually call MCP Playwright tools such as `browser_navigate`, `browser_snapshot`, `browser_click`, `browser_fill_form`, and `browser_take_screenshot`.
- Do not claim live execution from static files, previous reports, cached screenshots, or memory.
- If MCP Playwright tools are not available, help the user install or enable the MCP Playwright server before continuing. Do not silently substitute manual reasoning unless the user explicitly approves a non-MCP fallback.

## Subskills

| Subskill Name | Path | Key Output / Purpose |
| --- | --- | --- |
| **`step1-checklist`** | `step1-checklist/SKILL.md` | Generates website UI inventory and a reusable heuristic checklist based on Nielsen, Norman, Shneiderman, and widget-specific criteria. |
| **`task1b-execution`** | `task1b-execution/SKILL.md` | Executes a checklist against target website screens using live MCP Playwright browser testing and produces execution reports. |
| **`task2-user-testing`** | `task2-user-testing/SKILL.md` | Prepares moderated user testing templates and synthesizes participant notes, SUS scores, and usability reports. |
| **`task3-cross-platform`** | `task3-cross-platform/SKILL.md` | Builds cross-browser/device matrices, defines screenshot evidence protocol, and outputs compatibility reports. |
| **`findings-consolidation`** | `findings-consolidation/SKILL.md` | Consolidates defects and usability findings into a portable findings directory with deduplicated screenshots. |

---

## Subskill Details

### 1. `step1-checklist`
- Extracts UI inventory from specs, screenshots, live pages, or user-provided scope.
- Maps heuristics to `IA-01` General UI, `IA-02` Forms, `IA-03` Navigation, and `IA-04` Feedback.

### 2. `task1b-execution`
- Confirms `target_url`, target screens, role/account requirements, credentials, and safety rules.
- Uses MCP Playwright to navigate, log in when needed, inspect live DOM and interaction behavior, capture screenshot evidence, and produce per-screen reports.

### 3. `task2-user-testing`
- Generates interview protocol, participant table, session notes template, SUS sheet, and usability report template.
- Processes raw participant notes, calculates SUS scores, ranks severity, and populates a usability report.

### 4. `task3-cross-platform`
- Takes user inputs for OS, browsers, device classes, viewport sizes, and target flows.
- Builds a pairwise reduction matrix when full Cartesian testing is too costly, defines screenshot evidence rules, and outputs a compatibility report.

### 5. `findings-consolidation`
- Aggregates findings from checklist execution, user testing, cross-platform testing, bug reports, or manual notes.
- Deduplicates images into `findings/defect-screenshots/` with one representative image per unique finding.
- Preserves optional external tracker IDs or submission timestamps only when supplied by the user.

---

## Invocation Guidance

- To execute a specific task, navigate to or invoke the corresponding subskill:
  - Checklist generation: `gui-usability-testing/step1-checklist`
  - Checklist execution: `gui-usability-testing/task1b-execution`
  - User testing: `gui-usability-testing/task2-user-testing`
  - Cross-platform testing: `gui-usability-testing/task3-cross-platform`
  - Findings Consolidation: `gui-usability-testing/findings-consolidation`
