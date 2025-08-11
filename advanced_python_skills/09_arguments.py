def main_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

main_function(1, 2, 3, 3, 3, a=4, b=5)