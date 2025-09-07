from typing import List

class Statistics:

    __slots__ = ("data",)

    def __init__(self):
        self.data: List[float | int] = []
    
    def __call__(self, value: float | int) -> None:
        """
        >>> stats = Statistics()
        >>> stats(10)
        >>> stats(20.5)
        >>> stats.data
        [10, 20.5]
        """
        self.data.append(value)
        
    def __repr__(self) -> str:
        return f"Statistics(data={self.data})"
    
    def average(self) -> float:
        """
        >>> stats = Statistics()
        >>> stats(10)
        >>> stats(20.5)
        >>> stats.average()
        15.25
        """
        return sum(self.data) / len(self.data) if self.data else 0.0
    

stats = Statistics()
stats(10)
stats(20.5)
print(stats)
print(f"Average: {stats.average()}")
stats(30)
print(f"New Average: {stats.average()}")

if __name__ == "__main__":
    import doctest
    doctest.testmod()