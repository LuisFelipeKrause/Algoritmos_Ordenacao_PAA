from time import time
from random import shuffle

def partition(array, inicio, fim, comparacoes, trocas):
    pivot = array[fim]
    i = inicio - 1
    for j in range(inicio, fim):
        comparacoes[0] += 1
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
            trocas[0] += 1
    array[i + 1], array[fim] = array[fim], array[i + 1]
    trocas[0] += 1
    return i + 1

def quicksort(array, comparacoes, trocas):
    lista_aux = [(0, len(array) - 1)]

    while lista_aux:
        inicio, fim = lista_aux.pop()
        if inicio < fim:
            pivot_index = partition(array, inicio, fim, comparacoes, trocas)

            lista_aux.append((inicio, pivot_index - 1))
            lista_aux.append((pivot_index + 1, fim))

    return array

tamanho = 1000

lista_ordenada = list(range(tamanho))
lista_inversamente_ordenada = list(range(tamanho, 0, -1))
lista_aleatoria = list(range(tamanho))
shuffle(lista_aleatoria)

comparacoes = [0]
trocas = [0]

inicio = time()
resultado = quicksort(lista_inversamente_ordenada, comparacoes, trocas)
fim = time()

# Exibindo os resultados
print(f"Tempo de execução: {(fim - inicio) * 1000:.2f} ms")
print(f"Número total de comparações: {comparacoes[0]}")
print(f"Número total de trocas: {trocas[0]}")
