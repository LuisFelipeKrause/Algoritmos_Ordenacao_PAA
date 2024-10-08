from random import shuffle
from time import time

def selection_sort(lista):
    n = len(lista)
    comparacoes = 0  # Inicializa o contador de comparações
    for i in range(n):
        # Encontra o menor elemento na sublista [i:n]
        indice_minimo = i
        for j in range(i + 1, n):
            comparacoes += 1  # Incrementa o contador de comparações
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        
        # Troca o menor elemento encontrado com o primeiro elemento não ordenado
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    
    return lista, comparacoes  # Retorna a lista ordenada e o número de comparações

tamanho = 1000

lista_ordenada = list(range(tamanho))
lista_inversamente_ordenada = list(range(tamanho, 0, -1))
lista_aleatoria = list(range(tamanho))
shuffle(lista_aleatoria)

inicio = time()
resultado, total_comparacoes = selection_sort(lista_inversamente_ordenada)
fim = time()

print(f"Tempo de execução: {(fim - inicio) * 1000:.2f}ms")
print(f"Número total de comparações: {total_comparacoes}")
