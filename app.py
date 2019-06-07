# first tutorial
print("Hello World")
print('0----')
print(' ||||')
print('*' * 10)

# second tutorial
price = 10
price = 20
rating = 4.9
name = 'Marco'
is_published = False
print(price)
# Exercise
full_name = 'John Smith'
age = 20
is_new = True

# third tutorial
    # name = input('what is your name? ')
    # color = input('What is your favorite colour ')
    # print(name + ' likes ' + color)

# fourth tutorial
    # birth_year = input('Birth year: ')
    # print(type(birth_year))
    # age = 2019 - int(birth_year) # We also have float() and bool()
    # print(type(age))
    # print(age)

# Exercise: weight converter
    # weight_lbs = input('Weight in pounds: ')
    # weight_kg = 0.453592*float(weight_lbs)
    # print('Weight in kilograms: ' + str(weight_kg))

# fifth tutorial: Strings
course = "Python's Course for Beginners"
course = 'Python for "Beginners"'
course = ''' 
Hi John,

Here is our first email to you.

Thank you, 
The support team

'''
print(course)
course = 'Python for Beginners'
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:5])
another = course[:]
print(another)
name = 'Jennifer'
print(name[1:-1])

# sixth tutorial: Formatted Strings
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] ia a coder'
print(message)
print(msg)

# seventh tutorial: String Methods
course = 'Python for Beginners'
print(len(course))
print(course.upper())
print(course.lower())
print(course.find('P'))
print(course.find('Beginners'))
print(course.replace('Beginners', 'Absolute Beginners'))
print('Python' in course)
print(course.title())

# eighth tutorial: Arithmetic Operations
print(10 + 3 - 4 * 6)
print(10/3)
print(10//3)
print(10 % 3)
print(10 ** 3)
x = 10
x = x + 3
print(x)
x += 3
print(3)
x -= 3
print(x)

# ninth tutorial: Operator Precedence
x = (10 + 3) * 2 ** 2
print(x)

# tenth tutorial: Math Functions
import math  # search: python 3 math module for more information
x = 2.9
print(round(x))
print(abs(-2.9))
print(math.ceil(2.9))

# eleventh tutorial: If Statements
is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")

print("Enjoy your day")

# Exercise
price = 1
has_good_credit = True

if has_good_credit:
    price *= 0.9
else:
    price *= 0.8
print(f"Down payment: ${price}M")

# twelfth tutorial: Logical Operators
has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:  # and, or, not
    print("Eligible for loan")

# thirteenth tutorial: Comparison Operators
temperature = 30

if temperature > 30:  # >=, ==, !=
    print("It's a hot day")
else:
    print("It's not a hot day")

name = "Marco"

if len(name) < 3:
    print("Name must be at least 3 characters long")
elif len(name)>50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good")

# Project: weight converter
# old_weight = float(input("Weight: "))
# unit = input("(L)bs or (K)g: ")
#
# if unit.upper() == 'L':
#     new_weight = old_weight*0.45
#     print(f"You are {new_weight} pounds")
# elif unit.upper() == 'K':
#     new_weight = old_weight/0.45
#     print(f"You are {new_weight} pounds")
# else:
#     print("Error, try again")

# fourteenth tutorial: While Loops
i = 1
while i <= 5:
    print('*' * i)
    i += 1
print("Done")

# Project: Guessing Game
# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('You won!')
#         break
# else:
#     print("Sorry you failed")

# Project: Car Game
option = input("> ").lower()
started = False
stopped = True

while option != "quit":
    if option == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif option == "start":
        if started:
            print("Car already started!")
        else:
            print("Car started...Ready to go!")
            started = True
            stopped = False
    elif option == "stop":
        if stopped:
            print("Car already stopped!")
        else:
            print("Car stopped.")
            stopped = True
            started = False
    else:
        print("I don't understand that...")
    option = input("> ").lower()

