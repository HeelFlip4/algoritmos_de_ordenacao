from algoritmos import selection_sort, bubble_sort, insertion_sort
import os
from time import sleep 
import random 

if __name__ == "__main__":
    
    with open('/home/paiva/Área de Trabalho/bk/Projetos.py/projetoPY/Algoritmos/sla.txt', 'r') as arquivo:   
        conteudo = arquivo.read()
    print(conteudo)
    sleep(2)
    os.system('clear')
    
    ''''
    for _ in range(10):
        pontos = ['', '.', '..', '...']
        for _ in range(len(pontos)):
            os.system('clear')
            print('carregando', pontos[_])
            sleep(0.3)
            os.system('clear')'''
            
    put = input(f'ordernação vai ser por ?\n 1 - um arquivo \n 2 - Digite uma lista \n 3 - uma lista aleatoria: ')        
    os.system('clear')
    lista = []
    
    if put == '1':
        path = input('qual o endereço do arquivo: ')
        with open(path, 'r') as arquivo:   
            listastr = arquivo.read()
            inteiros = listastr.split(",")
            lista = []
        for n1 in inteiros:
            lista.append(int(n1))
        print(f'sua lista vai ser', lista, '\n')
            
    elif put == '2':
        listastr = input("Insira os valores separados por vírgula: ")
        inteiros = listastr.split(",")
        lista = []
        for n1 in inteiros:
            lista.append(int(n1))
        print(f'sua lista vai ser', lista, '\n')
            
    elif put == '3':
        numero_aleatorio = random.sample(range(1,1000), 15)
        lista = numero_aleatorio
        print(f'sua lista vai ser', lista, '\n')
    
    print('--------------------------------------------------\n')
    funcao = input(f'e qual algoritmos quer usar? \n 1 - selection \n 2 - bubble \n 3 - insertion \n')
    os.system('clear')
    print('--------------------------------------------------\n')
    
    if funcao == '1':
        print(lista, f'\n')
        selection_sort(lista)
        print(lista, '\n')
    
    elif funcao == '2':
        print(lista, f'\n')
        bubble_sort(lista)
        print(lista, '\n')
    
    elif funcao == '3':
        print(lista, f'\n')
        insertion_sort(lista) 
        print(lista, '\n')   
        

 

