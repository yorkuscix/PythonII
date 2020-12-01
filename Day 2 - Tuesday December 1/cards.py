suits = ['Spade', 'Heart', 'Club', 'Diamond']
values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

def generate_deck():
    deck = []
    for suit in suits:
        for value in values:
            deck.append(value + suit)
    return deck