# Naming a slice
record = '123456789101112131415161718192021222324252627282930';
PRICE = slice(0, 5)
print(record[PRICE])

# deleting from an array
numbers = [1, 2, 3, 4, 5]
DELETEDNUMS = slice(0, 2)
del numbers[DELETEDNUMS]
print(numbers)