def primes(n):                              # Sieve of Eratosthenes
    soma, sieve = [], [True] * n
    for p in range(2, n):
        if sieve[p]:
            soma.append(p)
            for i in range(p*p, n, p):
                sieve[i] = False
    return soma

print(primes(101))