# Ke hoach commit cho HW03

File nay dung de theo doi khi nao can commit trong qua trinh lam bai HW03. Nen commit sau moi moc co artifact that, ro rang va co the doi chieu voi yeu cau trong de.

## Nguyen tac chung

- Commit theo tung buoc testing procedure, khong can commit tung thay doi nho.
- Moi commit nen gom cac file cung mot muc dich.
- Khong nen commit ket qua gia. Neu file con la template `Cho kiem thu`, chi commit o giai doan scaffold/prepare.
- Sau khi co screenshot, user testing notes, form timestamp, hoac matrix result that, nen commit ngay de tranh mat minh chung.
- Commit message nen bat dau bang `docs:`, `test:`, hoac `feat:` tuy loai thay doi.

## Checklist commit khuyen nghi

| Thu tu | Khi nao commit | File nen add | Commit message goi y | Trang thai |
| --- | --- | --- | --- | --- |
| 1 | Sau khi tao/cap nhat cau truc submission ban dau | `HW03/submission/`, `HW03/.agents/` neu da co | `docs: scaffold HW03 scenario C submission` | Chua/Da lam |
| 2 | Sau khi nhom hoan thien shared GUI checklist, references, AI prompts | `HW03/submission/group/` | `docs: finalize shared GUI usability checklist` | Chua/Da lam |
| 3 | Sau khi chay checklist cho C1 Users list va co ghi chu/anh fail neu co | `HW03/submission/checklist_execution_scenario_c.md`, `HW03/submission/screenshots/checklist-failures/`, `HW03/submission/bug_usability_findings_log.md` | `test: execute checklist for C1 users list` | Chua/Da lam |
| 4 | Sau khi chay checklist cho C2 Assign Role / edit user | `HW03/submission/checklist_execution_scenario_c.md`, `HW03/submission/screenshots/checklist-failures/`, `HW03/submission/bug_usability_findings_log.md` | `test: execute checklist for C2 assign role screen` | Chua/Da lam |
| 5 | Sau khi chay checklist cho C3 Block-Unblock / Reset Password dialogs | `HW03/submission/checklist_execution_scenario_c.md`, `HW03/submission/screenshots/checklist-failures/`, `HW03/submission/bug_usability_findings_log.md` | `test: execute checklist for C3 account action dialogs` | Chua/Da lam |
| 6 | Sau khi submit findings len Google Form va dien timestamp vao log | `HW03/submission/bug_usability_findings_log.md`, `HW03/submission/screenshots/` | `docs: log scenario C bug and usability findings` | Chua/Da lam |
| 7 | Sau khi viet user testing protocol va pilot notes | `HW03/submission/user-testing/protocol.md`, `HW03/submission/user-testing/pilot_notes.md` | `docs: add scenario C user testing protocol and pilot notes` | Chua/Da lam |
| 8 | Sau khi chay xong 5 participants va nhap raw notes/SUS/metrics | `HW03/submission/user-testing/` | `test: add user testing sessions and SUS results` | Chua/Da lam |
| 9 | Sau khi chay cross-platform cho C1 va co anh matrix | `HW03/submission/cross-platform/matrix.md`, `HW03/submission/cross-platform/screenshots/` | `test: add C1 cross-platform compatibility results` | Chua/Da lam |
| 10 | Sau khi chay cross-platform cho C2 va co anh matrix | `HW03/submission/cross-platform/matrix.md`, `HW03/submission/cross-platform/screenshots/` | `test: add C2 cross-platform compatibility results` | Chua/Da lam |
| 11 | Sau khi chay cross-platform cho C3 va co anh matrix | `HW03/submission/cross-platform/matrix.md`, `HW03/submission/cross-platform/screenshots/` | `test: add C3 cross-platform compatibility results` | Chua/Da lam |
| 12 | Sau khi hoan thien AI Audit Report va AI Critique | `HW03/submission/ai-audit/`, `HW03/submission/ai_critique.md` | `docs: add AI audit report and AI critique` | Chua/Da lam |
| 13 | Sau khi them/kiem tra Agent Skills va demo video links | `HW03/.agents/`, `HW03/submission/agent-skills/`, `HW03/submission/demo-videos.md` | `feat: add EMS testing agent skills and demo links` | Chua/Da lam |
| 14 | Sau khi hoan thien main report, README, PDF, va file git log | `HW03/README.md`, `HW03/submission/main_report.md`, `HW03/submission/git_commit_log.txt`, cac file PDF neu co | `docs: finalize HW03 submission package` | Chua/Da lam |

## Lenh tao git commit log truoc khi nop

Chay lenh nay sau khi da commit gan nhu toan bo artifact:

```bash
git log --oneline --decorate --stat > HW03/submission/git_commit_log.txt
```

Sau do commit file log:

```bash
git add HW03/submission/git_commit_log.txt
git commit -m "docs: add final git commit log"
```

## Goi y kiem tra truoc khi commit

```bash
git status
git diff --stat
```

Neu muon xem noi dung thay doi chi tiet:

```bash
git diff
```

