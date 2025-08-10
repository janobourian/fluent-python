def power_of_two(maximum=0):
    i = 0
    while i <= maximum:
        yield 2 ** i
        i += 1

for number in power_of_two(10):
    print(number)

numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
squared_numbers = (n ** 2 for n in numbers)

for squared in squared_numbers:
    print(squared)