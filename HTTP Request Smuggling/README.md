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

## Lab: Exploiting HTTP request smuggling to reveal front-end request rewriting

### Solve

- Smuggle request để backend tiết lộ tên của **header IP** mà frontend thêm.
- Smuggle tiếp một request khác, giả IP thành 127.0.0.1 bằng header đó, để xóa user carlos.
    ![alt text](/HTTP%20Request%20Smuggling/images/image.png)

    - Thay nó bằng `X-DrRit-Ip: 127.0.0.1`
    - Gửi yêu cầu xóa người dùng `Carlos`

### PoC

- [Lab5.py](Lab5.py)

## Lab: Exploiting HTTP request smuggling to capture other users' requests


- [Lab6.py](Lab6.py)

## Lab: Exploiting HTTP request smuggling to deliver reflected XSS

### Solve

- Có một số trường bị ẩn ở api `/post/comment`

    ![alt text](/HTTP%20Request%20Smuggling/images/image-1.png)

    ![alt text](/HTTP%20Request%20Smuggling/images/image-2.png)

    - Thử payload XSS ở `userAgent`. Phần response: `"userAgent" value = "...>"` → payload sẽ là `"><script>alert(1)</script>`

### PoC

- [Lab7.py](Lab7.py)

## Lab: Response queue poisoning via H2.TE request smuggling

### Solve


- Intruder solve this lab

    ![alt text](/HTTP%20Request%20Smuggling/images/image-4.png)

    ![alt text](/HTTP%20Request%20Smuggling/images/image-3.png)

- Dán `session admin` vào, reload rồi xóa carlos

    ![alt text](/HTTP%20Request%20Smuggling/images/image-5.png)

    ![alt text](/HTTP%20Request%20Smuggling/images/image-6.png)

    ![alt text](/HTTP%20Request%20Smuggling/images/image-7.png)

## Lab: HTTP request smuggling, basic CL.TE vulnerability

- [Lab13.py](Lab13.py)

## Lab: HTTP request smuggling, basic TE.CL vulnerability

- [Lab14.py](Lab14.py)

