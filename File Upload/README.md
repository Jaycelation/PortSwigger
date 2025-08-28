## Lỗ hổng File Upload
- Lỗ hổng **File Upload** xảy ra khi máy chủ web cho phép tải tệp lên mà không xác thực đầy đủ thông tin (tên, loại, nội dung, kích thước ...). Điều này có thể dẫn đến tải lên tệp nguy hiểm, bao gồm tập lệnh cho phép thực thi mã từ xa `(RCE)`. Tấn công có thể gây thiệt hại ngay khi tải tệp lên hoặc thông qua yêu cầu HTTP kích hoạt thực thi tệp.

## Tác động to lớn của lỗ hổng File Upload

- Lỗ hổng **File Upload** có thể gây ra hậu quả nghiêm trọng, phụ thuộc vào hai yếu tố chính:
    - `Trang web không xác thực`: Sau khi tải tệp lên, nếu trang web không xác thực đúng kích thước, loại, hoặc nội dung của tệp, các tệp độc hại có thể vượt qua kiểm tra.
    - `Hạn chế sau khi tải lên`: Sau khi tệp được tải lên, nếu máy chủ không áp dụng các biện pháp kiểm soát nghiêm ngặt, tệp đó có thể bị thực thi hoặc truy cập sai mục đích.
- Trong kịch bản xấu nhất, nếu tệp không được xác thực đúng và cấu hình máy chủ cho phép thực thi các tệp như `.php`, `.jsp`, kẻ tấn công có thể tải lên tệp mã độc. Tệp này có thể hoạt động như một `web shell`, giúp kẻ tấn công kiểm soát hoàn toàn máy chủ, dẫn đến rò rỉ dữ liệu, truy cập trái phép hoặc chiếm quyền điều khiển máy chủ.

- Nếu tên tệp không được xác thực đúng cách, kẻ tấn công có thể ghi đè các tệp quan trọng bằng cách tải lên một tệp có cùng tên. Nếu máy chủ cũng tồn tại lỗ hổng `directory traversal`, kẻ tấn công thậm chí có thể tải tệp lên các vị trí ngoài ý muốn, làm tăng mức độ nghiêm trọng của cuộc tấn công.

- Ngoài ra, nếu không giới hạn kích thước tệp hợp lý, kẻ tấn công có thể thực hiện tấn công từ chối dịch vụ `(DoS)` bằng cách tải lên các tệp có kích thước cực lớn, làm đầy dung lượng ổ đĩa và gây gián đoạn hoặc làm sập máy chủ.

## Cách máy chủ web xử lý yêu cầu với tệp tin

- Cách xử lý truyền thống: Trước đây, các trang web chủ yếu là tĩnh, mỗi đường dẫn yêu cầu tương ứng trực tiếp với hệ thống thư mục và tệp trên máy chủ.

- Cách xử lý hiện đại: Dù ngày nay các trang web ngày càng động, máy chủ vẫn cần xử lý một số tệp tĩnh như hình ảnh, stylesheet, v.v.

- Quy trình xử lý:
    - Phân tích đường dẫn: Máy chủ xác định phần mở rộng tệp từ đường dẫn và ánh xạ nó với loại tệp `(MIME type)`.
    - Xử lý theo loại tệp:
        - Tệp không thực thi: Tệp như hình ảnh hoặc HTML tĩnh được gửi nguyên bản đến client.
        - Tệp thực thi (PHP, JSP):
            - Nếu máy chủ được cấu hình thực thi, nó sẽ chạy tệp và gửi kết quả về client.
            - Nếu không được cấu hình thực thi, có thể trả về lỗi hoặc hiển thị nội dung tệp dưới dạng văn bản thuần (dẫn đến nguy cơ lộ mã nguồn).
- Nguy cơ từ cấu hình sai: Nếu máy chủ không được cấu hình đúng, tệp thực thi có thể bị lộ mã nguồn hoặc thông tin nhạy cảm, tạo cơ hội cho kẻ tấn công khai thác.

## Các dạng File Upload

### Exploiting unrestricted file uploads to deploy a web shell

