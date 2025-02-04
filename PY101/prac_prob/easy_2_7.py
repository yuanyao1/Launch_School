def xor(value1, value2):
    return False if all([value1, value2]) else any([value1, value2])

print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)
print(xor("", 0) == False)