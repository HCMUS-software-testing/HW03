---
name: task1b-execution
description: Use when executing a GUI usability checklist on target website screens with required target URL, optional role credentials, and live MCP Playwright browser testing.
---

# Checklist Execution & Bug Logging

## Overview

Use this skill to execute a GUI usability checklist against target website screens, routes, or user journeys. It first confirms the website URL, target scope, account requirements, credentials, and safety rules, then performs live interactive browser testing via MCP Playwright.

---

## Critical Execution Rules

1. **Pre-Execution Account & URL Prompt:**
   - Before launching browser execution, verify that `target_url` and `target_scope` are known.
   - If the website requires login, ask the user for each required account type / role, username or email, password or authentication method, and data safety rules.
   - Do not attempt browser login with empty credentials, placeholder credentials, guessed accounts, or credentials from an unrelated project.

2. **Mandatory Live Browser Execution:**
   - Do not rely solely on cached text, past test logs, static screenshots, or summary artifacts.
   - Actually call MCP Playwright tools such as `browser_navigate`, `browser_snapshot`, `browser_fill_form`, `browser_click`, and `browser_take_screenshot` to open the live web app, log in when required, navigate screens, inspect live behavior, and capture fresh screenshot evidence.
   - If MCP Playwright tools are unavailable, stop and help the user install or enable the MCP Playwright server before continuing. Do not mark checklist items as executed without live MCP Playwright evidence.

---

## Workflow

### Step 1 - Environment Access Verification

If an access note file is helpful, create `test_environment_access.md` using this generic structure and ask the user to confirm or fill missing details:

```markdown
# Test Environment Access

## Web URL
| Field | Value |
| --- | --- |
| Target URL | `https://[your-target-url]` |
| Environment Notes | `[production / staging / local / ngrok / other]` |

## Accounts
### Account 1
| Field | Value |
| --- | --- |
| Account Type / Role | `[e.g. customer, editor, admin]` |
| Email / Username | `[provided by user]` |
| Password / Auth Method | `[provided by user]` |
| Screens / Flows Covered | `[routes or features]` |

### Account 2
| Field | Value |
| --- | --- |
| Account Type / Role | `[optional additional role]` |
| Email / Username | `[provided by user]` |
| Password / Auth Method | `[provided by user]` |
| Screens / Flows Covered | `[routes or features]` |

## Testing Rules
1. Only mutate data the user explicitly permits.
2. Do not edit, disable, delete, or expose other users' data.
3. Capture screenshot evidence for every defect or usability issue.
```

### Step 2 - Live MCP Playwright Browser Execution

1. Confirm `target_url`, target screens/routes, role credentials when needed, and safety rules.
2. Launch MCP Playwright browser tools:
   - `browser_navigate` -> Open the target URL or login page.
   - `browser_snapshot` -> Inspect accessible page structure before interacting.
   - `browser_fill_form` / `browser_click` -> Fill credentials and log in when required.
   - Verify landing page URL and session state.
3. Open each target screen, route, or user journey supplied by the user.
4. For each item in the checklist:
   - Evaluate live DOM elements, interactive states, validation triggers, network responses, and console errors.
   - Assign status: `Passed`, `Failed`, or `N/A`.
   - For `Failed` items, record observed behavior, expected behavior, heuristic reference, user impact, severity rating (0-4), and suggested fix.
   - Capture live screenshot evidence into `screenshots/<screen-or-flow>/` or `findings/defect-screenshots/`.

### Step 3 - Produce Execution Report

Generate a structured Markdown execution report containing:
- Test summary metadata: website, target URL, screen/flow, scope, date, browser/viewport, and account type if used.
- Live environment status and login verification screenshot links.
- Complete checklist execution table with Pass/Fail status based on live inspection.
- Summary of defect findings with relative links to live screenshot evidence.
