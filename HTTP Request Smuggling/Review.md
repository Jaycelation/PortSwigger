# HTTP Request Smuggling - Summary

| **Level**       | **Lab**                                                                | **Kỹ thuật**                                                   | **Rating** | **Status**   |
|------------------|------------------------------------------------------------------------|----------------------------------------------------------------|------------|--------------|
| `Practitioner` | HTTP request smuggling, confirming a CL.TE vulnerability via differential responses | Xác nhận CL.TE bằng diff response                             | ★★☆        | ✅       |
| `Practitioner` | HTTP request smuggling, confirming a TE.CL vulnerability via differential responses | Xác nhận TE.CL bằng diff response                             | ★★☆        | ✅       |
| `Practitioner` | Exploiting HTTP request smuggling to bypass front-end security controls, CL.TE vulnerability | Bypass security control (CL.TE)                               | ★★★        | ✅       |
| `Practitioner` | Exploiting HTTP request smuggling to bypass front-end security controls, TE.CL vulnerability | Bypass security control (TE.CL)                               | ★★★        | ✅       |
| `Practitioner` | Exploiting HTTP request smuggling to reveal front-end request rewriting | Smuggle để phát hiện rewriting                                | ★★★        | ✅       |
| `Practitioner` | Exploiting HTTP request smuggling to capture other users' requests      | Smuggle để đánh cắp request người khác                        | ★★★        | ✅       |
| `Practitioner` | Exploiting HTTP request smuggling to deliver reflected XSS              | Smuggle → XSS                                                 | ★★★        | ✅       |
| `Practitioner` | Response queue poisoning via H2.TE request smuggling                    | HTTP/2 + TE: poisoning queue                                  | ★★★        | ✅       |
| `Practitioner` | H2.CL request smuggling                                                | HTTP/2 + CL                                                   | ★★★★       | ❌   |
| `Practitioner` | HTTP/2 request smuggling via CRLF injection                            | CRLF → HTTP/2 smuggling                                       | ★★★★       | ❌   |
| `Practitioner` | HTTP/2 request splitting via CRLF injection                            | CRLF → request splitting                                      | ★★★★       | ❌   |
| `Expert`       | 0.CL request smuggling                                                 | Rare 0.CL desync                                              | ★★★★★      | ❌   |
| `Practitioner` | CL.0 request smuggling                                                 | CL.0 desync variant                                           | ★★★★       | ❌   |
| `Practitioner` | HTTP request smuggling, basic CL.TE vulnerability                      | Basic CL.TE                                                   | ★★☆        | ✅       |
| `Practitioner` | HTTP request smuggling, basic TE.CL vulnerability                      | Basic TE.CL                                                   | ★★☆        | ✅       |
| `Practitioner` | HTTP request smuggling, obfuscating the TE header                      | TE header obfuscation                                         | ★★★★       | ❌   |
| `Expert`       | Exploiting HTTP request smuggling to perform web cache poisoning       | Smuggle + cache poisoning                                     | ★★★★★      | ❌   |
| `Expert`       | Exploiting HTTP request smuggling to perform web cache deception       | Smuggle + cache deception                                     | ★★★★★      | ❌   |
| `Expert`       | Bypassing access controls via HTTP/2 request tunnelling                | HTTP/2 tunnelling → bypass auth                               | ★★★★★      | ❌   |
| `Expert`       | Web cache poisoning via HTTP/2 request tunnelling                      | HTTP/2 tunnelling → cache poisoning                           | ★★★★★      | ❌   |
| `Expert`       | Client-side desync                                                    | Desync trên client                                            | ★★★★★      | ❌   |
| `Expert`       | Server-side pause-based request smuggling                             | Delay/pause-based desync                                      | ★★★★★      | ❌   |
