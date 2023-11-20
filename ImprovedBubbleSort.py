import time
import random

def improved_bubble_sort(arr):
    n = len(arr)
    swaps = 0
    comparisons = 0

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True

        if not swapped:
            break

    return swaps, comparisons


def generate_list(size, case_type):
    if case_type == 'ascending':
        return list(range(1, size + 1))
    elif case_type == 'descending':
        return list(range(size, 0, -1))
    elif case_type == 'random':
        return random.sample(range(1, size + 1), size)


def run_experiment(size, case_type):
    data = generate_list(size, case_type)

    start_time = time.time()
    swaps, comparisons = improved_bubble_sort(data.copy())
    end_time = time.time()

    print(f"Case Type: {case_type.capitalize()} - Size: {size}")
    print("Sorted List:", data)
    print("Time: {:.6f} seconds".format(end_time - start_time))
    print("Swaps:", swaps)
    print("Comparisons:", comparisons)
    print("\n")


if _name_ == "_main_":
    sizes = [1000, 10000, 100000]

    for size in sizes:
        run_experiment(size, 'ascending')  # Best case: Already sorted
        run_experiment(size, 'random')     # Average case: Random order
        run_experiment(size, 'descending')  # Worst case: Descending order