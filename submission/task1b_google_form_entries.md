# Task 1B — Google-Form-ready entries for Bảo

## Submission status

- Student: Lê Mai Hoài Bảo (MSSV 23127326)
- Student email: **Bảo must enter/confirm real student email; not found in repo.**
- Scenario: A — Admin creates and manages events
- Tested deployment: `https://prod-dev.ems-fitus.cloud/`
- Test date: 2026-08-02 (Asia/Ho_Chi_Minh)
- Draft retained: `23127326_TASK1B_20260802_163308`, event ID 80; not published or deleted
- Google Form: https://forms.gle/CJQFQCAXcsDbXDMM9
- External submission: **Not performed. Bảo remains in control.**
- Form timestamps: **Pending — synchronize after Bảo submits.**

Before submission, Bảo must enter the real student email, open every referenced screenshot, and confirm that the form field names match the values below. After each receipt, replace the pending timestamp in this file and `bug_usability_findings_log.md` with the real receipt timestamp.

## Prepared entries

### T1B-A1-01

- Screen: A1 Events list
- Type: Usability
- Checklist IDs: IA-03-06, IA-04-07
- Description: Empty search result has no reset/clear action.
- Steps: Open Events; enter a query that matches no event; observe the empty state.
- Expected: Empty state explains the result and provides a direct Reset/Clear action.
- Actual: The message explains that no events match, but offers no action to clear the active query/filter.
- Severity: 2 — Moderate
- Suggested fix: Add a prominent `Reset filters` action in the empty state and return focus to Search after reset.
- Screenshot: `screenshots/task1b/a1-f01-empty-no-reset.png`
- Source task: Task 1B
- Form timestamp: Pending — synchronize after Bảo submits

### T1B-A1-03

- Screen: A1 Events list
- Type: Usability
- Checklist IDs: IA-01-10
- Description: Events table requires horizontal scrolling in the captured 1171×768 Safari window.
- Steps: Open Events in the captured 1171×768 Safari window; observe the table and its bottom edge.
- Expected: Core columns and actions remain visible without unnecessary horizontal scrolling in a compact desktop window.
- Actual: The wide table overflows horizontally and hides later columns/actions until the user scrolls sideways.
- Severity: 2 — Moderate
- Suggested fix: Prioritize core columns, allow controlled wrapping, and move secondary data into a details affordance at narrower widths.
- Screenshot: `screenshots/task1b/a1-overview.png`
- Source task: Task 1B
- Form timestamp: Pending — synchronize after Bảo submits

### T1B-A1-04

- Screen: A1 Events list
- Type: Bug
- Checklist IDs: IA-01-13
- Description: English notification panel contains untranslated Vietnamese text.
- Steps: Keep the UI in English; open Notifications; read the notification entries.
- Expected: All notification text uses the selected English locale.
- Actual: The panel includes `Phản hồi khiếu nại` while surrounding UI is English.
- Severity: 1 — Minor
- Suggested fix: Route all notification templates through the same locale resource and add EN/VI regression coverage.
- Screenshot: `screenshots/task1b/a1-f04-notification-mixed-language.png`
- Source task: Task 1B
- Form timestamp: Pending — synchronize after Bảo submits

### T1B-A1-05

- Screen: A1 Events list
- Type: Usability
- Checklist IDs: IA-01-07
- Description: Focused icon-only event action provides no visible tooltip.
- Steps: Move keyboard focus to an icon-only event action; pause on the focused control; observe its visible explanation.
- Expected: A focused or hovered icon-only action exposes a clear label/tooltip.
- Actual: The Delete icon receives a focus ring, but no visible label or tooltip appears.
- Severity: 2 — Moderate
- Suggested fix: Add persistent accessible names and a tooltip triggered by both hover and keyboard focus.
- Screenshot: `screenshots/task1b/a1-f05-action-focus-no-tooltip.png`
- Source task: Task 1B
- Form timestamp: Pending — synchronize after Bảo submits

### T1B-A1-06

- Screen: A1 Events list
- Type: Bug
- Checklist IDs: IA-03-03, IA-03-09
- Description: Search/filter state is lost after opening an event and navigating back.
- Steps: Search for the uniquely named Task 1B draft; open its details; use browser Back.
- Expected: The Events list restores the search query, filtered rows, and prior list position.
- Actual: The full list returns with the Search field cleared.
- Severity: 2 — Moderate
- Suggested fix: Persist list query/filter/page state in the URL or navigation state and restore it on return.
- Screenshots: before `screenshots/task1b/a1-f05-action-focus-no-tooltip.png`; after `screenshots/task1b/a1-f06-filter-not-retained.png`
- Source task: Task 1B
- Form timestamp: Pending — synchronize after Bảo submits

### T1B-A2-01

