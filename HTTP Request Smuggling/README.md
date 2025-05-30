## Lab: HTTP request smuggling, confirming a CL.TE vulnerability via differential responses

### CL.TE

- **Frontend** dùng `Content-Length` để xác định độ dài body → nó sẽ dừng ở đúng số byte trong `Content-Length`.
- **Backend** thấy `Transfer-Encoding: chunked` → nó đọc body theo định dạng chunked.
- Điều này tạo điều kiện để frontend **kết thúc request sớm**, còn backend thì **tiếp tục đọc** và xử lý phần “smuggled request”.

### PoC

- [Lab1.py](Lab1.py)

## Lab: HTTP request smuggling, confirming a TE.CL vulnerability via differential responses

### TE.CL

- **Frontend** (proxy) thấy header `Transfer-Encoding: chunked` → xử lý body theo chunked encoding.

- **Backend** lại thấy header `Content-Length` → đọc body theo content-length.

- Vì thế, frontend có thể đọc sai hoặc dừng đọc request sớm hơn, còn backend đọc thêm dữ liệu sau đó.

- Điều này tạo ra vùng **request smuggling** — phần dữ liệu tiếp theo được backend hiểu là request mới, trong khi frontend nghĩ request đã kết thúc.

### PoC

- [Lab2.py](Lab2.py)

## Lab: Exploiting HTTP request smuggling to bypass front-end security controls, CL.TE vulnerability

### PoC 

- [Lab3.py](Lab3.py)

## Lab: Exploiting HTTP request smuggling to bypass front-end security controls, TE.CL vulnerability

### PoC

- [Lab4.py](Lab4.py)