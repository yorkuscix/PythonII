import random

def find_lowest(lst):
    lowest = lst[0]
    for e in lst:
        if e < lowest:
            lowest = e
    return lowest

def selection_sort(lst):
    new_lst = []
    while len(lst) > 0:
        lowest = find_lowest(lst)
        lst.remove(lowest)
        new_lst.append(lowest)
    return new_lst

class Suit:
    suits = ['Spade', 'Heart', 'Club', 'Diamond']
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def __lt__(self, other):
        return self.suits.index(self.name) < self.suits.index(other.name)
    def __gt__(self, other):
        return self.suits.index(self.name) > self.suits.index(other.name)
    def __eq__(self, other):
        return self.name == other.name

class Number:
    values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def __lt__(self, other):
        return self.values.index(self.name) < self.values.index(other.name)
    def __gt__(self, other):
        return self.values.index(self.name) > self.values.index(other.name)
    def __eq__(self, other):
        return self.name == other.name

class Card:
    def __init__(self, number_name, suit_name):
        self.number = Number(number_name)
        self.suit = Suit(suit_name)
    def __str__(self):
        return str(self.number) + ' of ' + str(self.suit) + 's'
    def __lt__(self, other):
        return (self.suit < other.suit or
                self.suit == other.suit and self.number < other.number)
    def __gt__(self, other):
        return (self.suit > other.suit or
                self.suit == other.suit and self.number > other.number)
    def __eq__(self, other):
        return self.suit == other.suit and self.number == other.number

class Deck:
    suits = ['Spade', 'Heart', 'Club', 'Diamond']
    values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    def __init__(self):
        self.cards = []
        for suit in self.suits:
            for value in self.values:
                c = Card(value, suit)
                self.cards.append(c)
    def __str__(self):
        output = ""
        for card in self.cards:
            output = output + str(card) + ', '
        return output
    def draw(self):
        card = self.cards[0]
        self.cards.remove(card)
        return card
    def deal(self, num):
        hand = Deck()
        hand.cards = []
        for i in range(num):
            hand.cards.append(self.draw())
        return hand
    
    def cut_deck(self):
        length = len(self.cards)
        cut_loc = random.randint(0, length-1)
        self.cards[:] = self.cards[cut_loc:] + self.cards[:cut_loc]
    
    def insert(self, card):
        length = len(self.cards)
        loc = random.randint(0, length-1)
        self.cards[:] = self.cards[:loc] + [card] + self.cards[loc:]

    def shuffle(self):
        for i in range(100000):
            self.cut_deck()
            card = self.draw()
            self.insert(card)

    def sort(self):
        self.cards = selection_sort(self.cards)

def war():
    deck = Deck()
    deck.shuffle()
    p1Hand = deck.deal(26)
    p2Hand = deck.deal(26)
    while len(p1Hand.cards) > 0 and len(p2Hand.cards) > 0:
        print('p1Hand: ' + str(p1Hand))
        print('p2Hand: ' + str(p2Hand))
        p1Card = p1Hand.draw()
        p2Card = p2Hand.draw()
        print('Player 1 draws ' + str(p1Card) + ' and Player 2 draws ' + str(p2Card))
        if p1Card.number > p2Card.number:
            print("Player 1's card is higher!")
            p2Hand.insert(p1Card)
            p2Hand.insert(p2Card)
        if p2Card.number > p1Card.number:
            print("Player 2's card is higher!")
            p1Hand.insert(p1Card)
            p1Hand.insert(p2Card)
        if p2Card.number == p1Card.number:
            print("It's a tie")
            p1Hand.insert(p1Card)
            p2Hand.insert(p2Card)
        print('Press Enter to continue...')
        input()
    if len(p1Hand.cards) == 0:
        print('Player 1 wins!')
    if len(p2Hand.cards) == 0:
        print('Player 2 wins!')

def choose_card(hand):
    print('Hand:')
    for i in range(len(hand.cards)):
        print(str(i) + ') ' + str(hand.cards[i]))
    choice = int(input('Choice: '))
    return choice
