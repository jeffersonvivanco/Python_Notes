mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# list comprehension to filter the list
pos = [n for n in mylist if n > 0]

# One potential downside of using a list comprehension is that it might produce a large result if the original
# input is large. If this is a concern, you can use generator expressions to produce the filtered values iteratively
pos2 = (n for n in mylist if n > 0)
for x in pos2:
    print(x)

# filtering process with exception handling
values = ['1', '2', '3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, values))

# using itertools.compress()
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK'
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress
more5 = [n > 5 for n in counts]
more5Addresses = list(compress(addresses, more5))

# dictionary comprehension
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# make a dictionary of all prices over 200
p1 = {key:value for key, value in prices.items() if value > 200}
# make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key:value for key, value in prices.items() if key in tech_names}
print(p2)