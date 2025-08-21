class A(dict):

    def __missing__(self, name):
        print(f"Attempted to access missing attribute: {name}")
        return None

a = A()
a['x']