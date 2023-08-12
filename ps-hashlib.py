import hashlib

# str = "Hello my name is Bill Burr"
# print("Original Text: " + str)

# str = str.encode()

# result = hashlib.sha256(str)
# result = hashlib.md5(str)
# print('The hexedecimal hashed value : ' + result.hexdigest())



print('Hardcoded md5 hash of python file from site: 0dc79188955e12e3b4338d03b3abb4be ')
filename = "c:/Users/19023/Downloads/python-3.11.4-amd64(2).exe"
with open(filename, 'rb') as f:
    bytes = f.read()
    hash_output = hashlib.md5(bytes).hexdigest();
    print("md5 hash of the file python64but.exe: " + hash_output)