---
name: task2-user-testing
description: Use when preparing user testing templates (Task 2) for interviews and synthesizing post-interview notes, SUS scores, and usability reports.
---

# Task 2 - User Testing Preparation & Synthesis

## Overview

Use this skill to manage the complete User Testing lifecycle (Task 2). It provides tools for both **Phase 1 (Preparation & Interview Templates)** and **Phase 2 (Post-Interview Data Synthesis & Report Generation)**.

## Reference AI Audit Prompts

Derived from AI Audit Entry 13 and Task 2 session analysis (Entries 13 & 20):
- Prepares interview protocol and score templates before sessions.
- Synthesizes 5 think-aloud session notes, calculates SUS scores, and generates the final Usability Report.

---

## Phase 1 - Interview Template Preparation

When invoked prior to testing sessions, generate these Markdown templates:

1. `preparation_protocol.md`:
   - Testing objectives, target screens (e.g. D1, D2, D3), role assignments, and observer rules.
   - Goal-oriented task scenarios (give user goals, not step-by-step click commands).
   - Quantitative & qualitative metrics: Task completion rate (%), time-on-task, error count, SUS scale.

2. `participant_brief.md`:
   - Participant greeting, non-evaluative environment reassurance ("we are testing the system, not you"), think-aloud instructions, recording consent form.

3. `participant_table.md`:
   - Table of 5 participants (`P01` to `P05`) with masked contact numbers (`0909****76`), device/browser, session date/time, consent status, and YouTube/Drive recording links.

4. `session_notes_template.md`:
   - Structured observer log per participant: Start time, step-by-step observations, verbatim quotes, confusion points, completion status.

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
   - Create/fill `session_notes/P01_session_notes.md` through `P05_session_notes.md` using session notes template.

2. **Calculate SUS Scores:**
   - Compute SUS scores for all 5 participants and update `sus_score_sheet.md` with individual breakdown, average SUS score, and percentile benchmark grade (e.g. Grade A/B/C/D/F).

3. **Synthesize Usability Findings:**
   - Group recurring friction points across participants into coded findings (`UT-D-001`, `UT-D-002`, etc.).
   - Assign severity ratings:
     - `4`: Usability catastrophe (prevents completion)
     - `3`: Major usability problem (high frustration / significant delay)
     - `2`: Minor usability problem (low priority)
     - `1`: Cosmetic problem only
   - Map representative screenshots for each finding into `findings/defect-screenshots/`.

4. **Auto-Fill Final Usability Report (`usability_report.md`):**
   - Populate task completion rate matrix, SUS score summary, detailed findings table, and actionable UX recommendations.
