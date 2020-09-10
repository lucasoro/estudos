# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?


import time

def main(start):
    
    memo = [True] * 1_000_000
    primos = [2]
    
    for i in range(3, len(memo)):
        if len(primos) >= 10001:
            break
        if i % 2:
            if memo[i]:
                primos.append(i)
                for j in range(i * i, len(memo), i):
                    memo[j] = False
    return primos[len(primos) - 1]


if __name__ == "__main__":
    start = time.time()
    print(main(start))
    total = time.time() - start
    print("Time: {:.3f} seconds".format(total))