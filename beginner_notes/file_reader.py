# reads the file pi_digits.txt and prints the contents to the screen

# 'with' closes the file once is no longer needed
# if not using 'with', you have to manually close

try:
    with open('pi_digits.xt') as file_object:
        contents = file_object.readlines()
        print(contents)
except FileNotFoundError:
    print('File not found, please make sure you typed the correct path')

