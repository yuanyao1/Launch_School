# Problem
"""
Inputs: list of strings
Outputs: sorted list of the original list of strings from highest number of 
adjacent consonants

Explicit rules:
1. Two strings with same number of adjacent consonants stay in same order in
resulting sorted list
2. Consonants are considered adjacent if they are next to each other in the
same word or if there is a space between two consonants in adjacent words

Implicit rules:
1. Strings can have multiple words
2. Consonants are alphabetic letters but not a, e, i, o, u
3. What about numbers in a string? ignore
4. Will there be duplicate strings? No

Questions:
1. Are you considering the letter y as a consonant? Yes

Data Structures:
1. List representing original list
2. List representing new sorted list
3. Integer representing number of adjacent consonants
4. dictionary holding number of adjacent consonants to each string in the list
{
    string1: number of consonants,
    string2: number of consonants,
    ...
}

Algorithm:
0. initialize CONSONANTS tuple with ('a', 'e', 'i', 'o', 'u')
0. initialize orig_list to the input list
1. initialize sorted_result to an empty list
2. initialize consonants_per_str to an empty dictionary
2. initialize max_cons to 0
3. calculate the number of adjacent consonants per string
    - initialize adj_cons_num to 0
    - remove all whitespace in the string
    - split the string using successive calls to the split method
    - loop through each string of the orig_list and check to see if each char
    and the preceding char are consonants
    - if the char is a space then go to next char and check if that char and
    char from 2 spots before are consonants
    - update max_cons if the adjacent consonants is 2 or more and greater than
    the current max_cons value
4. store each strings and the number of consonants as key: value pairs in
the consonants_per_str dictionary
5. sort the dictionary by the values in descending order
6. return a list of the keys from the dictionary
"""

# def sort_by_consonant_count(lst):
#     cons_dict = {element: 0 for element in lst}

#     for key in cons_dict:
#         key_cleaned = key.replace(" ", "")
#         cons_dict[key] = count_cons(key_cleaned)
    
#     sorted_dict = dict(sorted(cons_dict.items(), key=lambda item: item[1], 
#                               reverse=True))

#     return list(sorted_dict.keys())

def sort_by_consonant_count(lst):
    lst.sort(key=count_cons, reverse=True)

    return lst

def count_cons(text):
    max_adj_cons = 0
    sub_text = ""
    sub_text_adj_cons = 0
    
    for char in text:
        if char in VOWELS:
            sub_text = ""
            sub_text_adj_cons = 0
            continue

        sub_text += char
        sub_text_adj_cons += 1
        
        if sub_text_adj_cons > max_adj_cons:
            max_adj_cons = sub_text_adj_cons
    
    return 0 if max_adj_cons < 2 else max_adj_cons

VOWELS = ('a', 'e', 'i', 'o', 'u')


# my_list = ['can can']
# print(sort_by_consonant_count(my_list))


# print(count_cons('cancan') == 2)
# print(count_cons('cancan'))
# my_list = ['aa', 'baa', 'ccaa', 'dddaa']
# print(sort_by_consonant_count(my_list))
# # ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']