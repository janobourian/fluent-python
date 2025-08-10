fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'kiwi', 'lemon']
fruits_iterator = iter(fruits)
print(f"First fruit: {next(fruits_iterator, 'No more fruits')}")
print(f"Second fruit: {next(fruits_iterator, 'No more fruits')}")
print(f"Third fruit: {next(fruits_iterator, 'No more fruits')}")
print(f"Fourth fruit: {next(fruits_iterator, 'No more fruits')}")
print(f"Fifth fruit: {next(fruits_iterator, 'No more fruits')}")
print(f"Sixth fruit: {next(fruits_iterator, 'No more fruits')}")
print(f"Seventh fruit: {next(fruits_iterator, 'No more fruits')}")
print(f"Eighth fruit: {next(fruits_iterator, 'No more fruits')}")
print(f"Ninth fruit: {next(fruits_iterator, 'No more fruits')}")
print(f"Tenth fruit: {next(fruits_iterator, 'No more fruits')}")
print(f"Eleventh fruit: {next(fruits_iterator, 'No more fruits')}")

# Infinite loop
fruits_iterable = iter(fruits)
while True:
    try:
        print(next(fruits_iterable))
    except StopIteration:
        print("No more fruits to iterate.")
        break
    
# Own iterator class

class PowerOfTwo:
    
    def __init__(self, maximum = 0):
        self.maximum = maximum
    
    def __iter__(self):
        self._n = 0
        return self
    
    def __next__(self):
        if self._n <= self.maximum:
            result = 2 ** self._n
            self._n += 1
            return result
        else:
            raise StopIteration
        
power_of_two_iterator = PowerOfTwo(10000)
for number in power_of_two_iterator:
    print(number)