name = input('Please tell me your name: ')
print('Hi ' + str(name) + ' , pleasure meeting you!')

age = input('How old are you: ')

# converting string to number
if int(age) < 21:
    print('You are younger than 21!')
else:
    print('You are an adult :(')