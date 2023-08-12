# regular expressions


import re

re_string = "1/1/2022 12:04:54 Evan Cameron.aspx Successful login"
result_pattern = r"Success\w*"
date_pattern = r"\d+/\d+/\d+"

rpattern = re.compile(result_pattern)
rpattern = re.compile(date_pattern)

"""

print("**********************************************************")

res = rpattern.match(re_string)
dt = dpattern.match(re_string)
print("[*]Match the pattern 'Success' followed by alphanumeric char(s)")
if res is not None:
    print(res.string)
    print(res.pos)
    print(res.group())
else:
    print("None")

res = rpattern.search(re_string)
dt = date_pattern.search(re_string)
print("[*]Match the pattern 'Success' followed by alphanumerical char(s)")
print(res.string)
print("result: " + res.group())
print(res.start())
print("date: " + dt.group())

"""

res = re.split(r"\s", re_string)
print("[*]Split up string by the whitespace and add each individual part together")
print("All tokens:", res)
print("Result token:", res[4])
print("Date token:", res[0])

# [*]Split up string by the whitespace and add each individual part together
# All tokens: ['1/1/2022', '12:04:54', 'Evan', 'Cameron.aspx', 'Successful', 'login']
# Result token: Successful
# Date token: 1/1/2022

print("************************************************************")

res =re.findall(r"\d", re_string)
print("[*] Print all the digits in a list")
print(res)

# [*] Print all the digits in a list
# ['1', '1', '2', '0', '2', '2', '1', '2', '0', '4', '5', '4']  

