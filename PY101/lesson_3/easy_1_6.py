str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

def find_string(str_orig):
    if str_orig.find("Dino") >= 0:
        return True
    
    return False

print(find_string(str1))
print(find_string(str2))

# def find_string(str_orig):
#     l_str = str_orig.split()
#     print(l_str)
#     return "Dino" in l_str

# print(find_string(str1))
# print(find_string(str2))

# print(str1.find("Dino"))
# print(str2.find("Dino"))