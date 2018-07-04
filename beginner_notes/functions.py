def greet_user(name = 'World'):
    print("Hello "+ name.title())

# Note: Pass by reference only works as long as you don't reassign the object you passed


# Arbitrary number of arguments, python creates a tuple from these arguments
def print_shows_attended(*shows):
    print(shows)

# Arbitrary number of key value pairs, python creates a dictionary from these arguments
def print_user_info(name, **info):
    print(name)
    print(info)

    