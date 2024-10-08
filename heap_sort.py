from time import time
from random import shuffle

def heapify(lista, n, i):
    maior = i  # Inicializa o maior como raiz
    esquerda = 2 * i + 1     # Índice do filho esquerdo
    direita = 2 * i + 2      # Índice do filho direito
    comparacoes = 0  # Inicializa o contador de comparações
    trocas = 0  # Inicializa o contador de trocas

    # Verifica se o filho esquerdo é maior que a raiz
    if esquerda < n:
        comparacoes += 1  # Incrementa o contador de comparações
        if lista[esquerda] > lista[maior]:
            maior = esquerda

    # Verifica se o filho direito é maior que o maior até agora
    if direita < n:
        comparacoes += 1  # Incrementa o contador de comparações
        if lista[direita] > lista[maior]:
            maior = direita

    # Troca a raiz com o maior, se necessário
    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]  # Troca
        trocas += 1  # Incrementa o contador de trocas
        # Chama heapify recursivamente na subárvore afetada
        sub_comparacoes, sub_trocas = heapify(lista, n, maior)
        comparacoes += sub_comparacoes  # Acumula comparações do heapify recursivo
        trocas += sub_trocas  # Acumula trocas do heapify recursivo

    return comparacoes, trocas  # Retorna o número total de comparações e trocas

def heap_sort(lista):
    n = len(lista)
    total_comparacoes = 0  # Inicializa o contador total de comparações
    total_trocas = 0  # Inicializa o contador total de trocas

    # Constrói um heap (rearranja a lista)
    for i in range(n // 2 - 1, -1, -1):
        comparacoes, trocas = heapify(lista, n, i)
        total_comparacoes += comparacoes
        total_trocas += trocas

    # Um a um extrai elementos do heap
    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]  # Move a raiz atual para o final
        total_trocas += 1  # Incrementa o contador de trocas
        comparacoes, trocas = heapify(lista, i, 0)  # Chama heapify na raiz
        total_comparacoes += comparacoes
        total_trocas += trocas

    return lista, total_comparacoes, total_trocas  # Retorna a lista ordenada, número total de comparações e trocas

tamanho = 10000

lista_ordenada = list(range(tamanho))
lista_inversamente_ordenada = list(range(tamanho, 0, -1))
lista_aleatoria = list(range(tamanho))
shuffle(lista_aleatoria)

inicio = time()
resultado, total_comparacoes, total_trocas = heap_sort(lista_ordenada)
fim = time()

print(f"Tempo de execução: {(fim - inicio) * 1000:.2f} ms")
print(f"Número total de comparações: {total_comparacoes}")
print(f"Número total de trocas: {total_trocas}")
