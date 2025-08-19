import timeit

TIMES = 100000
SETUP = """
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi']
"""

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.3f}'.format(x) for x in res))

clock('List comprehension', '[x**2 for x in range(10)]')
clock('Generator expression', '(x**2 for x in range(10))')
clock('List comprehension with sorted', "[''.join(sorted(fruit)) for fruit in fruits]")
clock('Generator expression with sorted', "(''.join(sorted(fruit)) for fruit in fruits)")
clock('List comprehension with join', "[''.join(fruit) for fruit in fruits]")
clock('Generator expression with join', "(''.join(fruit) for fruit in fruits)")