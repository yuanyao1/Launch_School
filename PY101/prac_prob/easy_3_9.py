def clean_up(string):
    result = ""
    for char in string:
        if char.isalpha():
            result += char
        elif len(result) == 0 or result[-1] != ' ':
            result += " "

    return result

print(clean_up("!"))        # " "
print(clean_up("!h"))       # " h"
print(clean_up(" !h"))      # " h"

#  len(result) != 0 and 
print(clean_up("!") == " ")
print(clean_up("!h") == " h")
print(clean_up(" !h") == " h")
print(clean_up("he:llo $%^world!") == "he llo world ")
print(clean_up("---what's my +*& line?") == " what s my line ")