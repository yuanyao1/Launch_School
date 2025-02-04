# Build a program that asks the user to enter the length and width of a room
# in meters, then prints the room's area in both square meters and square feet.
# Note: 1 square meter == 10.7639 square feet

# SQFT_EQUIVALENT = 10.7639

# def get_room_size(length, width):
#     pass

# def prompt(message):
#     print(f"==> {message}")

# def get_user_input():
#     user_input = input()

#     while invalid_number(user_input) or float(user_input) <= 0:
#         prompt("Please provide a positive number:")
#         user_input = input()

#     return float(user_input)

# def invalid_number(number_str):
#     try:
#         float(number_str)
#     except ValueError:
#         return True

#     return False

# messages = {
#     "length": "What is the length of the room?",
#     "width": "What is the width of the room?",
#     "positive_num": "Please provide a positive number.",
# }

# prompt(messages["length"])
# length = get_user_input()

# prompt(messages['width'])
# width = get_user_input()

# area_sq_m = length * width
# area_sq_f = area_sq_m * SQFT_EQUIVALENT

# print('The area of the room is:')
# print(f'{area_sq_m:.2f} sq meters')
# print(f'{area_sq_f:.2f} sq ft')


length = float(input("Enter the length of the room: "))
width = float(input("Enter the width of the room: "))
measurement_type = (input("Enter meters or feet for the measurement type: "))

area = length * width

if measurement_type == "meters":
    area_conversion = area * 10.7639
    print(f"The area of the room is {area:.2f} "
      f"square meters ({area_conversion:.2f} square feet).")
if measurement_type == "feet":
    area_conversion = area / 10.7639
    print(f"The area of the room is {area:.2f} "
      f"square feet ({area_conversion:.2f} square meters).")    