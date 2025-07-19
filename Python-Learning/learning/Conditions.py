x = 2
print(x == 2)
print(x == 3)
print(x < 3)
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

name = "John"
age = 23

if name == "John" and age == 23:
    print("Your name is John and you are also 23 years old.")
if name == "John" or name == "Rick":
    print("Your name is either John or Rick")

if name in ["John", "Rick"]:
    print("Your name is either John or Rick")

Sounds = {"cat": "meow", "dog": "woof", "snake": "hiss"}
for animal, sound in Sounds.items():
    print(animal, " goes ", sound)

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)

print(not False)

print(False == (not False))
