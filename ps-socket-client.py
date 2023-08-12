import socket 
import sys 

HOST = "127.0.0.1"   # The server's IP address
PORT = 12345         # The server's port 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(bytes(sys.argv[1], 'utf-8'))
    data = s.recv(4096)

print(data)