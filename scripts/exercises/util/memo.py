# # Fibonacci - Aplicação simples de memoização

import time

memo = {}

def fib(n):
    if n in memo:
        return memo[n]
    else:
        if n < 3:
            memo[n] = 1
        else:
            memo[n] = fib(n - 2) + fib(n - 1)
    return memo[n]


# def fib(n):
    # return 1 if n < 3 else fib(n - 1) + fib(n - 2)

num = 40
inicio = time.time()
print("---------------------------------------------------------------------------")
print("Número {0} da sequência de Fibonacci: {1}".format(num, fib(num)))
print("---------------------------------------------------------------------------")
print("Tempo de execução: {:.6f}".format(time.time() - inicio))
print("---------------------------------------------------------------------------")