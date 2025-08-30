import time
import functools

def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = [f'{k}={v!r}' for k, v in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}')
        return result
    return clocked

@functools.cache
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@clock
def fibonacci_iter(n):
    a, b = 0, 1
    for _ in range(0, n):
        a, b = b, a + b
    return a

if __name__ == '__main__':
    n = 35
    first_time = time.perf_counter()
    print(fibonacci(n))
    print(fibonacci_iter(n))
    print(f'Total time {time.perf_counter() - first_time:.8f}s')