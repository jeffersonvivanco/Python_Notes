from abc import ABCMeta, abstractmethod


# defining an abstract base class
class Shape(metaclass=ABCMeta):
    @abstractmethod
    def length(self):
        pass


# using base class
class Circle(Shape):
    def __init__(self, length):
        self._length = length

    def length(self):
        return self._length


s = Circle(2)
print(s)
print(s.length())