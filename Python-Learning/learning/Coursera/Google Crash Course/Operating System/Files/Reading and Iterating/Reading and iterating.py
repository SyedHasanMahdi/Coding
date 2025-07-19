file = open("spider.txt")
print(file.readline())
print(file.readline())  # next line
print(file.read())  # reads all after previous commands
file.close()

with open("spider.txt") as file:  # python will automatically close the file
    print(file.readline())

with open("spider.txt") as file:
    for line in file:
        print(line.upper())  # printed with uppercase

    with open("spider.txt") as file:
        for line in file:
            print(line.strip().upper())
            # strip removes new line character after every line

file = open("spider.txt")
lines = file.readlines()
file.close()
lines.sort()  # sorted alphabetically
print(lines)
# python returns /n to show new line character
