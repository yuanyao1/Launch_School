def multiply(numbers, multiplier):
    # new_numbers = []
    # for num in numbers:
    #     new_numbers.append(num * multiplier)
    new_numbers = [num * multiplier for num in numbers]
    return new_numbers

my_numbers = [1, 4, 3, 7, 2, 6]
print(multiply(my_numbers, 3))  # [3, 12, 9, 21, 6, 18]
print(my_numbers)