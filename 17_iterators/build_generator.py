def my_generator(value = 0):
    while value < 5:
        yield value
        value += 1

it = my_generator()
print(it)

for i in it:
    print(i)