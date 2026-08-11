# Ask the user for their name
#name = input("What'2s your name? ").strip().title()
# Print Hello
#print(f"hello, {name}")

#x = float(input("What's x? "))
#y = float(input("What's y? "))

# rounding to 2 decimal places
#z = x / y
#print(f"{z:.2f}")

# Outpiutting with commas to seperate thousands
#z = round( x + y)
#print(f"{z:,}")

#def hello(to):
 #   print(f"hello, ", to)

#name = input("What's your name? ").strip().title()
#hello(name)
    

#def hello(to = "world"):
#    print(f"hello, {to}")

#name = input("What's your name? ").strip().title()
#hello(name)
#hello()

# def main():
#     name = input("What's your name? ").strip().title()
#     hello(name)

#     hello()

# def hello(to = "world"):
#     print(f"hello, {to}")

# main()

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

main()