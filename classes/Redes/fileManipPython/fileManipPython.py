import os
import shutil

def exercicio1():
    for root, dirs, files in os.walk(".", topdown=True):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))


def exercicio2():
    # A
    os.getcwd()

    # B
    os.makedirs('SUBDIR1')
    os.makedirs('SUBDIR2')
    
    # C
    shutil.copy2('texto.txt', 'SUBDIR1')
    
    # D
    shutil.move('SUBDIR1/texto.txt', 'SUBDIR2/texto.txt')
    
    # E
    shutil.rmtree('SUBDIR1') # remoção de arquivos seria os.remove('path')

def exercicio3():
    f = open('teste.txt', 'w')
    f.write('Primeira linha\n')
    f.write('Segunda linha\n')
    f.read()
    f.close()

    f = open('teste.txt',' r')
    f.readline()
    f.readline()
    f.write('Terceira linha\n')
    f.close()

    f = open('teste.txt', 'r+')
    f.readline()
    f.writeline('Quarta linha\n')
    f.readline()
    f.seek(0,0)
    f.readlines()

def exercicio4():
    f = open('teste.txt','a+')
    f.write('l5\n')
    f.seek(0,0)
    f.readlines()
    f.close()

    f = open('teste.txt','w+')
    f.write('l6\n')
    f.seek(0,0)
    f.readlines()
    f.close()

    f = open('teste.txt','r+')
    f.write('l7\n')
    f.readlines()
    f.seek(0,0)
    f.readlines()
    f.close()

def exercicio5():
    f = open('teste.txt','rb')
    f.readline()
    f.readlines()
    f.close()

    f = open('teste.bin','wb+')
    f.write(bytearray([48,49,50]))
    f.seek(0,0)
    f.read()
    f.write('012')
    f.close()

    f = open('teste.bin','r+')
    f.read()
    f.write(bytearray([48,49,50]))
    f.write('012')
    f.seek(0,0)
    f.read()
    f.close()

exercicio1()
exercicio2()
exercicio3()
exercicio4()
