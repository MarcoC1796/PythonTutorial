# fifteenth tutorial: For Loops
from typing import List

for item in 'Python':
    print(item)

for item in ['Mosh', 'John', 'Sarah']:
    print(item)

for item in [1, 2, 3, 4]:
    print(item)

for item in range(10):
    print(item)

for item in range(5, 10):
    print(item)

for item in range(5, 10, 2):
    print(item)

# Exercise
prices = [10, 30, 60]
total = 0

for item in prices:
    total += item
print(f"The total is {total}")

# sixteenth tutorial: Nested Loops
for x in range(4):
    for y in range(3):
        print(f"({x},{y})")

# challenge: L
numbers = [2, 2, 2, 2, 5]
for item in numbers:
    output = ''
    for number in range(item):
        output += 'x'
    print(output)

# seventeenth tutorial: Lists
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names)
print(names[0])
print(names[-1])
print(names[-2])
print(names[2:])
print(names[2:4])
print(names[0:])
names[0] = 'Jon'
print(names)

# Exercise: largest number
list = [10, 2, 3, 4, 11, 5, 8, 4, 3]
biggest_number = list[0]
for item in list[1:]:
    if biggest_number < item:
        biggest_number = item
print(biggest_number)

# eighteenth tutorial: 2D Lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[0][1] = 20
print(matrix[0][1])
for row in matrix:
    for item in row:
        print(item)

# nineteenth tutorial: List Methods
numbers = [5, 2, 1, 7, 4]
numbers.append(20)
print(numbers)
numbers.insert(0, 10)
print(numbers)
numbers.remove(5)
print(numbers)
numbers.pop()
print(numbers)
print(numbers.index(4)) #can return an error if number is not in the list
#numbers.clear()
print(numbers)
print(50 in numbers)
print(numbers.count(5))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()
numbers.append(10)
print(numbers2)

# Exercise: remove list duplicates

list1 = [2, 5, 2, 3, 5, 3, 10, 9, 9]
uniques = []
for item in list1:
    if item not in uniques:
        uniques.append(item)
list1 = uniques
print(list1)

# Twentieth tutorial: Tuples
numbers = (1, 2, 3) # immutable
print(numbers[0])
# numbers[0] = 5 will trigger an error

# Twenty-first tutorial: Unpacking
coordinates = (1, 2, 3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
# vs
x, y, z = coordinates

cero1 = [1, 2, 3]
r, t, e = cero1

# Twenty-second tutorial: Dictionaries
customer = { # keys should be unique
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"])
print(customer.get("birthdate", "Jan 1 1980"))
customer["name"] = "Jack Smith"
print(customer["name"])
customer["birthdate"] = "Jan 1 1990"
print(customer["birthdate"])

# Exercise
# phone = input("Phone: ")
# digits_mapping ={
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
# }
# output = ""
# for ch in phone:
#     digits_mapping.get(ch, "!")
#     output += digits_mapping.get(ch, "!") + " "
# print(output)

# Project: Emoji Converter :)
# message = input(">")
# words = message.split(' ')
# emojis = {
#     ":)": "happy",
#     ":(": "sad"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)

# Twenty-third tutorial: Functions


def greet_user():
    print('Hi there')
    print('Welcome aboard')


print("Start")
greet_user()
print("Finish")

# Twenty-forth tutorial: Parameters


def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


print("Start")
greet_user("John", "Smith")
print("Finish")

# Twenty-fifth tutorial: Keyword Arguments
greet_user(last_name="Smith", first_name="John")

# Twenty-sixth tutorial: Return Statement


def square(number):
    return number * number


result = square(3)
print(result)

# Exercise: Creating a Reusable Function


def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "happy",
        ":(": "sad"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


print(emoji_converter("Hello :)"))

# Twenty-seventh tutorial: Exceptions
try:
    age = 0
    income = 2000
    risk = income/age
    print(age)
except ValueError:
    print('Invalid value')
except ZeroDivisionError:
    print('Age cannot be 0')

# Twenty-eighth tutorial: Comments
print("Sky is blue")