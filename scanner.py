import socket
import pyfiglet
import sys
from datetime import datetime
import os

header=pyfiglet.figlet_format("PORT SCANNER")   # design banner
print(header)

print('-'*50)
target_host=input("Hostname: ")     # get target website name from the user
try:
    target_ip=socket.gethostbyname(target_host)     # try to get the ip address of it (ip addresses are scanned, not the hostnames)
except:
    print("Invalid hostname..")
    sys.exit()
#target_ip=input("Enter ip address: ")
print(str(datetime.now())[:19])
date_time=str(datetime.now())[:19]
print('-'*50)
print("PORT\tSERVICE\n")
services={22:"ssh", 25:"smtp", 80:"http", 135:"microsoft-rpc", 139:"netbios-ssn", 443:"https", 445:"microsoft-smb", 21:"ftp", 53:"dns"}     # map services for likely-to-be-open ports 
try:
    with open(f"results {target_host}.txt", "w") as f:
        f.write(date_time)
        f.write('\n')
        f.write(f"Target hostname: {target_host}\n")
        f.write(f"Target IP: {target_ip}\n\n")
        for port in range(1,501):   # range of ports to scan
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)     # create a new socket to connect to each port
            socket.setdefaulttimeout(0.2)   # time to send a request and recieve a response
            openport=s.connect_ex((target_ip,port))     # connects to the port in the target (returns 0 if successful, 1 if not)   
            if openport==0:
                print(f"{port}\t{services[port]}")
                f.write(f"{port}\t{services[port]}\n")
            s.close()

except KeyboardInterrupt:       # interrupts
    sys.exit()
except socket.error as e:
    print("Socket error :(",e)
    sys.exit()

