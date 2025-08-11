class Calculator:
    
    def __init__(self, current_version: int):
        self.current_version = current_version
    
    def description(self) -> None:
        print(f"This is a calculator version {self.current_version}")
    
    @staticmethod
    def add_numbers(*numbers: float) -> float:
        return sum(numbers)

class Person:
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def description(self) -> str:
        return f"{self.name} is {self.age} years old."

if __name__ == "__main__":
    calc1 = Calculator(1)
    calc2 = Calculator(2)
    calc1.description()
    calc2.description()
    print("Sum of numbers:", Calculator.add_numbers(1.5, 2.5, 3.0))