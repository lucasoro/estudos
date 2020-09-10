import os
import sys, time

def main():

    os.system('cls' if os.name == 'nt' else 'clear')

    x1, x2, x3, x4, x5, x6, x7, x8, x9, jogador, contador = ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', False, 0
    print(' %s | %s | %s ' %(x7, x8, x9))
    print(' %s | %s | %s ' %(x4, x5, x6))
    print(' %s | %s | %s ' %(x1, x2, x3))

    if_over(x1, x2, x3, x4, x5, x6, x7, x8, x9, jogador, contador)


def if_over(x1, x2, x3, x4, x5, x6, x7, x8, x9, jogador, contador):
    if (verifica_linhas(x1, x2, x3, x4, x5, x6, x7, x8, x9, jogador, contador)):
        if jogador:
            print('Jogador o ganhou!')
            option = str(input('Deseja jogar de novo ?(s/n): '))
            if option == 's':
                main()
            sys.exit(1)

        else:
            print('Jogador x ganhou!')
            option = str(input('Deseja jogar de novo ?(s/n): '))
            if option == 's':
                main()
            sys.exit(1)

    if contador == 9:
        print('Empate!')
        option = str(input('Deseja jogar de novo ?(s/n): '))
        if option == 's':
            main()
        sys.exit(1)
    else:
        escolha(x1, x2, x3, x4, x5, x6, x7, x8, x9, jogador, contador)


def verifica_linhas(x1, x2, x3, x4, x5, x6, x7, x8, x9, jogador, contador):

    verificador = ' '
    return (x1 == x2 == x3 != verificador) or (x1 == x5 == x9 != verificador) or (x1 == x4 == x7 != verificador) or (x2 == x5 == x8 != verificador) or (x3 == x5 == x7 != verificador) or (x3 == x6 == x9 != verificador) or (x4 == x5 == x6 != verificador)



