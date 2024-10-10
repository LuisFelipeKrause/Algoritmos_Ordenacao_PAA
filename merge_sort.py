from time import time
from random import shuffle

def merge_sort(lista, contador_comparacoes):
    if len(lista) > 1:
        meio = len(lista) // 2  # Encontra o meio da lista
        metade_esquerda = lista[:meio]  # Divide a lista na metade esquerda
        metade_direita = lista[meio:]   # Divide a lista na metade direita

        # Recursivamente divide as duas metades
        merge_sort(metade_esquerda, contador_comparacoes)
        merge_sort(metade_direita, contador_comparacoes)

        # Índices para as sublistas
        i = j = k = 0

        # Ordena as duas metades
        while i < len(metade_esquerda) and j < len(metade_direita):
            contador_comparacoes += 1  # Incrementa o contador de comparações
            if metade_esquerda[i] < metade_direita[j]:
                lista[k] = metade_esquerda[i]
                i += 1
            else:
                lista[k] = metade_direita[j]
                j += 1
            k += 1
            trocas += 1

        # Verifica se ainda há elementos na metade esquerda
        while i < len(metade_esquerda):
            lista[k] = metade_esquerda[i]
            i += 1
            k += 1
            trocas += 1

        # Verifica se ainda há elementos na metade direita
        while j < len(metade_direita):
            lista[k] = metade_direita[j]
            j += 1
            k += 1
            trocas += 1
    return lista, contador_comparacoes  # Retorna a lista ordenada e o número de comparações

tamanho = 1000

lista_ordenada = list(range(tamanho))
lista_inversamente_ordenada = list(range(tamanho, 0, -1))
lista_aleatoria = list(range(tamanho))
shuffle(lista_aleatoria)

trocas = 0
contador_comparacoes = 0  # Inicializa o contador de comparações
inicio = time()
resultado, total_comparacoes = merge_sort(lista_ordenada, contador_comparacoes)
fim = time()

print(f"Tempo de execução: {(fim - inicio) * 1000:.2f}ms")
print(f"Número total de comparações: {total_comparacoes}")
print(f"Número total de trocas: {trocas}")