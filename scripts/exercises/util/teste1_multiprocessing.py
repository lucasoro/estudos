import time, random, multiprocessing

def teste1(queue):
    count = 0
    while True:
        print(random.randint(1, 150), "teste 1 , valor impresso %i" %count)
        time.sleep(random.randint(1, 3))
        count += 1
        queue.put(count)
        if count > 2:
            return queue


def teste2(queue):
    count = 0
    while True:
        print(random.randint(1, 150), "teste 2 , valor impresso %i" %count)
        time.sleep(random.randint(1, 3))
        count += 1
        queue.put(count)
        if count > 2:
            return queue


def main():
    matrix = []
    queue = multiprocessing.Queue(6)
    processos = [teste1, teste2]
    for processo in processos:
        proc = multiprocessing.Process(target=processo, args=(queue,))
        proc.start()
        proc.join()

    # pylint: disable= locally-disabled, unused-variable
    for i in range(queue.qsize()):
        matrix.append(queue.get())
    # pylint: enable= unused-variable

    print(matrix)

if __name__ == "__main__":
    main()
