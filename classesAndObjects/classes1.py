
class A:
    def __init__(self):
        self._internal = 'internal'
        self.public = 'public'
        self.__not_changed_by_inheritance = 'not changed, this is class A'

    def public_method(self):
        print('This is a public method')

    def _private_method(self):
        print('This is a private method')


class B(A):

    def __init__(self):
        super().__init__()

    def change_not_changed_by_inher_method(self):
        # try to change the var from A
        print('Cannot do it :)')


# using the property methods
class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # getter function
    @property
    def first_name(self):
        # Note the underscore
        return self._first_name

    # setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        # note the underscore
        self._first_name = value.upper()

    # deleter function (optional)
    @first_name.deleter
    def first_name(self):
        del self.first_name

    # computed attribute
    @property
    def full_name(self):
        return self.first_name.title() + ' ' + self.last_name.title()


# extending a property in a subclass
class Student(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    # to just extend getter property
    @Person.first_name.getter
    def first_name(self):
        print('getting name')
        return super().first_name

    # to just extend the setter property
    @Person.first_name.setter
    def first_name(self, value):
        print('Setting name to', value)
        super(Student, Student).first_name.__set__(self, value)

    def __repr__(self):
        return 'Student({0.first_name!r}, {0.last_name!r})'.format(self)

    def __str__(self):
        # !r indicates that __repr__() should be used instead of __str__()
        return '({0.first_name!r}, {0.last_name!r})'.format(self)


student = Student('Jefferson', 'Vivanco')
print(repr(student)) # Student('JEFFERSON', 'Vivanco')
print(str(student)) # ('JEFFERSON', 'Vivanco')
student.first_name = 'Amadeus'
print(student.full_name)