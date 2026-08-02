# Templates for AI-First Playwright MCP + BrowserStack Workflow

Các template này dùng kèm `submission/ai_first_playwright_browserstack_strategy.md`.

## 1. Screen Selection Template

```markdown
| Screen ID | Scenario | Screen name | Role | URL/Navigation path | Widgets/states covered | Evidence folder |
| --- | --- | --- | --- | --- | --- | --- |
| D1 | D | Create support request | User | Support -> Create request | Category, content, image attachment, submit, validation | submission/screenshots/D1/ |
| D2 | D | My Requests list/detail | User | Support -> My Requests -> detail | Request status, detail content, official response | submission/screenshots/D2/ |
| D3 | D | Support Requests list/detail | Admin | Admin -> Support Requests -> detail | Pending/Resolved tabs, search, image lightbox, internal note, official response | submission/screenshots/D3/ |
```

## 2. Playwright MCP Prompt Templates

### 2.1. Login and screen discovery

```text
Use Playwright MCP to open EMS at https://promoter-starboard-prude.ngrok-free.dev/.
Login as <role> using the account I provide.
Navigate to <screen name/path>.
Return:
1. current URL,
2. page title/heading,
3. visible primary actions,
4. visible form fields/tables/statuses,
5. screenshot path if captured.
Do not report a bug yet.
```

### 2.2. Checklist execution

```text
Use the shared checklist in submission/group/gui_usability_checklist_final.md.
Evaluate only screen <SCREEN_ID>: <SCREEN_NAME>.
For each checklist item, mark Pass, Fail, N/A, or Needs review.
Use only observable UI evidence from Playwright MCP snapshots/screenshots.
For every Fail, include:
- exact observed UI problem,
- checklist ID,
- likely user impact,
- screenshot path needed,
- suggested severity 1-4.
Return a Markdown table ready to paste into my execution report.
```

### 2.3. Finding cleanup

```text
Convert these raw observations into HW03 finding entries.
Use IDs starting from F-<next number>.
Each entry must include: screen, type Bug/Usability, steps or heuristic, expected, actual, severity 0-4, suggested fix, screenshot ref, and form timestamp placeholder.
Do not add findings without evidence.
```

### 2.4. Human review prompt

```text
Review this AI-generated checklist execution as a skeptical QA reviewer.
Flag any row that is vague, unsupported by screenshot/snapshot evidence, duplicated, not testable, or not relevant to the selected EMS screen.
Suggest the minimum corrections needed before submission.
```

## 3. Checklist Execution Table

```markdown
| Screen | Checklist ID | Result | Evidence | Notes | Screenshot ref | Finding ID |
| --- | --- | --- | --- | --- | --- | --- |
| D2 My Requests detail | IA-04-06 | Fail | Mobile BrowserStack screenshot shows official response below fold | Response status is not visible near the request summary on phone | submission/screenshots/checklist-failures/F-001.png | F-001 |
```

Allowed `Result` values: `Pass`, `Fail`, `N/A`, `Needs review`.

## 4. Finding Log Template

```markdown
| ID | Scenario/Screen | Type | Description | Steps/Heuristic | Severity | Suggested fix | Screenshot ref | Form-submission timestamp |
| --- | --- | --- | --- | --- | ---: | --- | --- | --- |
| F-001 | D2 My Requests detail | Usability | Support request status is hard to notice on phone. | IA-04-06: status should be visible by text and badge. | 3 | Move the status badge near the request summary and preserve it on mobile. | submission/screenshots/checklist-failures/F-001.png | 2026-..-.. ..:.. |
```

## 5. User Testing Protocol Template

```markdown
# User Testing Protocol - Scenario <A/B/C/D>

## Goal
<One realistic goal-based task. Do not list clicks.>

## Participant Criteria
- 5 real participants outside the class.
- Contact masked in report.
- Consent recorded before session.

## Metrics
| Metric | How to record |
| --- | --- |
| Task success | Completed / Partial / Failed |
| Time on task | Start when participant begins, stop when goal completed or abandoned |
| Errors | Count incorrect actions, failed submissions, wrong navigation |
| Hesitations | Count pauses/questions showing uncertainty |
| SUS or UEQ-S | Collect immediately after task |

## Moderator Script
1. I am testing the EMS interface, not you.
2. Please think aloud while working.
3. I will not guide clicks unless you are completely blocked.
4. You may stop at any time.

## Probe Questions
| Question | Purpose |
| --- | --- |
| Which part was most confusing? | Clarity |
| Where did you expect the next action to be? | Navigation/signifiers |
| Did any message help you recover from an error? | Feedback/recovery |
| Would you trust the result shown by the system? Why? | Confidence/trust |
```

## 6. Participant and Metrics Tables

```markdown
| Participant | Profile | Contact masked | Session date/time | Consent | Notes |
| --- | --- | --- | --- | --- | --- |
| P01 | Student/event participant | Zalo 09****1234 | 2026-..-.. ..:.. | Yes | Completed without hints |
```

```markdown
| Participant | Success | Time on task | Errors | Hesitations | SUS/UEQ-S score | Key friction |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| P01 | Completed | 03:42 | 1 | 2 | 72.5 | Could not identify the support request response quickly |
```

## 7. Cross-Platform Matrix Template

Use one matrix per screen.

