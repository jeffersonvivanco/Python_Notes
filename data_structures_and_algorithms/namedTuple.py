from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('joneysy@example.com', '2012-10-19')
email, date = sub
print(email, date)