- `Web shell` là một script độc hại cho phép kẻ tấn công thực thi các lệnh tùy ý trên một máy chủ web từ xa chỉ bằng cách gửi yêu cầu HTTP tới đúng endpoint.
- Nếu bạn có thể tải lên thành công `web shell` 
điều này có nghĩa là bạn có thể đọc và ghi các tệp tùy ý, lấy cắp dữ liệu nhạy cảm, thậm chí sử dụng máy chủ này để thực hiện các cuộc tấn công vào cơ sở hạ tầng nội bộ hoặc các máy chủ bên ngoài mạng. Ví dụ, đoạn mã `PHP` sau có thể được sử dụng để đọc các tệp tùy ý từ hệ thống tệp của máy chủ:
    ```php
    <?php echo File_Upload('/path/to/target/file'); ?>
    ```
    Hay chỉ đơn giản hơn là cho phép truyền lệnh hệ thống tùy ý qua tham số truy vấn `GET`:
    ```php
    <?php echo system($_GET['cmd']); ?>
    ```

#### Lab: Remote code execution via web shell upload

- Yêu cầu: tải lên một web shell PHP cơ bản và sử dụng nó để trích xuất nội dung của tệp `/home/carlos/secret`.
- Tài khoản cung cấp `wiener:peter`

- Trang web của bài lab:
    ![alt text](/File%20Upload/Image/image-1.png)

- Sau khi login, nhận thấy trang web cho phép upload lên 1 file để cập nhật ảnh đại diện:
    ![alt text](/File%20Upload/Image/image-2.png)
- Trên Burp, thử upload 1 file bất kỳ, endpoint cho phép làm điều này là `/my-account/avatar`
    ![alt text](/File%20Upload/Image/image-3.png)
- Thông báo phản hồi rằng đã cập nhật ảnh đại diện thành công, cùng với đó là hình ảnh đã được thay đổi
    ![alt text](/File%20Upload/Image/image-4.png)
    ![alt text](/File%20Upload/Image/image-5.png)

- Thử thay thế nó bằng 1 file [RCE](/RCE.php) được viết bằng mã `php`:
    ```php
    <?php echo system($_GET['cmd']); ?>
    ```
    ![alt text](/File%20Upload/Image/image-6.png)
- File vừa upload thành công
    ![alt text](/File%20Upload/Image/image-7.png)
- Thử up tiếp 1 file với nội dung:
    ```php
    <?php echo file_get_contents('/home/carlos/secret'); ?>
    ```
    - Hàm `file_get_contents` cho phép đọc nội dung của file tại địa chỉ `/home/carlos/secret`
- Sau khi upload, nội dung của file đã được đọc
    ![alt text](/File%20Upload/Image/image-8.png)
    `nmkjgM6OQiKk9gNYBVFJ2Hi2zWPuWXt7`

- Submit nội dung là đã hoàn thành lab này
    ![alt text](/File%20Upload/Image/image-9.png)

### Exploiting flawed validation of file uploads

- Trong thực tế, ít có website nào không có biện pháp bảo vệ chống lại các cuộc tấn công tải lên tệp như trong bài lab trước. Tuy nhiên, mặc dù có các biện pháp phòng ngừa, điều đó không có nghĩa là chúng luôn vững chắc. Bạn vẫn có thể khai thác những lỗ hổng trong các cơ chế này để chiếm quyền điều khiển từ xa `(web shell)`.

- Xác thực loại tệp bị lỗi
Khi gửi các biểu mẫu HTML, trình duyệt thường gửi dữ liệu qua yêu cầu `POST` với loại nội dung `application/x-www-form-url-encoded`. Điều này phù hợp khi gửi các thông tin văn bản đơn giản như tên hoặc địa chỉ. Tuy nhiên, nó không phù hợp khi gửi một lượng lớn dữ liệu nhị phân, chẳng hạn như một tệp hình ảnh hoặc tài liệu PDF. Trong trường hợp này, loại nội dung `multipart/form-data` được ưa chuộng.

- Tiếp tục với xác thực loại tệp bị lỗi: Cân nhắc một biểu mẫu có các trường tải lên hình ảnh, mô tả và tên người dùng. Khi gửi biểu mẫu này, yêu cầu có thể trông như sau:

    ```bash
        POST /images HTTP/1.1
        Host: normal-website.com
        Content-Length: 12345
        Content-Type: multipart/form-data; boundary=---------------------------012345678901234567890123456

        ---------------------------012345678901234567890123456
        Content-Disposition: form-data; name="image"; filename="example.jpg"
        Content-Type: image/jpeg

        [...binary content of example.jpg...]

        ---------------------------012345678901234567890123456
        Content-Disposition: form-data; name="description"

        This is an interesting description of my image.

        ---------------------------012345678901234567890123456
        Content-Disposition: form-data; name="username"

        wiener
        ---------------------------012345678901234567890123456--
    ```
