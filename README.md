# HW03 – GUI & Usability Testing on EMS (Event Management System)

> **Môn học:** CS423 / CSC15003 – Software Testing (AI-augmented edition)  
> **Hệ thống kiểm thử (SUT):** EMS (`https://prod-dev.ems-fitus.cloud/dashboard`)

---

## 1. THÔNG TIN NHÓM & PHÂN CÔNG SCENARIO 

| STT | MSSV | Họ và tên | Scenario | Danh sách 3 Màn hình kiểm thử |
| :---: | :---: | :--- | :---: | :--- |
| **1** | 23127075 | Lê Trung Kiên | **Scenario D** | 1. D1: Audit logs / activity feed <br> 2. D2: Export data dialog <br> 3. D3: System settings panel |
| **2** | 23127185 | Mai Thị Kim Duyên | **Scenario B** | 1. B1: Home / events listing - featured carousel, categories, search/filter <br> 2. B2: Event detail page - banner, schedule, register button, waitlist notice <br> 3. B3: Registration form - role selection, additional role, confirmation |
| **3** | 23127205 | Lâm Hữu Khánh | **Scenario C** | 1. C1: Users list - search, role/active filters, columns <br> 2. C2: Assign Role / edit user <br> 3. C3: Block-Unblock and Reset-Password dialogs - confirmation + audit |
| **4** | 23127326 | Lê Mai Hoài Bảo | **Scenario A** | 1. A1: Events list with status filters and notification dots <br> 2. A2: Add/Edit Event form - image upload + Rich-Text + date/time validation <br> 3. A3: Registration & Roles configuration panel - Max Slots / Waitlist / additional role |

---

## 2. BẢNG TỰ ĐÁNH GIÁ ĐIỂM CÁ NHÂN

### Sinh viên: Lâm Hữu Khánh (MSSV: 23127205) - Scenario C
> **Điểm tự đánh giá tổng cộng (Self-Assessed Grade):** `095` / 100

| No. | Criteria | Grade | Self-Assessed Grade | Ghi chú & Đường dẫn minh chứng |
| :---: | :--- | :---: | :---: | :--- |
| **1a** | Task 1A — Shared checklist (> 40 items, IA-01…IA-04) | 15 | 15 / 15 | Shared Checklist (`submission/group/gui_usability_checklist_final.md`) |
| **1b** | Task 1B — Checklist execution on ≥ 3 screens | 15 | 15 / 15 | Checklist Execution Table (`submission/checklist_execution_scenario_c.md`) |
| **2** | Task 2 — User testing with 5 real users | 25 | 25 / 25 | Usability Report (`submission/usability_report_scenario_c.md`) |
| **3** | Task 3 — Cross-Browser / Cross-Platform matrix | 25 | 25 / 25 | Compatibility Matrix (`submission/cross-platform/matrix.md`) |
| **4** | Task 4 — Bug & Usability Findings (Google Form + Log) | 10 | 10 / 10 | Bug Findings Log (`submission/bug_usability_findings_log.md`) |
| **5** | Task 5 — Agent Skills + YouTube Demo | 10 | 5 / 10 | Agent Skill + Video Link (`submission/agent-skills/skill_inventory.md`) |
| **TỔNG**| **TOTAL** | **100** | **95 / 100** | |

---

## 3. TÓM TẮT KẾT QUẢ KIỂM THỬ CÁ NHÂN (TEST SUMMARY)

### Sinh viên: Lâm Hữu Khánh (23127205) - Scenario C

- **Màn hình đã test:** C1 Users list, C2 Assign Role / edit user, C3 Block/Reset Password dialogs
- **GUI Checklist thiết kế:** Designed: `52` items (Bao phủ đầy đủ IA-01, IA-02, IA-03, IA-04)
- **Kết quả thực thi Checklist:** Executed: `52` | Passed: `35` | Failed: `17`
- **Số lượng Bug & Usability Issues phát hiện:** `18 findings` (`C-F001` đến `C-F018`)
- **Kết quả User Testing (5 người dùng ngoài lớp):** 
  - Mức hoàn thành: `100%` (5/5 người dùng)
  - Thời gian trung bình: `4m10s`
  - Số lỗi trung bình: `2.4` | Do dự trung bình: `1.8` | Trợ giúp trung bình: `1.8`
  - Điểm SUS trung bình: **`83.0 / 100`** (Hạng A - Good Usability)
  - Video phỏng vấn (YouTube): Pilot: https://youtu.be/lpxRwuFYGBM | U1: https://youtu.be/Qg45dvZBvzo | U2: https://youtu.be/MnQzUx25SYI | U3: https://youtu.be/5hYpKizmWhA | U4: https://youtu.be/syO6zu7qQhU | U5: https://youtu.be/ysRW-LvCq_M
- **Độ bao phủ Cross-Platform:** `15 / 15 cells` (3 OS x 5 Browsers x 3 Device classes)
- **Báo cáo AI Audit & AI Critique:** `submission/ai-audit/ai_audit_report.md` | `submission/ai_critique.md`
- **Agent Skill & YouTube Video:** `submission/agent-skills/skill_inventory.md` | `submission/demo-videos.md`
