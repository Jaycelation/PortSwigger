# JWT Vulnerabilities - Summary

| **Level**       | **Lab**                                                   | **Kỹ thuật**                                                       | **Rating** | **Status**   |
|------------------|------------------------------------------------------------|----------------------------------------------------------------------|------------|--------------|
| `Apprentice`   | JWT authentication bypass via unverified signature         | JWT với `alg:none` hoặc bỏ qua verify chữ ký                         | ★☆☆        | ✅       |
| `Apprentice`   | JWT authentication bypass via flawed signature verification| Lỗi verify (chấp nhận token signed với public key / khác thuật toán) | ★★☆        | ✅       |
| `Practitioner` | JWT authentication bypass via weak signing key             | Brute-force/guess key yếu (vd: `secret`)                             | ★★☆        | ✅       |
| `Practitioner` | JWT authentication bypass via jwk header injection         | Chèn `jwk` trong header để ép server dùng key attacker cung cấp      | ★★★        | ✅       |
| `Practitioner` | JWT authentication bypass via jku header injection         | Chèn `jku` → server fetch key từ URL attacker                        | ★★★        | ✅       |
| `Practitioner` | JWT authentication bypass via kid header path traversal    | `kid` traversal → load file local làm key                            | ★★★        | ✅       |
| `Expert`       | JWT authentication bypass via algorithm confusion          | `alg=RSA` ↔ `HMAC` confusion → attacker forge token                  | ★★★★       | ✅       |
| `Expert`       | JWT authentication bypass via algorithm confusion with no exposed key | Tương tự nhưng không có key lộ → khó hơn nhiều                      | ★★★★★      | ❌   |
