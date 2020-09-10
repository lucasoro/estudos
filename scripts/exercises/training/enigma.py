# SBC 2018 ENIGMA

def main():

    try:
        entrada1 = str(input())
        entrada2 = str(input())
    except:
        main()

    contador = 0

    for i in range(len(entrada1) - len(entrada2)):

        verificador = True
        entrada1_tratada = entrada1[i:len(entrada2) + i]

        for letra in range(len(entrada1_tratada)):
            if entrada1_tratada[letra] == entrada2[letra]:
                verificador = False
                
        if verificador:
            contador += 1


    return contador


if __name__ == "__main__":
    print(main())