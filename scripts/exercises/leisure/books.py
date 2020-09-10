"""
Problem
Supervin is a librarian handling an ancient book with N pages, numbered from 1 to N. Since the book is too old, unfortunately M pages are torn out: page number P1, P2, ..., PM.

Today, there are Q lazy readers who are interested in reading the ancient book. Since they are lazy, each reader will not necessarily read all the pages. Instead, the i-th reader will only read the pages that are numbered multiples of Ri and not torn out. Supervin would like to know the sum of the number of pages read by each reader.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing the three integers N, M, and Q, the number of pages in the book, the number of torn out pages in the book, and the number of readers, respectively. The second line contains M integers, the i-th of which is Pi. The third line contains Q integers, the i-th of which is Ri.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the total number of pages that will be read by all readers.
"""
# Início do Código

#pylint: disable=W0612
def verificacao(total, qtde_rasg, qtde_pessoas, rasgadas, pessoas):
    contador = 0
    for pessoa in pessoas:
        multiplo = int(pessoa)
        livro = [x for x in range(1, total + 1)]
        for pagina in livro:
            if (not(pagina % multiplo) and (not (str(pagina) in rasgadas))):
                contador += 1
    print(contador)


def tratamento():
    array = [str(input()), str(input()), str(input())]
    for termo in array:
        try:
            termo = [termo.split(" ")]
        except:
            continue
    total_pag = int(array[0].split(" ")[0])
    num_pag_rasg = int(array[0].split(" ")[1])
    numeros_leitores = int(array[0].split(" ")[2])
    try:
        segunda_linha = array[1].split(" ")
    except TypeError:
        segunda_linha = array[1]
    try:
        terceira_linha = array[2].split(" ")
    except TypeError:
        terceira_linha = array[2]
    verificacao(total_pag, num_pag_rasg, numeros_leitores, segunda_linha, terceira_linha)


def main():
    try:
        for i in range(int(input())):
            tratamento()
    except:
        main()


if __name__ == "__main__":
    main()