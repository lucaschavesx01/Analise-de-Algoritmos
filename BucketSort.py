import time
import random

def bucket_sort(arr):
    buckets = [[] for _ in range(len(arr))]
    for num in arr:
        index = int(num * len(arr))
        buckets[index].append(num)

    for i in range(len(buckets)):
        buckets[i] = sorted(buckets[i])

    result = []
    for bucket in buckets:
        result.extend(bucket)
    
    return result

def generate_input(size, case_type):
    if case_type == 'sorted':
        return list(range(1, size + 1))
    elif case_type == 'reverse_sorted':
        return list(range(size, 0, -1))
    elif case_type == 'random':
        return random.sample(range(1, size + 1), size)

def analyze_sorting(arr):
    comparisons = 0
    swaps = 0

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            comparisons += 1
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1

    return swaps, comparisons

def run_test(size, case_type):
    input_data = generate_input(size, case_type)
    
    start_time = time.time()
    sorted_data = bucket_sort(input_data.copy())
    end_time = time.time()

    swaps, comparisons = analyze_sorting(sorted_data)

    print(f"Case Type: {case_type.capitalize()}")
    print(f"Input Size: {size}")
    print(f"Sorted List: {sorted_data}")
    print(f"Execution Time: {end_time - start_time} seconds")
    print(f"Swaps: {swaps}")
    print(f"Comparisons: {comparisons}\n")

# Test cases
input_sizes = [1000, 10000, 100000]

for size in input_sizes:
    run_test(size, 'sorted')  # Best Case: Already sorted
    run_test(size, 'random')  # Average Case: Random order
    run_test(size, 'reverse_sorted')  # Worst Case: Sorted in descending order