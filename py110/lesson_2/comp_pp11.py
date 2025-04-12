dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

VOWELS = 'aeiou'

list_of_vowels = []

# for sublist in dict1.values():
#     for word in sublist:
#         for char in word:
#             if char in VOWELS:
#                 list_of_vowels.append(char)

list_of_vowels = [char
                  for sublist in dict1.values()
                  for word in sublist
                  for char in word
                  if char in VOWELS]

print(list_of_vowels)


# def vowels_in_word(word):
#     vowels = ''
#     for char in word:
#         if char in VOWELS:
#             vowels += char
    
#     return vowels

# all_vowels = ''

# for sublist in dict1.values():
#     for word in sublist:
#         if vowels_in_word(word) is not None:
#             all_vowels += vowels_in_word(word)

vowels_total = []
# for sublist in dict1.values():
#     for word in sublist:
#         if vowels_in_word(word) is not None:
#             vowels_total.extend(vowels_in_word(word))

# print(vowels_total)

# list_of_vowels = [vowels_total.extend(vowels_in_word(word))
#                   for sublist in dict1.values()
#                   for word in sublist
#                   if vowels_in_word(word) is not None]

# list_of_vowels = list(all_vowels)
# print(list_of_vowels)

# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']

# Write some code to create a list of every vowel (a, e, i, o, u)
# that appears in the contained strings, then print it.