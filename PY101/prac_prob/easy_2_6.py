def penultimate(string):
    string = string.strip()
    if not string:
        return "String is empty"
    
    words = string.split()
    print(len(words))

    if 1 <= len(words) <= 2:
        return string
    elif len(words) % 2 == 1:
        return words[len(words) // 2]
    else:
        return " ".join([words[(len(words) // 2) - 1], words[len(words) // 2]])


# print(penultimate("last word"))

# These examples should print True
# print(penultimate("last word") == "last")
# print(penultimate("Launch School is great!") == "is")

print(penultimate("") == "String is empty")
print(penultimate(" ") == "String is empty")
print(penultimate("one") == "one")
print(penultimate("last word") == "last word")
print(penultimate("Launch School Rocks!") == "School")
print(penultimate("Launch School is great!") == "School is")

print(penultimate(" one ") == "one")
print(penultimate(" last word ") == "last word")
print(penultimate(" Launch School Rocks!") == "School")
print(penultimate(" Launch School is great!") == "School is")

