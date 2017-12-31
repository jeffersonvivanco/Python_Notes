# Python_Notes

Some notes on python with examples.

## unpacking elements from iterables of arbitrary length
* unpack arrays, objects, tuples -> look at python_notes1.py
* ex:`>>> record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')`
* `>>> name, email, *phone_numbers = record`
* `>>> print(name)`
* `>>> Dave`
