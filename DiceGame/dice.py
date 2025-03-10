import random


class Dice:

    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    def roll(self):
        self._value = random.randint(1, 6)