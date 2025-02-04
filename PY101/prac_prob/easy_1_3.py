# Print all even numbers from 1 to 99, inclusive, with each number
# on a separate line

messages = {
    "start": "What is the start of the range?",
    "end": "What is the end of the range?",
}

def prompt(message):
    print(f"==> {message}")

def invalid_input(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

def get_user_input():
    user_input = input()

    while invalid_input(user_input):
        prompt("Please provide an integer:")
        user_input = input()

    return int(user_input)


prompt(messages["start"])
start = get_user_input()

prompt(messages["end"])
end = get_user_input()

while end <= start:
    prompt("Please provide a value larger than the start value:")
    end = get_user_input()

if start % 2 == 0:
    for number in range(start, end + 1, 2):
        print(number)
else:
    for number in range(start + 1, end + 1, 2):
        print(number)