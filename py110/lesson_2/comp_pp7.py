lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

def multiples_of_3(numbers):
    return [num for num in numbers if num % 3 == 0]

new_list = [multiples_of_3(subnums) for subnums in lst]
print(new_list)

# [[], [3, 12], [9], [15, 18]]
# return same structure but only numbers that are multiples of 3

# new_lst = []

# for sublist in lst:
#     sub = []
#     for element in sublist:
#         if element % 3 == 0:
#             sub.append(element)

#     new_lst.append(sub)

# print(new_lst)

# new_list = [[num for num in sublist if num % 3 == 0]
#             for sublist in lst]

# print(new_list)