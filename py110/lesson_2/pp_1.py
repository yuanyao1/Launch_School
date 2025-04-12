lst = [10, 9, -6, 11, 7, -16, 50, 8]

# lst_asc = sorted(lst)
# lst_des = sorted(lst, reverse=True)

# print(lst_asc)
# print(lst_des)

# lst.sort()
# print(lst)

# lst.sort(reverse=True)
# print(lst)

lst.sort(key=str)
print(lst)

lst.sort(key=str, reverse=True)
print(lst)
