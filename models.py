import random

CARDS = []
suits = ['S', 'C', 'D', 'H']
numbers = range(1, 14)
for suit in suits:
    for number in numbers:
        CARDS.append(suit + str(number))


class Deck:
    def __init__(self):
        self.cards = CARDS[:]
        
    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

class Hand:
    def __init__(self, cards={'S': [], 'C': [], 'D': [], 'H': []}):
        self.cards = cards

    def draw(self, deck):
        card = deck.draw()
        self.cards[card[0]].append(card[1:])

    def sort(self):
        for suit, numbers in self.cards.items():
            numbers.sort()

    def play(self, suit, index):
        card = self.cards[suit][index]
        del self.cards[suit][index]
        return card
