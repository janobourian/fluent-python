L = [1, 2, 3, 4, 5]

it = iter(L)
t = tuple(it)
print(t)

it = iter(L)
print(it)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())

it = iter(L)
a, b, c, d, e = it
print(a, b, c, d, e)