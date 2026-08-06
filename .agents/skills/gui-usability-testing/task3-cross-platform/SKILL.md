---
name: task3-cross-platform
description: Use when generating or executing a website cross-platform compatibility matrix, screenshot protocol, and evaluation report based on target URL, OS, browser, and device inputs.
---

# Cross-Platform Compatibility Matrix & Testing

## Overview

Use this skill to design and execute a cross-platform / cross-browser compatibility evaluation for any website. Given a target URL, target flows, and user-provided lists of operating systems, browsers, and device classes, it builds a combinatorial test matrix and prepares execution templates.

## Required Inputs

- `target_url`: website URL under test.
- Target screens, routes, or user journeys.
- Operating systems, browsers, device classes, and viewport sizes.
- Authentication requirement and account type / credentials for any private flows.
- Evidence watermark or tester identifier if the user wants one. Do not assume a student ID or email format.

When live execution is required and MCP Playwright is the selected browser tool, actually use MCP Playwright. If MCP Playwright is unavailable, help install or enable it before executing tests.

---

## Workflow

### Step 1 - Accept Platform Inputs

Prompt the user for or read the required testing dimensions:
- **Target URL:** website URL under test.
- **Target Scope:** screens, routes, forms, or user journeys to evaluate.
- **Operating Systems (OS):** e.g., Windows 11, Linux (Ubuntu), Android, iOS, macOS.
- **Web Browsers:** e.g., Chrome, Firefox, Edge, Opera, Samsung Internet, Safari.
- **Device Classes:** e.g., Desktop, Tablet, Mobile Phone.
- **Authentication:** account type / role and credentials if login is required.

### Step 2 - Build Combinatorial Matrix (Pairwise Reduction)

When cloud trial limits apply or full Cartesian testing is too costly, apply combinatorial/pairwise reduction to select the minimum number of cells that cover:
- All required OS at least once.
- All required browsers at least once.
- All required device classes at least once.
- The highest-risk browser/device combinations for the target website.

Example 5-cell matrix:

| Cell ID | Environment Name | OS | Browser & Version | Device Class | Viewport Resolution |
| --- | --- | --- | --- | --- | --- |
| `CP-01` | Linux Firefox Desktop | Linux (Ubuntu) | Firefox (Latest) | Desktop | 1920x1080 |
| `CP-02` | Win11 Edge Desktop | Windows 11 | Edge (Latest) | Desktop | 1920x1080 |
| `CP-03` | macOS Safari Desktop | macOS | Safari (Latest) | Desktop | 1440x900 |
| `CP-04` | Android Chrome Tablet | Android | Chrome Mobile | Tablet | 800x1280 |
| `CP-05` | iOS Safari Phone | iOS | Safari Mobile | Phone | 390x844 |

### Step 3 - Generate Screenshot Protocol (`screenshot_protocol.md`)

Define mandatory evidence rules:
1. Every cell must capture screenshots for each target screen, route, or user journey.
2. Every screenshot must include the target URL, environment name, timestamp, and optional user-provided watermark/tester identifier.
3. Save screenshots and downloads to a dedicated cross-platform evidence directory, for example `cross_platform/screenshots/`.

### Step 4 - Generate Compatibility Matrix & Report Templates

Generate:
1. `compatibility_matrix.md`:
   - Summary table mapping Cell ID x Screen/Flow -> Status (Pass/Fail/Defect ID), screenshot/download link, and defect references.
2. `cross_platform_report.md`:
   - Executive summary of compatibility findings, visual inspection notes (overflows, text truncation, z-index sticky element misalignment, touch target spacing), and cross-browser bug severity table.
