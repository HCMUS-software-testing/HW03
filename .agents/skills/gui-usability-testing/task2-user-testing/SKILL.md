---
name: task2-user-testing
description: Use when preparing moderated website user testing templates or synthesizing participant notes, SUS scores, task metrics, and usability reports.
---

# User Testing Preparation & Synthesis

## Overview

Use this skill to manage a complete website user testing lifecycle. It supports **Phase 1 (Preparation & Interview Templates)** and **Phase 2 (Post-Interview Data Synthesis & Report Generation)** for any target website or web application.

## Required Inputs

- `target_url`: website URL under test.
- Target user group and participant count. Default to 5 participants only if the user does not specify a different sample size.
- Target tasks, screens, routes, or journeys.
- Account requirements for participant sessions, including account type / role and credentials if login is required.
- Consent, recording, privacy, and data mutation constraints.

---

## Phase 1 - Interview Template Preparation

When invoked prior to testing sessions, generate these Markdown templates:

1. `preparation_protocol.md`:
   - Testing objectives, target URL, target screens/routes, role assignments, and observer rules.
   - Goal-oriented task scenarios (give user goals, not step-by-step click commands).
   - Quantitative and qualitative metrics: task completion rate (%), time-on-task, error count, SUS scale.

2. `participant_brief.md`:
   - Participant greeting, non-evaluative environment reassurance ("we are testing the system, not you"), think-aloud instructions, and recording consent form.

3. `participant_table.md`:
   - Participant rows (`P01`, `P02`, etc.) with masked contact information, device/browser, session date/time, consent status, and optional recording links.

4. `session_notes_template.md`:
   - Structured observer log per participant: start time, step-by-step observations, verbatim quotes, confusion points, completion status.

5. `sus_score_sheet.md`:
   - 10-item System Usability Scale (SUS) response table per participant.
   - Formula:
     - Odd items score = `Response - 1`
     - Even items score = `5 - Response`
     - Total SUS Score = `(Sum of 10 items) * 2.5`

6. `usability_report_template.md`:
   - Structure for executive summary, methodology, task performance table, SUS score breakdown, severity-ranked findings, and UX recommendations.

---

## Phase 2 - Post-Interview Synthesis & Auto-Filling

After interview sessions are conducted, process raw notes as follows:

1. **Populate Session Notes:**
   - Create/fill `session_notes/<participant_id>_session_notes.md` using the session notes template.

2. **Calculate SUS Scores:**
   - Compute SUS scores for all participants and update `sus_score_sheet.md` with individual breakdown, average SUS score, and percentile benchmark grade (e.g. Grade A/B/C/D/F).

3. **Synthesize Usability Findings:**
   - Group recurring friction points across participants into coded findings (`UT-001`, `UT-002`, etc.).
   - Assign severity ratings:
     - `4`: Usability catastrophe (prevents completion)
     - `3`: Major usability problem (high frustration / significant delay)
     - `2`: Minor usability problem (low priority)
     - `1`: Cosmetic problem only
   - Map representative screenshots for each finding into `findings/defect-screenshots/`.

4. **Auto-Fill Final Usability Report (`usability_report.md`):**
   - Populate task completion rate matrix, SUS score summary, detailed findings table, and actionable UX recommendations.
