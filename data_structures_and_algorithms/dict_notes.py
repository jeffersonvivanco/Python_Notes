from collections import OrderedDict

# ordered dictionary
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

# print values d
# for key in d:
#     print(key, d[key])



# calculating values of a dict
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# finding min price
min_price = min(zip(prices.values(), prices.keys()))

#sorting
prices_sorted = sorted(zip(prices.values(), prices.keys()))

# comparing two dictionaries
a = {
    'x':1,
    'y':2,
    'z':3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

#find keys in common
commonKeys = a.keys() & b.keys()
keysInANotInB = a.keys() - b.keys()
commonPairs = a.items() & b.items()

# make a new dictionary with certain keys removed with a dictionary comprehension
c = {key: a[key] for key in a.keys() - {'z', 'w'}}


# using ChainMap
from collections import ChainMap
my_a = {'x': 1, 'y': 2}
my_b = {'y': 2, 'z': 4}

my_c = ChainMap(my_a, my_b)

#add a new mapping
my_c = my_c.new_child()
my_c['j'] = 3

# discard last mapping
my_c = my_c.parents
print(my_c)