from random import shuffle
from time import time

def bubble_sort(arr):
    comparacoes = 0  # Inicializa o contador de comparações
    trocas = 0       # Inicializa o contador de trocas
    for n in range(len(arr) - 1, 0, -1):
        for i in range(n):
            comparacoes += 1  # Incrementa o contador de comparações
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                trocas += 1  # Incrementa o contador de trocas
    
    return arr, comparacoes, trocas  # Retorna o array ordenado, número de comparações e trocas

tamanho = 1000

lista_ordenada = list(range(tamanho))
lista_inversamente_ordenada = list(range(tamanho, 0, -1))
lista_aleatoria = list(range(tamanho))
shuffle(lista_aleatoria)

inicio = time()
resultado, total_comparacoes, total_trocas = bubble_sort(lista_inversamente_ordenada)
fim = time()

print(f"Tempo de execução: {(fim - inicio) * 1000:.2f}ms")
print(f"Número total de comparações: {total_comparacoes}")
print(f"Número total de trocas: {total_trocas}")
