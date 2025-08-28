| **Level**       | **Lab**                                      | **Kỹ thuật**                                | **Rating** | **Status** |
|------------------|----------------------------------------------|---------------------------------------------|------------|--------------------------|
| `Apprentice`   | Accessing private GraphQL posts              | IDOR / query dữ liệu private                 | ★☆☆        | ✅ |
| `Practitioner` | Accidental exposure of private GraphQL fields| Introspection query lộ field ẩn              | ★★☆        | ✅ |
| `Practitioner` | Finding a hidden GraphQL endpoint            | Fuzzing path để tìm `/graphql` endpoint      | ★★☆        | ✅ |
| `Practitioner` | Bypassing GraphQL brute force protections    | Query batching / alias để lách rate-limit    | ★★★        | ✅ |
| `Practitioner` | Performing CSRF exploits over GraphQL        | CSRF ép victim gửi mutation                  | ★★★        | ❌ |