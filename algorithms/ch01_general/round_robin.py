import itertools

def round_robin(*iterables):
    """
    >>> round_robin("ABC", "D", "EF")
    ['A', 'D', 'E', 'B', 'F', 'C']
    
    >>> round_robin(range(3), range(2), range(7))
    [0, 0, 0, 1, 1, 1, 2, 2, 3, 4, 5, 6]
    
    >>> round_robin("AB", "", "CDE")
    ['A', 'C', 'B', 'D', 'E']

    >>> round_robin("AB", "CD", "EF", "GH", "IJKLMN")
    ['A', 'C', 'E', 'G', 'I', 'B', 'D', 'F', 'H', 'J', 'K', 'L', 'M', 'N']
    """
    results = []
    for i in itertools.zip_longest(*iterables):
        results.extend(i)
    return [x for x in results if x is not None]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
