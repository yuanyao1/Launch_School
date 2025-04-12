# Display the initial empty 3x3 board.
# Ask the user to mark a square.
# Computer marks a square.
# Display the updated board state.
# If it's a winning board, display the winner.
# If the board is full, display tie.
# If neither player won and the board is not full, go to #2
# Play again?
# If yes, go to #1
# Goodbye!

# board = {
#     1: ' ', # top left
#     2: ' ', # top center
#     3: ' ', # top right
#     4: ' ', # middle left
#     5: ' ', # middle center
#     6: ' ', # middle right
#     7: ' ', # bottom left
#     8: ' ', # bottom left
#     9: ' ', # bottom left
# }

import random
import os

EMPTY_MARKER = ' '
HUMAN_MARKER = 'X'
COMP_MARKER = 'O'
MATCH_WINS = 3
TURN_CHOICE = ('player', 'computer', 'random')

WINNING_COMBOS = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9},  # rows
                  {1, 4, 7}, {2, 5, 8}, {3, 6, 9},  # columns
                  {1, 5, 9}, {3, 5, 7}]             # diagonals

scores = {
    'User': 0,
    'Computer': 0,
    'Tie':  0,
}

def prompt(message):
    print(f'>== {message}')

def display_board(board):
    # os.system('clear')

    print(f"You are {HUMAN_MARKER}. Computer is {COMP_MARKER}")
    print('     |     |')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}')
    print('     |     |')
    print('')

def initialize_board():
    return {square: EMPTY_MARKER for square in range(1, 10)}

def valid_choice(square):
    try:
        int(square)
    except ValueError:
        return False

    return int(square)

def get_squares(board, marker):
    return {key for key, value in board.items() if value == marker}

def join_or(lst, sep=', ', word='or'):
    values = [str(value) for value in lst]
    if not values:
        return ""
    elif len(values) == 1:
        return values[0]
    elif len(values) == 2:
        return f'{values[0]} {word} {values[1]}'

    return f'{sep.join(values[:-1])}{sep}{word} {values[-1]}'

def player_chooses_square(board):
    empty_squares = [str(num) for num in get_squares(board, EMPTY_MARKER)]
    print(f'empty squares: {empty_squares}')

    while True:
        prompt(f'Choose a square {join_or(empty_squares)}:')
        square = input().strip() # good practice use strip to remove leading
                                 # and trailing whitespaces
        # guard clause if statement if only break
        if square in empty_squares:
            break

        prompt("Not valid square. Try again.")

    board[int(square)] = HUMAN_MARKER

def comp_chooses_sq(board):
    empty_squares = get_squares(board, EMPTY_MARKER)

    # offensive
    if find_at_risk_square(board, WINNING_COMBOS, COMP_MARKER):
        return

    # defensive
    if find_at_risk_square(board, WINNING_COMBOS, HUMAN_MARKER):
        return

    if board[5] is EMPTY_MARKER:
        board[5] = COMP_MARKER
        return

    square = random.choice(list(empty_squares))
    board[square] = COMP_MARKER

def choose_square(board, current_player):
    if current_player == 'player':
        player_chooses_square(board)
    else:
        comp_chooses_sq(board)

def alternate_player(current_player):
    if current_player == 'player':
        return 'computer'
    
    return 'player'

def find_at_risk_square(board, winning_combos, marker):
    choices = get_squares(board, marker)

    for combo in winning_combos:
        winning_square = (combo - choices).pop()  
        if (len(combo.intersection(choices)) == 2 and
            board[winning_square] == EMPTY_MARKER):
            print(f'last combo free square: {winning_square}')
            board[winning_square] = COMP_MARKER
            return True

    return None

def board_full(board):
    empty_squares = get_squares(board, EMPTY_MARKER)
    return len(empty_squares) == 0

def someone_won(board):
    return bool(get_winner(board))

def get_winner(board):
    user_choices = get_squares(board, HUMAN_MARKER)
    comp_choices = get_squares(board, COMP_MARKER)

    for combo in WINNING_COMBOS:
        if combo.issubset(user_choices):
            return 'User'
        if combo.issubset(comp_choices):
            return 'Computer'
  
    return None

def display_score(board, scores):
    if get_winner(board) == 'User':
        scores['User'] += 1
    elif get_winner(board) == 'Computer':
        scores['Computer'] += 1
    else:
        scores['Tie'] += 1

    return (f'Scores: User: {scores['User']} | Computer: {scores['Computer']} |'
            f' Tie: {scores['Tie']}')

def start_playing(scores):
    while True:
        board = initialize_board()

        prompt(f'Decide who goes first: {TURN_CHOICE}')
        turn_input = input().strip().lower()
        while turn_input not in (TURN_CHOICE):
            prompt(f'Not valid choice. Please decide again: {TURN_CHOICE}')
            turn_input = input().strip().lower()
        
        if turn_input == 'random':
            while True:
                turn_input = random.choice(TURN_CHOICE)
                if turn_input != 'random':
                    break
        
        print(f'turn input: {turn_input}')
        current_player = turn_input

        while True:
            display_board(board)
            choose_square(board, current_player)
            current_player = alternate_player(current_player)
            if someone_won(board) or board_full(board):
                break

        display_board(board)
        if someone_won(board):
            prompt(f'{get_winner(board)} won!')
            # get_score() # print out the score
        else:
            prompt("It's a tie!")

        prompt(display_score(board, scores))

        if scores['User'] == MATCH_WINS:
            prompt('***** User wins Match! *****')
        if scores['Computer'] == MATCH_WINS:
            prompt('***** Computer wins Match *****!')

        if scores['User'] == 3 or scores['Computer'] == 3:
            prompt('Play a new match? y/n')
            user_input = input().strip().lower()
            while user_input not in ('y', 'n', 'yes', 'no'):
                prompt('Not valid response. Play a new match? y/n')
                user_input = input().strip().lower()
            scores = {key: 0 for key, value in scores.items()}
        else:
            prompt('Play again? y/n')
            user_input = input().strip().lower()
            while user_input not in ('y', 'n', 'yes', 'no'):
                prompt('Not valid response. Play again? y/n')
                user_input = input().strip().lower()

        if user_input in ('n', 'no'):
            prompt('Thanks for playing!')
            break

start_playing(scores)