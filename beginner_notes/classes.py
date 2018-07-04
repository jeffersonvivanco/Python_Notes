class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.school = ''
    def greeting(self):
        return 'Hello ' + self.name
    
zen = Student('Zen', 21)
zen.school = 'NYU'

# inheritance
class Freshman(Student):
    def __init__(self, name, age):
        super().__init__(name, age)

mitch = Freshman('Mitch', 17)
print(mitch.greeting())