import unittest

# middle is a tuple
def get_formatted_name(first, last, *middle):
    if middle:
        middle_name = ' '.join(middle)
        full_name = first + ' ' + middle_name + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()

# first = input('Please enter your first name: ')
# print()
# last = input('Please enter your last name: ')
# print('\nName: {full_name}'.format(full_name=get_formatted_name(first, last)))


class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name('jefferson', 'vivanco')
        self.assertEqual(formatted_name, 'Jefferson Vivanco')

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('jefferson', 'vivanco', 'amadeus', 'quetzel')
        self.assertEqual(formatted_name, 'Jefferson Amadeus Quetzel Vivanco')


# tells python to run the tests in this file
unittest.main()