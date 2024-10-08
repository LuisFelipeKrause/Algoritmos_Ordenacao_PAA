from time import time
from random import shuffle

def heapify(lista, n, i):
    maior = i  # Inicializa o maior como raiz
    esquerda = 2 * i + 1     # Índice do filho esquerdo
    direita = 2 * i + 2      # Índice do filho direito
    comparacoes = 0  # Inicializa o contador de comparações

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
        # Chama heapify recursivamente na subárvore afetada
        sub_comparacoes = heapify(lista, n, maior)
        comparacoes += sub_comparacoes  # Acumula comparações do heapify recursivo

    return comparacoes  # Retorna o número total de comparações

def heap_sort(lista):
    n = len(lista)
    total_comparacoes = 0  # Inicializa o contador total de comparações

    # Constrói um heap (rearranja a lista)
    for i in range(n // 2 - 1, -1, -1):
        total_comparacoes += heapify(lista, n, i)

    # Um a um extrai elementos do heap
    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]  # Move a raiz atual para o final
        total_comparacoes += heapify(lista, i, 0)  # Chama heapify na raiz

    return lista, total_comparacoes  # Retorna a lista ordenada e o número total de comparações

tamanho = 100000

lista_ordenada = list(range(tamanho))
lista_inversamente_ordenada = list(range(tamanho, 0, -1))
lista_aleatoria = list(range(tamanho))
shuffle(lista_aleatoria)

inicio = time()
resultado, total_comparacoes = heap_sort(lista_aleatoria)
fim = time()

print(f"Tempo de execução: {(fim - inicio) * 1000:.2f} ms")
print(f"Número total de comparações: {total_comparacoes}")
