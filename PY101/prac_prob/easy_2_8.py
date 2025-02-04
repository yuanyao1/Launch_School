# def oddities(lst):
#     new_lst = []
#     i = 0
#     while i < len(lst):
#         new_lst.append(lst[i])
#         i += 2
    
#     return new_lst

def oddities(lst):
    return lst[::2]

# def evens(lst):
#     return lst[1::2]

def evens(lst):
    new_lst = []
    i = 0
    while i < len(lst):
        if i % 2 == 1:
            new_lst.append(lst[i])
            i += 2
        else:
            i += 1
    
    return new_lst

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True
print()
print(evens([2, 3, 4, 5, 6]) == [3, 5])
print(evens([1, 2, 3, 4]) == [2, 4])        # True
print(evens(["abc", "def"]) == ['def'])     # True
print(evens([123]) == [])                   # True
print(evens([]) == [])                      # True