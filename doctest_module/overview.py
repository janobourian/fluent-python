"""
This is the 'example' module.

The example module supplies one function, fibonacci(n). For example:

>>> fibonacci(10)
34
>>> [fibonacci(n) for n in range(1, 11)]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
"""

def fibonacci(n):
    """
    Returns the nth Fibonacci number.
    >>> fibonacci(1)
    0
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    1
    >>> fibonacci(4)
    2
    >>> fibonacci(5)
    3
    >>> fibonacci(6)
    5
    >>> [fibonacci(n) for n in range(1, 11)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(fibonacci.__doc__)
    import doctest
    doctest.testmod()
    # doctest.testfile("./test_overview.txt")