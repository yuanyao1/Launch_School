# def is_color_valid(color):
#     if color == "blue" or color == "green":
#         return True
#     else:
#         return False

# def is_color_valid(color):
#     return color == "green" or color == "blue"
    

def is_color_valid(color):
    return color in ["blue", "green"]

print(is_color_valid("orange"))
print(is_color_valid("green"))