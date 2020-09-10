# SBC 2018 DESVENDANDO MONTY HALL

def main():

    n_jogos = int(input())
    matriz = []
    
    for x in range(n_jogos):
        matriz.append(int(input()))

    vitorias = 0

    for i in matriz:
        if i != 1:
            vitorias += 1

    print(vitorias)

if __name__ == "__main__":
    main()