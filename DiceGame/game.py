from player import Player


class Game:

    HUMAN_WINS = 0
    COMPUTER_WINS = 1

    def __init__(self, player1: Player, player2: Player):
        self._human = player1
        self._computer = player2

    @property
    def human(self):
        return self._human

    @property
    def computer(self):
        return self._computer

    def compare_and_return_winner(self):
        if self.human.dice.value > self.computer.dice.value:
            self.human.decrement_dice_value()
            return 0
        elif self.human.dice.value < self.computer.dice.value:
            self.computer.decrement_dice_value()
            return 1
        else:
            return None


    def is_game_over(self):
        if self.human.counter == 0:
            return True
        elif self.computer.counter == 0:
            return True
        else:
            return False

    def get_game_winner(self):
        if self.human.dice.value == 0:
            return self.human
        elif self.computer.dice.value == 0:
            return self.computer

    def start_round(self):
        print("\n===  Round starts!  ===")
        input("Press enter to roll your dice! \n")
        self.human.roll_dice()
        self.computer.roll_dice()
        print(f"(your number) | {self.human.dice.value} vs {self.computer.dice.value} | (computer number)")
        winner = self.compare_and_return_winner()
        if winner == Game.HUMAN_WINS:
            print("You WON this round!")
        elif winner == Game.COMPUTER_WINS:
            print("You LOST this round!")
        else:
            print("It's a tie!")
        print(f"your counter: {self.human.counter} | computer counter: {self.computer.counter}")

    def print_welcome_message(self):
        print("===========================")
        print("   Welcome to Dice Game!   ")
        print("===========================")

me = Player()
ps = Player(True)
game = Game(me, ps)
game.print_welcome_message()

while not game.is_game_over():
    game.start_round()

winner = game.get_game_winner()
if winner == Game.HUMAN_WINS:
    print("Congratulations! YOU WON THIS GAME!")
else:
    print("Sorry! You LOST this game!")
