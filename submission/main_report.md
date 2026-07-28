# Báo cáo chính HW03 - GUI & Usability Testing on EMS

## 1. Thông tin sinh viên và phạm vi

| Trường | Nội dung |
| --- | --- |
| MSSV | 23127326 |
| Họ và tên | Lê Mai Hoài Bảo |
| Email sinh viên | [Điền email dạng MSSV@....edu.vn] |
| Nhóm | [Điền tên/mã nhóm] |
| Scenario phụ trách | Scenario A - Admin creates and manages events |
| Function pool | A - Event administration |
| EMS URL | https://promoter-starboard-prude.ngrok-free.dev/ |
| Tài khoản sử dụng | Admin |

## 2. Scenario đã chọn và các màn hình kiểm thử

### 2.1 Scenario A - Admin creates and manages events

Scenario A tập trung vào vòng đời quản trị sự kiện trên EMS: xem danh sách sự kiện, tạo/chỉnh sửa sự kiện, cấu hình đăng ký và vai trò, sau đó có thể publish, preview, approve participant/review và check-in.

### 2.2 Danh sách màn hình

| ID | Màn hình | Lý do chọn | Vai trò | URL/đường dẫn | Evidence tổng quan |
| --- | --- | --- | --- | --- | --- |
| A1 | Events list with status filters and notification dots | Đây là màn hình trung tâm để admin xem, lọc và quản lý trạng thái sự kiện. | Admin | [Điền URL] | [screenshots/A1_overview...] |
| A2 | Add/Edit Event form - image upload + Rich-Text + date/time validation | Đây là form phức tạp nhất của Pool A, có upload ảnh, rich-text và validation ngày giờ. | Admin | [Điền URL] | [screenshots/A2_overview...] |
| A3 | Registration & Roles configuration panel - Max Slots / Waitlist / additional role | Đây là phần cấu hình đăng ký có nhiều toggle, số lượng slot, waitlist và role bổ sung. | Admin | [Điền URL] | [screenshots/A3_overview...] |

> Nếu thay đổi màn hình, màn hình mới vẫn phải thuộc Pool A và cần giải thích lý do chọn.

## 3. Task 1B - Checklist execution trên Scenario A

### 3.1 Checklist sử dụng

| Nội dung | Giá trị |
| --- | --- |
| Checklist nhóm | `submission/group/gui_usability_checklist_final.md` |
| Số lượng item checklist | [Điền số, yêu cầu > 40] |
| Interface aspects | IA-01 General UI standards, IA-02 Forms, IA-03 Navigation, IA-04 Feedback/state |
| File bảng chi tiết | `submission/checklist_execution.md` |

### 3.2 Kết quả tổng hợp theo màn hình

| Màn hình | Tổng item áp dụng | Passed | Failed | N/A | Tỷ lệ pass | Nhận xét chính |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| A1 | [ ] | [ ] | [ ] | [ ] | [ ]% | [Tóm tắt lỗi/điểm tốt] |
| A2 | [ ] | [ ] | [ ] | [ ] | [ ]% | [Tóm tắt lỗi/điểm tốt] |
| A3 | [ ] | [ ] | [ ] | [ ] | [ ]% | [Tóm tắt lỗi/điểm tốt] |

### 3.3 Checklist execution results per screen

| Checklist ID | Interface Aspect | Nội dung kiểm tra | A1 Events list | A2 Add/Edit Event | A3 Registration & Roles | Notes cho item Failed | Screenshot ref |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [IA-01-xx] | IA-01 | [Copy item từ checklist nhóm] | [Passed/Failed/N/A] | [Passed/Failed/N/A] | [Passed/Failed/N/A] | [Chỉ ghi khi Failed] | [screenshots/...] |
| [IA-02-xx] | IA-02 | [Copy item từ checklist nhóm] | [Passed/Failed/N/A] | [Passed/Failed/N/A] | [Passed/Failed/N/A] | [Chỉ ghi khi Failed] | [screenshots/...] |
| [IA-03-xx] | IA-03 | [Copy item từ checklist nhóm] | [Passed/Failed/N/A] | [Passed/Failed/N/A] | [Passed/Failed/N/A] | [Chỉ ghi khi Failed] | [screenshots/...] |
| [IA-04-xx] | IA-04 | [Copy item từ checklist nhóm] | [Passed/Failed/N/A] | [Passed/Failed/N/A] | [Passed/Failed/N/A] | [Chỉ ghi khi Failed] | [screenshots/...] |

### 3.4 Bug phát hiện từ Task 1B

| Bug ID | Screen | Steps to reproduce | Expected | Actual | Severity | Screenshot ref | Google Form timestamp |
| --- | --- | --- | --- | --- | ---: | --- | --- |
| BUG-001 | [A1/A2/A3] | [Các bước tái hiện] | [Kết quả mong đợi] | [Kết quả thực tế] | [0-4] | [screenshots/...] | [YYYY-MM-DD HH:mm] |

## 4. Task 2 - User Testing with 5 Real Users

### 4.1 Goal-based task scenario

