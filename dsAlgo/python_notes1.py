# Notes on Python by Jefferson Vivanco

# unpacking a sequence into seperate variables
p = (4, 5)
x, y = p

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data

s = 'Hello'
# discarding some values
a, _, _, _, _ = s

# you need to unpack N elements from an iterable, but the iterable may be longer than N elements
user_record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212', 'Smith')
name, email, *phone_numbers, last_name = user_record
print(phone_numbers, last_name)

# iterating over a sequence of tuples of varying length
records = [('foo', 1, 2), ('bar', 'hello'), ('foo', 3, 4)]
def do_foo(x, y):
    print('foo', x, y)
def do_bar(s):
    print('bar', s)
for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

# string splitting
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
# ---------- end of examples -------------