def escolha(x1, x2, x3, x4, x5, x6, x7, x8, x9, jogador, contador):


    if jogador:
        print('Jogador x:')
        choice = int(input('Insira a posição: '))
                                                                                #pylint: disable = unused-variable
        if choice == 1:
            if x1 != 'x' and x1 != 'o':
                x1 = 'x'
            else:
                print('Escolha uma posição válida!')
                contador -= 1
                if_over(x1, x2, x3, x4, x5, x6, x7, x8, x9, jogador, contador)
        elif choice == 2:
            if x2 != 'x' and x2 != 'o':
                x2 = 'x'
            else:
                print('Escolha uma posição válida!')
                contador -= 1
                if_over(x1, x2, x3, x4, x5, x6, x7, x8, x9, jogador, contador)
        elif choice == 3:
            if x3 != 'x' and x3 != 'o':
                x3 = 'x'
            else:
                print('Escolha uma posição válida!')
                contador -= 1
                if_over(x1, x2, x3, x4, x5, x6, x7, x8, x9, jogador, contador)
        elif choice == 4:
            if x4 != 'x' and x4 != 'o':
                x4 = 'x'
            else:
                print('Escolha uma posição válida!')
                contador -= 1
                if_over(x1, x2, x3, x4, x5, x6, x7, x8, x9, jogador, contador)
        elif choice == 5:
            if x5 != 'x' and x5 != 'o':
                x5 = 'x'
            else:
                print('Escolha uma posição válida!')
                contador -= 1
                if_over(x1, x2, x3, x4, x5, x6, x7, x8, x9, jogador, contador)
        elif choice == 6:
            if x6 != 'x' and x6 != 'o':
                    x6 = 'x'
            else:
                print('Escolha uma posição válida!')
                contador -= 1
                if_over(x1, x2, x3, x4, x5, x6, x7, x8, x9, jogador, contador)
        elif choice == 7:
            if x7 != 'x' and x7 != 'o':
                x7 = 'x'
            else:
                print('Escolha uma posição válida!')
                contador -= 1
                if_over(x1, x2, x3, x4, x5, x6, x7, x8, x9, jogador, contador)
        elif choice == 8:
            if x8 != 'x' and x8 != 'o':
                x8 = 'x'
            else:
                print('Escolha uma posição válida!')
                contador -= 1
                if_over(x1, x2, x3, x4, x5, x6, x7, x8, x9, jogador, contador)
        elif choice == 9:
            if x9 != 'x' and x9 != 'o':
                x9 = 'x'
            else:
                print('Escolha uma posição válida!')
                contador -= 1
                if_over(x1, x2, x3, x4, x5, x6, x7, x8, x9, jogador, contador)
        else:
            print('Escolha inválida!')
            contador -= 1
            if_over(x1, x2, x3, x4, x5, x6, x7, x8, x9, jogador, contador)


    else:
        print('Jogador o:')
        choice = int(input('Insira a posição: '))
        if choice == 1:
            if x1 != 'x' and x1 != 'o':
                x1 = 'o'
            else:
                print('Escolha uma posição válida!')
                contador -= 1
                if_over(x1, x2, x3, x4, x5, x6, x7, x8, x9, jogador, contador)
        elif choice == 2:
            if x2 != 'x' and x2 != 'o':
                x2 = 'o'
            else:
                print('Escolha uma posição válida!')
                contador -= 1
                if_over(x1, x2, x3, x4, x5, x6, x7, x8, x9, jogador, contador)
        elif choice == 3:
            if x3 != 'x' and x3 != 'o':
                x3 = 'o'
            else:
                print('Escolha uma posição válida!')
                contador -= 1
                if_over(x1, x2, x3, x4, x5, x6, x7, x8, x9, jogador, contador)
        elif choice == 4:
            if x4 != 'x' and x4 != 'o':
                x4 = 'o'
            else:
                print('Escolha uma posição válida!')
                contador -= 1
                if_over(x1, x2, x3, x4, x5, x6, x7, x8, x9, jogador, contador)
        elif choice == 5:
            if x5 != 'x' and x5 != 'o':
                x5 = 'o'
            else:
                print('Escolha uma posição válida!')
                contador -= 1
                if_over(x1, x2, x3, x4, x5, x6, x7, x8, x9, jogador, contador)
        elif choice == 6:
            if x6 != 'x' and x6 != 'o':
                x6 = 'o'
            else:
                print('Escolha uma posição válida!')
                contador -= 1
                if_over(x1, x2, x3, x4, x5, x6, x7, x8, x9, jogador, contador)
        elif choice == 7:
            if x7 != 'x' and x7 != 'o':
                x7 = 'o'
            else:
                print('Escolha uma posição válida!')
                contador -= 1
                if_over(x1, x2, x3, x4, x5, x6, x7, x8, x9, jogador, contador)
        elif choice == 8:
            if x8 != 'x' and x8 != 'o':
                x8 = 'o'
            else:
                print('Escolha uma posição válida!')
                contador -= 1
                if_over(x1, x2, x3, x4, x5, x6, x7, x8, x9, jogador, contador)
        elif choice == 9:
            if x9 != 'x' and x9 != 'o':
                x9 = 'o'
            else:
                print('Escolha uma posição válida!')
                contador -= 1
                if_over(x1, x2, x3, x4, x5, x6, x7, x8, x9, jogador, contador)
        else:
            print('Escolha inválida!')
            contador -= 1
            if_over(x1, x2, x3, x4, x5, x6, x7, x8, x9, jogador, contador)

    jogador = not jogador
    contador += 1
    print(' %s | %s | %s ' %(x7, x8, x9))
    print(' %s | %s | %s ' %(x4, x5, x6))
    print(' %s | %s | %s ' %(x1, x2, x3))
                                                                                #pylint: enable = unused-variable
    if_over(x1, x2, x3, x4, x5, x6, x7, x8, x9, jogador, contador)


if __name__ == "__main__":
    main()