from random import randint

caracteres = "1234567890abcdefghijklmnopqrstuvwxyz@#$%&"

for j in range(10):

    senha = ""
    for i in range(25):
        senha = senha + caracteres[randint(0, len(caracteres) - 1)]

    # senha = senha + '\n'

    print(senha)