statement = "The Flintstones Rock"
statement = statement.replace(" ", "")
print(statement)

char_freq = {}

# for char in statement:
#     if char_freq.get(char):
#         char_freq[char] += 1
#     else:
#         char_freq[char] = 1

for char in statement:
    char_freq[char] = char_freq.get(char, 0) + 1

print(char_freq)
print(char_freq.popitem())