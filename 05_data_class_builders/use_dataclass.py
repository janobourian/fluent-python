from dataclasses import dataclass

@dataclass(frozen=True)
class Coordinates:
    x: float | int
    y: float | int

    def __str__(self):
        ns = 'N' if self.y >= 0 else 'S'
        ew = 'E' if self.x >= 0 else 'W'
        return f"{abs(self.y)}°{ns}, {abs(self.x)}°{ew}"