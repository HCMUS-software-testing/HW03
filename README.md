# HW03 – Kiểm thử giao diện và tính khả dụng trên EMS (Hệ thống quản lý sự kiện)

> **Môn học:** CS423 / CSC15003 – Kiểm thử phần mềm (phiên bản có hỗ trợ AI)
> **Hệ thống kiểm thử (SUT):** EMS (`https://prod-dev.ems-fitus.cloud/`; đường dẫn ngrok trong đề trả về 404 khi Task 1B được chạy lại ngày 2026-08-02)

---

## 1. THÔNG TIN NHÓM & PHÂN CÔNG SCENARIO 

| STT | MSSV | Họ và tên | Scenario | Danh sách 3 Màn hình kiểm thử |
| :---: | :---: | :--- | :---: | :--- |
| **1** | 23127075 | Lê Trung Kiên | **Scenario D** | |
| **2** | 23127185 | Mai Thị Kim Duyên | **Scenario B** |1. B1: Home / events listing - featured carousel, categories, search/filter <br> 2. B2: Event detail page - banner, schedule, register button, waitlist notice <br> 3. B3: Registration form - role selection, additional role, confirmation; |
| **3** | 23127205 | Lâm Hữu Khánh | **Scenario C** | 1. C1: Users list - search, role/active filters, columns; <br> 2. C2: Assign Role / edit user; <br> 3. C3: Block-Unblock and Reset-Password dialogs - confirmation + audit; |
| **4** | 23127326 | Lê Mai Hoài Bảo | **Scenario A** | 1. A1: Events list with status filters and notification dots; <br> 2. A2: Add/Edit Event form - image upload + Rich-Text + date/time validation; <br> 3. A3: Registration & Roles configuration panel - Max Slots / Waitlist / additional role; |

---

## 2. BẢNG TỰ ĐÁNH GIÁ ĐIỂM THÀNH VIÊN

### 2.1 Thành viên 1: Lê Trung Kiên (MSSV: 23127075) - Scenario D
> **Điểm tự đánh giá tổng cộng (Self-Assessed Grade):** `[000 - 100]` / 100

| No. | Criteria | Grade | Self-Assessed Grade | Ghi chú & Minh chứng |
| :---: | :--- | :---: | :---: | :--- |
| **1a** | Task 1A — Shared checklist (> 40 items, IA-01…IA-04) | 15 | ___ / 15 | Shared Checklist |
| **1b** | Task 1B — Checklist execution on ≥ 3 screens | 15 | ___ / 15 | Checklist Execution Table |
| **2** | Task 2 — User testing with 5 real users | 25 | ___ / 25 | Usability Report |
| **3** | Task 3 — Cross-Browser / Cross-Platform matrix | 25 | ___ / 25 | Compatibility Matrix |
| **4** | Task 4 — Bug & Usability Findings (Google Form + Log) | 10 | ___ / 10 | Bug Findings Log |
| **5** | Task 5 — Agent Skills + YouTube Demo | 10 | ___ / 10 | Agent Skill + Video Link |
| **TỔNG**| **TOTAL** | **100** | **___ / 100** | |

---

### 2.2 Thành viên 2: Mai Thị Kim Duyên (MSSV: 23127185) - Scenario B
> **Điểm tự đánh giá tổng cộng (Self-Assessed Grade):** `[000 - 100]` / 100

| No. | Criteria | Grade | Self-Assessed Grade | Ghi chú & Minh chứng |
| :---: | :--- | :---: | :---: | :--- |
| **1a** | Task 1A — Shared checklist (> 40 items, IA-01…IA-04) | 15 | ___ / 15 | Shared Checklist |
| **1b** | Task 1B — Checklist execution on ≥ 3 screens | 15 | ___ / 15 | Checklist Execution Table |
| **2** | Task 2 — User testing with 5 real users | 25 | ___ / 25 | Usability Report |
| **3** | Task 3 — Cross-Browser / Cross-Platform matrix | 25 | ___ / 25 | Compatibility Matrix |
| **4** | Task 4 — Bug & Usability Findings (Google Form + Log) | 10 | ___ / 10 | Bug Findings Log |
| **5** | Task 5 — Agent Skills + YouTube Demo | 10 | ___ / 10 | Agent Skill + Video Link |
| **TỔNG**| **TOTAL** | **100** | **___ / 100** | |

---

### 2.3 Thành viên 3: Lâm Hữu Khánh (MSSV: 23127205) - Scenario C
> **Điểm tự đánh giá tổng cộng (Self-Assessed Grade):** `[000 - 100]` / 100

