import functools

def filter_even_numbers(nums: list[int]) -> list[int]:
    """
    >>> filter_even_numbers([1, 2, 3, 4, 5, 6])
    [2, 4, 6]
    >>> filter_even_numbers([10, 15, 20, 25])
    [10, 20]
    """
    return list(filter(lambda x: x % 2 == 0, nums))


def filter_even_numbers_comps(nums: list[int]) -> list[int]:
    """
    >>> filter_even_numbers([1, 2, 3, 4, 5, 6])
    [2, 4, 6]
    >>> filter_even_numbers([10, 15, 20, 25])
    [10, 20]
    """
    return [x for x in nums if x % 2 == 0]

def square_all(nums: list[int]) -> list[int]:
    """
    >>> square_all([1, 2, 3, 4])
    [1, 4, 9, 16]
    >>> square_all([0, -1, -2])
    [0, 1, 4]
    """
    return list(map(lambda x: x ** 2, nums))

def concat_strings(strings: list[str]) -> str:
    """
    >>> concat_strings(["Hello", "World", "!"])
    'HelloWorld!'
    >>> concat_strings(["a", "b", "c", "d"])
    'abcd'
    """
    return functools.reduce(lambda x, y: x + y, strings, "")

def flatten_list_of_lists(list_of_lists: list[list[int]]) -> list[int]:
    """
    >>> flatten_list_of_lists([[1, 2], [3, 4], [5]])
    [1, 2, 3, 4, 5]
    >>> flatten_list_of_lists([[10], [20, 30], [40, 50, 60]])
    [10, 20, 30, 40, 50, 60]
    """
    return [item for current_list in list_of_lists for item in current_list]

def invert_dict(d: dict[str, int]) -> dict[int, str]:
    """
    >>> invert_dict({"a": 1, "b": 2, "c": 3})
    {1: 'a', 2: 'b', 3: 'c'}
    >>> invert_dict({"x": 10, "y": 20})
    {10: 'x', 20: 'y'}
    """
    return {v: k for k, v in d.items()}

def word_length_dict(words: list[str]) -> dict[str, int]:
    """
    >>> word_length_dict(["apple", "banana", "cherry"])
    {'apple': 5, 'banana': 6, 'cherry': 6}
    >>> word_length_dict(["a", "ab", "abc"])
    {}
    >>> word_length_dict(["a1111", "a1234b", "abcd"])
    {'abcd': 4}
    """
    return {word: len(word) for word in words if len(word) > 3 and word.isalpha()}

if __name__ == "__main__":
    import doctest
    doctest.testmod()