class BuzzFizz:
    
    def __init__(self):
        self.buzz = "Buzz"
        self.fizz = "Fizz"
    
    def __len__(self):
        return len(self.buzz) + len(self.fizz)
    
    def __getitem__(self, _):
        return self.buzz + self.fizz
    
    def __repr__(self):
        return f"BuzzFizz(buzz='{self.buzz}', fizz='{self.fizz}')"
    
    def __str__(self):
        return f"{self.buzz} {self.fizz}"
    
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        return True  # Suppress exceptions
    
instance = BuzzFizz()
print(len(instance))
print(instance[0])
print(repr(instance))
print(str(instance))

with instance as bf:
    print("Inside the context")
    print(bf)
    # Uncomment the next line to see exception handling in action
    # raise ValueError("An error occurred inside the BuzzFizz context")

print("Outside the context")