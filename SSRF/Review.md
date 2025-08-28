# Server-Side Request Forgery (SSRF) - Summary

| **Level**       | **Lab**                                             | **Kỹ thuật**                                             | **Rating** | **Status** |
|------------------|------------------------------------------------------|----------------------------------------------------------|------------|------------|
| `Apprentice`   | Basic SSRF against the local server                  | Gửi request tới `http://127.0.0.1/` (localhost)          | ★☆☆        | ✅     |
| `Apprentice`   | Basic SSRF against another back-end system           | Truy cập hệ thống nội bộ khác (vd: `http://192.168.x.x`) | ★★☆        | ✅     |
| `Practitioner` | Blind SSRF with out-of-band detection                | Sử dụng OAST (Burp Collaborator) để phát hiện            | ★★★        | ✅     |
| `Practitioner` | SSRF with blacklist-based input filter               | Bypass blacklist (`127.0.0.1` → `2130706433`, `[::1]`)   | ★★★        | ✅     |
| `Practitioner` | SSRF with filter bypass via open redirection vuln    | Dùng open redirect trung gian để vượt filter             | ★★★        | ✅     |
| `Expert`       | Blind SSRF with Shellshock exploitation              | SSRF → trigger Shellshock qua header                     | ★★★★       | ✅     |
| `Expert`       | SSRF with whitelist-based input filter               | Bypass whitelist (`@`, DNS rebinding, URL encoding)      | ★★★★       | ✅     |
