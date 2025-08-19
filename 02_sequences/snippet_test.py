import timeit

TIMES = 1000

SETUP = """
def factorial(n):
    if n <= 1:
        return n
    return n * factorial(n-1)
"""

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.3f}'.format(x) for x in res))

clock('Factorial', '[factorial(x) for x in range(100)]')