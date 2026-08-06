---
name: task1b-execution
description: Use when executing a GUI usability checklist on target screens (Task 1B) using MCP Playwright and Chrome DevTools based on credentials from test_environment_access.md.
---

# Task 1B - Checklist Execution & Bug Logging

## Overview

Use this skill to execute a GUI usability checklist against target application screens (such as Scenario D: D1, D2, D3). It first ensures environment access parameters are documented and confirmed by the user, then performs live interactive browser testing via Playwright MCP & Chrome DevTools MCP.

---

## CRITICAL EXECUTION RULES (MANDATORY)

1. **Pre-Execution Account & URL Prompt:**
   - **BEFORE launching browser execution, AI MUST verify if valid environment credentials exist.**
   - If `test_environment_access.md` does not exist or contains default placeholders (`[Điền URL]`, `[User Email]`, `[Password]`), AI **MUST IMMEDIATELY PROMPT THE USER** to provide/fill:
     - SUT Web URL
     - User Account Email & Password (for user screens like D1, D2)
     - Admin Account Email & Password (for admin screens like D3)
   - Do NOT attempt browser login with empty or placeholder credentials.

2. **Mandatory Live Browser Execution:**
   - AI **MUST NOT** rely solely on cached text, past test logs, or static summary artifacts.
   - AI **MUST ACTIVELY CALL** MCP Playwright tools (`browser_navigate`, `browser_fill_form`, `browser_click`, `browser_take_screenshot`) or Browser Agent to open the live web app, log in, navigate screens, inspect live DOM/console/network errors, and capture fresh screenshot evidence.

---

## Workflow

### Step 1 - Environment Access Verification & Template Creation

If `test_environment_access.md` is missing, create it using this structure and ask the user to confirm/fill the details:

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

### Step 2 - Live Playwright & DevTools Browser Execution

1. Read `test_environment_access.md` and confirm SUT URL, role credentials, and safety rules.
2. **Launch Playwright MCP / Browser Tools:**
   - `browser_navigate` -> Open login page URL.
   - `browser_fill_form` / `browser_click` -> Fill user/admin credentials and log in.
   - Verify landing page URL and session state.
3. Open target screen (e.g., `D1` Create Request, `D2` My Requests, `D3` Admin Support Requests).
4. For each item in the checklist:
   - Evaluate live DOM elements, interactive states, validation triggers, network responses, and console errors.
   - Assign status: `Passed`, `Failed`, or `N/A`.
   - For `Failed` items, record: Observed behavior, Expected behavior, Heuristic reference, User impact, Severity rating (0-4), and Suggested fix.
   - Capture live screenshot evidence into `screenshots/<Screen>/` or `findings/defect-screenshots/`.

### Step 3 - Produce Execution Report (`task1b_<Screen>.md`)

Generate a structured Markdown execution report containing:
- Test summary metadata (Student, Screen, Scope, Date, Environment URL).
- Live environment status & login verification screenshot links.
- Complete checklist execution table with Pass/Fail status based on live inspection.
- Summary of defect findings with relative links to live screenshot evidence.
