# You can pass None to next to instruct it to return a terminating value
with open('names.txt') as f:
    try:
        while True:
            line = next(f, None)
            if line is None:
                break
            print(line, end='')
    except StopIteration:
        pass

# to make an iterator from an array
names = ['Zalma', 'Jeff', 'Buzz']
it = iter(names)
try:
    while True:
        name = next(it, None)
        if name is None:
            break
        print(name)
except StopIteration:
    pass

ferrets = [['Buzz', 'Boots', 'Billie']]

ferret_names = [n for f in ferrets for n in f]

ferret_names2 = list(n for n in (f for f in ferrets))

print(ferret_names)
print(ferret_names2)