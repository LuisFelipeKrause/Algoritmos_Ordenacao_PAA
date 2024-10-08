from time import time
from random import shuffle

def insertion_sort(lista):
    comparacoes = 0  # Inicializa o contador de comparações
    trocas = 0       # Inicializa o contador de trocas
    # Percorre a lista começando do segundo elemento
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        # Move os elementos da lista[0...i-1] que são maiores que a chave
        # para uma posição à frente de sua posição atual
        while j >= 0:
            comparacoes += 1  # Incrementa o contador de comparações
            if lista[j] > chave:
                lista[j + 1] = lista[j]
                trocas += 1  # Incrementa o contador de trocas
                j -= 1
            else:
                break  # Sai do loop se não for necessário mover
        lista[j + 1] = chave
        if j + 1 != i:  # Verifica se houve realmente uma troca
            trocas += 1  # Incrementa o contador de trocas
    
    return lista, comparacoes, trocas  # Retorna a lista ordenada, número de comparações e trocas

tamanho = 1000

lista_ordenada = list(range(tamanho))
lista_inversamente_ordenada = list(range(tamanho, 0, -1))
lista_aleatoria = list(range(tamanho))
shuffle(lista_aleatoria)

inicio = time()
resultado, total_comparacoes, total_trocas = insertion_sort(lista_ordenada)
fim = time()

print(f"Tempo de execução: {(fim - inicio) * 1000:.2f}ms")
print(f"Número total de comparações: {total_comparacoes}")
print(f"Número total de trocas: {total_trocas}")
