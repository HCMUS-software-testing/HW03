# AI-First Strategy: Playwright MCP + BrowserStack for HW03

Tài liệu này trả lời câu hỏi: có thể dùng MCP Playwright và BrowserStack để hoàn thành HW03 theo chiến thuật AI-first không?

Câu trả lời ngắn: có, và khá hợp với đề. Nhưng không nên hiểu là giao hết bài cho AI. Chiến thuật đúng là dùng AI để điều khiển trình duyệt, gợi ý quan sát, tạo bảng, soát bằng chứng và giảm thao tác lặp; còn sinh viên vẫn phải chọn scenario, kiểm chứng kết quả, chụp bằng chứng thật, chạy user testing với người thật, submit form và viết verdict trong AI Audit Report.

## 1. Vai trò của từng công cụ

| Công cụ | Dùng cho phần nào của HW03 | Giá trị chính | Không thay thế được |
| --- | --- | --- | --- |
| Playwright MCP | Task 1B, hỗ trợ Task 2, chuẩn bị Task 3 | AI thao tác EMS, đọc DOM/accessibility tree, chụp screenshot, ghi lại step/finding có cấu trúc | Nhận định cuối của sinh viên, user testing với 5 người thật |
| BrowserStack Live | Task 3 | Chạy EMS trên OS/browser/device thật hoặc cloud, lấy ảnh evidence có browser/OS/device | Checklist execution nội dung sâu nếu chỉ thao tác thủ công |
| BrowserStack MCP | Task 3, bug triage, session management | Cho AI mở BrowserStack session, quản lý workflow test bằng natural language trong IDE hỗ trợ MCP | Tài khoản BrowserStack, kiểm tra thủ công ảnh evidence |
| BrowserStack Automate + Playwright | Task 3 nâng cao, demo skill | Chạy lại các smoke steps trên nhiều browser/device, có video/log/session link | Đánh giá usability định tính và screenshot overlay theo yêu cầu bài |

Nguồn chính thức: BrowserStack MCP kết nối AI agent với BrowserStack testing infrastructure; BrowserStack Playwright Automate hỗ trợ chạy test trên nhiều browser và mobile devices; Playwright MCP cho phép LLM tương tác web page bằng structured accessibility snapshots.

## 2. Chiến thuật khuyến nghị

Nên dùng mô hình hai lớp:

1. Local exploratory layer: dùng Playwright MCP để AI đăng nhập EMS, đi qua các màn hình thuộc scenario, chạy checklist, đề xuất finding và chụp screenshot ban đầu.
2. Cross-platform evidence layer: dùng BrowserStack Live hoặc BrowserStack MCP/Automate để mở cùng màn hình trên matrix OS/browser/device, chụp ảnh thật có URL, device identity và overlay email `MSSV@....edu.vn`.

Lý do: đề bài cần bằng chứng thật trên EMS và real cross-platform captures. Playwright MCP rất tốt để điều hướng và ghi nhận vấn đề nhanh, nhưng ảnh desktop local không đủ cho Task 3. BrowserStack xử lý phần cloud device/browser, còn AI giúp bạn điều phối và chuẩn hóa báo cáo.

## 3. Phạm vi nên tự động hóa

| Hạng mục | Mức tự động hóa nên dùng | Cách làm |
| --- | --- | --- |
| Tạo shared checklist | AI draft + human review | Dùng checklist hiện có trong `submission/group/gui_usability_checklist_final.md`, bổ sung prompt và ghi lý do AI missed items. |
| Chạy checklist từng màn hình | AI-assisted, không fully automated | Playwright MCP mở màn hình, đọc UI, chụp ảnh, đề xuất Pass/Fail; sinh viên xác nhận từng Fail. |
| User testing | Không tự động hóa người dùng | AI chỉ tạo protocol, form ghi chú, SUS/UEQ-S table và phân tích raw notes. |
| Cross-platform matrix | AI-assisted + BrowserStack evidence | AI sinh matrix tối thiểu 5-7 cells/screen; BrowserStack tạo session và screenshot thật. |
| Bug log + Google Form | AI chuẩn hóa nội dung, sinh viên submit | AI viết expected/actual/severity/fix; sinh viên kiểm tra rồi submit form. |
| AI Audit Report | Tự động hóa bằng skill/script | Mỗi session prompt lớn cần append vào `submission/ai-audit/ai_audit_report.md`. |

## 4. Setup đề xuất

### 4.1. Playwright MCP

Nếu dùng Codex CLI, cấu hình Playwright MCP theo hướng dẫn Microsoft:

```toml
[mcp_servers.playwright]
command = "npx"
args = ["@playwright/mcp@latest"]
```

Hoặc dùng lệnh:

```bash
codex mcp add playwright npx "@playwright/mcp@latest"
```

Yêu cầu chính: Node.js 18+ và một MCP client hỗ trợ tool server. Khi dùng, ưu tiên prompt theo nhiệm vụ nhỏ: mở URL, đăng nhập, đi đến màn hình, chụp screenshot, ghi finding.

### 4.2. BrowserStack MCP

