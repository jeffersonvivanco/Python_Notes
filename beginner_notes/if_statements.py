# Python uses the values True and False to decide whether the code inside
# an if statement should be executed.
# == checks if the values are equal
# != checks if the values are not equal
# if list_name checks if list has at least one element
name = 'Jeff'
name2 = 'Amadeus'
age = 23

names = ['Jeff', 'Zen', 'Zalms']

for n in names:
    if n == name and age == 23:
        print(n)

# check if value is in list
if name in names:
    print(str(name) + ' is in the list!')

# check whether value is not in the list, you can use elif to check for more conditions
if name2 not in names:
    print(str(name2) + ' is not in the list')



