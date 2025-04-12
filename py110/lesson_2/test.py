# def person_key(person):
#     name, age, grade = person
#     return (grade)

# people = [
#     ("Jack", 30, "A"),
#     ("John", 25, "B"),
#     ("Betty", 25, "B"),
#     ("Anna", 30, "C")]

# sorted_people = sorted(people, key=person_key)
# print(person_key(people[1]))
# print(sorted_people)
# [('Betty', 25), ('John', 25), ('Anna', 30), ('Jack', 30)]

# a = 2
# b = [5, 8]
# lst = [a, b] # [2, [5, 8]]

# # lst[0] += 2 # [4, [5, 8]]
# lst[0] = 4
# print(f'a = {a}')
# print(f'a id = {id(a)}')
# print(id(lst[0]))
# print(lst)
# print()

# a = 10
# print(f'a = {a}')
# print(f'a id = {id(a)}')
# print(id(lst[0]))
# print(lst)
# print()

# lst[1][0] -= a # [4, [3, 8]]
# print(lst)

# a = [1, 2]
# b = [3]
# c = 4
# lst = [a, b, c] # [[1, 2], [3], 4]

# lst[0][0] = 'dog'   # equivalent to a[0] = 'dog'
# print(a)            # ['dog', 2]
# print(lst)          # [['dog', 2], [3], 4]
# print(a is lst[0])  # True

# lst[0] = [77]
# print(a)            # ['dog', 2]
# print(lst)          # [[77], [3], 4]
# print(a is lst[0])  # False

# lst[1].append('cat')
# print(b)            # [3, 'cat']
# print(lst)          # [[77], [3, 'cat'], 4]
# print(b is lst[1])  # True

# lst[1][0] += 20
# print(b)            # [23, 'cat']
# print(lst)          # [[77], [23, 'cat'], 4]
# print(b is lst[1])  # True

# b.pop()
# print(b)            # [23]
# print(lst)          # [[77], [23], 4]
# print(b is lst[1])  # True

# b = 'mouse'
# # reassignment of b but the element at lst[1] still points to [3]
# # if you instead did lst[1] = 'mouse', b would remain [3]
# print(b)            # 'mouse'
# print(lst)          # [[77], [23], 4]
# print(b is lst[1])  # False

# lst[2] += 10
# print(c)            # 4
# print(lst)          # [[77], [23], 14]
# print(c is lst[2])  # False

	
# lst[0][1] = 8    # equivalent to a[1] = 8
# print(lst)       # [[1, 8], [2]]
# print(f'a = {a}')         # [1, 8]
# lst[1] = 'dog'
# print(lst)
# print(f'b = {b}')

# DATA[1][0]['three']

# todo_lists[0]['todos'][2]['name'] = 'Orange Juice'

# [1, 3, 4, 2, 4, 6, 5, 7, 9, 10, 12]
# [] # index 0
# [3, 4, 2, 4, 6, 5, 7, 9, 10, 12]

# [4] # index 1 is 4
# [4, 2, 4, 6, 5, 7, 9, 10, 12]

# [4, 4] # index 2 is 4
# [2, 4, 6, 5, 7, 9, 10, 12]

# [4, 4] # index 3 is 5
# [4, 6, 5, 7, 9, 10, 12]

# [4, 4] # index 4 is 9
# [6, 5, 7, 9, 10, 12]

# [4, 4, 12] # index 5 is 12
# [5, 7, 9, 10, 12]

def even_values(lst):
    evens = []

    for value in lst:
        if value % 2 == 0:
            evens.append(value)
        lst.pop(0)
        print(lst)

    return evens

even_values([1, 3, 4, 2, 4, 6, 5, 7, 9, 10, 12])