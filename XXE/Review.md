# XML External Entity (XXE) Injection - Summary

| **Level**       | **Lab**                                                               | **Kỹ thuật**                                                     | **Rating** | **Status** |
|------------------|------------------------------------------------------------------------|------------------------------------------------------------------|------------|------------|
| `Apprentice`   | Exploiting XXE using external entities to retrieve files              | Khai thác `<!ENTITY>` để đọc file local (`/etc/passwd`)          | ★☆☆        | ✅     |
| `Apprentice`   | Exploiting XXE to perform SSRF attacks                                | Dùng XXE gửi request SSRF tới internal service                   | ★★☆        | ✅     |
| `Practitioner` | Blind XXE with out-of-band interaction                                | Sử dụng OAST (Collaborator) để phát hiện                         | ★★★        | ✅     |
| `Practitioner` | Blind XXE with out-of-band interaction via XML parameter entities     | Dùng parameter entity + OAST                                     | ★★★        | ✅     |
| `Practitioner` | Exploiting blind XXE to exfiltrate data using a malicious external DTD| External DTD server attacker → exfil data                        | ★★★★       | ✅     |
| `Practitioner` | Exploiting blind XXE to retrieve data via error messages              | Trigger error message chứa dữ liệu                               | ★★★        | ✅     |
| `Practitioner` | Exploiting XInclude to retrieve files                                 | Dùng `XInclude` injection để đọc file                            | ★★★        | ✅     |
| `Practitioner` | Exploiting XXE via image file upload                                  | Embed payload XXE trong file image upload                        | ★★★        | ✅     |
| `Expert`       | Exploiting XXE to retrieve data by repurposing a local DTD            | Tái sử dụng DTD hệ thống để đọc dữ liệu nhạy cảm                 | ★★★★       | ✅     |
