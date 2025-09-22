import random
from typing import List

random_list = [random.randint(0, 100000) for _ in range(100000)]
print("Unsorted list:", random_list)

def bubble_sort(arr: List) -> List:
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

sorted_list = bubble_sort(random_list)
print("Sorted list:", sorted_list)