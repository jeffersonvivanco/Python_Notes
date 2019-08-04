# TODO Look up what list() does & lambda

# this function only works for hashable types
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 2, 2, 3, 4, 4, 5, 6]
a_dededuped = list(dedupe(a))

a2 = [{'x': 1, 'y':2}, {'x': 1, 'y': 3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
# this function works for non hashable types such as dictionaries
def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

# the purpose of the key argument in the function above is to specify
# a function that converts sequence items into a hashable type for the
# purposes of duplicate detection

# to take duplicates based on x and y values
a_dededuped2 = list(dedupe2(a2, key=lambda d: (d['x'], d['y'])))

# to take duplicates based on only x
a_dededuped3 = list(dedupe2(a2, key=lambda d: d['x']))

