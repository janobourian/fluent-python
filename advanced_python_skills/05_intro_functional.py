fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
result = list(map(lambda fruit: fruit.capitalize(), fruits))
print(f"Capitalized fruits: {result}")

filtered_fruits = list(filter(lambda fruit: fruit.startswith('a') or fruit.startswith('e'), fruits))
print(f"Filtered fruits (starting with 'a' or 'e'): {filtered_fruits}")

fruits_with_price = {'apple': 1.2, 'banana': 0.5, 'cherry': 2.0, 'date': 3.0, 'elderberry': 4.5, 'fig': 2.5, 'grape': 1.8}
filtered_fruits_with_price = list(filter(lambda fruit: fruits_with_price[fruit] < 2.0, fruits_with_price))
print(f"Fruits with price less than 2.0: {filtered_fruits_with_price}")
filtered_fruits_dict_with_price = dict(filter(lambda item: item[1] < 2.0, fruits_with_price.items()))
print(f"Filtered fruits with price less than 2.0: {filtered_fruits_dict_with_price}")