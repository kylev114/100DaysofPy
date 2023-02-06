# TITLE: BlackJack Game
# DESCRIPTION: Simulates blackjack game with user input 
# for play, starting balance, and game finish against computer dealer.
# DATE: 

import random

# Generate dict of 13 cards with 4 suits; {card key; suit value}
suits = ['hearts', 'diamonds', 'clubs', 'spades']
numbers = list(range(2,11))
faces = ['jack', 'queen', 'king', 'ace']
cards13 = numbers + faces
deck52 = {}
for i in cards13: deck52[i] = suits
#print(deck52)

# Draw a random card
def drawCard ():
    value = random.choice(cards13)
    suit = random.choice(suits)
    return print(value,'of',suit)

def draw2Card():
    value = random.choice(cards13)
    suit = random.choice(suits)
    return print(value,'of',suit)

# if input('Welcome to the Table, would you like to play? y or n\n').lower() == 'y':
#     balance = input('How much money would you like to add')
# else: 
#     print("Ok, thanks for stopping by!")
#     exit()


#♠♥♦♣♤♡♧♢