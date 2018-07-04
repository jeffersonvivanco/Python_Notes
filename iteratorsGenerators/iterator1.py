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