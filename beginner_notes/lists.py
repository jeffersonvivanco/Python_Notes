family = []
family.append('Buzz')
family.append('Phoebe')
family.append('Zen')

# inserting elements into a specific index
# index -1 will always return the last item in the list
family.insert(1, 'Zalma')

# deleting elements from an array
del family[1]

# removing but getting the element back, pop can also pop from any position
removedGirl = family.pop()
family.remove('Phoebe') # removing by value if you don't know the position

print(str(family) + ' and removed ' + str(removedGirl))

# sorting lists
# use sorted to not affect the original list
cars = ['bmw', 'suzuki', 'audi', 'toyota']
cars.sort(reverse=True)
cars.reverse() # to reverse the list
print(str(cars) + ' there are ' + str(len(cars)) + ' cars')

# looping through lists
for car in cars:
    print(car)

# making numerical lists

# you can use the range function to generate a series of numbers
for value in range(1, 5):
    print(value)

# can also make lists of numbers
evenNumbers = list(range(2, 7, 2))
print(evenNumbers)

# squares
for value in range(2, 11, 2):
    print(str(value**2))

# list comprehensions
numbersSquared = [value**2 for value in range(1, 11)]
print(numbersSquared)

# slicing a list, ex: lets slice numbersSquared to return only the first 2 elements
# if you want to copy a list, use a slice ex: to copy all elements, do [:]
# if you want to get items from a certain distance of the end of the list use a negative
# number like so: [-3:], this will get the last 3 items in the list
print(str(numbersSquared[0:3]))

# tuple: an immutable list, you can't write over an element in a list, but you can write over a list
dimesions = (200, 50)


