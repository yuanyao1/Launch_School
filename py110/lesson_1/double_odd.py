def double_odd_index(numbers):
    doubled_nums = []

    for idx, num in enumerate(numbers):
        print(f'idx: {idx} with num = {num}')
        # if idx % 2 == 1:
        #     doubled_nums.append(num * 2)
        # else:
        #     doubled_nums.append(num)
        doubled_nums.append(num * 2 if idx % 2 == 1 else num)

    return doubled_nums

my_numbers = [1, 4, 3, 7, 2, 6]
print(double_odd_index(my_numbers))  # [1, 8, 3, 14, 2, 12]

# not mutated
print(my_numbers)                      # [1, 4, 3, 7, 2, 6]