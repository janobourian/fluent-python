from collections.abc import Sequence
from random import shuffle
from typing import TypeVar

T = TypeVar('T')

def sample(population: Sequence[T], size:int) -> list[T]:
    if size < 1:
        raise ValueError('Sample size must be at least one')
    result = list(population)
    shuffle(result)
    return result[:size]

print(sample(range(10), 3))