---
name: gui-usability-testing
description: Use when designing GUI usability testing artifacts for a project, especially homework or QA work that needs project-specific checklists grounded in UI heuristics and screen/widget specs.
---

# GUI Usability Testing

## Overview

Use this skill to turn project specs into GUI usability testing artifacts. The first supported step is creating a reusable checklist that is specific to the project screens, flows, roles, and widgets.

This skill is based on the HW03 group artifacts in `submission/group`, where the final checklist was improved by reviewing AI output against EMS-specific UI details.

## Step 1 - Create Checklist

### Inputs

Ask for or read these project specs before generating the checklist:

- Project overview and user roles.
- Feature pools, scenarios, and target screens.
- Interface aspects or quality dimensions required by the assignment.
- UI widget inventory from specs, screenshots, wireframes, or existing pages.
- Any required output columns, minimum item count, language, and reference-source rules.

If specs are incomplete, make conservative assumptions and list them before the checklist. Do not invent screens, roles, or widgets that are not implied by the specs.

### Source Principles

Every checklist item must map to at least one recognized source:

- Nielsen's 10 usability heuristics, especially visibility of system status, match with the real world, user control and freedom, consistency and standards, error prevention, recognition rather than recall, flexibility and efficiency, aesthetic and minimalist design, error recovery, and help/documentation.
- Norman's 6 principles as used by the course materials, such as visibility/discoverability, feedback, affordances, signifiers, mapping, constraints, consistency, and conceptual model.
- Shneiderman's 8 golden rules, especially consistency, universal usability, informative feedback, closure, error prevention, easy reversal, internal locus of control, and reduced short-term memory load.
- Per-widget checklist expectations from the project specs and course checklist topics.

Use exact principle names in the `Reference` column. Do not cite vague labels such as `Human-centered design` unless the provided spec explicitly uses that as a checklist reference.

### Build The UI Inventory First

Before writing checklist rows, extract a compact inventory:

| Category | What to extract |
| --- | --- |
| Screens | Page names, dialogs, panels, and mobile views. |
| Roles | User groups that see different UI or permissions. |
| Flows | Multi-step tasks, confirmations, recovery paths, and completion states. |
| Widgets | Forms, inputs, date/time pickers, uploads, rich-text editors, buttons, icon buttons, menus, sidebars, breadcrumbs, tabs, search, filters, tables, cards, pagination, carousels, badges, toasts, banners, loading indicators, empty states, confirmation dialogs, modals, image preview/lightbox, QR/barcode, ratings, export/download controls, language switchers. |
| Dynamic states | Loading, disabled, success, failure, empty, stale data, permission denied, expired session, destructive action, and validation error states. |

Use this inventory to decide which per-widget checklist groups are needed. For example, if the specs mention image upload and rich-text editing, include explicit upload and rich-text items instead of generic form-only items.

### Checklist Structure

Default output is a Markdown table:

| ID | Interface Aspect | Checklist Item | Reference | Rationale | Priority | Review Notes |
| --- | --- | --- | --- | --- | --- | --- |

Use stable IDs by aspect:

- `IA-01-xx`: General UI standards.
- `IA-02-xx`: Forms and data entry.
- `IA-03-xx`: Navigation and information architecture.
- `IA-04-xx`: Feedback, status, and recovery.
- Add project-specific aspect IDs only if the assignment requires them.

For HW03-style checklist design, produce more than 40 items and cover all four aspects. Balance the checklist across aspects; avoid putting most rows into only one category.

### Generation Rules

1. Start from the UI inventory, not from the principles list.
2. For each screen or widget family, write observable checks that a tester can mark `Passed` or `Failed`.
3. Make each item concrete enough to execute on a screen, for example "date picker prevents end date before start date" instead of "date validation is good".
4. Include project vocabulary and roles from the specs, such as `Event`, `Registration`, `Admin`, `Participant`, or `Support Request`.
5. Add at least one item for each critical widget family found in the specs.
6. Add state coverage for loading, empty, error, disabled, success, stale data, and destructive actions when relevant.
7. Include accessibility-adjacent checks that are visible/testable from GUI review: contrast, keyboard focus order, labels, tooltips, responsive layout, and readable status text.
8. Include internationalization items when specs mention multiple languages, such as EN/VI text completeness and layout stability after language switching.
9. Do not duplicate rows with different wording. Merge overlapping items and keep the more testable version.
10. Keep rationale short and tied to user impact.

### Per-Widget Prompts

Use these prompts internally while generating rows:

| Widget family | Checklist focus |
| --- | --- |
| Forms and inputs | Required markers, labels, placeholders, validation timing, error placement, preserved data after failure, defaults, tab order, disabled submit state. |
| Date/time and numeric controls | Correct control type, valid ranges, cross-field constraints, timezone or format clarity, impossible-value prevention. |
| Upload and media preview | Accepted file type/size, progress, retry/error message, preview correctness, remove/replace action. |
| Rich-text editor | Basic formatting, paste behavior, saved rendering, no raw HTML leakage, content not breaking layout. |
| Navigation controls | Active location, breadcrumb/back behavior, role-based menu visibility, deep-link recovery, mobile navigation. |
| Search/filter/pagination | Visible criteria, reset action, result count, no-result state, preserved filters after returning from detail. |
| Tables/cards/lists | Essential fields first, readable density, sortable/filterable columns when expected, status badges, responsive behavior. |
| Buttons/icon buttons | Clear labels or tooltips, visual hierarchy, hover/focus/active/disabled states, destructive action distinction. |
| Toasts/banners/dialogs | Clear result, visible but non-blocking placement, confirmation consequences, undo or recovery where possible. |
| Progress/loading/empty states | Informative loading, closure for long flows, meaningful empty state, next action, stale-data indication. |

### Review Pass

After drafting, review the checklist before returning it:

- Coverage: all required interface aspects are present and the item count meets the assignment minimum.
- Project fit: every important screen, role, flow, and widget from the specs has at least one relevant item.
- Reference accuracy: every row cites a real Nielsen, Norman, or Shneiderman principle; remove weak or invented references.
- Testability: each item is observable in the GUI and can be marked pass/fail.
- Missed-by-AI notes: identify items likely added by human/domain review and explain why a generic AI prompt might miss them.

For HW03-style submissions, include a short `Nguồn tham khảo` section after the table and preserve the prompt or prompt summary used to generate the checklist.

### Output Contract

Return, in order:

1. `Assumptions` if any input spec is missing.
2. `UI Inventory` table.
3. `GUI Usability Checklist` table.
4. `Review Notes` for project-specific additions or corrected references.
5. `Nguồn tham khảo` with sources provided by the assignment or project files.

Do not claim the checklist is final until a human has reviewed it against the actual UI or screenshots.
