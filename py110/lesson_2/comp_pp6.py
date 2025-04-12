lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

def increment_values(dictionary):
    return {key: value + 1 for key, value in dictionary.items()}

lst3 = [increment_values(member) for member in lst]
print(lst3, lst, sep='\n')

# lst1 = [{key: value + 1
#          for dictionary in lst
#          for key, value in dictionary.items()}]
# print(lst1)

# lst2 = [{key: value + 1
#          for key, value in dictionary.items()}
#          for dictionary in lst
#          ]
# print(lst2)
