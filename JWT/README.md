## JWT Expert Lab

### Lab 01: JWT authentication bypass via algorithm confusion

- Login, thử vào `/admin`

    ![alt text](/JWT/images/image.png)

    - Xem với `JWT Web Token`

    ![alt text](/JWT/images/image-1.png)

    - Thuật toán là `RS256`. Bài này tập trung khai thác trên lỗi logic về cách thống nhất thuật toán, với logic code kiểu như này

    ![alt text](/JWT/images/image-2.png)


    - Thử fuzzing ở [đây](/JWT/jwt_fuzzing.txt) thì thấy thành công lấy keys ở payload `/.well-known/jwks.json`

    ![alt text](/JWT/images/image-3.png)

    ![alt text](/JWT/images/image-4.png)

- Sử dụng công cụ 

    - Tạo `RSA Key` với key lấy được

    ![alt text](/JWT/images/image-5.png)

    - Chọn `Encode as` -> `Base64`

    ![alt text](/JWT/images/image-6.png)

    - Tạo `Symmetric Key` random, copy key được encode vào

    ![alt text](/JWT/images/image-7.png)

    - Trở lại với `Repeater`, thay đổi thuật toán `alg:HS256` và `sub:administrator`, chọn `sign` rồi sử dụng `Sign Key` đã ký trước đó

    ![alt text](/JWT/images/image-8.png)


    - Chọn `Attack`, thành công lấy được `admin pannel`

    ![alt text](/JWT/images/image-9.png)

    - Thay lại endpoint thành `/admin/delete?username=carlos` là solve được bài này

    ![alt text](/JWT/images/image-10.png)

    ![alt text](/JWT/images/image-11.png)