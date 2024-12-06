# def is_empty_or_blank(string):
#     if string.count(" ") == len(string) or not string:
#        return True
#     else:
#         return False 

def is_empty_or_blank(string):
    return not string.isalnum()

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True