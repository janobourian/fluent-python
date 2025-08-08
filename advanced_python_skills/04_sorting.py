# Sort and Sorted
# Sort is a list method 
# Sorted is a function for iterables

fruits = ['banana', 'apple', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'kiwi', 'lemon']
fruits.sort()
print("Sorted fruits using sort():", fruits)

sorted_fruits = sorted(fruits, reverse=True)
print("Sorted fruits using sorted():", sorted_fruits)

fruits_dict = {'banana': 3, 'apple': 1, 'cherry': 2, 'date': 4, 'elderberry': 5, 'fig': 6, 'grape': 7, 'kiwi': 8, 'lemon': 9}
sorted_fruits_dict = sorted(fruits_dict, key=lambda item: fruits_dict[item])
print("Sorted fruits_dict using sorted():", sorted_fruits_dict)