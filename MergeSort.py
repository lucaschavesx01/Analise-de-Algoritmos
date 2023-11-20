import time
import random

def merge_sort(arr):
    if len(arr) > 1:
        meio = len(arr) // 2
        parte_esquerda = arr[:meio]
        parte_direita = arr[meio:]

        merge_sort(parte_esquerda)
        merge_sort(parte_direita)

        i = j = k = 0

        while i < len(parte_esquerda) and j < len(parte_direita):
            if parte_esquerda[i] < parte_direita[j]:
                arr[k] = parte_esquerda[i]
                i += 1
            else:
                arr[k] = parte_direita[j]
                j += 1
            k += 1

        while i < len(parte_esquerda):
            arr[k] = parte_esquerda[i]
            i += 1
            k += 1

        while j < len(parte_direita):
            arr[k] = parte_direita[j]
            j += 1
            k += 1

def estudar_ordenacao(tamanho, caso):
    if caso == "melhor":
        arr = list(range(tamanho))
        random.shuffle(arr)
    elif caso == "medio":
        arr = random.sample(range(tamanho * 3), tamanho)
    elif caso == "pior":
        arr = list(range(tamanho, 0, -1))
    else:
        raise ValueError("Caso inválido")

    inicio = time.time()
    trocas, comparacoes = [0, 0]

    # Medindo o tempo de execução, trocas e comparações
    def merge_sort_contador(arr):
        nonlocal trocas, comparacoes
        if len(arr) > 1:
            meio = len(arr) // 2
            parte_esquerda = arr[:meio]
            parte_direita = arr[meio:]

            merge_sort_contador(parte_esquerda)
            merge_sort_contador(parte_direita)

            i = j = k = 0

            while i < len(parte_esquerda) and j < len(parte_direita):
                comparacoes += 1
                if parte_esquerda[i] < parte_direita[j]:
                    arr[k] = parte_esquerda[i]
                    i += 1
                else:
                    arr[k] = parte_direita[j]
                    j += 1
                k += 1
                trocas += 1

            while i < len(parte_esquerda):
                arr[k] = parte_esquerda[i]
                i += 1
                k += 1
                trocas += 1

            while j < len(parte_direita):
                arr[k] = parte_direita[j]
                j += 1
                k += 1
                trocas += 1

    merge_sort_contador(arr)
    fim = time.time()
    tempo_execucao = fim - inicio

    print(f"Caso: {caso.capitalize()} - Tamanho: {tamanho}")
    print("Tempo de execução:", tempo_execucao)
    print("Quantidade de trocas:", trocas)
    print("Quantidade de comparações:", comparacoes)
    print("Lista ordenada:", arr)
    print("\n")

# Testando para os casos especificados
estudar_ordenacao(1000, "melhor")
estudar_ordenacao(1000, "medio")
estudar_ordenacao(1000, "pior")

estudar_ordenacao(10000, "melhor")
estudar_ordenacao(10000, "medio")
estudar_ordenacao(10000, "pior")

estudar_ordenacao(100000, "melhor")
estudar_ordenacao(100000, "medio")
estudar_ordenacao(100000, "pior")