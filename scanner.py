import socket
import pyfiglet
import sys
from datetime import datetime

protocols=[]
header=pyfiglet.figlet_format("PORT SCANNER")
print(header)

print('-'*50)
target_host=input("Enter hostname: ")
target_ip=socket.gethostbyname(target_host)
#target_ip=input("Enter ip address: ")
#print(socket.gethostbyaddr(target_ip)[0])
print(str(datetime.now()))
print('-'*50)

try:
    for port in range(1,501):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.2)
        openport=s.connect_ex((target_ip,port))
        if openport==0:
            print(f"{port} is open..")
        s.close()

except KeyboardInterrupt:
    sys.exit()
except socket.error as e:
    print("Socket error :(",e)
    sys.exit()
