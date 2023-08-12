import sys
import os 

# print("Current Working Directory:", os.getcwd())
# print("PID:", os.getpid())
# print("Name:", os.name)
# print("Platform:", sys.platform)

# Current Working Directory: C:\Users\19023\Documents\python-libraries-functions
# PID: 14764
# Name: nt
# Platform: win32



#    *************************************************



# os.system("ping 127.0.0.1")
# os.system("ping " + sys.argv[1])

# Pinging 127.0.0.1 with 32 bytes of data:
# Reply from 127.0.0.1: bytes=32 time<1ms TTL=128
# Reply from 127.0.0.1: bytes=32 time<1ms TTL=128
# Reply from 127.0.0.1: bytes=32 time<1ms TTL=128
# Reply from 127.0.0.1: bytes=32 time<1ms TTL=128

# Ping statistics for 127.0.0.1:
#     Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),      
# Approximate round trip times in milli-seconds:
#     Minimum = 0ms, Maximum = 0ms, Average = 0ms




# os.remove("temp.txt")




#     *************************************************

# plural site code: not working 
# with open(os.path.join(sys.path[0], 'log.txt'), 'r') as f:
#     sys.stdout.write(f.read())


#chatgpt suggestions:
# log_file_path = os.path.join(sys.path[0], "logs", "log.txt")

# with open(log_file_path, "r") as f:
#     sys.stdout.write(f.read())




# *****************************************************








for root, dirs, files in os.walk(".",topdown=False):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))

# .\__pycache__\base64.cpython-311.pyc
# .\log.txt
# .\notes.py
# .\out-err.log
# .\out.log
# .\ps-base64.py
# .\ps-hashlib.py
# .\ps-os.py
# .\ps-strings.py
# .\ps-sys.py
# .\logs
# .\__pycache__









