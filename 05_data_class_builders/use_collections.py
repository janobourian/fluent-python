from collections import namedtuple

Coordinates = namedtuple('Coordinates', ['x', 'y'])
point = Coordinates(1, 2)
print(point)
print(point.x, point.y)
print(issubclass(Coordinates, tuple))