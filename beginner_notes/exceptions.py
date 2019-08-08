two_numbers = input('Give me two numbers to divide\n')

two_numbers = two_numbers.split(' ')

if len(two_numbers) != 2:
    print('You did not enter two numbers!')
    exit(1)

try:
    res = int(two_numbers[0])/int(two_numbers[1])
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("You didn't type a number")
else:
    print(res)


# custom exception
class CustomError(Exception):
    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)

try:
    print('Going to raise an custom exception')
    raise CustomError('This is a custom error')
except CustomError as e:
    print(e.args)
    print('Printed out custom error :)')