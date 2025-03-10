from suit import Suit


class Card:

    SPECIAL_CARD_AND_VALUE = {
        14 :"Ace",
        13: "King",
        12: "Queen",
        11: "Jack"
    }

    def __init__(self, suit: Suit, value):
        self._suit = suit

        if value < 2 or value > 14:
            raise ValueError(f"Invalid card value: {value}")

        self._value = value

    @property
    def suit(self):
        return self._suit

    @property
    def value(self):
        return self._value

    def is_special(self) -> bool:
        return self.value > 10

    def show(self):
        rank = self.value
        suit = self.suit.description.capitalize()
        symbol = self.suit.symbol

        if self.is_special():
            desc = Card.SPECIAL_CARD_AND_VALUE.get(rank)
            print(f"{desc} {suit} {symbol}")
        else:
            print(f"{rank} {suit} {symbol}")
