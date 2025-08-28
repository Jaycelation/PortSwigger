# OS Command Injection - Summary

| **Level**       | **Lab**                                                   | **Kỹ thuật**                                      | **Rating** | **Status** |
|------------------|------------------------------------------------------------|---------------------------------------------------|------------|------------|
| `Apprentice`   | OS command injection, simple case                          | Truyền payload trực tiếp (`; id`, `&& whoami`)    | ★☆☆        | ✅     |
| `Practitioner` | Blind OS command injection with time delays                | Dùng `ping`, `sleep` để đo thời gian phản hồi     | ★★☆        | ✅     |
| `Practitioner` | Blind OS command injection with output redirection         | Ghi output ra file webroot để đọc kết quả         | ★★★        | ✅     |
| `Practitioner` | Blind OS command injection with out-of-band interaction    | Kích hoạt DNS/HTTP request ra ngoài (OAST)        | ★★★        | ✅     |
| `Practitioner` | Blind OS command injection with out-of-band data exfiltration | Dùng DNS exfil để rò dữ liệu nhạy cảm            | ★★★★       | ✅     |
