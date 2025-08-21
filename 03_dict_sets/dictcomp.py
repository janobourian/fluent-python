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

country_code = {country: code for code, country in dial_codes}
print(country_code)
filtered_code = {code: country.upper() for country, code in sorted(country_code.items()) if code < 66}
print(filtered_code)

def dump(**kwargs):
    return kwargs

print(dump(**country_code))

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 4, 'b': 5, 'd': 6}
print(d1 | d2)
print({**d1, **d2})
d1 |= d2
print(d1)

def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': 'book'}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {'type': 'movie', 'director': name}:
            return [name]
        case {'type': 'movie', 'directors': [*names]}:
            return names
        case {'type': 'movie'}:
            raise ValueError(f"Invalid 'movie' record: {record!r}")
        case _:
            raise ValueError(f"Unknown record type: {record!r}")

# Example usage of get_creators function
record1 = {'type': 'book', 'api': 2, 'authors': ['Author A', 'Author B']}
record2 = {'type': 'movie', 'director': 'Director A'}
record3 = {'type': 'book', 'api': 1, 'author': 'Author C'}
record4 = {'type': 'movie', 'directors': ['Director B', 'Director C']}
print(get_creators(record1))
print(get_creators(record2))
print(get_creators(record3))
print(get_creators(record4))

fruits = ['apple', 'banana', 'cherry']
print([*fruits])