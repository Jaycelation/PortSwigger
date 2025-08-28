# NoSQL Injection - Summary

| **Level**       | **Lab**                                                      | **Kỹ thuật**                                          | **Rating** | **Status** |
|------------------|---------------------------------------------------------------|-------------------------------------------------------|------------|------------|
| `Apprentice`   | Detecting NoSQL injection                                     | Phát hiện lỗi NoSQLi bằng payload test (`'`, `{}`, …) | ★☆☆        | ✅     |
| `Apprentice`   | Exploiting NoSQL operator injection to bypass authentication  | Sử dụng toán tử `$ne`, `$gt`, … để bypass login       | ★★☆        | ✅     |
| `Practitioner` | Exploiting NoSQL injection to extract data                    | Dùng injection để dump dữ liệu (error/boolean based)  | ★★★        | ✅     |
| `Practitioner` | Exploiting NoSQL operator injection to extract unknown fields | Sử dụng `$regex`, `$where` để suy đoán field ẩn       | ★★★        | ✅     |