```markdown
| Cell | Screen | OS | Browser | Device class | Device/profile | Result | Screenshot ref | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CP-01 | D2 My Requests detail | Windows 11 | Chrome | Desktop | 1920x1080 | Pass | submission/cross-platform/screenshots/D2_CP-01_windows_chrome_desktop.png | No layout issue |
| CP-02 | D2 My Requests detail | Windows 11 | Edge | Desktop | 1920x1080 | Pass | submission/cross-platform/screenshots/D2_CP-02_windows_edge_desktop.png | No layout issue |
| CP-03 | D2 My Requests detail | macOS | Safari | Desktop | macOS desktop | Pass | submission/cross-platform/screenshots/D2_CP-03_macos_safari_desktop.png | No layout issue |
| CP-04 | D2 My Requests detail | Android | Chrome | Phone | Pixel device | Fail | submission/cross-platform/screenshots/D2_CP-04_android_chrome_phone.png | Official response panel overlaps sticky footer |
| CP-05 | D2 My Requests detail | Android | Firefox | Phone | Android phone | Pass | submission/cross-platform/screenshots/D2_CP-05_android_firefox_phone.png | No layout issue |
| CP-06 | D2 My Requests detail | iOS | Safari | Phone | iPhone device | Pass | submission/cross-platform/screenshots/D2_CP-06_ios_safari_phone.png | No layout issue |
| CP-07 | D2 My Requests detail | iPadOS/Android | Opera/Samsung Internet | Tablet | Tablet device | Pass | submission/cross-platform/screenshots/D2_CP-07_tablet_opera_or_samsung.png | No layout issue |
```

Coverage check:

```markdown
| Dimension | Required | Covered? | Evidence |
| --- | --- | --- | --- |
| OS | 3 | Windows, macOS, Android/iOS | CP-01, CP-03, CP-04 |
| Browsers | 5 | Chrome, Edge, Safari, Firefox, Opera/Samsung Internet | CP-01..CP-07 |
| Device classes | 3 | Desktop, phone, tablet | CP-01, CP-04, CP-07 |
```

## 8. BrowserStack Prompt Templates

### 8.1. BrowserStack MCP session

```text
Use BrowserStack MCP to launch EMS URL https://promoter-starboard-prude.ngrok-free.dev/ on <OS>, <browser>, <device>.
Navigate to <screen path>.
Confirm the page is loaded and the EMS URL is visible.
Capture a screenshot for HW03 evidence.
The screenshot must preserve BrowserStack device/browser identity and my overlay email <MSSV@....edu.vn>.
Return the session details, screenshot path/link, and any visible layout issue.
```

### 8.2. Automate smoke run

```text
Generate a minimal Playwright smoke flow for EMS screen <SCREEN_ID>.
The script should:
1. open the EMS URL,
2. login if needed,
3. navigate to the target screen,
4. assert the main heading or primary action is visible,
5. capture a screenshot,
6. mark BrowserStack session passed/failed.
Keep credentials in environment variables.
```

## 9. Screenshot Naming

```text
submission/screenshots/checklist-failures/<finding-id>_<screen-id>_<short-problem>.png
submission/screenshots/usability-findings/<finding-id>_<participant-or-theme>.png
submission/cross-platform/screenshots/<screen-id>_<cell-id>_<os>_<browser>_<device>.png
```

Examples:

```text
submission/screenshots/checklist-failures/F-001_D2_status-below-fold.png
submission/screenshots/usability-findings/F-006_P03_response-hesitation.png
submission/cross-platform/screenshots/D2_CP-04_android_chrome_pixel-8.png
```

## 10. AI Audit Entry Template

For a normal AI session:

```bash
rtk python3 .agents/skills/ai-audit-entry/scripts/append_ai_audit_entry.py \
  --purpose "Hỗ trợ chạy Playwright MCP và BrowserStack cho HW03" \
  --prompt "<copy exact prompt>" \
  --output "Tạo bảng execution/matrix/finding draft; sinh viên đã kiểm tra lại bằng screenshot và raw notes." \
  --tool-model "Codex / GPT-5"
```

For one continuous generated artifact:

```bash
rtk python3 .agents/skills/ai-audit-entry/scripts/append_ai_audit_entry.py \
  --purpose "Tạo tài liệu hướng dẫn AI-first cho HW03" \
  --prompt "<copy exact prompt>" \
  --output-file submission/ai_first_playwright_browserstack_strategy.md \
  --tool-model "Codex / GPT-5"
```

## 11. Final Pre-Submission Checklist

```markdown
| Item | Done? | Notes |
| --- | --- | --- |
| Scenario and >= 3 screens selected |  |  |
| Shared checklist has >40 items and sources |  |  |
| Checklist executed on every selected screen |  |  |
| Failed checklist items have screenshots |  |  |
| User testing has 5 real participants and raw notes |  |  |
| SUS or UEQ-S calculated |  |  |
| Cross-platform matrix covers 3 OS, 5 browsers, 3 device classes per screen |  |  |
| Every cross-platform screenshot has URL, device/browser identity, and email overlay |  |  |
| Every finding submitted to Google Form |  |  |
| Aggregated log matches Google Form count |  |  |
| AI Audit Report includes this workflow |  |  |
| AI Critique is 200-300 words |  |  |
| Git commit log exported |  |  |
```
