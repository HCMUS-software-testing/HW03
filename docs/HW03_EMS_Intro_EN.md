# HW03 - GUI & Usability Testing on the Event Management System (EMS)

**Course:** Software Testing - AI-First Edition (2026)  
**Subtitle:** Design a shared GUI checklist, test your scenario, evaluate usability, and go cross-platform.  
**SUT:** <https://prod-dev.ems-fitus.cloud/dashboard>

## At a Glance

What you will deliver: four graded tasks, one shared team checklist, everything logged the AI-first way.

| # | Deliverable | Description | Points |
| --- | --- | --- | ---: |
| 1 | GUI Checklist | A team checklist (>40 items) applied to your 3+ screens. | 30 |
| 2 | Usability Report | Heuristic evaluation of the functions you own. | 25 |
| 3 | Cross-Platform | 3 OS x 5 browsers x 3 device types on your 3 screens. | 25 |
| 4 | Findings + Skills | Submit bugs to the form; build reusable Agent Skills. | 20 |

## The System Under Test

**EMS - Event Management System** is a live web app of the Faculty of IT for creating events, registering, check-in, support, and analytics.

**URL:** <https://prod-dev.ems-fitus.cloud/dashboard>

| Area | Details |
| --- | --- |
| What it does | Admin side: events, users, categories, check-in, support, settings, analytics. |
| What it does | User side: browse and register for events, get a QR ticket, rate events, ask for support. |
| What it does | UI-rich: forms, drag-drop reorder, uploads, rich-text, toasts, status colours, EN/VI. |
| Web (SUT) | `prod-dev.ems-fitus.cloud/dashboard` |
| Admin | `admin@gmail.com` / `Admin@123` |
| User side | Register your own student/guest account. |
| Support group | <https://zalo.me/g/rupogxlykt3yxd3snodl> |

## How the Work Is Split

You share the checklist; you own a scenario end-to-end.

| Scope | Responsibilities |
| --- | --- |
| Group - shared | Design one GUI checklist (>40 items). Cover all four interface aspects IA-01...IA-04. Submit checklist + reference sources + AI prompts. |
| Individual - your core | Pick one scenario: A, B, C or D. List >= 3 screens of that function group. Run the checklist, usability, and cross-platform testing on them. |

> **No duplication:** Inside a group, no two members may own the same scenario and the same set of screens.

## Choose One

Each scenario maps to a function group of EMS. Everyone in the team should try to cover all four.

| Scenario | Name | Focus |
| --- | --- | --- |
| A | Admin creates & manages events | Event lifecycle: create, validate, configure, publish, approve, check-in. |
| B | User registers for an event | Public discovery & registration: browse, event detail, sign-up, QR ticket. |
| C | Admin manages users | User administration: roles, block/unblock, reset password, export. |
| D | User asks Support, Admin resolves | Support-request lifecycle across the user and the admin sides. |

## Scope

Choose at least three screens from your scenario's function group.

| A - Events | B - Register | C - Users | D - Support |
| --- | --- | --- | --- |
| Events list + status filters | Home + featured carousel | Users list + filters | User: create request (+image) |
| Add/Edit Event (upload, rich-text, date validation) | Event detail page | Assign role / edit user | User: my requests + response |
| Registration & Roles config | Registration form (roles, waitlist) | Block / Unblock + Reset password | Admin: requests list (Pending/Resolved) |
| Participants approval | My Registrations + QR ticket | Export to Excel | Admin: request detail + reply |
| Check-in tab | Post-event star review | | |

## Task 1 - GUI Checklist (30 pts)

Ground it in Nielsen / Norman / Shneiderman, then execute it on your screens.

| Part | Scope | Requirements |
| --- | --- | --- |
| Part A - Shared (group) | Checklist design | > 40 items across IA-01...IA-04. AI drafts it; you review and add missed items. For each added item, say why AI missed it. Submit checklist + sources + AI prompts. |
| Part B - Execution (individual) | Checklist execution | Run the checklist on each of your >= 3 screens. Mark every item Passed / Failed per screen. Notes column: reason for each Fail. Screenshots for Failed items; log every bug. |

