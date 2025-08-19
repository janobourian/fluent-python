# arrays
from array import array
from random import random

FILE_NAME = './02_sequences/array.bin'
TOTAL_FLOATS = 10**7

floats = array('d', (random() for _ in range(TOTAL_FLOATS)))

with open(FILE_NAME, 'wb') as f:
    floats.tofile(f)

with open(FILE_NAME, 'rb') as f:
    floats2 = array('d')
    floats2.fromfile(f, TOTAL_FLOATS)