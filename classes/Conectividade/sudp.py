#!/usr/bin/env python3
import socket
import sys

porta, ip = int(input("Entre com a porta: ")), input("Entre com o ip: ")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.bind((ip, porta))
except:
   print('# erro de bind')
   sys.exit()

while True:
    data, addr = s.recvfrom(1024)
    print('sensor ', addr, ' enviou:', data)

print('o servidor encerrou')
s.close()

