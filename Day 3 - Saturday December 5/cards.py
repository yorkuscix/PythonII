# this is a comment. Python ignores these lines

# import random allows us to generate random numbers
import random

suits = ['Spade', 'Heart', 'Club', 'Diamond']
values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

def generate_deck():
    deck = []
    for suit in suits:
        for value in values:
            deck.append(value + suit)
    return deck

def draw(deck):
    card = deck[0] # get the top card of the deck and store it in a variable
    deck.remove(card) # remove that card from the deck
    return card # return the card we drew

# this function calls draw multiple times to draw a list of cards
def deal(deck, num):
    hand = [] # create an empty list
    for i in range(num): # repeat num times
        hand.append(draw(deck)) # draw a card and place it in the hand
    return hand

def cut_deck(deck, i):
    top = deck[:i] # get the cards from the beginning to index i
    bottom = deck[i:] # get all cards from index i to the end
    deck[:] = bottom + top # put them back in the reverse order

# insert a card into the deck at index i
def insert(deck, card, i):
    top = deck[:i]
    bottom = deck[i:]
    deck[:] = top + [card] + bottom

def shuffle(deck):
    for i in range(100): # shuffle 100 times
        length = len(deck) # get the length of the deck
        i = random.randint(0, length-1) # get a random index in the list
        cut_deck(deck, i) # cut the deck at that index
        card = draw(deck) # draw the top card from the deck
        i = random.randint(0, length-1) # get a random index in the list
        insert(deck, card, i) # insert the drawn card at that index

# try typing in the shell:
# deck = generate_deck()
# deck
# shuffle(deck)
# deck
#
#
# first, the deck should be in order, then it should be shuffled randomly