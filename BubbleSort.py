import time
import random

def bubble_sort(arr):
    n = len(arr)
    trocas = 0
    comparacoes = 0

    for i in range(n):
        trocas_passo = 0
        for j in range(0, n-i-1):
            comparacoes += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                trocas += 1
                trocas_passo += 1

        # Se não houve trocas nesta passagem, a lista está ordenada
        if trocas_passo == 0:
            break

    return trocas, comparacoes

def run_bubble_sort(size, caso):
    if caso == 'melhor':
        arr = list(range(1, size + 1))  # Lista já ordenada
    elif caso == 'pior':
        arr = list(range(size, 0, -1))  # Lista em ordem decrescente
    elif caso == 'medio':
        arr = random.sample(range(1, size + 1), size)  # Lista com valores aleatórios

    inicio = time.time()
    trocas, comparacoes = bubble_sort(arr.copy())
    fim = time.time()

    print(f'\nCaso {caso.capitalize()} (Tamanho: {size}):')
    print(f'Lista Ordenada: {arr}')
    print(f'Tempo de Execução: {fim - inicio:.6f} segundos')
    print(f'Quantidade de Trocas: {trocas}')
    print(f'Quantidade de Comparações: {comparacoes}')

# Testando com diferentes tamanhos e casos
run_bubble_sort(1000, 'melhor')
run_bubble_sort(1000, 'medio')
run_bubble_sort(1000, 'pior')

run_bubble_sort(10000, 'melhor')
run_bubble_sort(10000, 'medio')
run_bubble_sort(10000, 'pior')
