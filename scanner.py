import socket
import pyfiglet
import sys
from datetime import datetime

protocols=[]
header=pyfiglet.figlet_format("PORT SCANNER")
print(header)

print('-'*50)
target_host=input("Hostname: ")
try:
    target_ip=socket.gethostbyname(target_host)
except:
    print("Invalid hostname..")
    sys.exit()
#target_ip=input("Enter ip address: ")
print(str(datetime.now())[:19])
print('-'*50)
print("PORT\tSERVICE\n")
services={22:"ssh", 25:"smtp", 80:"http", 135:"microsoft-rpc", 139:"netbios-ssn", 443:"https", 445:"microsoft-smb", 21:"ftp", 53:"dns"}
try:
    for port in range(1,501):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.2)
        openport=s.connect_ex((target_ip,port))
        if openport==0:
            print(f"{port}\t{services[port]}")
        s.close()

except KeyboardInterrupt:
    sys.exit()
except socket.error as e:
    print("Socket error :(",e)
    sys.exit()

