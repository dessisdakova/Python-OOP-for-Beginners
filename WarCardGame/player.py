from card import Card
from deck import Deck


class Player:

    def __init__(self, name, deck: Deck, is_computer=False):
        self._name = name
        self._deck = deck
        self._is_computer = is_computer

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def deck(self):
        return self._deck

    @property
    def is_computer(self):
        return self._is_computer

    def has_empty_deck(self) -> bool:
        return self.deck.size == 0

    def draw_card(self):
        if not self.has_empty_deck():
            return self.deck.draw()
        else:
            return None

    def add_card(self, card: Card):
        self.deck.add(card)
