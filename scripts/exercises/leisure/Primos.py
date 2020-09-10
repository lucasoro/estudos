# Atkin otimizado

# def primes(n):
#     n, correction = n-n%6+6, 2-(n%6>1)
#     sieve = [True] * (n//3)
#     for i in range(1,int(n**0.5)//3+1):
#       if sieve[i]:
#         k=3*i+1|1
#         sieve[      k*k//3      ::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
#         sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
#     return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]

# print(sum(primes(2000000)))


# Crivo de Eratosthenes

def crivo(numero):
    primos = []
    soma = 0
    lista = [True] * numero
    for i in range(2, numero):
        if lista[i]:
            primos.append(i)
            soma += i
            for j in range(i * i, numero, i):
                lista[j] = False
    return primos, soma

print(crivo(100))