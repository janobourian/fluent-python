from collections.abc import Callable

def bisection_method(func: Callable[[float], float], low: float, high: float, /, *, epsilon: float = 1e-10) -> float:
    """
    >>> f = lambda x: x**3 - x - 2
    >>> root = bisection_method(f, 1, 2)
    >>> root
    1.5213797068595886
    >>> abs(f(root)) < 1e-10
    True
    """
    if func(low) * func(high) >= 0:
        raise ValueError("Function must have different signs at the endpoints.")
    while (high - low) > epsilon:
        mid = (low + high) / 2
        if func(mid) == 0:
            return mid
        elif func(low) * func(mid) < 0:
            high = mid
        else:
            low = mid
    return (low + high) / 2

def function(x: float) -> float:
    return x**3 - x - 2

result = bisection_method(function, 1, 2)
print(f"Root found: {result}")
print(f"Function value at root: {function(result)}")