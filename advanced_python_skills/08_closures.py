def print_message(message):
    def printer():
        print(message)
    return printer

print_message("Hello, World!")()

class Multiplier:
    
    def __init__(self, n):
        self._n= n
     
    def multiply(self, x):
        return self._n * x

multiplier = Multiplier(5)
print(multiplier.multiply(3))