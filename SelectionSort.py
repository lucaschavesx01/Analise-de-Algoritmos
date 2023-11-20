import time
import random

def selection_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
        swaps += 1

    return comparisons, swaps

def generate_input(size, case):
    if case == "best":
        return list(range(1, size + 1))
    elif case == "average":
        return random.sample(range(1, size + 1), size)
    elif case == "worst":
        return list(range(size, 0, -1))

def run_experiment(size, case):
    arr = generate_input(size, case)
    start_time = time.time()

    comparisons, swaps = selection_sort(arr)

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Case: {case.capitalize()} Case")
    print(f"Input Size: {size}")
    print(f"Sorted List: {arr}")
    print(f"Execution Time: {execution_time:.6f} seconds")
    print(f"Comparisons: {comparisons}")
    print(f"Swaps: {swaps}")
    print("\n" + "-"*40 + "\n")

if _name_ == "_main_":
    sizes = [1000, 10000, 100000]

    for size in sizes:
        run_experiment(size, "best")
        run_experiment(size, "average")
        run_experiment(size, "worst")