import random

CONDITIONS = {
    'rock': {
        'abbr': 'r',
        'beats': ("scissors", "lizards")
    },
    'paper': {
        'abbr': 'p',
        'beats': ("rock", "spock")
    },
    'scissors': {
        'abbr': 'sc',
        'beats': ("paper", "lizard")
    },
    'lizard': {
        'abbr': 'l',
        'beats': ("spock", "paper")
    },
    'spock': {
        'abbr': 'sp',
        'beats': ("scissors", "rock")
    }
}

CHOICES = tuple(CONDITIONS.keys())
ABBR_CHOICES = [element['abbr'] for element in CONDITIONS.values()]
MAX_WINS = 3

scores = {
    'user': 0,
    'comp': 0,
    'tie':  0,
}

messages = {
    'tie': "It's a tie!",
    'user_win': "You win!",
    'comp_win': "Computer wins!",
    'grand_win_user': "You are the grand winner!",
    'grand_win_comp': "Computer is the grand winner!",
    'scoreboard': 'User: {user_pts} | Computer: {comp_pts} | Ties: {tie_pts}',
}

def prompt(message):
    print(f"==> {message}")

def get_winner(user, comp):
    if user == comp:
        return messages['tie']

    if comp in CONDITIONS[user]['beats']:
        return messages['user_win']

    return messages['comp_win']

def get_user_selection():
    user_input = input().lower()

    while user_input not in CHOICES and user_input not in ABBR_CHOICES:
        prompt(f'Please pick either {", ".join(CHOICES)} or shorthand'
               f' {", ".join(ABBR_CHOICES)}')
        user_input = input().lower()

    if user_input in ABBR_CHOICES:
        for key, value in CONDITIONS.items():
            if value['abbr'] == user_input:
                user_input = key

    return user_input

def keep_score(game):
    if game == messages['user_win']:
        scores['user'] += 1
    elif game == messages['comp_win']:
        scores['comp'] += 1
    else:
        scores['tie'] += 1

def continue_play():
    if scores['user'] == MAX_WINS:
        prompt(messages['grand_win_user'])
        return 'no'

    if scores['comp'] == MAX_WINS:
        prompt(messages['grand_win_comp'])
        return 'no'

    prompt("Play again? y/n")
    return input().lower()

def run_game():
    play = "yes"

    while play in ("y", "yes"):
        prompt(f'Choose one: {", ".join(CHOICES)}')
        user_selection = get_user_selection()

        prompt(f'You selected {user_selection}')

        computer_selection = random.choice(CHOICES)
        prompt(f'Computer selected {computer_selection}')

        result = get_winner(user_selection, computer_selection)
        prompt(result)

        keep_score(result)
        prompt(messages['scoreboard'].format(user_pts = scores['user'],
                                            comp_pts = scores['comp'],
                                            tie_pts = scores['tie']))

        play = continue_play()

        while play not in ("n", "no", "y", "yes"):
            prompt('Please enter y for "yes" or n for "no"')
            play = input().lower()

prompt(f"Let's play {", ".join(CHOICES)}!")
run_game()