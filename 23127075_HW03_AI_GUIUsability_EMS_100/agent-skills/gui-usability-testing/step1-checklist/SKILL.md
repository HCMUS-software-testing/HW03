---
name: step1-checklist
description: Use when generating a website-specific GUI usability checklist based on target URL, target scope, Nielsen heuristics, Norman principles, Shneiderman rules, and UI widget specs.
---

# GUI Usability Checklist Generation

## Overview

Use this skill to turn a target website, specs, screenshots, or user journeys into a reusable GUI usability testing checklist. It extracts a UI inventory and maps heuristic principles to concrete, observable checklist items.

## Inputs

Gather or inspect these inputs before generating the checklist:
- `target_url`: the website URL. Required when the checklist is based on live pages; ask the user if missing.
- Website overview, domain concepts, and user roles.
- Target features, journeys, routes, and screens.
- Authentication requirement and available account types if private screens must be inventoried.
- Required interface aspects:
  - `IA-01`: General UI standards
  - `IA-02`: Forms and data entry
  - `IA-03`: Navigation and information architecture
  - `IA-04`: Feedback, status, and system recovery
- UI widget inventory from specs, screenshots, or live pages.
- Target minimum item count (default: >40 items).

## Source Principles

Every item must reference at least one recognized standard:
- **Nielsen's 10 Usability Heuristics:** Visibility of system status, match between system and real world, user control & freedom, consistency & standards, error prevention, recognition rather than recall, flexibility & efficiency, aesthetic & minimalist design, error recovery, help & documentation.
- **Norman's 6 Design Principles:** Visibility/discoverability, feedback, affordances, signifiers, mapping, constraints.
- **Shneiderman's 8 Golden Rules:** Strive for consistency, seek universal usability, offer informative feedback, design dialogs to yield closure, prevent errors, permit easy reversal of actions, support internal locus of control, reduce short-term memory load.

## Workflow

1. **Extract UI Inventory:**
   - Map screens, roles, multi-step flows, widget families (forms, date pickers, uploads, rich-text, search/filters, tables, tabs, modals, badges), and dynamic states (loading, disabled, empty, error, stale data).
   - If using live pages and login is required, ask for the needed account type and credentials before inspecting private screens.

2. **Generate Checklist Table:**
   - Format as Markdown table:
     `| ID | Interface Aspect | Checklist Item | Reference | Rationale | Priority | Review Notes |`
   - Balance items across `IA-01` to `IA-04`.
   - Ensure items are concrete and observable (can be marked `Passed` or `Failed`).

3. **Human Review Pass:**
   - Review AI output against website domain realities to remove duplicates or generic fluff before finalizing.

## Output Contract

- Summary of UI Inventory.
- Markdown Checklist Table (>40 items unless the user requests another size).
- Reference sources section (`Nguồn tham khảo` or `References`, matching the requested report language).