- Phần thân của yêu cầu được chia thành các phần riêng biệt cho từng trường trong biểu mẫu. Mỗi phần chứa một tiêu đề `Content-Disposition`, cung cấp thông tin cơ bản về trường đầu vào mà nó liên quan đến. Các phần này cũng có thể chứa tiêu đề `Content-Type`, cho biết loại `MIME` của dữ liệu đã được gửi qua trường nhập liệu đó.


- Một cách mà các trang web có thể thử xác thực các tệp tải lên là kiểm tra xem tiêu đề `Content-Type` dành riêng cho đầu vào này có khớp với loại `MIME` mong đợi hay không. Ví dụ, nếu máy chủ chỉ mong đợi các tệp hình ảnh, thì máy chủ có thể chỉ cho phép các loại như `image/jpeg` và `image/png`. Có thể phát sinh vấn đề khi giá trị của tiêu đề này được máy chủ ngầm tin tưởng. Nếu không thực hiện xác thực nào khác để kiểm tra xem nội dung của tệp có thực sự khớp với loại MIME được cho là hay không, thì biện pháp phòng thủ này có thể dễ dàng bị bỏ qua bằng các công cụ như **Burp Repeater**.


#### Lab: Web shell upload via Content-Type restriction bypass


- Thử upload 1 file lên làm avatar
    ![alt text](/File%20Upload/Image/image.png)
- Như bài lab trước, lần này upload file có nội dung tương tự để đọc nội dung file tại địa chỉ `/home/carlos/secret`. Nhưng lần này phải thay đổi nội dung `Content-Type` thành `image/jpeg`
    ![alt text](/File%20Upload/Image/image-10.png)
- Reload lại trang `home` và `GET` lại endpoint `/files/avatars/avatar.php` là đã đọc được nội dung file 
    ![alt text](/File%20Upload/Image/image-11.png)

- Submit nội dung là hoàn thành bài lab này
    ![alt text](/File%20Upload/Image/image-12.png)


### Preventing file execution in user-accessible directories

- Mặc dù việc ngăn chặn các loại tệp nguy hiểm được tải lên ngay từ đầu là tốt hơn, nhưng biện pháp phòng ngừa thứ hai là ngừng việc máy chủ thực thi bất kỳ kịch bản nào mà lỡ lọt qua.

- Các máy chủ thường chỉ chạy các kịch bản có `MIME type` đã được cấu hình rõ ràng để thực thi. Nếu không, chúng có thể chỉ trả về một thông báo lỗi hoặc, trong một số trường hợp, phục vụ nội dung của tệp như văn bản thuần túy.
- Ví dụ:
    ```php
        GET /static/exploit.php?command=id HTTP/1.1
        Host: normal-website.com

        HTTP/1.1 200 OK
        Content-Type: text/plain
        Content-Length: 39

        <?php echo system($_GET['cmd']); ?>
    ```
    - Response trả về là `200 OK` nhưng `Content-Type` lại ở định dạng `text/plain` tức văn bản thuần túy (plain text), không phải là HTML hay PHP.

- Hành vi này có thể hữu ích vì nó có thể giúp rò rỉ mã nguồn, nhưng nó vô hiệu hóa mọi nỗ lực tạo `shell web`.

- Cấu hình này thường khác nhau giữa các thư mục. Một thư mục nơi người dùng tải tệp lên sẽ có các biện pháp kiểm soát nghiêm ngặt hơn so với các vị trí khác trong hệ thống tệp mà không dự định chứa tệp do người dùng cung cấp. Nếu bạn có thể tìm cách tải lên một kịch bản vào thư mục khác mà không phải thư mục chứa tệp người dùng, máy chủ có thể vẫn thực thi kịch bản của bạn.


#### Lab: Web shell upload via path traversal

- Sau khi upload avartar bằng mã khai thác `php`, nhận thấy phản hồi của trang web trả về đúng với nội dung mã khai thác `(text/plain)`.
    ![alt text](/File%20Upload/Image/image-13.png)
- Thử lại bằng cách thay đổi đường dẫn file qua kỹ thuật `path traversal` 
    ```bash
    Content-Disposition: form-data; name="avatar"; filename="../avatar.php"
    ```
    ![alt text](/File%20Upload/Image/image-14.png)