| No. | Criteria | Grade | Self-Assessed Grade | Ghi chú & Minh chứng |
| :---: | :--- | :---: | :---: | :--- |
| **1a** | Task 1A — Shared checklist (> 40 items, IA-01…IA-04) | 15 | ___ / 15 | Shared Checklist |
| **1b** | Task 1B — Checklist execution on ≥ 3 screens | 15 | ___ / 15 | Checklist Execution Table |
| **2** | Task 2 — User testing with 5 real users | 25 | ___ / 25 | Usability Report |
| **3** | Task 3 — Cross-Browser / Cross-Platform matrix | 25 | ___ / 25 | Compatibility Matrix |
| **4** | Task 4 — Bug & Usability Findings (Google Form + Log) | 10 | ___ / 10 | Bug Findings Log |
| **5** | Task 5 — Agent Skills + YouTube Demo | 10 | ___ / 10 | Agent Skill + Video Link |
| **TỔNG**| **TOTAL** | **100** | **___ / 100** | |

---

### 2.4 Thành viên 4: Lê Mai Hoài Bảo (MSSV: 23127326) - Scenario A
> **Điểm tự đánh giá tổng cộng (Self-Assessed Grade):** `[000 - 100]` / 100

| No. | Criteria | Grade | Self-Assessed Grade | Ghi chú & Minh chứng |
| :---: | :--- | :---: | :---: | :--- |
| **1a** | Task 1A — Shared checklist (> 40 items, IA-01…IA-04) | 15 | ___ / 15 | Shared Checklist |
| **1b** | Task 1B — Checklist execution on ≥ 3 screens | 15 | ___ / 15 | Checklist Execution Table |
| **2** | Task 2 — User testing with 5 real users | 25 | ___ / 25 | Usability Report |
| **3** | Task 3 — Cross-Browser / Cross-Platform matrix | 25 | 25 / 25 | `submission/cross_platform_matrix.md` + 15 screenshots |
| **4** | Task 4 — Bug & Usability Findings (Google Form + Log) | 10 | ___ / 10 | Bug Findings Log |
| **5** | Task 5 — Agent Skills + YouTube Demo | 10 | ___ / 10 | Agent Skill + Video Link |
| **TỔNG**| **TOTAL** | **100** | **___ / 100** | |

---

## 3. TÓM TẮT KẾT QUẢ KIỂM THỬ CỦA TỪNG THÀNH VIÊN (TEST SUMMARIES)

### 3.1 Lê Trung Kiên (23127075) - Scenario D
- **Màn hình đã test:** 
- **GUI Checklist:** Designed: _____ | Executed: _____ | Passed: _____ | Failed: _____
- **Số lượng Bug & Usability Issues:** _____
- **User Testing:** 5 người dùng | Điểm SUS/UEQ-S: _____ / 100
- **Cross-Platform:** _____ / 45 cells covered
- **Agent Skill & YouTube Video:** `https://youtu.be/...`

### 3.2 Mai Thị Kim Duyên (23127185) - Scenario B
- **Màn hình đã test:** B1, B2, B3
- **GUI Checklist:** Designed: _____ | Executed: _____ | Passed: _____ | Failed: _____
- **Số lượng Bug & Usability Issues:** _____
- **User Testing:** 5 người dùng | Điểm SUS/UEQ-S: _____ / 100
- **Cross-Platform:** _____ / 45 cells covered
- **Agent Skill & YouTube Video:** `https://youtu.be/...`

### 3.3 Lâm Hữu Khánh (23127205) - Scenario C
- **Màn hình đã test:** C1, C2, C3
- **GUI Checklist:** Designed: _____ | Executed: _____ | Passed: _____ | Failed: _____
- **Số lượng Bug & Usability Issues:** _____
- **User Testing:** 5 người dùng | Điểm SUS/UEQ-S: _____ / 100
- **Cross-Platform:** _____ / 45 cells covered
- **Agent Skill & YouTube Video:** `https://youtu.be/...`

### 3.4 Lê Mai Hoài Bảo (23127326) - Kịch bản A
- **Màn hình đã test:** A1, A2, A3
- **Checklist giao diện:** Thiết kế: 51 | Thực thi: 153 (51 × 3 màn hình) | Áp dụng: 96 | Đạt: 82 | Không đạt: 14 | Không áp dụng: 57 | Tỷ lệ đạt: 85.4%
- **Task 1B theo màn hình:** A1: 25 áp dụng, 18 đạt, 7 không đạt, 26 không áp dụng (72.0%); A2: 38, 34, 4, 13 (89.5%); A3: 33, 30, 3, 18 (90.9%).
- **Số lượng lỗi và vấn đề tính khả dụng:** 11 phát hiện được xác nhận bằng tương tác trong Task 1B
- **Kiểm thử người dùng:** 5 người dùng | Điểm SUS/UEQ-S: _____ / 100
- **Đa nền tảng:** 15/15 ô đã kiểm tra (12 đạt, 3 không đạt; đủ coverage bắt buộc)
- **Kỹ năng tác tử và video YouTube:** `https://youtu.be/...`
