import socket 

HOST = "127.0.0.1"   # local ip for loopback
PORT = 12345         # the server's port

# first parameter picks what network protocol
# secont parameter picks what type of socket 
# SOCK_STREAM sends and receives TCP packets 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(),
    print('[R]Ready')
    while True:
        client, addr = s.accept() # wait for msg, says who sent the msg 
        with client:
            print(f"[S] Incoming Message From: {addr}")
            data = client.recv(4096)
            if data == b"Disconnect":
                print("[E] End of Message from " + str(addr))
                break