- Screen: A2 Add/Edit Event
- Type: Bug
- Checklist IDs: IA-02-12
- Description: Thumbnail upload accepts a `.txt` file as an image.
- Steps: Open Create/Edit Event; choose `upload_invalid.txt` in Thumbnail upload; observe the preview.
- Expected: Unsupported non-image files are rejected before preview/upload with a specific validation message.
- Actual: The `.txt` file is accepted and a broken thumbnail preview is rendered without an error.
- Severity: 2 — Moderate
- Suggested fix: Restrict the file picker and validate MIME type, signature, extension, and size before creating a preview.
- Screenshot: `screenshots/task1b/a2-f01-invalid-thumbnail-accepted.png`
- Source task: Task 1B
- Form timestamp: Pending — synchronize after Bảo submits

### T1B-A2-02

- Screen: A2 Add/Edit Event
- Type: Bug
- Checklist IDs: IA-02-11, IA-03-09
- Description: Leaving a populated edit form gives no unsaved-change warning and loses the unsaved title.
- Steps: Change the title in the populated event edit form; use browser Back before saving; observe navigation and the cleared edit context.
- Expected: The app asks for confirmation and keeps the unsaved edit until the user explicitly chooses to discard it.
- Actual: Navigation occurs immediately with no warning; the unsaved title is lost.
- Severity: 3 — Major
- Suggested fix: Track dirty form state and show a confirmation dialog for in-app and browser navigation.
- Screenshots: before `screenshots/task1b/a2-f02-unsaved-before.png`; after `screenshots/task1b/a2-f02-unsaved-after-no-warning.png`
- Source task: Task 1B
- Form timestamp: Pending — synchronize after Bảo submits

### T1B-A2-03

- Screen: A2 Add/Edit Event
- Type: Usability
- Checklist IDs: IA-01-07
- Description: Back and Thumbnail/Banner camera icon-only controls lack visible labels/tooltips on hover or keyboard focus; rich-text icons did expose tooltips.
- Steps: Open the retained edit form; hover Back and the media camera controls; keyboard-focus the Thumbnail camera; pause.
- Expected: Every icon-only action provides a clear visible label/tooltip on both hover and keyboard focus.
- Actual: Back and the Thumbnail/Banner camera controls show no visible label/tooltip on the tested hover/focus states.
- Severity: 2 — Moderate
- Suggested fix: Add accessible names plus tooltips triggered by hover and keyboard focus, or add visible labels.
- Screenshots: `screenshots/task1b/a2-icon-hover-back-no-tooltip.png`; `screenshots/task1b/a2-icon-keyboard-focus-unlabeled-camera.png`; `screenshots/task1b/a2-icon-hover-thumbnail-camera-no-tooltip.png`; `screenshots/task1b/a2-icon-hover-banner-camera-no-tooltip.png`
- Source task: Task 1B
- Form timestamp: Pending — synchronize after Bảo submits

### T1B-A3-01

- Screen: A3 Registration & Roles
- Type: Bug
- Checklist IDs: IA-02-04
- Description: `Max Slots` remains active when `Is Unlimited` is enabled.
- Steps: Enable Student Registration; enable `Is Unlimited`; inspect and edit `Max Slots`.
- Expected: Unlimited capacity disables, clears, or hides the conflicting finite `Max Slots` control.
- Actual: `Max Slots` remains visible and editable while Unlimited is ON.
- Severity: 2 — Moderate
- Suggested fix: Disable and clear `Max Slots` when Unlimited is enabled, and restore it only when Unlimited is disabled.
- Screenshot: `screenshots/task1b/a3-f01-unlimited-max-slots-active.png`
- Source task: Task 1B
- Form timestamp: Pending — synchronize after Bảo submits

### T1B-A3-03

- Screen: A3 Registration & Roles
- Type: Bug
- Checklist IDs: IA-02-04
- Description: Waitlist remains enabled after Student Registration is disabled.
- Steps: Enable Student Registration and Waitlist; disable Student Registration; observe Waitlist.
- Expected: Disabling the parent registration mode disables or clears dependent Waitlist state.
- Actual: Student role controls disappear, but Waitlist remains ON.
- Severity: 3 — Major
- Suggested fix: Define the dependency explicitly: clear/disable Waitlist when Student Registration is OFF and validate it again on save.
- Screenshot: `screenshots/task1b/a3-f03-waitlist-with-student-off.png`
- Source task: Task 1B
- Form timestamp: Pending — synchronize after Bảo submits

### T1B-A3-04

- Screen: A3 Registration & Roles
- Type: Bug
- Checklist IDs: IA-02-11, IA-03-09
- Description: An unsaved Registration & Roles change is lost without warning.
- Steps: Change Reminder from 24 to 25; use Back without saving; reopen the retained draft.
- Expected: The app warns before navigation and retains the change until the user explicitly discards it.
- Actual: Navigation immediately returns to Events; reopening the draft shows the saved value 24, so the unsaved value 25 was lost.
- Severity: 3 — Major
- Suggested fix: Add a shared dirty-form guard covering nested role/options state and browser/router navigation.
- Screenshots: `screenshots/task1b/a3-unsaved-reminder-25-before-back.png`; `screenshots/task1b/a3-unsaved-back-no-warning-destination.png`; `screenshots/task1b/a3-unsaved-reopen-reminder-24-persisted.png`
- Source task: Task 1B
- Form timestamp: Pending — synchronize after Bảo submits
