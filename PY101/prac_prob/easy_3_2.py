def crunch(string):
    collapsed_lst = ""

    for i in range(0, len(string)):
        if i == (len(string) - 1) or string[i] != string[i+1]:
            collapsed_lst += string[i]

    return collapsed_lst

# def crunch(string):
#     str_lst = list(string)
#     collapsed_lst = []
#     index = 0

#     while index < len(str_lst):
#         if index == len(str_lst) - 1:
#             collapsed_lst.append(str_lst[index])
#         elif str_lst[index] != str_lst[index + 1]:
#             collapsed_lst.append(str_lst[index])
        
#         index += 1

#     collapsed_str = "".join(collapsed_lst)
#     return collapsed_str

print(crunch("Utah"))
print(crunch("Idaho"))
print()
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')
print()