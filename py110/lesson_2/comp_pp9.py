# return a list that contains only the dictionaries
# where all the numbers are even
# Expected result: [{e: [8], f: [6, 10]}]
# Algo:
# function that takes in an element from the list and returns the element
# if all the values are even
# list comprehension or for loop to iterate through the list

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

print(lst[1].values())
# a = {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]}
# a_values = [num % 2 == 0
#             for element in a.values()
#             for num in element
#             ]
# print(a_values)
# print(all(a_values))

def is_evens(item):
    evens = [num % 2 == 0
             for element in item.values()
             for num in element]
    
    if all(evens):
        return item
    # returns None if no item has all even numbers

result = [item for item in lst if is_evens(item)]
print(result)

# def get_pair(item):
#     for value in item.values():
#         for num in value:
#             if num % 2 != 0:
#                 return None
#     return item

# result = [get_pair(item) for item in lst if get_pair(item) is not None]
# print(result)

