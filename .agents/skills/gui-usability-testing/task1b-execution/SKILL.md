---
name: task1b-execution
description: Use when executing a GUI usability checklist on target screens (Task 1B) using MCP Playwright and Chrome DevTools based on credentials from test_environment_access.md.
---

# Task 1B - Checklist Execution & Bug Logging

## Overview

Use this skill to execute a GUI usability checklist against target application screens (such as Scenario D: D1, D2, D3). It first ensures environment access parameters are documented, then performs automated/interactive browser testing via Playwright MCP & Chrome DevTools MCP.

## Reference AI Audit Prompts

This skill is derived from AI Audit Entries 9, 11, and 12:
- **Pattern:** Read project docs & `submission/test_environment_access.md` -> Load `gui_usability_checklist_final.md` -> Use Playwright MCP & Chrome DevTools MCP -> Execute per-screen checklist -> Capture screenshots -> Generate `task1b_<Screen>.md`.

## Workflow

### Step 1 - Generate Environment Access Template (`test_environment_access.md`)

If `test_environment_access.md` does not exist or needs initialization, create it using this structure:

```markdown
# Test Environment Access

## Web URL
| Field | Value |
| --- | --- |
| EMS URL | `https://[your-target-url]` |
| Ghi chú | `[Environment details, ngrok / staging link]` |

## Accounts
### User Account (for D1, D2)
| Field | Value |
| --- | --- |
| Email / Username | `[User Email]` |
| Password | `[User Password]` |
| Role | `User` |

### Admin Account (for D3)
| Field | Value |
| --- | --- |
| Email / Username | `[Admin Email]` |
| Password | `[Admin Password]` |
| Role | `Admin` |

## Testing Rules
1. Khi test trang admin, nếu có thao tác CRUD tài khoản user, chỉ được thao tác trên tài khoản user được cấp.
2. Không sửa, khóa, xóa hoặc thay đổi dữ liệu của người dùng khác.
3. Chụp bằng chứng hình ảnh cho mọi phát hiện lỗi (defect/usability issue).
```

### Step 2 - Playwright & DevTools Execution

1. Read `test_environment_access.md` to retrieve SUT URL, role credentials, and safety rules.
2. Launch Playwright MCP / Chrome DevTools MCP:
   - Navigate to login page, fill credentials, submit form, verify session landing page.
3. Open target screen (e.g., `D1` Create Request, `D2` My Requests, `D3` Admin Support Requests).
4. For each item in `gui_usability_checklist_final.md`:
   - Evaluate live DOM elements, interactive states, validation triggers, network responses, and console errors.
   - Assign status: `Passed`, `Failed`, or `N/A`.
   - For `Failed` items, record: Observed behavior, Expected behavior, Heuristic reference, User impact, Severity rating (0-4), and Suggested fix.
   - Capture screenshot evidence into `screenshots/<Screen>/` or `findings/defect-screenshots/`.

### Step 3 - Produce Execution Report (`task1b_<Screen>.md`)

Generate a structured Markdown execution report containing:
- Test summary metadata (Student, Screen, Scope, Date, Environment).
- Environment status & login verification.
- Complete checklist execution table with Pass/Fail status.
- Summary of defect findings with relative links to screenshot evidence.
