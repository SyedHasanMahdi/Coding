even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)
sounds = {"cat": "meow", "dog": "woof"}
print(sounds["cat"])
print("the odd numbers are %s" % odd_numbers)
print([1, 2, 3] * 3)

x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

name="Joe"
age=10
print("Hello, %s!" % name)
print("%s is %d years old!" % (name, age) )

mylist = [1,2,3]
print("A list : %s" % mylist)

data=("john", "doe", 53.44)
format_string="Hello %s %s. Your current balance is $%s."
print(format_string % data)

astring="Hello world!"
print("single quotes are ' '")
print(len(astring))
print(astring.index("o"))
print(astring.count("l"))


print(astring[3:7])
print(astring[3:7:2])
print(astring[3:7:1])
print(astring[::-1])


print(astring.upper())
print(astring.lower())
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

afewwords=astring.split(" ")
print(afewwords)


print("What's your name?")
x= input()
print("Hello %s, have a good day" % x)

