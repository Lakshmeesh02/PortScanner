import socket
import pyfiglet
import sys
from datetime import datetime

header=pyfiglet.figlet_format("PORT SCANNER")
print(header)

print('-'*50)
target_ip=input("Enter target ipv4 address: ")
print(str(datetime.now()))
print('-'*50)

try:
    for port in range(1,1001):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.02)
        openport=s.connect_ex((target_ip,port))
        if openport==0:
            print(f"{port} is open..")
        s.close()

except KeyboardInterrupt:
    sys.exit()
except socket.error:
    print("Socket error :(")
    sys.exit()
