16:

result = str(pow(2, 1000))
soma = 0

for i in range(len(result)):
    try:
        soma += int(result[i:i + 1])
    except IndexError:
        continue

print(soma)