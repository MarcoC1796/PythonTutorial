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

# Exercise: defining module
import utils
list = [2, 34, 25, 2, 56, 23, 6, 54, 3]
print(utils.find_max(list))

# Thirtieth-third tutorial: Packages
#   Add a  _init_.py file in the directory. Or add directly a new package
import ecommerce.shipping
ecommerce.shipping.calc_shipping()

from ecommerce.shipping import calc_shipping # Also: from ecommerce import shipping
calc_shipping()

# Thirtieth-forth tutorial: Generating Random Values
#   Search Python 3 module index to see all python built-in modules
import random

for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(10, 20))

members = ["John", "Mary", "Bob", "Josh"]
leader = random.choice(members)
print(leader)

# Exercise: dice
class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second  # Interpreted as a tuple


dice = Dice()
print(dice.roll())

# Thirtieth-fifth tutorial: Files and Directories

from pathlib import Path

#   Absolute path: c:\Program Files\Microsoft
#   Relative path: starting on a given directory

path = Path("ecommerce")
print(path.exists())

path2 = Path("emails")
path2.mkdir()
path2.rmdir()

path = Path()
print(path.glob('*.py'))  # *: everything, *.*: all the files, *.py all the python files
                          #  Searches for files in the current directory
for file in path.glob('*.py'):
    print(file)