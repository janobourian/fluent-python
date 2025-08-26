from typing import NamedTuple

Coordinates = NamedTuple('Coordinates', [('x', float), ('y', float)])
point = Coordinates(1, 2)
print(point)
print(point.x, point.y)
print(isinstance(point, tuple))
print(issubclass(Coordinates, tuple))

class Position(NamedTuple):
    x: float | int
    y: float | int

    def __str__(self):
        ns = 'N' if self.y >= 0 else 'S'
        ew = 'E' if self.x >= 0 else 'W'
        return f"{abs(self.y)}°{ns}, {abs(self.x)}°{ew}"