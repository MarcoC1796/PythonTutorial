# fifteenth tutorial: For Loops
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