## Task 2 - User Testing -> Usability Report (25 pts)

Design a scenario, run it with five real users, then analyse the results.

| Protocol | What to collect |
| --- | --- |
| Design: a goal-based task scenario on your screens. | Task success rate. |
| Recruit 5 real users outside the class (contacts masked). | Time on task. |
| Run sessions: moderated, think-aloud, observe neutrally. | Errors / hesitations. |
| Collect: success, time, errors + SUS / UEQ-S + probes. | SUS or UEQ-S score. |
| Analyse: rank by severity -> prioritised recommendations. | Open-ended probes. |

## Task 3 - Cross-Browser / Cross-Platform (25 pts)

Build a compatibility matrix for each of your three screens.

| Dimension | Requirement | Examples |
| --- | --- | --- |
| Operating systems | 3 | Windows, macOS, Android / iOS |
| Browsers | 5 | Chrome, Firefox, Safari, Edge, Opera |
| Device classes | 3 | Desktop, tablet, phone |

**Coverage:** Not all 45 combinations are required, but you must hit every OS, every browser, and every device class at least once per screen.

**Tools:** BrowserStack / LambdaTest trial. Overlay `MSSV@....edu.vn` on every screenshot beside the EMS URL.

## Report Everything Twice

Every defect and suggestion goes to the form and into one aggregated log.

| Channel | Requirement |
| --- | --- |
| Google Form | Submit each finding at <https://forms.gle/CJQFQCAXcsDbXDMM9>. Use your student-ID email `MSSV@....edu.vn`. |
| Aggregated Log | One file consolidating all findings. Columns: ID, Screen, Type, Severity, Fix, Screenshot, Timestamp. It must match your form submissions. |

## How to Work

Use AI as a disciplined assistant, and prove it.

- Guide, don't dump: drive the AI step-by-step through the technique, not one generic prompt.
- Human review: you own the correctness; never submit raw AI output.
- AI Audit Report: log every AI interaction: tool, time, prompt, output (mandatory appendix).
- AI Critique: 200-300 words on where the AI was wrong, biased, or incomplete.
- Anti-cheat: real EMS screenshots, real cross-platform captures, real participants.
- Git log: one commit per step: design, execution, bug logging, evaluation.

## Grading

100 points across five graded components.

| # | Component | Scope | Points |
| --- | --- | --- | ---: |
| 1a | Shared checklist (>40 items) + sources + AI prompts | Group | 15 |
| 1b | Checklist execution on >= 3 screens + bug reports | Individual | 15 |
| 2 | Usability Report (heuristics + severity + fixes) | Individual | 25 |
| 3 | Cross-browser / platform matrix | Individual | 25 |
| 4 | Findings submission (form) + aggregated log | Individual | 10 |
| 5 | Agent Skills + demo videos | Individual | 10 |
| | **Total** | | **100** |

## Submission

Individual ZIP + shared group artefacts on Moodle.

| Your ZIP contains | Remember |
| --- | --- |
| Main report (Markdown + PDF). | Filename: `<MSSV>_HW03_AI_GUIUsability_EMS_<grade>.zip` |
| Bug & Usability Findings Log. | No late submission. |
| Cross-platform screenshots (with your email). | Missing a required doc -> 0. |
| AI Audit Report + AI Critique. | Shared prompts between students -> 0. |
| Git commit log + Agent Skills + README. | Oral defence: random 30%. |

## Get Started

Your first five moves:

1. Form your team and pick who takes A, B, C, D.
2. Open the SUT and register your own user account.
3. Together, draft the >40-item checklist (AI + review).
4. List your >= 3 screens and run the checklist.
5. Evaluate usability, go cross-platform, log every finding.

**Questions:** lqvu@fit.hcmus.edu.vn and the TA team (see the brief).
