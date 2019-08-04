# this is a dictionary that maps keys to more than one value (called multidict)
from collections import defaultdict

# make a dictionary

d = {
    'a': [1, 2],
    'b': [3, 4]
}

d2 = {
    'a': {1, 2},
    'b': {3, 4}
}

# to make a list
d3 = defaultdict(list)

# to make a set
d4 = defaultdict(set)

def add_to_list_set():
    d3['a'].append(1)
    d3['a'].append(1)
    d4['a'].add(1)
    d4['a'].add(1)

add_to_list_set()


print("In a list, here is a of d3 => ", d3['a'])
print("In a set, here is a of d4 => ", d4['a']);