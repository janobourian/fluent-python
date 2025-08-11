def wrapper(func):
    def inner():
        print("I am a decorator function")
        func()
    return inner

def hello_world():
    print("Hello, World!")

## Longest way
decorated_function = wrapper(hello_world)
decorated_function()

def wrapper_with_args(func):
    def inner(*args, **kwargs):
        print("I am a decorator function with arguments")
        return func(*args, **kwargs)
    return inner

@wrapper_with_args
def main_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

main_function(1, 2, 3, 3, 3, a=4, b=5)