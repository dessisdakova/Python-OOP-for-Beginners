import random

from card import Card
from suit import Suit


class Deck:

    SUITS = ("spades", "hearts", "diamonds", "clubs")

    def __init__(self, is_empty=False):
        self._cards = []
        if not is_empty:
            self.build()


    @property
    def cards(self):
        return self._cards

    @property
    def size(self):
        return len(self.cards)

    def build(self):
        for suit in Deck.SUITS:
            for rank in range(2, 15):
                self.cards.append(Card(Suit(suit), rank))

    def show(self):
        for card in self.cards:
            card.show()


    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if self.cards:
            return self.cards.pop()
        else:
            return None

    def add(self, card: Card):
        self.cards.insert(0, card)
