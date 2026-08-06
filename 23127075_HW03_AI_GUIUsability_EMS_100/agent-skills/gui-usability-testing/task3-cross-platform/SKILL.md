---
name: task3-cross-platform
description: Use when generating a cross-platform compatibility matrix, screenshot protocol with watermark overlay, and evaluation reports (Task 3) based on user-provided OS, Browser, and Device inputs.
---

# Task 3 - Cross-Platform Compatibility Matrix & Testing

## Overview

Use this skill to design and execute a Cross-Platform / Cross-Browser compatibility evaluation (Task 3). Given user-provided lists of Operating Systems, Web Browsers, and Device Classes, it builds an optimal combinatorial test matrix and prepares all execution templates.

## Reference AI Audit Prompts

Derived from AI Audit Entries 14, 15, and 16:
- Converts 3 OS x 5 Browsers x 3 Devices into a reduced pairwise matrix.
- Generates screenshot overlay protocol (`MSSV@...`), compatibility matrix, and cross-platform report.

---

## Workflow

### Step 1 - Accept Platform Inputs

Prompt the user for or read the required testing dimensions:
- **Operating Systems (OS):** e.g., Windows 11, Linux (Ubuntu), Android, iOS, macOS.
- **Web Browsers:** e.g., Chrome, Firefox, Edge, Opera, Samsung Internet, Safari.
- **Device Classes:** e.g., Desktop, Tablet, Mobile Phone.

### Step 2 - Build Combinatorial Matrix (Pairwise Reduction)

When cloud trial limits apply (e.g. 1-minute BrowserStack / TestingBot trials), apply combinatorial/pairwise reduction to select the minimum number of cells (e.g. 5 cells) that cover:
- All required OS at least once.
- All required Browsers at least once.
- All required Device Classes (Desktop, Tablet, Phone) at least once.

Example Optimal 5-Cell Pairwise Matrix:
| Cell ID | Environment Name | OS | Browser & Version | Device Class | Viewport Resolution |
| --- | --- | --- | --- | --- | --- |
| `CP-01` | Linux Firefox Desktop | Linux (Ubuntu) | Firefox (Latest) | Desktop | 1920x1080 |
| `CP-02` | Win11 Opera Desktop | Windows 11 | Opera (Latest) | Desktop | 1920x1080 |
| `CP-03` | Win11 Edge Desktop | Windows 11 | Edge (Latest) | Desktop | 1920x1080 |
| `CP-04` | Android Samsung Tab | Android 13 | Samsung Internet | Tablet | 800x1280 |
| `CP-05` | Android Chrome Phone | Android 13 | Chrome Mobile | Phone | 390x844 |

### Step 3 - Generate Screenshot Protocol (`screenshot_protocol.md`)

Define mandatory evidence rules:
1. Every cell must capture screenshots for target screens (e.g. D1, D2, D3).
2. Every screenshot must feature the **Student Email Overlay Watermark** (e.g., `23127075@clc.fitus.edu.vn` or `MSSV@...`), environment name, and timestamp.
3. Save downloads to `task3_cross_platform/screenshots/downloads/`.

### Step 4 - Generate Compatibility Matrix & Report Templates

Generate:
1. `compatibility_matrix.md`:
   - Summary table mapping Cell ID x Screen (D1, D2, D3) -> Status (Pass/Fail/Defect ID), download screenshot link, and defect references.
2. `cross_platform_report.md`:
   - Executive summary of compatibility findings, visual inspection notes (overflows, text truncation, z-index sticky element misalignment, touch target spacing), and cross-browser bug severity table.
