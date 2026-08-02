# Repository Guidelines

## Project Structure & Module Organization

This repository contains HW03 software testing homework materials and submission artifacts. It is documentation-first; there is no application source tree or package manifest.

- `docs/`: assignment briefs, EMS context, and converted reference documents. Prefer reading `*.md` files; only open PDFs when no Markdown counterpart exists or the user explicitly asks.
- `submission/`: student-facing deliverables, test environment notes, GUI usability checklists, screenshots, and audit records.
- `submission/task1B/`: Task 1B testing reports.
- `submission/group/`: shared group checklist files. Do not modify finalized checklist files unless explicitly requested.
- `ai-reasoning/`: AI-supporting notes and reference material. Prefer Markdown over PDFs to reduce token usage.
- `.agents/` and `.codex/`: local agent/tooling metadata; do not edit unless the task explicitly requires it.

## Build, Test, and Development Commands

There is no build step or automated test suite for this repository. Use local inspection commands instead:

- `rtk rg --files`: list project files quickly.
- `rtk sed -n '1,120p' docs/<file>.md`: inspect a Markdown document.
- `rtk rg $'\f||▍|›' docs/*.md submission/*.md`: check for common PDF extraction artifacts.
- `rtk git status --short`: review changed and untracked files before finishing work.

Per workspace convention, prefix shell commands with `rtk`.

## Coding Style & Naming Conventions

Use Markdown for repository documentation. Keep heading levels logical, paragraphs short, and structured data in tables where appropriate. Preserve Vietnamese accents and source wording when they are part of requirements, UI evidence, accounts, or test data.

Wrap commands, file paths, credentials, routes, statuses, and identifiers in backticks, for example `Admin@123`, `PUBLISHED`, `submission/task1B/task1b_D1.md`, or `/support-request`.

Primary submission content should be written in Vietnamese unless the user explicitly requests another language. Keep exact English UI labels when they are evidence from the tested system.

## Testing Guidelines

For documentation changes, verify manually:

- Tables have matching column counts.
- Links, routes, email addresses, and account details are preserved.
- Screenshot paths remain valid.
- No obvious PDF extraction artifacts remain.

When testing web flows, follow `submission/test_environment_access.md` exactly and use MCP Playwright or Chrome DevTools where helpful.

## Commit & Pull Request Guidelines

Git history uses short messages such as `fixed: gui usability checklist` and `add: test env access markdown for AI`. Use concise, imperative commit messages that describe the changed artifact.

Pull requests should summarize the documentation changed, note any checklist or test-flow updates, and include screenshots only when they support visual or usability evidence.
