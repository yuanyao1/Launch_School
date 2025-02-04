def stringy(integer):
    result = ""
    for i in range(integer):
        result = result + "1" if i % 2 == 0 else result + "0"

    return result

# def stringy(integer):
#     result = "".join(["1" if i % 2 == 0 else "0" for i in range(integer)])
#     return result

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True