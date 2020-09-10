#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

# Versão antiga - OLD
# runtime: 24113.61541 seconds (6 hrs 42 mins) / ans = 142913828922 (Correct)
    # import time

    # def verifica_primo(primo):
    #     if primo >= 2:
    #         for i in range(2,primo):
    #             if not (primo % i):
    #                 return False
    #     else:
    # 	    return False
    #     return True


    # start = time.time()
    # numero = 9
    # soma = 17

    # while numero < 2_000_000:
    #     if verifica_primo(numero):
    #         soma += numero
    #     numero += 2

    # print(soma)
    # elapsed = time.time() - start
    # print("Time: {:.5f} seconds".format(elapsed))

import time

start = time.time()

def primes(n):                              # Sieve of Eratosthenes
    soma, sieve = [], [True] * n
    for p in range(2, n):
        if sieve[p]:
            soma.append(p)
            for i in range(p*p, n, p):
                sieve[i] = False
    return soma

print(sum(primes(2_000_000)))
elapsed = time.time() - start
print("Time: {:.2f} seconds".format(elapsed))