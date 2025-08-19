# Single-line list comprehensions
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi']
new_fruits = [''.join(sorted(fruit)) for fruit in fruits]
print(new_fruits)

# Cartesian product using list comprehension
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']
sizes = ['small', 'medium', 'large']
combinations = [(color, size) for color in colors for size in sizes]
print(combinations)
dict_combinations = {f"{color}_{size}": (color, size) for color in colors for size in sizes}
print(dict_combinations)

# Single generator expression
new_fruits_gen = (''.join(sorted(fruit)) for fruit in fruits)
print(new_fruits_gen)
for fruit in new_fruits_gen:
    print(fruit)