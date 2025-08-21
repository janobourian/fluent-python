from collections import abc

print(issubclass(list, abc.Sequence))
print(issubclass(tuple, abc.Sequence))
print(issubclass(list, abc.MutableSequence))
print(issubclass(tuple, abc.MutableSequence))
print(issubclass(range, abc.MutableSequence))

## Map and filter with comprehensions

dial_codes = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
    (49, 'Germany'),
    (39, 'Italy'),
    (33, 'France'),
    (44, 'United Kingdom'),
    (27, 'South Africa'),
    (34, 'Spain'),
    (41, 'Australia'),
    (64, 'New Zealand'),
    (31, 'Netherlands'),
    (46, 'Sweden'),
    (358, 'Finland'),
    (48, 'Poland'),
    (52, 'Mexico'),
    (60, 'Malaysia'),
    (63, 'Philippines'),
    (65, 'Singapore'),
    (66, 'Thailand'),
]

using_functions = list(filter(lambda x: len(x) > 5, map(lambda x: x[1], dial_codes)))
print(using_functions)

using_comprehensions = [country for code, country in dial_codes if len(country) > 5]
print(using_comprehensions)

genexp = (country for code, country in dial_codes if len(country) > 5)
print(genexp.__next__())
print(genexp.__next__())
print(genexp.__next__())
print(genexp.__next__())

def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True

print(fixed(1))
print(fixed([1]))
print(fixed("hello"))

first_tuple = (1, 2, 3)
first_tuple = first_tuple + (4, 5)
print(first_tuple)