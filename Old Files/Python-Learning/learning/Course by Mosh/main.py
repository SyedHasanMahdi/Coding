course = 'Python for Beginners'
# index    012345
print(course.upper())
print(course.find('y'))  # case sensitive
print(course.find('for'))

print(course.replace('for', "4"))
print('Python' in course)

weight = input("Weight: ")
weight = float(weight)
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))

i = 1
while i <= 5:
    print(i)
    i = i + 1
i = 1
while i <= 10:
    print(i * "*")
    i = i + 1

names = ["Hasan", "Bob", "Mosh", "Ali", "Sam", "Mary"]
# index     0       1        2      3      4      5
print(names[0])
names[2] = "Mash"
print(names)
print(names[0:3])

numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)
numbers.insert(0,-1)
print(numbers)
numbers.remove(3)
print(numbers)
print(1 in numbers)
print(10 in numbers)
print(len(numbers))