BrowserStack MCP cần BrowserStack account, `Username`, `Access Key`, AI-enabled client và Node.js 22+ theo tài liệu BrowserStack. Không commit credential vào repo. Nếu cấu hình project-specific cho VS Code/Cursor, dùng biến môi trường hoặc file MCP local nằm ngoài submission.

Ví dụ cấu hình dạng project-specific:

```json
{
  "mcpServers": {
    "browserstack": {
      "command": "npx",
      "args": ["-y", "@browserstack/mcp-server@latest"],
      "env": {
        "BROWSERSTACK_USERNAME": "YOUR_USERNAME",
        "BROWSERSTACK_ACCESS_KEY": "YOUR_ACCESS_KEY"
      }
    }
  }
}
```

Không đưa file chứa key vào ZIP nộp bài. Trong report chỉ ghi tool đã dùng, session link, browser/device và ảnh evidence.

### 4.3. BrowserStack Automate with Playwright

Dùng Automate khi bạn muốn chạy lại cùng một smoke flow trên nhiều browser/device. Các capability quan trọng:

| Capability | Ý nghĩa |
| --- | --- |
| `os`, `os_version` | Chọn desktop OS như Windows/macOS. |
| `browser`, `browser_version` | Chọn browser như Chrome, Edge, Firefox, Safari/WebKit tùy hỗ trợ. |
| `device`, `realMobile` | Chọn mobile/tablet device khi chạy mobile. |
| `browserstack.local` | Bật Local Testing nếu site không public. EMS hiện là ngrok public URL, thường không cần bật. |
| `browserstack.debug` | Tự động capture visual logs để debug. |
| `browserstack.video` | Lưu video session, hữu ích cho bằng chứng phụ. |
| `browserstack.console`, `browserstack.networkLogs` | Thu log console/network khi phân tích lỗi. |

EMS đang có URL public qua ngrok, nên BrowserStack cloud thường truy cập trực tiếp được. Nếu ngrok chặn, hết hạn hoặc yêu cầu local/private access, dùng BrowserStack Local Testing.

## 5. Quy trình làm bài AI-first

### Bước 1: Chọn scenario và màn hình

Tạo file screen list cho scenario cá nhân:

```markdown
| Screen ID | Screen name | Role | URL/Navigation path | Why selected |
| --- | --- | --- | --- | --- |
| B1 | Home / events listing | User | Home page | Covers carousel, search, category browsing |
| B2 | Event detail | User | Home -> event card -> detail | Covers event information and register CTA |
| B3 | Registration form | User | Event detail -> Register | Covers form validation and role selection |
```

Prompt AI:

```text
Read the HW03 EMS requirements and my selected scenario/screens. Check whether the selected screens satisfy the assignment scope. Do not invent screens. Return risks and missing evidence only.
```

### Bước 2: Chạy checklist bằng Playwright MCP

Với mỗi màn hình:

1. Mở EMS bằng Playwright MCP.
2. Đăng nhập đúng role.
3. Điều hướng đến màn hình cần test.
4. Chụp screenshot tổng quan.
5. Chạy từng checklist item liên quan.
6. Ghi `Pass`, `Fail`, hoặc `N/A`.
7. Với mỗi `Fail`, chụp screenshot riêng và tạo finding.

Prompt AI nên dùng:

```text
Use Playwright MCP to inspect EMS screen <SCREEN_ID>. Apply the shared GUI checklist from submission/group/gui_usability_checklist_final.md. For each item, propose Pass/Fail/N/A with observable evidence from the current UI. Do not finalize failed items without a screenshot reference. Return a Markdown execution table.
```

Quy tắc human review: nếu AI đánh `Fail` chỉ vì suy luận từ DOM nhưng ảnh không chứng minh được, hạ xuống `Needs review` và tự kiểm tra lại.

### Bước 3: Chuẩn hóa finding

Mỗi finding từ checklist phải có format đủ để copy vào report và Google Form:

```markdown
| Field | Content |
| --- | --- |
| ID | F-001 |
| Scenario/Screen | B2 Event detail |
| Type | Usability |
| Steps/Heuristic | IA-04-06: event status should be clear by text and badge |
| Expected | The registration status is visible near the primary register action. |
| Actual | The status is only visible below the fold on phone viewport. |
| Severity | 3 |
| Suggested fix | Move status badge near the register button and keep text visible on mobile. |
| Screenshot | submission/screenshots/checklist-failures/F-001.png |
| Form timestamp | 2026-..-.. ..:.. |
```

### Bước 4: Thiết kế user testing

Không dùng AI giả lập participant. AI chỉ giúp viết protocol và phân tích raw notes.

Prompt AI:

```text
Create a moderated think-aloud user testing protocol for Scenario <A/B/C/D> using my selected screens. The task must be goal-based, not click-by-click. Include success criteria, time-on-task, error/hesitation count, SUS or UEQ-S collection, probe questions, and a note template. Keep it suitable for 5 real participants outside the class.
```

Sau khi chạy 5 người thật, đưa raw notes cho AI:

