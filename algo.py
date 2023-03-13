#percorre a lista inteira ate achar o menor indice 
def selection_sort(lista):
    n = len(lista)    
    for j in range(n-1):
        min_index = j
        for i in range(j, n):
            if lista[i] < lista[min_index]:
                min_index = i
        
        if lista[j] > lista[min_index]:
            memoria = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = memoria 

#verifica o proximo indice e se for mnor faz a troca 
def bubble_sort (lista):
    n = len(lista)
    for f in range(n-1):
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                
#cria mini tabelas e vai adicionando conforme o indice
def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        memoria = lista[i]
        j = i - 1
        
        while j >= 0 and lista[j] > memoria:
            lista[j+1] = lista[j]
            j = j - 1
        lista[j + 1] = memoria 
    
