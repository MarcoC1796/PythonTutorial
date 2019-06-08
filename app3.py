# Twenty-ninth tutorial: Classes
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1 = Point()
point1.x = 10
point1.y = 10
print(point1.y)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)

# Thirtieth tutorial: Constructors
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")

point = Point(10,20)
point.x = 11
print(point.x)

# Exercise: person
class Person:
    def __init__(self, name):
        self.name=name

    def talk(self):
        print(f"Hi! My name is {self.name}")

marco = Person("Marco")
marco.talk()

# Thirtieth-first tutorial: Inheritance
class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")

class Cat(Mammal):
    pass

dog1 = Dog()
dog1.walk()
dog1.bark()

# Thirtieth-second tutorial: Modules
import converters  # You can also use: from converters import kg_to_lbs. No need to prefix with module name.

print(converters.kg_to_lbs(70))
