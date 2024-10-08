from time import time
from random import shuffle


def insertion_sort(lista):
    # Percorre a lista começando do segundo elemento
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        # Move os elementos da lista[0...i-1] que são maiores que a chave
        # para uma posição à frente de sua posição atual
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista


tamanho = 1000

lista_ordenada = list(range(tamanho))
lista_inversamente_ordenada = list(range(tamanho, 0, -1))
lista_aleatoria = list(range(tamanho))
shuffle(lista_aleatoria)

inicio = time()
resultado = insertion_sort(lista_inversamente_ordenada)
fim = time()
print(f"Tempo de execução: {(fim - inicio) * 1000} ms")
