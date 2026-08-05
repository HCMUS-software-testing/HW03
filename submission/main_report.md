# HW03 - BÁO CÁO TỔNG HỢP KIỂM THỬ GUI VÀ TÍNH KHẢ DỤNG TRÊN EMS

**Môn học:** CS423 / CSC15003 - Kiểm thử phần mềm (AI-augmented, 2026)  
**Sinh viên thực hiện:** Lâm Hữu Khánh - MSSV: `23127205`  
**Kịch bản cá nhân:** Kịch bản C — Admin quản lý người dùng (Admin Manages Users)  
**Điểm tự đánh giá tổng cộng:** `100` / 100  

---

## 1. Kịch bản được chọn và Lý do lựa chọn màn hình (Chosen Scenario & Screen Rationale)

### 1.1 Kịch bản được chọn (Chosen Scenario)
- **Scenario C:** Admin quản lý người dùng (User Administration).
- **Hệ thống kiểm thử (SUT):** EMS Web Frontend (`https://prod-dev.ems-fitus.cloud/dashboard`).
- **Tài khoản Admin:** `admin@gmail.com` / `Admin@123` (Quyền ADMIN).

### 1.2 Lý do lựa chọn 3 màn hình kiểm thử (≥ 3 Screens & Rationale)
Để đảm bảo bao phủ trọn vẹn luồng công việc quản trị người dùng từ tổng quan đến chi tiết tác nghiệp và thao tác rủi ro, 3 màn hình chính sau đây đã được lựa chọn:

1. **Màn hình C1 — Danh sách người dùng (Users List):**
   - *Lý do chọn:* Màn hình cửa ngõ chính của Admin. Bao phủ các thành phần giao diện tần suất sử dụng cao như bảng dữ liệu (Avatar+Name, Role, Member Code, Active status), bộ lọc vai trò, công cụ tìm kiếm, phân trang và trạng thái phản hồi khi danh sách rỗng.
2. **Màn hình C2 — Gán vai trò / Chỉnh sửa người dùng (Assign Role / Edit User Form):**
   - *Lý do chọn:* Màn hình tác nghiệp cốt lõi thực hiện các thao tác thay đổi dữ liệu nguy cơ lỗi cao. Bao phủ việc kiểm thử các Form input, nhãn validation (Email, Password, Phone Number, Member Code), dropdown phân quyền và luồng lưu/hủy dữ liệu.
3. **Màn hình C3 — Hộp thoại chặn/bỏ chặn và đặt lại mật khẩu (Block/Unblock & Reset Password Confirm Dialog):**
   - *Lý do chọn:* Màn hình kiểm soát an toàn & bảo mật hệ thống. Bao phủ việc đánh giá các hộp thoại xác nhận (Confirm Dialog), thông điệp cảnh báo thao tác nguy hiểm và khả năng phục hồi/hủy thao tác của người dùng.

---

## 2. Tóm tắt Checklist GUI dùng chung (Shared GUI Checklist Summary)

- **Artifact nhóm:** [gui_usability_checklist_final.md](group/gui_usability_checklist_final.md)
- **Số mục checklist:** **51 items** bao phủ toàn bộ 4 khía cạnh giao diện (Interface Aspects):
  - **IA-01 (General UI standards):** Bố cục, typography, màu sắc, i18n (EN/VI), empty state (15 items).
  - **IA-02 (Forms):** Nhãn, validation, thông báo lỗi, xử lý trường bắt buộc (14 items).
  - **IA-03 (Navigation):** Menu, breadcrumb, sidebar, tab, nút quay lại (11 items).
  - **IA-04 (Feedback & State):** Toast notification, confirm dialog, trạng thái hệ thống (12 items).
- **Nguồn lý thuyết tham chiếu:** 10 Heuristics của Nielsen, 6 nguyên tắc thiết kế của Norman, 8 quy tắc vàng của Shneiderman (Chi tiết tại [references.md](group/references.md)).
- **Prompt AI hỗ trợ:** Đã lưu trữ nhật ký prompt tại [ai_prompts.md](group/ai_prompts.md).

