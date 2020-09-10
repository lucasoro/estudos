#!/usr/bin/env python

# -*- coding: utf-8 -*-

# EXERCICIO: COMPLETE O ALGORITMO DE BLOCK CIPHER

#-----------------------------------------------------------
# calcula plain XOR key. Devem ser strings de mesmo tamanho

def xor_cipher(plain, key):

    hkey = []
    result = []
    
    for i in key:
        hkey.append(ord(i))
    i = 0
    for c in plain:
        result.append(ord(c)^hkey[i])
        i += 1
        if i == len(key):
            i = 0
    return result

#-----------------------------------------------------------
# transforma um array de bytes em caracteres ASCII

def to_ascii(result):
    cipher = ''
    for i in result:
        cipher += chr(i)
    return cipher


#-----------------------------------------------------------
# calcula o cipher de um único bloco.
# plain deve ser uma string com o tamanho exato do bloco
# K0 e K1 devem ser strings com metade do tamanho de um bloco
# retorna o texto criptografado já no formato de string

def bloco_cipher(plain,K0,K1):
    global bloco
    meiobloco = int(bloco/2)
    R0 = plain[0:meiobloco]
    L0 = plain[meiobloco:bloco]
    F0 = to_ascii(xor_cipher(R0,K0))
    R1 = to_ascii(xor_cipher(F0,L0))
    L1 = R0
    F1 = to_ascii(xor_cipher(R1,K1))
    R2 = to_ascii(xor_cipher(F1,L1))
    L2 = R1
    return(R2+L2)

#-----------------------------------------------------------
# faz a descriptografia de um único bloco

def bloco_decipher(cipher,K0,K1):
    global bloco
    meiobloco = int(bloco/2)
    L0 = cipher[0:meiobloco]
    R0 = cipher[meiobloco:bloco]
    
    F0 = to_ascii(xor_cipher(R0,K0))
    R1 = to_ascii(xor_cipher(F0,L0))
    L1 = R0
    F1 = to_ascii(xor_cipher(R1,K1))
    R2 = to_ascii(xor_cipher(F1,L1))
    L2 = R1
    return(L2+R2)


#-----------------------------------------------------------
# divide uma mensagem em blocos
# completa o ultimo bloco com PADDING caso necessário
# retorna um array de strings, cada uma representando um bloco

def divide_blocos(msg):
    global bloco
    msize = len(msg)
    pad = bloco - msize % bloco
    msg += '\0' * pad
    nb = int(len(msg)/bloco)

    print('A mensagem tem {} bytes e precisa de {} bytes de padding para formar {} blocos: '.format(msize, pad, nb))

    blocos = []
    for i in range(0,nb):
        blocos.append(msg[i*bloco:(i+1)*bloco])
    return(blocos)

#---------------------------------------------------------------------------------------

bloco = 8 
msg = str(input('Digite a mensagem: '))
blocos = divide_blocos(msg)
print(blocos)

         
K0=''
while len(K0) is not int(bloco/2):
    K0 = input('Digite a primeira chave de 4 bytes: '.format(bloco/2))

K1=''
while len(K1) is not int(bloco/2):
    K1 = input('Digite a segunda chave de {} bytes: '.format(bloco/2))


ciphers = []
for b in blocos:
    ciphers.append(bloco_cipher(b,K0,K1))
    
print(''.join(ciphers))


#----------------------------------------------------------------------------------------
# faça a chamada de descriptografia

decipher = []
for b in ciphers:
    decipher.append(bloco_decipher(b, K1, K0))

print("".join(decipher))
