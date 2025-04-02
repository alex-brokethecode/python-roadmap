# Card Shuffling and Dealing: Write a Python program that simulates shuffling a deck of cards
# and dealing a hand of a specified number of cards

from random import shuffle


def get_deck():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    suits = ['♣', '♦', '♥', '♠']

    return [f'{card}{suit}' for card in cards for suit in suits]


def deal_cards(deck: list[str], number: int) -> list[str]:
    return [deck.pop() for _ in range(number)]


def start_game():
    deck = get_deck()
    shuffle(deck)

    player1 = deal_cards(deck, 7)
    player2 = deal_cards(deck, 7)

    print('Player 1: ', player1)
    print('Player 2: ', player2)


start_game()
