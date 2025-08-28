# SQL Injection - Summary

| **Level**       | **Lab**                                                                 | **Kỹ thuật**                                                     | **Rating** | **Status** |
|------------------|--------------------------------------------------------------------------|------------------------------------------------------------------|------------|------------|
| `Apprentice`   | SQL injection vulnerability in WHERE clause allowing retrieval of hidden data | Basic UNION/OR injection để lấy dữ liệu ẩn                      | ★☆☆        | ✅     |
| `Apprentice`   | SQL injection vulnerability allowing login bypass                         | `' OR '1'='1` → bypass auth                                     | ★☆☆        | ✅     |
| `Practitioner` | SQL injection attack, querying the database type and version on Oracle    | `SELECT banner FROM v$version`                                  | ★★☆        | ✅     |
| `Practitioner` | SQL injection attack, querying the database type and version on MySQL and Microsoft | `SELECT @@version` hoặc `SELECT version()`                     | ★★☆        | ✅     |
| `Practitioner` | SQL injection attack, listing the database contents on non-Oracle databases | `information_schema.tables/columns`                            | ★★★        | ✅     |
| `Practitioner` | SQL injection attack, listing the database contents on Oracle             | `all_tables`, `all_tab_columns`                                | ★★★        | ✅     |
| `Practitioner` | SQL injection UNION attack, determining the number of columns returned by the query | `ORDER BY` / `UNION NULL` test                                 | ★★☆        | ✅     |
| `Practitioner` | SQL injection UNION attack, finding a column containing text              | Inject `'abc'` để xác định cột nhận string                      | ★★☆        | ✅     |
| `Practitioner` | SQL injection UNION attack, retrieving data from other tables             | UNION SELECT từ bảng khác                                      | ★★★        | ✅     |
| `Practitioner` | SQL injection UNION attack, retrieving multiple values in a single column | `CONCAT(user, ':', pass)`                                      | ★★★        | ✅     |
| `Practitioner` | Blind SQL injection with conditional responses                            | Boolean-based (`AND '1'='1'`)                                  | ★★☆        | ✅     |
| `Practitioner` | Blind SQL injection with conditional errors                               | Error-based (`CASE WHEN … THEN to_char(1/0) END`)              | ★★☆        | ✅     |
| `Practitioner` | Visible error-based SQL injection                                         | Lỗi hiển thị trực tiếp                                          | ★★☆        | ✅     |
| `Practitioner` | Blind SQL injection with time delays                                      | Time-based (`SLEEP(5)`)                                        | ★★☆        | ✅     |
| `Practitioner` | Blind SQL injection with time delays and information retrieval            | Time-based + extract dữ liệu bit-by-bit                        | ★★★        | ✅     |
| `Practitioner` | Blind SQL injection with out-of-band interaction                          | Trigger DNS/HTTP request OAST                                  | ★★★        | ✅     |
| `Practitioner` | Blind SQL injection with out-of-band data exfiltration                    | Exfil dữ liệu qua DNS query                                    | ★★★★       | ✅     |
| `Practitioner` | SQL injection with filter bypass via XML encoding                         | Encode payload (`&#x27; OR &#x31;=&#x31;`) để bypass filter     | ★★★        | ✅     |
