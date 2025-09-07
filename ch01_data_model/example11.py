import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [
            Card(rank, suit)
            for suit in self.suits
            for rank in self.ranks
        ]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
    def __random__(self):
        return choice(self._cards)
    
    def __iter__(self):
        return iter(self._cards)
    
    def __next__(self):
        return next(self._cards)

current_deck = FrenchDeck()
print(len(current_deck))
print(current_deck.__random__())