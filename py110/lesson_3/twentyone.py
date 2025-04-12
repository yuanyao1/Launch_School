import random

SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
          'Jack', 'Queen', 'King', 'Ace']
MAX_WINNING_HAND = 21
DEALER_FLOOR = 17
MATCH_WINS = 3

scores = {
    'player': 0,
    'dealer': 0,
    'tie':  0,
}

def prompt(msg):
    print(f'==> {msg}')

def initialize_deck():
    deck = [[suit, value] for suit in SUITS for value in VALUES]
    random.shuffle(deck)
    return deck

def deal_cards(deck):
    player_cards = []
    dealer_cards = []
    for _ in range(2):
        player_cards.append(deck.pop())
        dealer_cards.append(deck.pop())

    return player_cards, dealer_cards

def join_and(lst, sep=', ', word='and'):
    if len(lst) == 2:
        return f'{lst[0]} {word} {lst[1]}'

    return f'{sep.join(lst[:-1])}{sep}{word} {lst[-1]}'

def show_hand(hand):
    values = [value[1] for value in hand]
    return join_and(values)

def busted(hand, max_hand):
    return hand > max_hand

def hit_or_stay(deck, hand, hand_total, max_hand):
    prompt('(h)it or (s)tay?')
    response = input().strip().lower()
    while response not in ['hit', 'h', 'stay', 's']:
        prompt('Invalid response. (h)it or (s)tay?')
        response = input().strip().lower()

    if response in ('hit', 'h'):
        prompt('Player hits.')
        hand.append(deck.pop())
        hand_total = total(hand, max_hand)
        prompt(f'Player has: {show_hand(hand)} for total: {hand_total}')
    else:
        prompt('Player stays.')

    return response

def dealer_hits(deck, hand, hand_total, max_hand, floor):
    if hand_total >= floor:
        prompt('Dealer stays.')
        return False

    prompt("Dealer hits.")
    hand.append(deck.pop())
    hand_total = total(hand, max_hand)
    prompt(f'Dealer has: {show_hand(hand)} for total: {hand_total}')

    return True

def total(hand, max_hand):
    total_hand = 0
    values = []

    for _, value in hand:
        values.append(value)
        if value in ['Jack', 'Queen', 'King']:
            total_hand += 10
        elif value == 'Ace':
            total_hand += 11
        else:
            total_hand += int(value)

    for _ in range(values.count('Ace')):
        if total_hand <= max_hand:
            break
        total_hand -= 10

    return total_hand

def get_result(player_hand, dealer_hand, max_hand):
    if busted(player_hand, max_hand):
        return 'Player busted'
    if busted(dealer_hand, max_hand):
        return 'Dealer busted'
    if player_hand > dealer_hand:
        return 'Player'
    if player_hand < dealer_hand:
        return 'Dealer'

    return 'Tie'

def display_result(p_hand, d_hand, p_tot, d_tot, max_hand):
    prompt('******** FINAL RESULT ********')
    prompt(f'Dealer has: {show_hand(d_hand)} for total: {d_tot}')
    prompt(f'Player has: {show_hand(p_hand)} for total: {p_tot}')
    result = get_result(p_tot, d_tot, max_hand)

    match result:
        case 'Player busted':
            prompt('Player busted. Dealer wins!')
        case 'Dealer busted':
            prompt('Dealer busted. Player wins!')
        case 'Player':
            prompt('Player wins!')
        case 'Dealer':
            prompt('Dealer wins!')
        case _:
            prompt("It's a tie!")
    prompt('******************************')

    return result

def keep_score(result, score):
    if result == 'Player busted' or result == 'Dealer':
        scores['dealer'] += 1
    elif result == 'Dealer busted' or result == 'Player':
        scores['player'] += 1
    else:
        scores['tie'] += 1

    return (f'Scores: Player: {score['player']} | '
            f'Dealer: {score['dealer']} | '
            f'Tie: {score['tie']}')

def play_again():
    prompt("Play again? (y)es/(n)o")
    response = input().strip().lower()

    while response not in ('yes', 'y', 'no', 'n'):
        prompt("Invalid response. Play again? y/n")
        response = input().strip().lower()

    if response in ('no', 'n'):
        prompt('******** Thanks for playing! ********')
        print()
    else:
        print()
        prompt('******** NEW ROUND ********')

    return response in ('yes', 'y')

def match_won(score):
    if score['player'] == MATCH_WINS:
        prompt('***** Player wins Match! *****')
        return True
    if score['dealer'] == MATCH_WINS:
        prompt('***** Dealer wins Match! *****')
        return True
    
    return False

def start_playing(max_hand, dealer_floor, score):
    print()
    if max_hand == 21:
        prompt("******** Let's play Twenty-One! ********")
    else:
        prompt(f'******** Let\'s play {max_hand}! ********')

    deck = initialize_deck()

    while True:
        # Begin game with new deck of cards if majority of cards used
        if len(deck) < 27:
            deck = initialize_deck()

        print(f'cards in deck is {len(deck)}')
        player_cards, dealer_cards = deal_cards(deck)
        player_total = total(player_cards, max_hand)
        dealer_total = total(dealer_cards, max_hand)

        prompt(f'Dealer has: {dealer_cards[0][1]} and unknown card')
        prompt(f'Player has: {show_hand(player_cards)} for total: '
               f'{player_total}')

        # Player turn
        while True:
            if (busted(player_total, max_hand) or
                (hit_or_stay(deck, player_cards, player_total, max_hand)
                in ('stay', 's'))):
                break
            player_total = total(player_cards, max_hand)

        if busted(player_total, max_hand):
            result = display_result(player_cards, dealer_cards, player_total,
                           dealer_total, max_hand)
            
            prompt(keep_score(result, score))

            if match_won(score) and play_again():
                score = {key: 0 for key, value in score.items()}
                continue
            if play_again():
                continue
            break

        prompt("Dealer's turn...")
        while True:
            if busted(dealer_total, max_hand):
                result = display_result(player_cards, dealer_cards, player_total,
                               dealer_total, max_hand)
                prompt(keep_score(result, score))
                match_won(score)

                break

            if not dealer_hits(deck, dealer_cards, dealer_total,
                               max_hand, dealer_floor):

                result = display_result(player_cards, dealer_cards, player_total,
                               dealer_total, max_hand)
                prompt(keep_score(result, score))
                match_won(score)

                break

            dealer_total = total(dealer_cards, max_hand)

        if not play_again():
            break

start_playing(MAX_WINNING_HAND, DEALER_FLOOR, scores)




    # bet = bet_hand(chips)
    # prompt('Please enter the amount of money do you want to play with:')
    # chips = input().strip().lower()

    # while invalid_number(chips):
    #     prompt('Please enter a whole number:')
    #     chips = input().strip().lower()

# def invalid_number(num_str):
#     try:
#         int(num_str)
#     except ValueError:
#         return True

#     return False

# def bet_hand(chips):
#     prompt('Place down your bet:')
#     bet_size = input().strip().lower()

#     while invalid_number(bet_size) and bet_size > chips:
#         prompt('Invalid bet size. Give a whole number less than or equal to'
#                'your remaining amount:')
    
#     return bet_size

# def chips_total():
#     pass