import json

with open('calculator_messages.json', 'r') as file:
    data = json.load(file)

# print(data["first_number"])

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

def prompt(message):
    print(f"==> {message}")

def get_language():
    prompt(data["language"])
    language = input()
    while language not in ("English", "Spanish"):
        prompt(data["language_again"])
        language = input()
        if language in ("English", "Spanish"):
            return language

    return language


def run_calculator():
    prompt(data[lang]["first_number"])
    number1 = input()

    while invalid_number(number1):
        prompt(data[lang]["valid_number"])
        number1 = input()

    prompt(data[lang]["second_number"])
    number2 = input()

    while invalid_number(number2):
        prompt(data[lang]["valid_number"])
        number2 = input()

    prompt(data[lang]["choose_operation"])
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(data[lang]["choose"])
        operation = input()

    match operation:
        case '1':
            output = float(number1) + float(number2)
        case '2':
            output = float(number1) - float(number2)
        case '3':
            output= float(number1) * float(number2)
        case '4':
            output = float(number1) / float(number2)

    prompt(f"{data[lang]["result"]} {output}")

prompt('Welcome to Calculator!')

lang = get_language()
print(lang)

while True:
    run_calculator()
    prompt(data[lang]["another_calc"])
    response = input()

    while response not in ("No", "Yes", "Si", "no"):
        print(data[lang]["valid_response"])
        response = input()

    if response in ("No", "no"):
        break






# def get_operation():
#     op = ""
#     while (op != 'add' and
#            op != 'subtract' and
#            op != 'multiply' and
#            op != 'divide'):
#         op = input("Do you want to add, subtract, multiple or divide? ")
#     return op

# def operate(num_1, num_2, operation):
#     match operation:
#         case 'add':
#             return num_1 + num_2
#         case 'subtract':
#             return num_1 - num_2
#         case 'multiply':
#             return num_1 * num_2
#         case 'divide':
#             return num_1 / num_2

# def prompt(message):
#     print(f'==> {message}')

# def invalid_number(number):
#     if not number.isdigit():
#         return True
#     else:
#         return False

# prompt("Welcome to Calculator!")
# print()

# prompt("What's the first number? ")
# num1 = int(input())
# prompt("What's the second number? ")
# num2 = int(input())
# print()

# operation = get_operation()
# result = operate(num1, num2, operation)
# print(f'{num1} {operation} {num2} = {result}')