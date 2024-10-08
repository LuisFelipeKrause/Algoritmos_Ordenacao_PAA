from random import shuffle
from time import time

def bubble_sort(arr):
    for n in range(len(arr) - 1, 0, -1):
        for i in range(n):
            if arr[i] > arr[i + 1]:
                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr


# Chamada da função para gerar as listas
tamanho = 1000

lista_ordenada = list(range(tamanho))
lista_inversamente_ordenada = list(range(tamanho, 0, -1))
lista_aleatoria = list(range(tamanho))
shuffle(lista_aleatoria)

inicio = time()
resultado = bubble_sort(lista_aleatoria)
fim = time()
print(f"Tempo de execução: {(fim - inicio) * 1000} ms")
