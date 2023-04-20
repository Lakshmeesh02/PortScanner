import socket
import sys
from datetime import datetime

host = "127.0.0.1"
port = 100

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

s.listen(1)
date_time=str(datetime.now())[:19]
print("Waiting for a client to connect...")
print(date_time)
while 1:
    try:
        conn, addr = s.accept()
        print("Client connected:", addr)
    except KeyboardInterrupt:
        sys.exit()

conn.close()
