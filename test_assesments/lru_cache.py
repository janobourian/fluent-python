class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.stack = []
    
    def get(self, key: int) -> int:
        return self.cache.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if len(self.stack) < self.capacity and key not in self.stack:
            self.stack.append(key)
            self.cache[key] = value
        elif len(self.stack) < self.capacity and key in self.stack: 
            _ = self.remove_from_stack(key)
            self.cache[key] = value
        elif len(self.stack) == self.capacity and key in self.stack:
            _ = self.remove_from_stack(key)
            self.cache[key] = value
        else:
            key_to_remove = self.stack[0]
            _ = self.remove_from_stack(key_to_remove)
            del self.cache[key_to_remove]
            self.cache[key] = value
    
    def remove_from_stack(self, key:int) -> None:
        self.stack.pop(self.stack.index(key))
        self.stack.append(key)