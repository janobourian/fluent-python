def f(a, b):
    a += b
    return a

x = 1
y = 2
print("Integers:")
print(f(x, y))
print(x, y)

print("Lists:")
a = [1, 2]
b = [3, 4]
print(f(a, b))
print(a, b)

print("Tuples:")
c = (1, 2)
d = (3, 4)
print(f(c, d))
print(c, d)