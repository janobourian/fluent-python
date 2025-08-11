# Any
empty_iterable = []
print(any(empty_iterable))  # Output: False
list_of_numbers = [1, 2, 3, 4, 5]
mapped_numbers = map(lambda x: x % 2 == 0, list_of_numbers)
print(any(list(mapped_numbers)))  # Output: True

# All
mapped_numbers = map(lambda x: x % 2 == 0, list_of_numbers)
print(all(empty_iterable))  # Output: True
print(all(mapped_numbers))  # Output: False
