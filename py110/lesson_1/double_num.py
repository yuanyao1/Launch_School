def double_numbers(numbers):
    for idx, current_num in enumerate(numbers):
        numbers[idx] = current_num * 2
    # numbers = [num * 2 for num in numbers] reassignment, not mutation
    return numbers

my_numbers = [1, 4, 3, 7, 2, 6]
print(double_numbers(my_numbers)) # [2, 8, 6, 14, 4, 12]
print(my_numbers)                 # [2, 8, 6, 14, 4, 12] mutation