from typing import Dict

class Factorial:
    
    def __init__(self):
        self.cache: Dict[int, int] = {0:1, 1:1}
    
    def __call__(self, n: int) -> int:
        if n not in self.cache:
            self.cache[n] = n * self(n - 1)
        return self.cache[n]

factorial = Factorial()
print(factorial(5))
print(factorial(10))
print(factorial.cache)
print(factorial(5))