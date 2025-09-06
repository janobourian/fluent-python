class Node:
    
    __slots__ = 'data', 'next', 'prev'

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:

    __slots__ = 'head', 'tail', '_size'

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    def __repr__(self):
        return f"DLL([{', '.join(map(str, self))}])"
    
    def _first_insert(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self._size += 1

    def _insert_between(self, value, left, right):
        # TODO: 
        ...
    
    def _remove_node(self, node):
        # TODO: 
        ...
    
    def append(self, value):
        if self.head is None and self.tail is None:
            return self._first_insert(value)
        
        new_node = Node(value)
        last_node = self.tail
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node
        self.tail = new_node
        self._size += 1
    
    def append_left(self, value):
        if self.head is None and self.tail is None:
            return self._first_insert(value)
        
        new_node = Node(value)
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        self._size += 1
        

    def pop(self):
        ...

    def pop_left(self):
        ...

    def find(self, value):
        ...
    
    def insert_after(self, node, value):
        ...

    def remove(self, value):
        ...
    
    def display(self):
        ...


my_list = DoublyLinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print("List size:", len(my_list))
print(my_list)
my_list.append(40)
print("List after appending 40:", my_list)
for value in my_list:
    print(value)
print("List size:", len(my_list))
my_list.append_left(5)
print("List after appending 5 to the left:", my_list)
my_list.append_left(1)
print("List after appending 1 to the left:", my_list)
my_list.append_left(1)
print("List after appending 1 to the left:", my_list)
