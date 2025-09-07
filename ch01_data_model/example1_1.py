from random import choice
import collections

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:

    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
    
    def __random__(self):
        return choice(self._cards)
    
    def __repr__(self):
        return f"FrenchDeck({self._cards})"


first_deck = FrenchDeck()
print(first_deck._cards)
print(len(first_deck))
print(first_deck[0])
print(first_deck)
print(first_deck.__random__())

for card in first_deck:  # doctest +ELLIPSIS
    print(card)

for card in reversed(first_deck):  # doctest +ELLIPSIS
    print(card)

print(Card(rank='2', suit='spades') in first_deck)  # doctest +ELLIPSIS
print(Card(rank='2', suit='beasts') in first_deck)  # doctest +ELLIPSIS