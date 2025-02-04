import random

def prompt(message):
    print(f"==> {message}")

def get_name(name_ = 'Teddy'):
    name_entry = input()
    if not name_entry:
        return name_
    
    return name_entry

prompt("Please provide a name:")
name = get_name()

start = 20
end = 100
age = random.randint(start, end)
print(f'{name} is {age} years old!')

# print(f'Teddy is {(range(start, end + 1))} years old!')