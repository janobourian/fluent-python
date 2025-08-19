import random

fruits = ['tangerine', 'nectarine', 'grape', 'honeydew', 'lemon', 'vanilla bean', 'quince', 'ugli fruit', 'cherry', 'date', 'papaya', 'raspberry', 'banana', 'apple', 'strawberry', 'mango', 'kiwi', 'fig', 'orange', 'elderberry']
fruits.sort()
print(fruits)

result = sorted(fruits, key=len, reverse=True)
print(result)