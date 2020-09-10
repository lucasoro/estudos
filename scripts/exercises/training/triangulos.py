# SBC 2015 TRIÂNGULOS

# para construir um triangulo é necessário que a medida de qualquer um dos lados seja menor que a soma dos outros dois lados e maior que a diferença entre eles.

def tratamento_do_input():
    
    varetas = input()
    varetas = varetas.split(" ")
    
    for i in range(len(varetas)):
        varetas[i] = int(varetas[i])
    
    return varetas


def main():
    
    varetas = tratamento_do_input()
    possibilidade = False
    for m in varetas:
        for n in varetas:
            for o in varetas:
                if m == n or n == o or o == m:
                    continue
                if m < n + o and m > abs(n - o):
                    possibilidade = True


    return "S" if possibilidade else "N"



if __name__ == "__main__":
    print(main())