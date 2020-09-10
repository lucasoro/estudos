#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Bibliotecas
import os, hashlib, time

# Agoritmo básico - verifica dados comparando com credenciais escritas no código fonte
# Implementação que permite 5 tentativas
def basic():

    # Número de tentativas restantes
    attempts = 5
    while attempts > 0:

        # Credenciais
        USER = "puc"
        PASSWD = "senha"

        # Leitura do input
        user_input=input("Digite o usuário: ")
        passwd_input=input("Digite a senha: ")
        
        # Verificação dos dados
        if passwd_input == PASSWD and user_input == USER:
            print("Acesso concedido!")
            exit(0)
        
        # caso incorretos, diminui o total de tentativas restantes
        else:
            print("Acesso negado!")
            attempts -= 1
            print("Tente novamente! Tentativas restantes: {}".format(attempts))
    
    # Identifica que todas as tentativas falharam
    print("Tentativas demais! Tente novamente mais tarde.")


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
# Implementação que permite 5 tentativas
def verify():

    # Número de tentativas restantes
    attempts = 5
    while attempts > 0:

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
        if verificado:
            print("Acesso concedido!")
            exit(0)
        else:
            print("Acesso negado!")
            attempts -= 1
            print("Tente novamente! Tentativas restantes: {}".format(attempts))

    # Identifica que todas as tentativas falharam
    print("Tentativas demais! Tente novamente mais tarde.")


# Menu do segundo algoritmo de verificação
def elaborate():

    # Booleano que controla a quantidade de tentativas
    verificador_input = False
    while not verificador_input:

        # Limpa a tela
        os.system('cls') if os.name == "nt" else os.system("clear")
        
        # Descrição das opções no menu
        print("Opções:")
        print("Opção 1: Adicionar usuário ao banco de dados")
        print("Opção 2: Verificar existencia do usuário")
        
        # Determina qual opção foi escolhida, caso inválida, tenta ler novamente
        try:
            option = int(input("Escolha a opção: "))
        except:
            print("Input inválido! ")
            time.sleep(2)
            continue

        # Chama devidamente cada método responsável por cada opção
        if option == 1:
            adding_to_database()
            
            # Identifica que o input fornecido é válido
            verificador_input = not verificador_input
        elif option == 2:
            verify()

            # Identifica que o input fornecido é válido
            verificador_input = not verificador_input
        else:
            print("Input inválido! ")
            time.sleep(2)


# Menu principal
def menu():

    # Booleano que verifica se o input fornecido é válido
    verificador_input = False
    while not verificador_input:

        # Limpa a tela
        os.system('cls') if os.name == "nt" else os.system("clear")
        
        # Lista opções do menu
        print("Opções:")
        print("Opção 1: algoritmo básico")
        print("Opção 2: algoritmo elaborado")
        
        # Determina qual opção foi escolhida, caso inválida, tenta ler novamente
        try:
            option = int(input("Escolha a opção: "))
        except:
            print("Input inválido!")
            time.sleep(2)
            continue

        # Chama devidamente cada método responsável por cada opção
        if option == 1:
            basic()

            # Identifica que o input fornecido é válido
            verificador_input = True

        elif option == 2:
            elaborate()

            # Identifica que o input fornecido é válido
            verificador_input = True
        else:
            print("Input inválido! ")
            time.sleep(2)
        
# Chamada do método de menu
if __name__ == "__main__":
    menu()