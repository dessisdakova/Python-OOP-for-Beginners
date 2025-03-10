from dice import Dice


class Player:

    def __init__(self, is_computer=False):
        self._is_computer = is_computer
        self._counter = 10
        self._dice = Dice()

    @property
    def is_computer(self):
        return self._is_computer

    @property
    def dice(self):
        return self._dice
    @property
    def counter(self):
        return self._counter

    def increment_dice_value(self):
        self._counter += 1

    def decrement_dice_value(self):
        self._counter -= 1

    def roll_dice(self):
        self.dice.roll()