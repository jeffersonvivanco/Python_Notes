my_names = ['Jefferson', 'Amadeus', 'Quetzel', 'Vivanco']
fullName = ' '.join(my_names)

info = ['Jefferson', 23, 1994]
s = '-'.join(str(i) for i in info)

print('Jefferson', 'Vivanco', sep='-')

# generator function that emits fragments
def sample():
    yield 'Hello'
    yield 'Jeff'
    yield 'Vivanco'

text = ' '.join(sample())

# interpolation using format()
interp = 'Hi, my name is {name}'
t = interp.format(name='Jeff')
print(t)

# using 