# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

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

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False
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

def prompt(message):
    print(f"==> {message}")

prompt('Welcome to Calculator!')

prompt("What's the first number?")
number1 = input()

while invalid_number(number1):
    prompt("Hmm... that doesn't look like a valid number.")
    number1 = input()

prompt("What's the second number?")
number2 = input()

while invalid_number(number2):
    prompt("Hmm... that doesn't look like a valid number.")
    number2 = input()

prompt('What operation would you like to perform?\n'
      '1) Add 2) Subtract 3) Multiply 4) Divide')
operation = input()

while operation not in ["1", "2", "3", "4"]:
    prompt('You must choose 1, 2, 3, or 4')
    operation = input()


match operation:
    case '1':
        output = int(number1) + int(number2)
    case '2':
        output = int(number1) - int(number2)
    case '3':
        output= int(number1) * int(number2)
    case '4':
        output = int(number1) / int(number2)

print(f"The result is: {output}")