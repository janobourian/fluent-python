import random
from typing import List

random_list = [random.randint(0, 100) for _ in range(10)]
print("Unsorted list:", random_list)

def insert_sort(arr:List) -> List:
    for i in range(1, len(arr)):
        j = i - 1
        next_element = arr[i]
        while (arr[j] > next_element) and (j >= 0):
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = next_element
    return arr

inserted_sorted_list = insert_sort(random_list)
print("Sorted list:", inserted_sorted_list)