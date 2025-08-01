fruits = ["apple", "banana", "cherry"]

iterator = iter(fruits)

while True:
    try:
        fruit = next(iterator)
        print(fruit)
    except StopIteration:
        break

class Powers:
    
    def __init__(self, base, max_exponent):
        self.base = base
        self.max_exponent = max_exponent
        self.current_exponent = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_exponent > self.max_exponent:
            raise StopIteration
        result = self.base ** self.current_exponent
        self.current_exponent += 1
        return result

powers_of_two = Powers(0.25, 25)

for power in powers_of_two:
    print(power)