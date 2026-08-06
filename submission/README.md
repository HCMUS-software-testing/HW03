# README nộp bài HW03 EMS

## 1. Thông tin nộp bài

| Trường | Nội dung |
| --- | --- |
| MSSV | 23127326 |
| Họ và tên | Lê Mai Hoài Bảo |
| Nhóm | 06 |
| Kịch bản | A - Quản trị viên tạo và quản lý sự kiện |
| Nhóm chức năng | Quản trị sự kiện |
| Self-Assessed Grade | 100/100 |
| Tên file ZIP | `23127326_HW03_AI_GUIUsability_EMS_100.zip` |

## 2. Self-assessment

| No. | Criteria | Grade | Self-Assessed Grade | Minh chứng |
| --- | --- | ---: | ---: | --- |
| 1a | Task 1A - Shared checklist (> 40 items, IA-01...IA-04) + reference sources + AI prompts | 15 | 15 | `submission/gui_usability_checklist.md`, `submission/reference_sources_and_ai_prompts.md` |
| 1b | Task 1B - Checklist execution on >= 3 screens + bug reports | 15 | 15 | `submission/main_report.md`, `submission/checklist_execution.md` |
| 2 | Task 2 - User testing with 5 real users | 25 | 25 | Đủ 5 phiên, raw data, SUS, metrics, recordings và 4 findings có ảnh hoặc video/audio tương ứng. |
| 3 | Task 3 - Cross-Browser / Cross-Platform matrix | 25 | 25 | `submission/main_report.md`, `submission/cross_platform_matrix.md`, `submission/screenshots/task3/` |
| 4 | Bug & Usability Findings submission + aggregated log | 10 | 10 | `submission/bug_usability_findings_log.md`, đủ 18/18 timestamp Google Form |
| 5 | Agent Skills | 10 | 10 | `submission/skills/`, `submission/agent_skills_demo.md`, [video demo](https://youtu.be/dFPpF-rf13w) |
| | **Total** | **100** | **100** | Đủ artefact nội dung; PDF và commit cuối sẽ được thực hiện ở bước đóng gói. |

## 3. Tóm tắt kiểm thử

| Nội dung | Kết quả |
| --- | --- |
| Kịch bản đã chọn | A - Quản trị viên tạo và quản lý sự kiện |
| Màn hình đã kiểm thử | A1 Danh sách sự kiện; A2 Thêm/Sửa sự kiện; A3 Đăng ký và vai trò |
| Số tiêu chí checklist đã thiết kế | 51 tiêu chí checklist dùng chung |
| Số tiêu chí checklist đã thực thi | 153 dòng (51 dòng cho mỗi màn hình) |
| Áp dụng / Không áp dụng | 96 / 57 |
| Đạt / Không đạt | 82 / 14 (tỷ lệ đạt 85.4% trên các dòng áp dụng) |
| Tổng Task 1B theo màn hình | A1: 51 / 25 / 18 / 7 / 26 / 72.0%; A2: 51 / 38 / 34 / 4 / 13 / 89.5%; A3: 51 / 33 / 30 / 3 / 18 / 90.9% (`tổng dòng / áp dụng / đạt / không đạt / không áp dụng / tỷ lệ đạt`) |
| Số lỗi | 10: 7 lỗi chức năng Task 1B và 3 lỗi tương thích Task 3 |
| Số phát hiện tính khả dụng | 8: 4 phát hiện Task 1B và 4 phát hiện Task 2 |
| Tổng số findings | 18: 11 Task 1B, 4 Task 2 và 3 Task 3 |
| User-testing participants | 5/5 phiên chính đã đủ dữ liệu; pilot đã hoàn thành |
| Pilot user | Trần Hữu Lộc (`098****620`), ngoài lớp/P1–P5, đã consent; hoàn thành trong `08:24`, error/hesitation/can thiệp `0/0/0`, không cần điều chỉnh; [video](https://youtu.be/RBcwhBtWzQ0) |
| Điểm SUS trung bình | 74.0/100 |
| Usability issues by severity | 8 phát hiện tính khả dụng: S0: 0, S1: 0, S2: 8, S3: 0, S4: 0 |
| Compatibility cells covered | 15/15 (12 Pass, 3 Fail; đủ 3 OS, 5 browsers và 3 device classes trên mỗi màn hình) |
| Demo videos | [YouTube – 23127326-AgentSkill](https://youtu.be/dFPpF-rf13w) |

## 4. Individual ZIP required contents

| Required content theo đề | File/thư mục trong submission |
| --- | --- |
| Main report Markdown | `submission/main_report.md` |
| Main report PDF | `submission/main_report.pdf` — sẽ xuất ở bước cuối |
| User-testing evidence | `submission/user_testing_evidence.md`, recordings/screenshots nếu có |
| Bug & Usability Findings Log | `submission/bug_usability_findings_log.md` |
| Cross-browser / cross-platform screenshots | `submission/screenshots/task3/` |
| AI Critique | `submission/ai_critique.md`; `submission/ai_critique.pdf` — PDF sẽ xuất ở bước cuối |
| AI Audit Report | `submission/ai_audit_report.md`; `submission/ai_audit_report.pdf` — PDF sẽ xuất ở bước cuối |
| Git commit log | `submission/git_commit_log.txt` |
| Agent Skills + demo-video links | `submission/skills/`, `submission/agent_skills_demo.md` |
| Checklist + reference sources + AI prompts | `submission/gui_usability_checklist.md`, `submission/reference_sources_and_ai_prompts.md` |

## 5. Checklist trước khi đóng ZIP

- [x] `main_report.md` có scenario, >= 3 screens và lý do chọn.
- [x] `main_report.md` có checklist-execution results per screen.
- [x] `main_report.md` có Usability Report và cross-platform report summary.
- [ ] Có PDF cho báo cáo chính.
- [ ] Có PDF cho AI Critique và AI Audit Report.
- [x] Có checklist > 40 items và đủ IA-01...IA-04 tại `submission/gui_usability_checklist.md`.
- [x] Có reference sources và prompt AI thật tại `submission/reference_sources_and_ai_prompts.md`.
- [x] Screenshot Failed items là ảnh thật từ EMS.
- [x] Có 5 participant thật, contact đã che giữa.
- [x] Có session notes, SUS responses, metrics table và recording.
- [x] Bốn finding Task 2 có minh chứng tương ứng; UX-003 dùng video/audio probe P3.
- [x] Có 15 screenshot cross-platform cho mỗi cell; overlay hiển thị `23127326@student.hcmus.edu.vn`, URL EMS và browser/OS/device.
- [x] Mọi finding đã submit Google Form và có timestamp trong log: 18/18.
- [x] AI Audit Report có tool/model/date-time/prompt/output cho 9 entry đã giữ lại.
- [x] AI Critique nằm trong giới hạn 200–300 từ.
- [x] Có git commit log text-based.
- [x] Có Agent Skills và link demo.
- [ ] Tạo commit cuối, cập nhật thêm commit đó vào `submission/git_commit_log.txt` và đóng ZIP sau khi xuất PDF.
