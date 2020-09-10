# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
# Number stored on another file (numero_e13) in order to keep this workspace organized.

import numero_e13

numero = numero_e13.numero
lista_numeros = []
final = 0
for i in range(0, len(str(numero)), 50):
    lista_numeros.append(int(str(numero)[i:i+50]))

for j in lista_numeros:
    final += j

print(str(final)[:10])