[Viết task cho người dùng theo mục tiêu, không viết từng bước click. Ví dụ cho Pool A nếu participant đóng vai admin: “Bạn cần tạo một sự kiện học thuật mới, cấu hình đăng ký phù hợp và kiểm tra lại sự kiện trong danh sách quản trị.”]

### 4.2 Thiết kế đo lường

| Metric | Cách đo |
| --- | --- |
| Task success | Completed / Partial / Failed |
| Time on task | Từ lúc participant bắt đầu đến khi kết thúc task |
| Error / hesitation count | Đếm lỗi thao tác, dừng lâu, quay lại, hỏi lại, nhập sai |
| Post-task score | SUS hoặc UEQ-S |
| Probe questions | Clarity, error recovery, speed, trust |

### 4.3 Pilot session

| Nội dung | Ghi chú |
| --- | --- |
| Người pilot | [Một người không tính vào 5 participant chính] |
| Vấn đề phát hiện | [Task wording/dữ liệu/flow] |
| Điều chỉnh trước 5 session chính | [Điền thay đổi] |

### 4.4 Participant table

| ID | Hồ sơ phù hợp | Liên hệ đã che | Ngày giờ session | Thiết bị/trình duyệt | Recording ref |
| --- | --- | --- | --- | --- | --- |
| P1 | [Sinh viên/giảng viên/event organizer...] | [Zalo/email/phone che giữa] | [ ] | [ ] | [videos/...] |
| P2 | [ ] | [ ] | [ ] | [ ] | [videos/...] |
| P3 | [ ] | [ ] | [ ] | [ ] | [videos/...] |
| P4 | [ ] | [ ] | [ ] | [ ] | [videos/...] |
| P5 | [ ] | [ ] | [ ] | [ ] | [videos/...] |

### 4.5 Metrics table

| Participant | Success | Time on task | Error count | Hesitation count | SUS/UEQ-S score | Ghi chú chính |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| P1 | [Completed/Partial/Failed] | [mm:ss] | [ ] | [ ] | [ ] | [ ] |
| P2 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| P3 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| P4 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| P5 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| **Tổng hợp** | [Success rate] | [Mean] | [Mean] | [Mean] | [Mean] | [ ] |

### 4.6 Ranked usability findings

| ID | Screen | Finding | Evidence | Severity | Screenshot ref | Recommendation |
| --- | --- | --- | --- | ---: | --- | --- |
| UX-001 | [A1/A2/A3] | [Vấn đề usability] | [Participant/metric/probe quote] | [0-4] | [screenshots/...] | [Khuyến nghị cụ thể] |

### 4.7 Prioritised recommendations

| Priority | Recommendation | Lý do | Finding liên quan |
| --- | --- | --- | --- |
| P0 | [Sửa ngay] | [Ảnh hưởng nghiêm trọng] | [UX-...] |
| P1 | [Sửa sớm] | [Ảnh hưởng vừa] | [UX-...] |
| P2 | [Cải thiện sau] | [Tối ưu trải nghiệm] | [UX-...] |

## 5. Task 3 - Cross-Browser / Cross-Platform

### 5.1 Coverage summary

| Dimension | Yêu cầu theo đề | Coverage thực tế |
| --- | --- | --- |
| Operating systems | 3 OS per screen | [Windows, macOS, Android/iOS...] |
| Browsers | 5 browsers per screen | [Chrome, Firefox, Safari, Edge, Opera/Samsung Internet...] |
| Device classes | 3 device classes per screen | [Desktop, tablet, phone] |
| Screenshot requirement | Mỗi cell có screenshot, ảnh hiển thị EMS URL, browser/OS/device, và email overlay | [Đã đủ/Chưa đủ] |

### 5.2 Compatibility matrix summary

Chi tiết đầy đủ nằm ở `submission/cross_platform_matrix.md`.

| Screen | Cells covered | Passed | Failed | OS covered | Browsers covered | Device classes covered |
| --- | ---: | ---: | ---: | --- | --- | --- |
| A1 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| A2 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| A3 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

### 5.3 Compatibility defects

| ID | Screen | Environment | Defect | Expected | Actual | Severity | Screenshot ref | Google Form timestamp |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- |
| CP-BUG-001 | [A1/A2/A3] | [OS + Browser + Device] | [Overflow/overlap/broken layout...] | [ ] | [ ] | [0-4] | [screenshots/...] | [ ] |

## 6. Bug & Usability Findings submission

| Nội dung | Giá trị |
| --- | --- |
| Google Form | https://forms.gle/CJQFQCAXcsDbXDMM9 |
| Aggregated log | `submission/bug_usability_findings_log.md` |
| Tổng Bug | [ ] |
| Tổng Usability findings | [ ] |
| Tổng Compatibility defects | [ ] |
| Đối soát form và log | [Khớp/Chưa khớp] |

## 7. AI appendix

| Artefact | File |
| --- | --- |
| AI Audit Report | `submission/ai-audit/ai_audit_report.md` |
| AI Critique 200-300 words | `submission/ai_critique.md` |

## 8. Kết luận

[Tóm tắt mức độ ổn định UI của các màn hình Pool A, rủi ro nổi bật, và 3 đề xuất ưu tiên nhất.]
