def moving_average(iterable, n=3):
    """
    >>> moving_average([40, 30, 50, 46, 39, 44], n=1)
    [40.0, 30.0, 50.0, 46.0, 39.0, 44.0]
    >>> moving_average([40, 30, 50, 46, 39, 44], n=3)
    [40.0, 42.0, 45.0, 43.0]
    >>> moving_average([1, 2, 3, 4, 5], n=2)
    [1.5, 2.5, 3.5, 4.5]
    >>> moving_average([10, 20, 30, 40], n=4)
    [25.0]
    >>> moving_average([5, 15, 25], n=1)
    [5.0, 15.0, 25.0]
    >>> moving_average([], n=3)
    []
    >>> moving_average([1, 2], n=3)
    []
    >>> moving_average([1, 2, 3], n=0)
    []
    >>> moving_average([1, 2, 3], n=-1)
    []
    >>> moving_average([1, 2, 3], n=5)
    []
    """
    if not iterable or n <= 0 or n > len(iterable):
        return []
    
    average = []
    while n <= len(iterable):
        average.append(sum(iterable[:n]) / n)
        iterable = iterable[1:]
    return average

if __name__ == "__main__":
    import doctest
    doctest.testmod()