lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

sorted_lst = []
for sublist in lst:
    sorted_lst.append(sorted(sublist))

print(sorted_lst)
print(lst)

# sorted_lst = [sorted(sublist) for sublist in lst]
# print(sorted_lst)
# print(lst)