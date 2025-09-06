def fibo(position=0):
    a, b = 0, 1
    for _ in range(position):
        a, b = b, a + b
    return a