def center_of(string):
    length = len(string)
    if length % 2 == 1:
        return string[length // 2]
    
    return string[(length // 2) - 1] + string[length // 2]

print(center_of(" "))
print(center_of("a"))
print(center_of("ab"))
print(center_of("abl"))
print(center_of("able"))


print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True