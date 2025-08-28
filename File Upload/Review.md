| **Level**       | **Lab**                                              | **Kỹ thuật**                                            | **Rating** | **Status** |
| --------------- | ---------------------------------------------------- | ------------------------------------------------------- | ---------- | ---------- |
| `Apprentice`   | Remote code execution via web shell upload           | Upload thẳng webshell (không filter)                    | ★☆☆        | ✅     |
| `Apprentice`   | Web shell upload via Content-Type restriction bypass | Giả mạo header `Content-Type`                           | ★☆☆        | ✅     |
| `Practitioner` | Web shell upload via path traversal                  | Dùng `../` ghi file ra webroot                          | ★★☆        | ✅     |
| `Practitioner` | Web shell upload via extension blacklist bypass      | Extension thay thế (`.phtml`, `.php5`, `.phar`)         | ★★☆        | ✅     |
| `Practitioner` | Web shell upload via obfuscated file extension       | Obfuscation (`.php.`, `.pHp`, `%00`)                    | ★★☆        | ✅     |
| `Practitioner` | Remote code execution via polyglot web shell upload  | Polyglot file (ảnh + PHP code)                          | ★★★        | ✅     |
| `Expert`       | Web shell upload via race condition                  | Race condition: truy cập file trước khi sanitize/rename | ★★★★       | ❌ |
