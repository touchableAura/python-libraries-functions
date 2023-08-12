import socket 

def scan_ports(target):
    for port in range(12344, 12347):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1) # set timeout for the connection attempt
        result = s.connect_ex((target, port))
        if result == 0:
            print(f'Port {port}: Open')
        else:
            print(f'Port {port}: Closed')
        s.close()

if __name__ == "__main__":
    machine = input("Enter the target Name or IP: ")
    IPscanned = socket.gethostbyname(machine)

print(f"Scanning {machine} ({IPscanned}) For Open Ports....")
scan_ports(IPscanned)

# instructions
# run the following in separate cmd prmpt window
# run ps-socket-server
# run ps-socket-client
# run ps-socket-portscan






#issues w/ ps code 

# machine = input("Enter the target Name or IP: ")
# IPscanned = socket.gethostbyname(machine)

# print("Scanning {} ({}) For Open Ports....".format(machine, IPscanned))

# for port in range(12344, 12347):
#     result = s.connect_ex((IPscanned, port)) # connect_ex returns an error
#     if result == 0:
#         print('Port {}: Open'.format(port))
#     else:
#         print('Port {}:'.format(port))
# s.close()