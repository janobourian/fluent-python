import functools

def clock(active=False):
    def wrapper(func):
        @functools.wraps(func)
        def clocked(*args, **kwargs):
            if active:
                print(f'[{func.__name__}] args={args}, kwargs={kwargs}')
            return func(*args, **kwargs)
        return clocked
    return wrapper

@clock(active=False)
def f1(a, b=2):
    print(f'in f1: a={a}, b={b}')

@clock(active=True)
def f2(c, d=4):
    print(f'in f2: c={c}, d={d}')

if __name__ == '__main__':
    f1(1)
    f1(1, b=3)
    f2(2)
    f2(2, d=5)