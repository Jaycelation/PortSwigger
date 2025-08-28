# Cross-Site Scripting (XSS) - Summary

| **Level**       | **Lab**                                                                 | **Kỹ thuật**                                                         | **Rating** | **Status**   |
|------------------|--------------------------------------------------------------------------|----------------------------------------------------------------------|------------|--------------|
| `Apprentice`   | Reflected XSS into HTML context with nothing encoded                     | Inject trực tiếp vào HTML (không encode)                             | ★☆☆        | ✅       |
| `Apprentice`   | Stored XSS into HTML context with nothing encoded                        | Stored payload trong DB → render ra HTML                             | ★★☆        | ✅       |
| `Apprentice`   | DOM XSS in document.write sink using source location.search              | DOM sink `document.write(location.search)`                           | ★★☆        | ✅       |
| `Apprentice`   | DOM XSS in innerHTML sink using source location.search                   | DOM sink `innerHTML = location.search`                               | ★★☆        | ✅       |
| `Apprentice`   | DOM XSS in jQuery anchor href attribute sink using location.search source| jQuery sink: `$('a').attr('href', location.search)`                   | ★★☆        | ✅       |
| `Apprentice`   | DOM XSS in jQuery selector sink using a hashchange event                 | jQuery selector từ `location.hash`                                   | ★★☆        | ✅       |
| `Apprentice`   | Reflected XSS into attribute with angle brackets HTML-encoded            | Escape `< >` nhưng không escape quote                                | ★★☆        | ✅       |
| `Apprentice`   | Stored XSS into anchor href attribute with double quotes HTML-encoded    | Escape `"` nhưng không escape `'` hoặc protocol                      | ★★☆        | ✅       |
| `Apprentice`   | Reflected XSS into a JavaScript string with angle brackets HTML encoded  | Escape `< >` nhưng không escape quote trong JS                       | ★★☆        | ✅       |
| `Practitioner` | DOM XSS in document.write sink inside a select element                   | Special sink context trong `<select>`                                | ★★★        | ✅       |
| `Practitioner` | DOM XSS in AngularJS expression with angle brackets and double quotes encoded | AngularJS sandbox expression injection                          | ★★★        | ✅       |
| `Practitioner` | Reflected DOM XSS                                                       | Reflected DOM-based (sink lấy từ URL param)                          | ★★☆        | ✅       |
| `Practitioner` | Stored DOM XSS                                                          | Stored input dùng trong DOM sink                                     | ★★☆        | ✅       |
| `Practitioner` | Reflected XSS into HTML context with most tags and attributes blocked    | Bypass filter (dùng tag ít phổ biến)                                 | ★★★        | ✅       |
| `Practitioner` | Reflected XSS into HTML context with all tags blocked except custom ones | Dùng custom tag/trick vẫn execute                                    | ★★★        | ✅       |
| `Practitioner` | Reflected XSS with some SVG markup allowed                              | Lợi dụng `<svg>` và event handler                                   | ★★★        | ❌   |
| `Practitioner` | Reflected XSS in canonical link tag                                     | Inject vào `<link rel="canonical">`                                  | ★★★        | ❌   |
| `Practitioner` | Reflected XSS into a JavaScript string with single quote and backslash escaped | Bypass escape trong JS string                                    | ★★★        | ❌   |
| `Practitioner` | Reflected XSS into a JavaScript string with angle brackets and double quotes encoded and single quotes escaped | Context escape phức tạp | ★★★★       | ❌   |
| `Practitioner` | Stored XSS into onclick event with angle brackets and double quotes encoded and single quotes and backslash escaped | Inject trong inline event | ★★★★       | ❌   |
| `Practitioner` | Reflected XSS into a template literal with all special chars escaped (Unicode-escaped) | Bypass Unicode escaping trong template literal       | ★★★★       | ❌   |
| `Practitioner` | Exploiting XSS to steal cookies                                         | Payload thực hiện document.cookie exfiltration                      | ★★★        | ❌   |
| `Practitioner` | Exploiting XSS to capture passwords                                     | Payload keylogger trong form                                        | ★★★        | ❌   |
| `Practitioner` | Exploiting XSS to bypass CSRF defenses                                  | XSS + auto-submit form để bypass CSRF token                         | ★★★★       | ❌   |
| `Expert`       | Reflected XSS with AngularJS sandbox escape without strings             | Sandbox escape không dùng string                                    | ★★★★★      | ❌   |
| `Expert`       | Reflected XSS with AngularJS sandbox escape and CSP                     | Sandbox escape + CSP bypass                                         | ★★★★★      | ❌   |
| `Expert`       | Reflected XSS with event handlers and href attributes blocked           | Payload nâng cao khi bị chặn `on*` và `href=`                       | ★★★★★      | ❌   |
| `Expert`       | Reflected XSS in a JavaScript URL with some characters blocked          | Craft URL JS payload bypass chặn kí tự                              | ★★★★★      | ❌   |
| `Expert`       | Reflected XSS protected by very strict CSP, with dangling markup attack | Dùng dangling markup để bypass CSP                                  | ★★★★★      | ❌   |
| `Expert`       | Reflected XSS protected by CSP, with CSP bypass                         | Exploit CSP misconfig để inject script                              | ★★★★★      | ❌   |
