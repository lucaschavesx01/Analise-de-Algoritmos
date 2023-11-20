import time
import random

def insertion_sort(arr):
    comparisons = 0
    swaps = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            comparisons += 1
            swaps += 1
        arr[j + 1] = key
        swaps += 1
    return comparisons, swaps

def generate_random_list(size):
    return [random.randint(1, 1000000) for _ in range(size)]

def generate_sorted_list(size, reverse=False):
    return list(range(size, 0, -1)) if reverse else list(range(1, size + 1))

def run_insertion_sort_and_measure(arr):
    start_time = time.time()
    comparisons, swaps = insertion_sort(arr)
    end_time = time.time()
    execution_time = end_time - start_time
    return comparisons, swaps, execution_time

def perform_study(size):
    print(f"Size: {size}")
    
    # Best case: Sorted in ascending order
    arr = generate_sorted_list(size)
    comparisons, swaps, execution_time = run_insertion_sort_and_measure(arr)
    print(f"\nBest Case (Sorted in ascending order):")
    print(f"Execution Time: {execution_time:.6f} seconds")
    print(f"Comparisons: {comparisons}")
    print(f"Swaps: {swaps}")
    print("Sorted List:", arr)

    # Average case: Random order
    arr = generate_random_list(size)
    comparisons, swaps, execution_time = run_insertion_sort_and_measure(arr)
    print(f"\nAverage Case (Random order):")
    print(f"Execution Time: {execution_time:.6f} seconds")
    print(f"Comparisons: {comparisons}")
    print(f"Swaps: {swaps}")
    print("Sorted List:", arr)

    # Worst case: Sorted in descending order
    arr = generate_sorted_list(size, reverse=True)
    comparisons, swaps, execution_time = run_insertion_sort_and_measure(arr)
    print(f"\nWorst Case (Sorted in descending order):")
    print(f"Execution Time: {execution_time:.6f} seconds")
    print(f"Comparisons: {comparisons}")
    print(f"Swaps: {swaps}")
    print("Sorted List:", arr)

# Perform study for different sizes
perform_study(1000)
perform_study(10000)
perform_study(100000)