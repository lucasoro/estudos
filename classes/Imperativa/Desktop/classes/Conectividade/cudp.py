#!/usr/bin/env python3
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

    print('Entre com o IP de destino: ')
    ip = input()

    print('Entre com a porta de destino: ')
    porta = int(input())

    print('Entre com a mensagem: ')
    msg = input()

    s.sendto(bytes(msg, 'utf-8'), (ip, porta))

print('o cliente encerrou')
s.close()