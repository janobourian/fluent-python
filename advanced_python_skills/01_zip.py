countries = ['USA', 'Canada', 'Mexico', 'UK', 'Germany', 'France', 'Italy']
capitals = ['Washington, D.C.', 'Ottawa', 'Mexico City', 'London', 'Berlin', 'Paris', 'Rome']
people = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace']
countries_and_capitals = zip(countries, capitals, people)

for country, capital, person in countries_and_capitals:
    print(f'The capital of {country} is {capital} for {person}.')
    
zipped_list = [('USA', 'Washington, D.C.', 'Alice'),
               ('Canada', 'Ottawa', 'Bob'),
               ('Mexico', 'Mexico City', 'Charlie'),
               ('UK', 'London', 'David'),
               ('Germany', 'Berlin', 'Eve'),
               ('France', 'Paris', 'Frank'),
               ('Italy', 'Rome', 'Grace')]

unzipped_countries, unzipped_capitals, unzipped_people = zip(*zipped_list)
print("Unzipped countries:", unzipped_countries)
print("Unzipped capitals:", unzipped_capitals)
print("Unzipped people:", unzipped_people)
print("Zipped list:", zipped_list)

### Second lesson

from itertools import zip_longest

names = ['Alice', 'Bob', 'Charlie', 'David']
ages = [25, 30, 35]
cities = ['New York', 'Los Angeles']

zipped_info = zip_longest(names, ages, cities, fillvalue='Unknown')

for name, age, city in zipped_info:
    print(f'{name} is {age} years old and lives in {city}.')