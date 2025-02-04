def prompt(message):
    print(f"==> {message}")


print("Enter the first number:")
num1 = float(input())

print("Enter the second number:")
num2 = float(input())

prompt(f'{num1} + {num2} = {num1 + num2}')
prompt(f'{num1} - {num2} = {num1 - num2}')
prompt(f'{num1} * {num2} = {num1 * num2}')
prompt(f'{num1} / {num2} = {num1 / num2}')
prompt(f'{num1} // {num2} = {num1 // num2}')
prompt(f'{num1} % {num2} = {num1 % num2}')
prompt(f'{num1} ** {num2} = {num1 ** num2}')