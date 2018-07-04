# simple dictionary
family = {
    'brother': 'Buzz',
    'sister': 'Phoebe',
    'mom': 'Lourdes',
    'crazy_sister': 'Lourdes',
    'crazier_sister': 'Prettywoman'
}

# updating key value pair
family['sister'] = 'Zen'

# deleting key value pair
# del family['crazy_sister']


# printing the key, value pairs, .keys() gets all the keys, .values() returns all the values
for key, value in family.items():
    print(str(key) + ' : ' + str(value))

# using a set to get all unique values of a dictionary
print(set(family.values()))

# using lists inside dictionaries
favorite_languages = {
    'jen' : ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['javascript']
}
for name, languages in favorite_languages.items():
    print(str(name.title()) + " likes " + str(languages))
