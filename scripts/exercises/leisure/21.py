# THIS CODE DOES NOT BELONGS TO ME! ESSE CÓDIGO NÃO FOI ESCRITO POR MIM!

import random
import multiprocessing
import math
import time

#Config

simulations = 1_000_000
num_decks = 4
shuffle_perc = 75

def simulate(queue, batch_size):
    deck = []

    def new_deck():
        std_deck = [
#           2  3  4  5  6  7  8  9  10  J   Q   K   A
            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,

        ]
        # adicionar mais baralhos
        std_deck = std_deck * num_decks

        random.shuffle(std_deck)

        return std_deck[:]

    def play_hand():
        dealer = []
        player = []

        player.append(deck.pop(0))
        dealer.append(deck.pop(0))
        player.append(deck.pop(0))
        dealer.append(deck.pop(0))

        while sum(player) < 12:
            player.append(deck.pop(0))

        while sum(dealer) < 18:
            exit = False
            if sum(dealer) == 17:
                exit = True
                for i, card in enumerate(dealer):
                    if card == 11:
                        exit = False
                        dealer[i] = 1

            if exit:
                break
            dealer.append(deck.pop(0))
        
        soma_p = sum(player)
        soma_d = sum(dealer)

        if soma_d > 21:
            return 1
        if soma_d == soma_p:
            return 0
        if soma_d > soma_p:
            return -1
        if soma_d < soma_p:
            return 1

    deck = new_deck()

    win = 0
    draw = 0
    lose = 0

    for i in range(0, batch_size): #pylint: disable=W0612
        if(float(len(deck)) / (52 * num_decks)) * 100 < shuffle_perc:
            deck = new_deck()
        
        result = play_hand()

        if result == 1:
            win += 1
        if result == 0:
            draw += 1
        if result == -1:
            lose += 1

    queue.put([win, draw, lose])

    
start_time = time.time()

cpus = multiprocessing.cpu_count()
batch_size = int(math.ceil(simulations/float(cpus)))

queue = multiprocessing.Queue()

processes = []

def main():
    for i in range(0, cpus): #pylint: disable=W0612
        process = multiprocessing.Process(target=simulate, args=(queue, batch_size))
        processes.append(process)
        process.start()

    for proc in processes:
        proc.join()

    finish_time = time.time() - start_time

    win = 0
    draw = 0
    lose = 0

    for i in range(cpus):
        result = queue.get()
        win += result[0]
        draw += result[1]
        lose += result[2]


    print
    print('Cores utilizados: %d' %cpus)
    print('Total de simulações: %d' %simulations)
    print('Simulações por segundo: %d' %(float(simulations)/finish_time))
    print('Tempo de execução: %.2fs' %finish_time)
    print('Procentagem de vitórias: %.2f%%' %(win/float(simulations)* 100))
    print('Procentagem de Empates: %.2f%%' %(draw/float(simulations)* 100))
    print('Procentagem de Derrotas: %.2f%%' %(lose/float(simulations)* 100))
    print

if __name__ == "__main__":
    main()
