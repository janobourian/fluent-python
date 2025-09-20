import collections

## ChainMap examples

defaults = {'color': 'red', 'user': 'guest', 'size': 'large'}
user_settings = {'user': 'admin', 'color': 'black'}
chain = collections.ChainMap(user_settings, defaults)
print("ChainMap example:", chain)
print("ChainMap keys:", list(chain.keys()))
print("ChainMap values:", list(chain.values()))
print("ChainMap items:", list(chain.items()))
print("ChainMap length:", len(chain))
print("ChainMap list:", list(chain))
print("ChainMap parent:", chain.parents)

# Counter examples
import re

words = re.findall(r'\w+', open('collections_info/quijote.txt').read().lower())

ctr = collections.Counter(words)
print("Counter most common:", ctr.most_common(10))

c = collections.Counter('abracadabra')
print("Counter 'abracadabra':", c)

# deque examples
d = collections.deque('abcdefg')
print("Initial deque:", d)