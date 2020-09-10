# The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

# Number stored on another file (numero_e8) in order to keep this workspace organized.


import numero_e8
num = numero_e8.numero

def multi(lista):
    resultado = 1
    for valor in lista:
        resultado = int(valor) * resultado
    return resultado



def remove_zero(lista):
    lista_final = []
    for k in range(len(lista) - 1):
        if lista[k]:
            lista_final.append(lista[k])
    return lista_final

def main(numero):
    lista = []
    i = 0
    while i < 988:
        lista_inner = []
        for count in range(i, i + 13):
            lista_inner.append(str(numero)[count])
            count += 1
        lista.append(lista_inner)
        i += 1
    for j in range(988):
        lista[j] = multi(lista[j])
    final = remove_zero(lista)
    return sorted(final)[len(final) - 1]


print(main(num))