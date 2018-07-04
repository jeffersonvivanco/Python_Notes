# comparing user objects by their user_id attr
# instead of using attrgetter you can use lambda like
# key=lambda u: u.user_id
# However, attrgetter() is a bit faster than lambda and allows multiple fields
# You can also use the same technique for max and min

from operator import attrgetter

class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(23), User(9), User(11)]
sorted_users = sorted(users, key=attrgetter('user_id'))
print(sorted_users)