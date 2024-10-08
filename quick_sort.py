from time import time
from random import shuffle

def quicksort(arr):
    if len(arr) <= 1:
        return arr, 0  # Se a lista tiver 1 ou menos elementos, não há comparações

    pivot = arr[0]
    left = []
    right = []
    comparacoes = 0  # Inicializa o contador de comparações

    for x in arr[1:]:
        comparacoes += 1  # Incrementa o contador de comparações
        if x < pivot:
            left.append(x)
        else:
            right.append(x)

    left_sorted, left_comparacoes = quicksort(left)
    right_sorted, right_comparacoes = quicksort(right)

    # Total de comparações feitas
    total_comparacoes = comparacoes + left_comparacoes + right_comparacoes
    return left_sorted + [pivot] + right_sorted, total_comparacoes  # Retorna a lista ordenada e o número de comparações

tamanho = 1000

lista_ordenada = list(range(tamanho))
lista_inversamente_ordenada = list(range(tamanho, 0, -1))
lista_aleatoria = list(range(tamanho))
shuffle(lista_aleatoria)

resultado, total_comparacoes = quicksort(lista_aleatoria)

inicio = time()
resultado, total_comparacoes = quicksort(lista_aleatoria)
fim = time()

print(f"Tempo de execução: {(fim - inicio) * 1000:.2f} ms")
print(f"Número total de comparações: {total_comparacoes}")
