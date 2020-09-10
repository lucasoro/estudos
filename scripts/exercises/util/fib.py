# Fibonacci - Definição e implementação de memoização

# 1 1 2 3 5

memo = {0:0, 1:1, 2:1}

# def fibonacci(num):
#     return 1 if num < 3 else fibonacci(num - 1) + fibonacci(num - 2)

def fibonacci(num):
    try:
        num = int(num)
    except:
        return "Valor inserido inválido!"
    if num in memo:
        return memo[num]
    else:
        memo[num] = fibonacci(num - 1) + fibonacci(num - 2)
        return memo[num]


print(fibonacci(10))