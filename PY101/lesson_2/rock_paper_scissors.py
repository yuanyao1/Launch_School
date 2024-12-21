# The user makes a choice.
# The computer makes a choice.
# The winner is displayed.

import random

OPTIONS = ("rock", "paper", "scissors")

def prompt(message):
    print(f"==> {message}")

def get_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "Tie"
    if ((user_choice == "rock" and comp_choice == "scissors") or
        (user_choice == "paper" and comp_choice == "rock") or
        (user_choice == "scissors" and comp_choice == "paper")):
        return "You win."

    return "Computer wins."

prompt(f"Let's play {", ".join(OPTIONS)}!")
play = "yes"

while play:
    prompt(f'Choose one: {", ".join(OPTIONS)}')
    user_selection = input()

    while user_selection not in OPTIONS:
        prompt(f'Please pick either {", ".join(OPTIONS)}')
        user_selection = input()

    prompt(f'You selected {user_selection}')

    computer_selection = random.choice(OPTIONS)
    prompt(f'Computer selected {computer_selection}')

    result = get_winner(user_selection, computer_selection)
    prompt(result)

    prompt("Play again? y/n")
    play = input().lower()

    while play not in ("n", "no", "y", "yes"):
        prompt('Please enter y for "yes" or n for "no"')
        play = input().lower()

    if play in ("n", "no"):
        play = ""