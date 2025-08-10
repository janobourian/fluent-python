def fibonacci_numbers(n):
    a, b = 0, 1
    i = 0
    while i <= n:
        yield a
        i = i + 1
        a, b = b, a + b

for number in fibonacci_numbers(100):
    print(number)