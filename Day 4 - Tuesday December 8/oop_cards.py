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