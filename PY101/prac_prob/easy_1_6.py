# Write a program that asks the user to enter an integer greater than 0,
# then asks whether the user wants to determine the sum or the product
# of all numbers between 1 and the entered integer, inclusive.

OPERATIONS = {
    's': 'sum',
    'p': 'product',
}

CHOICES = OPERATIONS.keys()

def prompt(msg):
    print(f'>== {msg}')

def get_product(num):
    result = 1
    while num:
        result *= num
        num -= 1

    return result

def get_sum(num):
    return sum(range(1,num + 1))

def invalid_value(num_str):
    try:
        int(num_str)
    except ValueError:
        return True

    return False

def invalid_operation(oper_str):
    if oper_str not in CHOICES:
        return True

    return False

def main():
    prompt("Please enter an integer greater than 0:")
    value = input()
    while invalid_value(value) or int(value) <= 0:
        prompt("Invalid input. Please enter an integer greater than 0:")
        value = input()

    value = int(value)

    prompt('Enter "s" to compute the sum, or "p" to compute the product:')
    operation = input()
    while invalid_operation(operation):
        prompt('Invalid operation. Enter "s" for sum, or "p" for product:')
        operation = input()

    if operation == 's':
        print(f'The {OPERATIONS[operation]} of the integers between 1 and'
              f' {value} is {get_sum(value)}')

    if operation == 'p':
        print(f'The {OPERATIONS[operation]} of the integers between 1 and'
              f' {value} is {get_product(value)}')

main()