- `GET` lại request, lần này thay đổi endpoint khớp với path vừa rồi là đã đọc được nội dung file
    ![alt text](/File%20Upload/Image/image-15.png)
- Submit nội dung là hoàn thành bài lab này
    ![alt text](/File%20Upload/Image/image-16.png)


### Insufficient blacklisting of dangerous file types

- Một trong những cách rõ ràng để ngăn chặn người dùng tải lên các script độc hại là tạo danh sách đen các phần mở rộng tệp có thể nguy hiểm như .php. 
Tuy nhiên, việc sử dụng danh sách đen có thể dễ dàng bị vượt qua vì rất khó để liệt kê tất cả các phần mở rộng tệp có thể sử dụng để thực thi mã. Những danh sách đen này đôi khi có thể bị lách qua bằng cách sử dụng các phần mở rộng tệp ít phổ biến hơn nhưng vẫn có thể thực thi được, chẳng hạn như `.php5`, `.shtml`, và nhiều phần mở rộng khác.
- Ghi đè cấu hình máy chủ
Như đã đề cập trong phần trước, các máy chủ thường không thực thi các tệp trừ khi chúng được cấu hình để làm như vậy. Ví dụ, trước khi một máy chủ Apache thực thi các tệp PHP được yêu cầu bởi một khách hàng, các nhà phát triển có thể phải thêm các chỉ thị sau vào tệp `/etc/apache2/apache2.conf` của họ:
    ```bash
    LoadModule php_module /usr/lib/apache2/modules/libphp.so
    AddType application/x-httpd-php .php
    ```
- Nhiều máy chủ cũng cho phép các nhà phát triển tạo các tệp cấu hình đặc biệt trong các thư mục riêng biệt để ghi đè hoặc thêm vào một số cài đặt toàn cục. Ví dụ, máy chủ Apache sẽ tải một tệp cấu hình đặc biệt cho thư mục từ tệp có tên `.htaccess` nếu có.

- Tương tự, các nhà phát triển có thể tạo cấu hình riêng cho thư mục trên các máy chủ IIS thông qua tệp `web.config`. Tệp này có thể bao gồm các chỉ thị như sau, cho phép các tệp `JSON` được phục vụ cho người dùng:
    ```bash
    <staticContent>
    <mimeMap fileExtension=".json" mimeType="application/json" />
    </staticContent>
    ```

- Các máy chủ web sử dụng những tệp cấu hình như thế này khi có, nhưng bạn thường không được phép truy cập chúng thông qua các yêu cầu `HTTP`. Tuy nhiên, đôi khi bạn có thể gặp phải những máy chủ không ngăn chặn bạn tải lên tệp cấu hình độc hại của riêng bạn. Trong trường hợp này, ngay cả khi phần mở rộng tệp bạn cần đã bị đưa vào danh sách đen, bạn vẫn có thể lừa máy chủ ánh xạ phần mở rộng tệp tùy chỉnh của mình thành một loại `MIME` có thể thực thi.

#### Lab: Web shell upload via extension blacklist bypass

- Lần này thử upload 1 file shell php như các bài lab trước, nhưng kết quả trả về không là `200 OK` mà là `403 Forbidden` kèm với dòng thông báo `php files are not allowed` - tức là trang web không cho phép upload file `.php`
    ![alt text](/File%20Upload/Image/image-17.png)
