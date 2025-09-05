class BasicIterator:
    
    def __init__(self):
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        raise StopIteration

    def __getitem__(self, index):
        return index
    
    def __repr__(self):
        return "BasicIterator()"

operation = BasicIterator()
for op in operation:
    print(op)