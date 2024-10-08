from random import shuffle
from time import time


def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        # Encontre o menor elemento na sublista [i:n]
        indice_minimo = i
        for j in range(i+1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        
        # Troca o menor elemento encontrado com o primeiro elemento não ordenado
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]


# Chamada da função para gerar as listas
tamanho = 50000

lista_ordenada = list(range(tamanho))
lista_inversamente_ordenada = list(range(tamanho, 0, -1))
lista_aleatoria = list(range(tamanho))
shuffle(lista_aleatoria)

inicio = time()
resultado = selection_sort(lista_inversamente_ordenada)
fim = time()
print(f"Tempo de execução: {(fim - inicio) * 1000} ms")