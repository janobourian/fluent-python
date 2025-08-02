fruits = ["apple", "banana", "cherry", "date", "elderberry"]
enumerate_fruits = list(enumerate(fruits, start=0))

for index, fruit in enumerate_fruits:
    print(f"{fruit}{index}.jpg")