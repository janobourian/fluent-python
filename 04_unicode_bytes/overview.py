import sys

s = "Café"
print(s)
print(len(s))
print(sys.getsizeof(s))

b = s.encode('utf-8')
print(b)
print(len(b))
print(sys.getsizeof(b))

c = b.decode('utf-8')
print(c)
print(len(c))
print(sys.getsizeof(c))