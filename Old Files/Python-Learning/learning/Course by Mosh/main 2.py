numbers = [1, 2, 3, 4, 5]
print(numbers)
# short version of printing all values
for item in numbers:
    print(item)
# long version
i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1

numbers = range(5)
print(numbers)  # range(0, 5)
for num in numbers:
    print(num)
numbers = range(5, 10)
for num in numbers:
    print(num)
numbers = range(0, 10, 2)  # step of a2
for num in numbers:
    print(num)
