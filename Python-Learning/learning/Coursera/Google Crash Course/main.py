def greeting(name):
    print("Welcome, " + name)

greeting("Kay")

def greeting2(name, department):
    print("Welcome, " + name)
    print("You are part of " + department)

greeting2("Kay", "IT")

def area_triangle(base, height):
    return base*height/2

area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("The sum of both areas is " + str(sum))


def convert_seconds(seconds):
    hourse = seconds // 3600
    minutes = (seconds - hourse * 3600) // 60
    remaining_seconds = seconds - hourse * 3600 - minutes * 60
    return hourse, minutes, remaining_seconds
# // floor division - divides number and keeps integer part of result       5//2 = 2

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

