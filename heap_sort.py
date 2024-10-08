from time import time
from random import shuffle


def heapify(lista, n, i):
    maior = i  # Inicializa o maior como raiz
    esquerda = 2 * i + 1     # Índice do filho esquerdo
    direita = 2 * i + 2      # Índice do filho direito

    # Verifica se o filho esquerdo é maior que a raiz
    if esquerda < n and lista[esquerda] > lista[maior]:
        maior = esquerda

    # Verifica se o filho direito é maior que o maior até agora
    if direita < n and lista[direita] > lista[maior]:
        maior = direita

    # Troca a raiz com o maior, se necessário
    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]  # Troca
        # Chama heapify recursivamente na subárvore afetada
        heapify(lista, n, maior)

def heap_sort(lista):
    n = len(lista)

    # Constrói um heap (rearranja a lista)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    # Um a um extrai elementos do heap
    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]  # Move a raiz atual para o final
        heapify(lista, i, 0)  # Chama heapify na raiz
    return lista


tamanho = 100000

lista_ordenada = list(range(tamanho))
lista_inversamente_ordenada = list(range(tamanho, 0, -1))
lista_aleatoria = list(range(tamanho))
shuffle(lista_aleatoria)

inicio = time()
resultado = heap_sort(lista_inversamente_ordenada)
fim = time()
print(f"Tempo de execução: {(fim - inicio) * 1000} ms")
