languages = {'Python', 'Java', 'JavaScript', 'Python', 'C++'}
print('Languages set:', languages)

languages2 = {'Python', 'Ruby', 'JavaScript'}
print('Union:', languages.union(languages2))
print('Intersection:', languages.intersection(languages2))
print('Difference:', languages.difference(languages2))

cities = ('New York', 'London', 'Paris', 'Tokyo', 'New York')
print('\nCities tuple:', cities)
print('Occurrences of New York:', cities.count('New York'))
print('Index of London:', cities.index('London'))
print('Is Berlin in tuple?', 'Berlin' in cities)

try:
    cities[0] = 'Berlin'
except TypeError as e:
    print(f'Error modifying tuple: {e}')