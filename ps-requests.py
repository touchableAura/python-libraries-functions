import requests 

website = requests.get("https://www.example.com")

# print("Status Code: " + str(website.status_code))
# print("\n" + str(website.headers))
# print("\n" + str(website.url))
# print (website.text)     # response in unicode
print(website.content)   # response in bytes 













### instructions + expected results ###

# using command prompt, navigate to folder where this file is located
# run the program with the following print statements using py ps-requests.py

# print("Status Code: " + str(website.status_code))
# print("\n" + str(website.headers))
# print("\n" + str(website.url))

# expect:

#b'<!doctype html>\n<html>\n<head>\n    <title>Example Domain</title>\n\n    <meta charset="utf-8" />\n    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />\n    <meta name="viewport" content="width=device-width, initial-scale=1" />\n    <style type="text/css">\n    body {\n        background-color: #f0f0f2;\n        margin: 0;\n        padding: 0;\n        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;\n        \n    }\n    div {\n        width: 600px;\n        margin: 5em auto;\n        padding: 2em;\n        background-color: #fdfdff;\n        border-radius: 0.5em;\n        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);\n    }\n    a:link, a:visited {\n        color: #38488f;\n        text-decoration: none;\n    }\n    @media (max-width: 700px) {\n        div {\n
#    margin: 0 auto;\n            width: auto;\n        }\n    }\n    </style>    \n</head>\n\n<body>\n<div>\n    <h1>Example Domain</h1>\n    <p>This domain is for use in illustrative examples in documents. You may use this\n    domain in literature without prior coordination or asking for permission.</p>\n    <p><a href="https://www.iana.org/domains/example">More information...</a></p>\n</div>\n</body>\n</html>\n'

# C:\Users\19023\Documents\python-libraries-functions>py ps-requests.py
# Status Code: 200

# {'Content-Encoding': 'gzip', 'Accept-Ranges': 'bytes', 'Age': '300582', 'Cache-Control': 'max-age=604800', 'Content-Type': 'text/html; charset=UTF-8', 'Date': 'Mon, 07 Aug 2023 15:54:46 GMT', 'Etag': '"3147526947+gzip"', 'Expires': 'Mon, 14 Aug 2023 15:54:46 GMT', 'Last-Modified': 'Thu, 17 Oct 2019 07:18:26 GMT', 'Server': 'ECS (bsa/EB24)', 'Vary': 'Accept-Encoding', 'X-Cache': 'HIT', 'Content-Length': '648'}

# https://www.example.com/


## next, comment those out and uncomment the following:

# print (website.text)  


# expect:
# <!doctype html>
# <html>
# <head>
#     <title>Example Domain</title>

#     <meta charset="utf-8" />
#     <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
#     <meta name="viewport" content="width=device-width, initial-scale=1" />
#     <style type="text/css">
#     body {
#         background-color: #f0f0f2;
#         margin: 0;
#         padding: 0;
#         font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;

#     }
#     div {
#         width: 600px;
#         margin: 5em auto;
#         padding: 2em;
#         background-color: #fdfdff;
#         border-radius: 0.5em;
#         box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
#     }
#     a:link, a:visited {
#         color: #38488f;
#         text-decoration: none;
#     }
#     @media (max-width: 700px) {
#         div {
#             margin: 0 auto;
#             width: auto;
#         }
#     }
#     </style>
# </head>

# <body>
# <div>
#     <h1>Example Domain</h1>
#     <p>This domain is for use in illustrative examples in documents. You may use this
#     domain in literature without prior coordination or asking for permission.</p>
#     <p><a href="https://www.iana.org/domains/example">More information...</a></p>
# </div>
# </body>
# </html>

# finally, comment that out and run that last statement

# expect:
# C:\Users\19023\Documents\python-libraries-functions>py ps-requests.py
# b'<!doctype html>\n<html>\n<head>\n    <title>Example Domain</title>\n\n    <meta charset="utf-8" />\n    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />\n    <meta name="viewport" content="width=device-width, initial-scale=1" />\n    <style type="text/css">\n    body {\n        background-color: #f0f0f2;\n        margin: 0;\n        padding: 0;\n        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;\n        \n    }\n    div {\n        width: 600px;\n        margin: 5em auto;\n        padding: 2em;\n        background-color: #fdfdff;\n        border-radius: 0.5em;\n        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);\n    }\n    a:link, a:visited {\n        color: #38488f;\n        text-decoration: none;\n    }\n    @media (max-width: 700px) {\n        div {\n
#    margin: 0 auto;\n            width: auto;\n        }\n    }\n    </style>    \n</head>\n\n<body>\n<div>\n    <h1>Example Domain</h1>\n    <p>This domain is for use in illustrative examples in documents. You may use this\n    domain in literature without prior coordination or asking for permission.</p>\n    <p><a href="https://www.iana.org/domains/example">More information...</a></p>\n</div>\n</body>\n</html>\n'


