import multiprocessing
import time
import random

def teste():
    for i in range(1, 10):
        print("Olá", i)
        time.sleep(random.randint(1, 4))

processos = []

def main():
    for i in range(multiprocessing.cpu_count()): 
        processo = multiprocessing.Process(target=teste)
        processos.append(processo)
        processo.start()
    # for processo in processos:
    #     processo.join()

if __name__ == "__main__":
    main()