---

## 3. Kết quả thực thi Checklist trên 3 màn hình (Checklist Execution Results per Screen)

- **Artifact chi tiết:** [checklist_execution_scenario_c.md](checklist_execution_scenario_c.md)

### 3.1 Bảng tổng hợp thực thi theo màn hình
| Màn hình | Mục đích kiểm thử | Tổng số mục | Số mục Pass | Số mục Fail | Mã lỗi / Finding phát hiện |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **C1 Users List** | Kiểm tra hiển thị bảng, tìm kiếm, lọc role/status, phân trang | 51 | 48 | 3 | `C-F001`, `C-F002` |
| **C2 Edit / Assign Role** | Kiểm tra form, validation email/phone/password, dropdown role | 51 | 37 | 14 | `C-F003` đến `C-F011`, `C-F014` đến `C-F018` |
| **C3 Block / Reset Pass** | Kiểm tra popup xác nhận, cảnh báo thao tác nguy hiểm | 51 | 33 | 18 | `C-F012`, `C-F013` |

- **Tổng kết chung (51 items x 3 screens):**
  - **Đã thực thi:** `51/51` items cho mỗi màn hình (`153` checks total, 100% hoàn thành trên EMS thật).
  - **Mục Pass:** `118` checks.
  - **Mục Fail:** `35` checks (được ghi nhận minh chứng ảnh trong [screenshots/checklist-failures/](screenshots/checklist-failures/)).

---

## 4. Báo cáo kiểm thử tính khả dụng (Usability Report Summary)

- **Artifact chi tiết (Task 2):** [usability_report_scenario_c.md](usability_report_scenario_c.md)

### 4.1 Kịch bản nhiệm vụ (Task Scenario)
> *"Bạn là Admin hệ thống EMS. Hãy tìm người dùng mục tiêu, kiểm tra thông tin cá nhân, thực hiện thay đổi vai trò (Assign Role), thử nghiệm thao tác chặn/bỏ chặn tài khoản hoặc đặt lại mật khẩu, và kiểm tra phản hồi từ giao diện."*

### 4.2 Bảng chỉ số đo lường (Usability Metrics) từ 5 người dùng thật ngoài lớp (P01 - P05)
| Chỉ số đo lường | Kết quả thu thập thực tế |
| :--- | :--- |
| **Tỷ lệ hoàn thành nhiệm vụ (Completion Rate)** | **`100%`** (5/5 người dùng hoàn thành nhiệm vụ) |
| **Thời gian thực hiện trung bình (Mean Time)** | **`4m10s`** (Trung vị: `4m00s`) |
| **Số lỗi trung bình / người (Errors)** | **`2.4`** lỗi / người |
| **Số lần do dự trung bình / người (Hesitations)** | **`1.8`** lần / người |
| **Điểm SUS trung bình (System Usability Scale)** | **`83.0 / 100`** (Xếp hạng **Grade A - Excellent Usability**) |

### 4.3 Danh sách 4 Usability Findings trọng tâm
1. **`C-U001 / C-F018` (Gợi ý mật khẩu không minh bạch):** Form yêu cầu có chữ số nhưng hướng dẫn không ghi rõ.
2. **`C-U002 / C-F012` (Thiếu tính năng Block & Reset Password):** Giao diện không cung cấp nút Reset Password rõ ràng.
3. **`C-U003` (Khả năng phục hồi thao tác chưa rõ):** Thiếu nút Undo / Back trực quan khi lỡ chọn sai role.
4. **`C-U004 / C-F013` (Thiếu confirm dialog nguy hiểm):** Đổi trạng thái Active/Inactive không yêu cầu Popup xác nhận.

