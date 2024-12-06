# numbers = {
#     'high':   100,
#     'medium': 50,
#     'low':    25,
# }

# half_numbers = []

# for number in numbers.values():
#     half_numbers.append(number // 2)

# print(half_numbers)

numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

# for key in numbers:
#     print(f'A {key} number is {numbers[key]}'.)

# print(numbers.items())

# for item in numbers.items():
#     print(f'A {item[0]} number is {item[1]}.')

for key, value in numbers.items():
    print(key)
    print(value)
    