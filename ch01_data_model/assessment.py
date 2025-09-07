from dataclasses import dataclass
from typing import List

@dataclass
class Card:
    rank: str
    suit: str

    def __str__(self):
        return f"{self.rank} - {self.suit}"

class Deck:
    
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ['spades', 'hearts', 'diamonds', 'clubs']

    def __init__(self):
        self._cards: List[Card] = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position: int | slice) -> str | List[str]:
        if isinstance(position, slice):
            return [str(card) for card in self._cards[position]]
        else:
            return str(self._cards[position])

    def __iter__(self):
        for card in self._cards:
            yield str(card)
    
    def __contains__(self, item: str) -> bool:
        return item in (str(card) for card in self._cards)

class Vector2D:
    
    def __init__(self, x: float | int, y: float | int):
        self.x = x
        self.y = y
    
    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar: float | int) -> 'Vector2D':
        return Vector2D(self.x * scalar, self.y * scalar)

    def __abs__(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __bool__(self) -> bool:
        return bool(self.x or self.y)
    
    def __repr__(self) -> str:
        return f"Vector2D({self.x:.1f}, {self.y:.1f})"
    
    def __str__(self) -> str:
        return f"({self.x:.1f}, {self.y:.1f})"

class Basket:

    def __init__(self):
        self.items: dict[str, int] = {}

    def __bool__(self) -> bool:
        return bool(self.items)
    
    def __len__(self) -> int:
        return sum(self.items.values())

    def __iter__(self):
        for item, quantity in self.items.items():
            yield (item, quantity)

    def __contains__(self, item: str) -> bool:
        return item in self.items
    
    def add(self, item: str, quantity: int = 0):
        if quantity <= 0:
            return
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def clear(self):
        self.items.clear()
    
class Book:
    
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"{self.title} by {self.author} ({self.year})"
    
    def __repr__(self) -> str:
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"