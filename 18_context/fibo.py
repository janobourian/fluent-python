def fibo(n):
    a, b = 0, 1
    total_iterations = 0
    yield a
    total_iterations += 1
    while total_iterations < n:
        yield b
        a, b = b, a+b
        total_iterations += 1

for fibonacci_number in fibo(100):
    print(fibonacci_number)