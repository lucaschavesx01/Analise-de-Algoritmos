import time
import random

def quick_sort(arr):
    comparisons = [0]  # Utilizamos uma lista para passar a variável por referência
    swaps = [0]  # Utilizamos uma lista para passar a variável por referência
    _quick_sort(arr, 0, len(arr) - 1, comparisons, swaps)

def _quick_sort(arr, low, high, comparisons, swaps):
    if low < high:
        partition_index, comp, swp = partition(arr, low, high)
        comparisons[0] += comp
        swaps[0] += swp

        _quick_sort(arr, low, partition_index - 1, comparisons, swaps)
        _quick_sort(arr, partition_index + 1, high, comparisons, swaps)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    comparisons = 0
    swaps = 0

    for j in range(low, high):
        comparisons += 1
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    swaps += 1

    return i + 1, comparisons, swaps

def generate_random_list(size):
    return random.sample(range(size * 3), size)

def main():
    sizes = [1000, 10000, 100000]

    for size in sizes:
        print(f"\nSorting for size: {size}")
        # Best case: Already sorted
        sorted_list = list(range(size))
        start_time = time.time()
        comparisons = [0]
        swaps = [0]
        quick_sort(sorted_list)
        end_time = time.time()
        print(f"Best case: {end_time - start_time:.6f} seconds")
        print(f"Comparisons: {comparisons[0]}, Swaps: {swaps[0]}")

        # Average case: Random order
        random_list = generate_random_list(size)
        start_time = time.time()
        comparisons = [0]
        swaps = [0]
        quick_sort(random_list)
        end_time = time.time()
        print(f"Average case: {end_time - start_time:.6f} seconds")
        print(f"Comparisons: {comparisons[0]}, Swaps: {swaps[0]}")

        # Worst case: Descending order
        descending_list = list(range(size, 0, -1))
        start_time = time.time()
        comparisons = [0]
        swaps = [0]
        quick_sort(descending_list)
        end_time = time.time()
        print(f"Worst case: {end_time - start_time:.6f} seconds")
        print(f"Comparisons: {comparisons[0]}, Swaps: {swaps[0]}")

if _name_ == "_main_":
    main()