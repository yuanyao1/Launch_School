numbers = [1, 2, 3, 4]
print(id(numbers))
# numbers.clear()
# print(numbers)

# del numbers[:]

while numbers:
   numbers.pop()

print(numbers)
print(id(numbers))