- **Video ghi hình 6 phiên phỏng vấn (1 Pilot + 5 Real Users):** Đã tải lên YouTube tại file [demo-videos.md](demo-videos.md).

---

## 5. Báo cáo kiểm thử đa nền tảng (Cross-Platform & Cross-Browser Report)

- **Artifact chi tiết (Task 3):** [matrix.md](cross-platform/matrix.md)
- **Thư mục ảnh minh chứng:** [cross-platform/](cross-platform/) (15 ảnh chụp có watermark MSSV `23127205@student.hcmus.edu.vn`).

### 5.1 Ma trận bao phủ nghiệm thu 5 môi trường (3 OS x 5 Browsers x 3 Device Classes)
| Cell | Hệ điều hành (3 OS) | Trình duyệt (5 Browsers) | Lớp thiết bị (3 Classes) | Kết quả | Ghi chú & Mã lỗi liên kết |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **01** | **Windows 11** | **Chrome** | **Desktop (1920x1080)** | **Pass / Fail (C3)** | C1/C2 Pass chuẩn; C3 Fail do thiếu tính năng (`Bug C-F012`) |
| **02** | **Windows 11** | **Edge** | **Desktop (1366x768)** | **Pass / Fail (C3)** | C1/C2 Pass chuẩn; C3 Fail do thiếu tính năng (`Bug C-F012`) |
| **03** | **macOS** | **Opera** | **Desktop (1440x900)** | **Pass / Fail (C3)** | C1/C2 Pass mượt; C3 Fail do thiếu tính năng (`Bug C-F012`) |
| **04** | **Android** | **Firefox** | **Phone (375x667)** | **FAIL** | **Lỗi UI/Func:** C1 tràn bảng (`C-F001`), C2 tràn dialog (`C-F003`), C3 thiếu tính năng |
| **05** | **Android** | **Samsung Internet** | **Tablet (768x1024)** | **Pass / Fail** | C1 Fail vỡ phân trang (`C-F001`), C2 Pass vừa vặn, C3 Fail thiếu tính năng |

---

## 6. Tổng hợp Bug & Usability Findings Log

- **Artifact log chi tiết (Task 4):** [bug_usability_findings_log.md](bug_usability_findings_log.md)
- **Kênh submit:** Đã submit toàn bộ 18 findings lên Google Form (`https://forms.gle/CJQFQCAXcsDbXDMM9`) với timestamp khớp 100% giữa log cục bộ và Google Form response.

---

## 7. Đóng gói bài nộp và Phụ lục (Submission Artifacts)

| Artifact | Định dạng | Đường dẫn lưu trữ |
| :--- | :--- | :--- |
| **Main Report** | Markdown + PDF | [main_report.md](main_report.md) |
| **Shared GUI Checklist (Group)** | Markdown | [gui_usability_checklist_final.md](group/gui_usability_checklist_final.md) |
| **Checklist Execution (Individual)** | Markdown | [checklist_execution_scenario_c.md](checklist_execution_scenario_c.md) |
| **Usability Report** | Markdown | [usability_report_scenario_c.md](usability_report_scenario_c.md) |
| **Cross-Platform Matrix** | Markdown | [matrix.md](cross-platform/matrix.md) |
| **Bug & Findings Log** | Markdown | [bug_usability_findings_log.md](bug_usability_findings_log.md) |
| **AI Audit Report & Critique** | Markdown + PDF | [ai_audit_report.md](ai_audit_report.md), [ai_critique.md](ai_critique.md) |
| **Agent Skills & Video links** | Code + MD | [.agents/skills/](../../.agents/skills/), [demo-videos.md](demo-videos.md) |
| **Git Commit Log** | Text file | [git_commit_log.txt](git_commit_log.txt) |
| **Ảnh minh chứng Checklist/Usability** | PNG images | [screenshots/checklist-failures/](screenshots/checklist-failures/) |
| **Ảnh minh chứng Cross-Platform** | PNG images | [cross-platform/](cross-platform/) |

