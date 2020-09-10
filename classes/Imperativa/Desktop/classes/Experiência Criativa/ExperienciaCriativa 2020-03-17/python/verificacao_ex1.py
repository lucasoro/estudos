#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Bibliotecas
import os, hashlib, time

# Agoritmo básico - verifica dados comparando com credenciais escritas no código fonte
def basic():
    
    # Credenciais
    USER = "puc"
    PASSWD = "senha"

    # Leitura do input
    user_input=input("Digite o usuário: ")
    passwd_input=input("Digite a senha: ")

    # Verificação dos dados
    print("Acesso concedido!") if user_input == USER and passwd_input == PASSWD else print("Acesso negado!")


# Algoritmo elaborado - Adiciona dados ao arquivo credenciais.txt - senha 'encriptada'
def adding_to_database():

    # Limpa a tela
    os.system('cls') if os.name == "nt" else os.system("clear")

    # Leitura de input
    user = str(input("Insira o usuário: "))
    passwd = str(input("Digite a senha: "))

    # Aplica a hash sha-1 a senha
    hashed_passwd = hashlib.sha1(passwd.encode('utf-8')).hexdigest()

    # Abre o arquivo para escrita
    f = open("credenciais.txt", "a", encoding='utf-8')

    # Escreve no arquivo
    f.write("\n" + user + " : " + hashed_passwd + "\n")

    # Notifica o usuário da alteração no arquivo
    print("Usuário {} adicionado ao banco de dados!".format(user))

    # Fecha o arquivo
    f.close()


# Verifica a existência de credenciais no arquivo credenciais.txt
def verify():

    # Booleano de controle
    verificado = False

    # Captura de input
    user = str(input("Insira o usuário: "))
    passwd = str(input("Digite a senha: "))

    # Codificação em hash sha-1 da senha passada pelo usuário
    hashed_passwd = hashlib.sha1(passwd.encode('utf-8')).hexdigest()

    # Concatenação do usuário e da senha em uma só string
    credentials = (user + " : " + hashed_passwd).encode('utf-8')

    # Abertura do arquivo para leitura
    f = open("credenciais.txt", "r")

    # Leitura linha por linha do arquivo, a fim de encontrar as credenciais passadas
    for line in f.readlines():
        if str(credentials).encode('utf-8')[2:-1] in str(line).encode('utf-8')[:-1]:
            verificado = True
        else:
            continue
    
    # Identifica se o acesso foi garantido ou não
    print("Acesso negado!") if not verificado else print("Acesso concedido!")


# Menu do segundo algoritmo de verificação
def elaborate():

    # Limpa a tela
    os.system('cls') if os.name == "nt" else os.system("clear")

    # Descrição das opções no menu
    print("Opções:")
    print("Opção 1: Adicionar usuário ao banco de dados")
    print("Opção 2: Verificar existencia do usuário")

    # Determina qual opção foi escolhida, caso inválida, tenta ler novamente
    try:
        option = int(input("Escolha a opção: "))
        adding_to_database() if option == 1 else verify()
    except:
        print("Opção inválida!")
        time.sleep(2)
        elaborate()

# Menu principal
def menu():

    # Limpa a tela
    os.system('cls') if os.name == "nt" else os.system("clear")

    # Lista opções do usuário
    print("Opções:")
    print("Opção 1: algoritmo básico")
    print("Opção 2: algoritmo elaborado")

    # Determina o que fazer baseado na escolha do usuário
    try:
        option = int(input("Escolha a opção: "))
        if option == 1: basic()
        if option == 2: elaborate()

    # Caso a escolha seja inválida, lê novamente
    except:
        print("Opção inválida!")
        time.sleep(2)
        menu()

# Chamada da função de menu
if __name__ == "__main__":
    menu()