- Thử bypass lại bằng cách thay đổi 1 số tham số:
    ![alt text](/File%20Upload/Image/image-18.png)
    - Sửa tên file thành `.htaccess`
    - Thay đổi `Content-Type` thành `text/plain`
    - Thay đổi nội dung payload php thành `AddType application/x-httpd-php .l33t`. Điều này ánh xạ một phần mở rộng tùy ý `(.l33t)` tới ứng dụng loại `MIME` thực thi `/x-httpd-php`. Vì máy chủ sử dụng module `mod_php` nên nó biết cách xử lý việc này rồi.
    - Tham khảo thêm tại [htaccess](https://httpd.apache.org/docs/2.4/howto/htaccess.html)
- Bypass này cho phép xử lý các tệp có phần mở rộng `.l33t`. Thay vì coi chúng là tệp văn bản bình thường, Apache sẽ xử lý chúng như các tệp `PHP`. Điều này có thể cho phép kẻ tấn công tải lên một tệp `PHP` với phần mở rộng `.l33t` (vốn có thể không bị nghi ngờ là một tệp `PHP`) và thực thi mã `PHP` trên máy chủ khi truy cập vào tệp đó.
- Sau đó, upload lại file giúp `RCE`, nhưng lần này thay đổi phần mở rộng thành `.l33t`
    ![alt text](/File%20Upload/Image/image-19.png)
- `GET` lại đến endpoint `/files/avatars/avatar.l33t` là có thể xem được nội dung file
    ![alt text](/File%20Upload/Image/image-20.png)
- Submit nội dung là hoàn thành bài lab này
    ![alt text](/File%20Upload/Image/image-21.png)


### Obfuscating file extensions

- Ngay cả danh sách đen `(blacklist)` toàn diện nhất cũng có thể bị vượt qua bằng các kỹ thuật làm mờ cổ điển. Ví dụ, nếu mã xác thực phân biệt chữ hoa chữ thường và không nhận ra rằng `exploit.pHp` thực chất là một tệp `.php`, điều này có thể tạo ra sự khác biệt. Nếu mã sau đó ánh xạ phần mở rộng tệp sang loại `MIME` mà không phân biệt chữ hoa chữ thường, bạn có thể lén tải lên các tệp PHP độc hại vượt qua xác thực và có khả năng được máy chủ thực thi.

- Bạn cũng có thể đạt được kết quả tương tự bằng các kỹ thuật sau:

    1. Cung cấp nhiều phần mở rộng. Tùy thuộc vào thuật toán phân tích tên tệp, tệp sau đây có thể được hiểu là tệp PHP hoặc hình ảnh `JPG: exploit.php.jpg`.
    Thêm các ký tự dư thừa. Một số thành phần có thể bỏ qua khoảng trắng, dấu chấm, hoặc các ký tự khác: `exploit.php`.
    2. Sử dụng mã hóa URL (hoặc mã hóa URL kép) cho các ký tự như dấu chấm, dấu gạch chéo xuôi, hoặc dấu gạch chéo ngược. Nếu giá trị không được giải mã khi xác thực phần mở rộng tệp, nhưng lại được giải mã phía máy chủ, điều này cũng cho phép tải lên tệp độc hại: `exploit%2Ephp`.
    3. Thêm dấu chấm phẩy hoặc ký tự null byte được mã hóa URL trước phần mở rộng. Nếu mã xác thực được viết bằng ngôn ngữ cấp cao như PHP hoặc Java, nhưng máy chủ xử lý tệp bằng các hàm cấp thấp như C/C++, điều này có thể tạo ra sự khác biệt: `exploit.asp;.jpg` hoặc `exploit.asp%00.jpg`.
    4. Sử dụng ký tự unicode đa byte, có thể chuyển thành null byte hoặc dấu chấm sau khi chuyển đổi hoặc chuẩn hóa unicode. Các chuỗi như `xC0 x2E, xC4 xAE` hoặc `xC0 xAE` có thể được chuyển thành `x2E` nếu tên tệp được phân tích dưới dạng chuỗi UTF-8, nhưng sau đó được chuyển thành ký tự ASCII trước khi được sử dụng trong đường dẫn.
    5. Một số biện pháp phòng thủ liên quan đến việc loại bỏ hoặc thay thế các phần mở rộng nguy hiểm để ngăn tệp được thực thi. Tuy nhiên, nếu việc biến đổi này không được áp dụng lặp đi lặp lại, bạn có thể đặt chuỗi bị cấm theo cách mà việc xóa nó vẫn để lại một phần mở rộng hợp lệ. Ví dụ, hãy xem điều gì xảy ra nếu bạn loại bỏ `.php` khỏi tên tệp sau:
        ```php
            exploit.p.phphp
        ```
- Đây chỉ là một phần nhỏ trong số nhiều cách có thể làm mờ phần mở rộng tệp.

#### Lab: Web shell upload via obfuscated file extension

- Như các bài lab trước, lần này cũng thử upload 1 shell code lên và quan sát phản hồi.
    ![alt text](/File%20Upload/Image/image-23.png)
    - Thông báo trả về cho thấy trang web chỉ cho phép upload những file có định dạng `JPG & PNG`
- Thử thay đổi phần mở rộng thành `.php.png`, thêm 1 chút tham số mã hóa `%00` (tương đương với `null byte` trong URL encoded)
    ![alt text](/File%20Upload/Image/image-22.png)
    - Ngay lập tức, thông báo rằng file `avartar.php.png` đã được upload thành công
- Gọi lại tới endpoint `files/avatars/avatar.php` và truyền tham số `?cmd=ls`
    ![alt text](/File%20Upload/Image/image-24.png)
- Xem đường dẫn, thử đọc file `/etc/passwd`
    ![alt text](/File%20Upload/Image/image-25.png)
    ![alt text](/File%20Upload/Image/image-26.png)
- Đầu bài yêu cầu đọc file tại đường dẫn `/home/carlos/secret`
    ![alt text](/File%20Upload/Image/image-27.png)
- Submit nội dung là hoàn thành bài lab này
    ![alt text](/File%20Upload/Image/image-28.png)

### Flawed validation of the file's contents

- Thay vì tin tưởng vào `Content-Type` được chỉ định trong yêu cầu, các máy chủ an toàn hơn sẽ cố gắng xác minh rằng nội dung của tệp thực sự khớp với loại tệp được mong đợi.

- Trong trường hợp chức năng tải lên hình ảnh, máy chủ có thể cố gắng kiểm tra các thuộc tính nội tại của hình ảnh, chẳng hạn như kích thước của nó. Ví dụ, nếu bạn cố gắng tải lên một script PHP, script này sẽ không có kích thước hình ảnh nào cả. Do đó, máy chủ có thể suy luận rằng nó không thể là một hình ảnh và sẽ từ chối tải lên.

- Tương tự, một số loại tệp luôn chứa một chuỗi byte cụ thể trong phần `header` hoặc `footer`. Những chuỗi này có thể được sử dụng như một dấu vân tay hoặc chữ ký để xác định xem nội dung có khớp với loại tệp mong đợi hay không. Ví dụ, tệp JPEG luôn bắt đầu bằng các byte `FF D8 FF`.

- Đây là cách xác thực loại tệp mạnh mẽ hơn, nhưng ngay cả cách này cũng không hoàn toàn đáng tin cậy. Bằng cách sử dụng các công cụ đặc biệt, chẳng hạn như `ExifTool`, có thể dễ dàng tạo ra một tệp `JPEG "polyglot"` (đa hình), chứa mã độc trong metadata của nó.

#### Lab: Remote code execution via polyglot web shell upload

- Như những bài trước, thử upload 1 file mã khai thác lên và chờ phản hồi từ web
    ![alt text](/File%20Upload/Image/image-29.png)
    - Lỗi trả về là `file is not a valid image`, khả năng cao trang web đã lọc thông tin tải lên đầu vào, chỉ cho phép upload ảnh đúng định dạng `png/jpeg`

- Tôi đã chuẩn bị một ảnh có đúng định dạng với yêu cầu của trang web. Sử dụng `exiftool` cho biết thông tin về nó
    ![alt text](/File%20Upload/Image/image-30.png)

- Sử dụng `exiftool` để upload mã khai thác ẩn vào trong phần `comment`
    ![alt text](/File%20Upload/Image/image-31.png)

- Xem lại nội dung của nó
    ![alt text](/File%20Upload/Image/image-32.png)

- Tôi đã upload thử avatar lên và thành công
    ![alt text](/File%20Upload/Image/image-34.png)
- Sau đó chuyển nó đến repeater và thay đổi định dạng mới thành `.php`.
    ![alt text](/File%20Upload/Image/image-33.png)
    - Việc đổi định dạng thành `.php` sẽ giúp thực thi mã `php` được ẩn bên trong ảnh
    - Trang web không thể quét được vì nó đã xác thực định dạng ảnh (`.png`) ngay từ đầu là hợp lệ

- Gọi đến api `GET /files/avatars/Djp_thun.php?` và truyền tham số `cmd=ls` để list ra những file có trong thư mục hiện tại
    ![alt text](/File%20Upload/Image/image-35.png)

- Bài yêu cầu đọc nội dung của file tại path `/home/carlos/secret` nên tôi truyền đường dẫn đó vào
    ![alt text](/File%20Upload/Image/image-37.png)

- Sau 1 hồi loay hoay (nó hơi rối) cuối cùng tôi đã tìm được file `secret`, submit nó là hoàn thành bài này
    ![alt text](/File%20Upload/Image/image-36.png)
