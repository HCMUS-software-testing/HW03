# Task 2 - Bảng Điểm SUS

## 1. Thang Điểm SUS

Người tham gia trả lời mỗi câu từ `1` đến `5`.

| Điểm | Ý nghĩa |
| ---: | --- |
| 1 | Rất không đồng ý |
| 2 | Không đồng ý |
| 3 | Trung lập |
| 4 | Đồng ý |
| 5 | Rất đồng ý |

## 2. Câu Hỏi SUS Đã Dùng

| ID | Statement |
| --- | --- |
| SUS-01 | Tôi nghĩ tôi muốn sử dụng hệ thống này thường xuyên nếu có nhu cầu gửi hoặc theo dõi yêu cầu hỗ trợ. |
| SUS-02 | Tôi thấy hệ thống này phức tạp không cần thiết. |
| SUS-03 | Tôi thấy hệ thống này dễ sử dụng. |
| SUS-04 | Tôi nghĩ tôi cần người có kỹ thuật hỗ trợ thì mới dùng được hệ thống này. |
| SUS-05 | Tôi thấy các chức năng trong flow support request được liên kết với nhau hợp lý. |
| SUS-06 | Tôi thấy hệ thống có quá nhiều điểm không nhất quán. |
| SUS-07 | Tôi nghĩ hầu hết mọi người có thể học cách dùng flow này rất nhanh. |
| SUS-08 | Tôi thấy hệ thống này rườm rà hoặc bất tiện khi sử dụng. |
| SUS-09 | Tôi cảm thấy tự tin khi sử dụng flow support request này. |
| SUS-10 | Tôi cần học thêm nhiều thứ trước khi có thể sử dụng flow này thành thạo. |

## 3. Cách Tính

- Với câu lẻ `SUS-01`, `SUS-03`, `SUS-05`, `SUS-07`, `SUS-09`: contribution = score - 1.
- Với câu chẵn `SUS-02`, `SUS-04`, `SUS-06`, `SUS-08`, `SUS-10`: contribution = 5 - score.
- SUS score = tổng contribution x `2.5`, trên thang `0-100`.

## 4. Raw Score Table

| Participant | SUS-01 | SUS-02 | SUS-03 | SUS-04 | SUS-05 | SUS-06 | SUS-07 | SUS-08 | SUS-09 | SUS-10 | SUS score |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| P01 | 5 | 2 | 4 | 2 | 5 | 2 | 4 | 1 | 4 | 2 | 82.5 |
| P02 | 4 | 2 | 4 | 2 | 5 | 1 | 4 | 1 | 4 | 1 | 85.0 |
| P03 | 4 | 2 | 4 | 1 | 3 | 3 | 4 | 2 | 4 | 1 | 75.0 |
| P04 | 5 | 2 | 4 | 1 | 3 | 2 | 4 | 1 | 4 | 1 | 82.5 |
| P05 | 3 | 2 | 3 | 2 | 4 | 5 | 2 | 3 | 4 | 2 | 50.0 |
| **Mean** | 4.2 | 2.0 | 3.8 | 1.6 | 4.0 | 2.6 | 3.6 | 1.6 | 4.0 | 1.4 | 75.0 |

## 5. Diễn Giải

| Range | Diễn giải tham khảo |
| --- | --- |
| `< 50` | Usability yếu, cần ưu tiên sửa các điểm cản trở lớn. |
| `50-68` | Dưới trung bình hoặc trung bình thấp, cần cải thiện rõ. |
| `68-80` | Chấp nhận được nhưng vẫn có điểm vướng. |
| `> 80` | Trải nghiệm tốt, chủ yếu còn cải tiến nhỏ hoặc theo ngữ cảnh. |

SUS trung bình của 5 phiên là `75.0`, nằm trong vùng chấp nhận được nhưng chưa thật sự mạnh. Điểm thấp nhất là P05 với `50.0`, chủ yếu do participant cảm nhận sự thiếu nhất quán giữa giao diện user/admin và nhầm lẫn ở navigation admin.
