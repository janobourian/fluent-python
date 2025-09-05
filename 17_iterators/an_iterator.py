class MyIterator:
    
    def __init__(self, max_value = 0):
        self.start_value = 0
        self.max_value = max_value
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start_value < self.max_value:
            current_value = self.start_value
            self.start_value += 1
            return current_value
        else:
            raise StopIteration

    def __repr__(self):
        return f"MyIterator({self.max_value})"

it = MyIterator(5)
print(it)
for i in it:
    print(i)