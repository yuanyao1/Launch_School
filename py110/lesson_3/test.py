# input: list, string (optional), string (optional)
# output: string

# Data Structure:
# function has 3 parameters with 2 default values
# string that gets updated by joining each element

# Algo:
# initialize empty string to variable result
# use f string interpolation and join method to concatenate every element
# in the list
# check to see if list contains 0, 1, or 2 elements

# def join_or(lst, sep=', ', word='or'):
#     numbers = [str(num) for num in lst]
#     if not numbers:
#         return ""
#     elif len(numbers) == 1:
#         return numbers[0]
#     elif len(numbers) == 2:
#         return f'{numbers[0]} {word} {numbers[1]}'

#     return f'{sep.join(numbers[:-1])}{sep}{word} {numbers[-1]}'

# print(join_or([1, 2, 3]))               # => "1, 2, or 3"
# print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
# print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
# print(join_or([]))                      # => ""
# print(join_or([5]))                     # => "5"
# print(join_or([1, 2]))                  # => "1 or 2"


#test cases
# print(total([['suit','Ace'], ['suit',10]]))
# print()

# print(total([['suit','Ace'], ['suit','Ace'], ['suit',9]]))
# print()

# print(total([['suit','Ace'], ['suit','Ace'], ['suit',10]]))
# print()

# print(total([['suit','Ace'], ['suit','Ace'], ['suit',10], ['suit','9']]))
# print()

# print(total([['suit','Ace'], ['suit','Ace'], ['suit','Ace'], ['suit',10]]))
# print()

# print(total([['suit','Ace'], ['suit','Ace'], ['suit','Ace'], ['suit',10], ['suit',10]]))
# print()



# target_letters = ['a', 'b', 'c', 'd', 'e']
# characters = ['a', 'b', 'b', 'd', 'f', 'f', 'z', 'z', 'z']

# ???
# result = {}
# for letter in target_letters:
# result = {
#     letter: {
#         "present": letter in characters, 
#         "count": characters.count(letter) 
#     } 
#     for letter in target_letters
# }

#     # temp = {}
#     # temp['present'] = letter in characters
#     # temp["count"] = characters.count(letter)
#     # result[letter] = temp
    
# print(÷result)

# {'a': {}, 'b': {}, ...}

# {
#     'a': { 'present': True, 'count': 1 },
#     'b': { 'present': True, 'count': 2 },
#     'c': { 'present': False, 'count': 0 },
#     'd': { 'present': True, 'count': 1 },
#     'e': { 'present': False, 'count': 0 },
# }

# key: {key1: checking if the value in target_letters is in characters, key2: getting
# the count of those characters in characters lst))

target_letters = ['a', 'b', 'c', 'd', 'e']
characters = ['a', 'b', 'b', 'd', 'f', 'f', 'z', 'z', 'z']

# result = {}
# for letter in target_letters:
#     result[letter] = {'present': letter in characters,
#                       'count': characters.count(letter)}

result = {letter: {'present': letter in characters,
                   'count': characters.count(letter)}
                   for letter in target_letters}
print(result)