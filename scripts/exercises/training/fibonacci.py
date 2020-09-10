# Dynamic programming (?)

# 0, 1, 2, 3, 5, 8, 13, 21, 34, 55... --> Fib_n = (fib_n - 1) + (fib_n - 2)

import time, multiprocessing

def naive_fib(numero, queue):
    if numero == 1:
        return 0
    elif numero == 2:
        return 1
    else:
        # queue.put(naive_fib((numero - 1), queue) + naive_fib((numero - 2), queue))
        return naive_fib((numero - 1), queue) + naive_fib((numero - 2), queue)


memo = [0, 1]

def dynamic_fib(numero, queue):
    if numero <= len(memo):
        return memo[numero - 1]
    elif numero in memo:
        return numero
    else:
        local = (dynamic_fib((numero - 1), queue) + dynamic_fib((numero - 2), queue))
        memo.append(local)
        # queue.put((dynamic_fib((numero - 1), queue) + dynamic_fib((numero - 2), queue)))
        return local

def main():
    manager = multiprocessing.Manager()
    queue = manager.Queue()
    fib1 = multiprocessing.Process(target=naive_fib, args=(9, queue))
    fib2 = multiprocessing.Process(target=dynamic_fib, args=(9, queue))
    fib1.start()
    fib2.start()
    while not queue.empty():
        print(queue.get())


if __name__ == "__main__":
    main()