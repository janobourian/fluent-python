def factorial(n):
    """Calculate the factorial of a non-negative integer n.

    Args:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of the input integer n.
    """
    return 1 if n == 0 else n * factorial(n - 1)

print(factorial(5))
print(factorial.__doc__)

def reverse(text: str) -> str:
    """Reverse a string.

    Args:
        text (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """
    return text[::-1]

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=reverse))