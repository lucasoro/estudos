#!/usr/bin/env python3
import socket
import sys

ESTADO = 'OFF'

# ----- funções auxiliares

def interpretaComando(comando, s):
    global ESTADO
    print('Recebi o comando', comando)
    if comando.lower() == '%s ligar':
        ESTADO = 'ON'
    elif 'desligar' in comando.lower():
        ESTADO = 'OFF'
    elif 'consulta' in comando.lower():
        # print('esqueci de fazer o exercicio 3A')
        s.send(bytes(ESTADO, 'utf-8'))
    else:
        print("Comando inválido!")

# ----------------

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Entre com o IP do servidor')
IP= input()

print('Entre com a porta do servidor')
PORTA= int(input())

print('Entre com o ID do sensor')
ID = input()

try:
    s.connect((IP, PORTA))
    #Envia o identificador
    s.send(bytes(ID,'utf-8'))

except:
    print('erro de conexao')

while True:
    try:
        dados = str(s.recv(100),'utf-8')
        interpretaComando(dados, s)
        # print('Esqueci de fazer o exercicio 3B')
    except:
        print('Erro na conexão com o monitor')
        sys.exit()