```text
Analyze these five real user testing notes. Group repeated usability issues, calculate success rate/mean time/error counts from the table, rank findings by severity 0-4, and propose concrete fixes. Do not create participant data that is not present.
```

### Bước 5: Lập cross-platform matrix

Mỗi màn hình cần phủ đủ 3 OS, 5 browsers và 3 device classes. Matrix tối thiểu khuyến nghị:

| Cell | OS | Browser | Device class | BrowserStack mode |
| --- | --- | --- | --- | --- |
| CP-01 | Windows 11 | Chrome | Desktop | Live or Automate |
| CP-02 | Windows 11 | Edge | Desktop | Live or Automate |
| CP-03 | macOS | Safari | Desktop | Live |
| CP-04 | Android | Chrome | Phone | Live |
| CP-05 | Android | Firefox | Phone | Live |
| CP-06 | iOS | Safari | Phone | Live |
| CP-07 | iPadOS or Android | Opera/Samsung Internet | Tablet | Live |

Nếu trial BrowserStack không có một browser cụ thể, thay bằng browser khác được đề cho phép hoặc ghi rõ limitation trong report. Safari nên chạy trên macOS/iOS để evidence hợp lệ.

### Bước 6: Chụp screenshot evidence trên BrowserStack

Mỗi screenshot Task 3 phải có:

1. EMS URL đang hiển thị.
2. Browser/OS/device identity từ BrowserStack.
3. Overlay email `MSSV@....edu.vn`.
4. Màn hình đúng với screen ID.

Tên file gợi ý:

```text
submission/cross-platform/screenshots/<screen-id>_<cell-id>_<os>_<browser>_<device>.png
```

Ví dụ:

```text
submission/cross-platform/screenshots/B2_CP-04_android_chrome_pixel-8.png
```

Nếu BrowserStack không cho overlay trực tiếp, thêm overlay bằng công cụ annotation sau khi chụp, nhưng không che URL, device info hoặc lỗi UI.

### Bước 7: Viết report và AI audit

Trong `main_report.md`, tách rõ phần AI hỗ trợ và phần sinh viên xác nhận:

```markdown
AI-assisted workflow:
- Playwright MCP was used to navigate EMS screens and draft checklist execution notes.
- BrowserStack was used to capture real cross-platform screenshots.
- The student reviewed all Pass/Fail decisions, submitted findings manually, and verified screenshot evidence.
```

Mỗi prompt quan trọng cần ghi vào `submission/ai-audit/ai_audit_report.md`. Với output là file liên tục, dùng script audit với `--output-file`. Với output rời rạc, dùng summary ngắn.

## 6. Rủi ro và cách tránh mất điểm

| Rủi ro | Cách xử lý |
| --- | --- |
| AI tự bịa finding hoặc participant | Chỉ giữ finding có screenshot hoặc raw note thật. Participant phải là người thật ngoài lớp. |
| Screenshot không đủ overlay email/URL/device | Kiểm tra ảnh ngay sau khi chụp; nếu thiếu, chụp lại. |
| BrowserStack session không mở được ngrok URL | Test URL trong BrowserStack Live trước; nếu fail, thử refresh ngrok, đổi browser, hoặc dùng Local Testing nếu có private/local issue. |
| Checklist quá generic | Bám EMS widgets: upload ảnh, rich text, waitlist, QR ticket, support image lightbox, role/admin permission. |
| Matrix không phủ đủ dimension | Với mỗi screen, tick đủ 3 OS, 5 browsers, 3 device classes trước khi chuyển screen khác. |
| AI Audit thiếu prompt | Append audit ngay sau mỗi phiên AI lớn; không đợi cuối bài mới nhớ lại. |

## 7. Kết luận thực dụng

Dùng MCP Playwright + BrowserStack là chiến thuật tốt cho HW03 vì nó khớp với tinh thần AI-first và yêu cầu cross-platform. Cấu hình tối ưu là:

1. Playwright MCP cho exploratory GUI execution.
2. BrowserStack Live/MCP cho cross-platform evidence.
3. BrowserStack Automate + Playwright nếu muốn tạo smoke scripts lặp lại.
4. Human review bắt buộc trước mọi Pass/Fail, bug severity, Google Form submission và AI Audit verdict.

## 8. Nguồn tham khảo

- HW03 brief: `docs/2026.HW03.GUI Usability EMS_En.md`
- EMS intro: `docs/HW03_EMS_Intro_EN.md`
- Microsoft Playwright MCP: https://github.com/microsoft/playwright-mcp
- BrowserStack MCP overview: https://www.browserstack.com/docs/browserstack-mcp-server/overview
- BrowserStack MCP setup: https://www.browserstack.com/docs/browserstack-mcp-server/get-started
- BrowserStack local MCP setup: https://www.browserstack.com/docs/browserstack-mcp-server/get-started/local-mcp
- BrowserStack Automate with Playwright: https://www.browserstack.com/docs/automate/playwright
- BrowserStack Playwright Local Testing: https://www.browserstack.com/docs/automate/playwright/local-testing
