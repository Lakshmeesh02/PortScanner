import socket
import sys

host = "192.168.1.100"
port = 100

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

s.listen(1)

print("Waiting for a client to connect...")
while 1:
    conn, addr = s.accept()
    print("Client connected:", addr)
    if KeyboardInterrupt:       # interrupts
        sys.exit()

conn.close()
