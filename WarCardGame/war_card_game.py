from card import Card
from deck import Deck
from player import Player


class WarCardGame:

    PLAYER = 0
    COMPUTER = 1
    TIE = 2

    def __init__(self, player: Player, computer: Player, deck: Deck):
        self._player = player
        self._computer = computer
        self._deck = deck

        self.make_initial_decks()

    def make_initial_decks(self):
        self._deck.shuffle()
        self.make_deck(self._player)
        self.make_deck(self._computer)

    def make_deck(self, character):
        for i in range(26):
            card = self._deck.draw()
            character.add_card(card)

    def start_battle(self, cards_from_war=None):
        print("\n == Let's start the battle ==\n")

        player_card = self._player.draw_card()
        computer_card = self._computer.draw_card()
        print(f"Your card: ")
        player_card.show()
        print(f"Computer card: ")
        computer_card.show()

        winner = self.get_round_winner(player_card, computer_card)
        cards_won = self.get_cards_won(player_card, computer_card, cards_from_war)

        if winner == WarCardGame.PLAYER:
            print("You won this round!")
            self.add_carts_to_character(self._player, cards_won)
        elif winner == WarCardGame.COMPUTER:
            print("You lost. Computer won.")
            self.add_carts_to_character(self._computer, cards_won)
        else:
            print("It's a tie. This is war!")
            self.start_war(cards_won)

        return winner

    def get_round_winner(self, first_card: Card, second_card: Card):
        if first_card.value > second_card.value:
            return WarCardGame.PLAYER
        elif first_card.value < second_card.value:
            return WarCardGame.COMPUTER
        else:
            return WarCardGame.TIE

    def get_cards_won(self, first_card, second_card, previous_cards) -> list:
        if previous_cards:
            return [first_card, second_card] + previous_cards
        else:
            return [first_card, second_card]

    def add_carts_to_character(self, character: Player, list_of_cards):
        for card in list_of_cards:
            character.add_card(card)

    def start_war(self, cards_from_battle):
        player_cards = []
        computer_cards = []

        for i in range(3):
            player_cards.append(self._player.draw_card())
            computer_cards.append(self._computer.draw_card())

        print("Six hidden cards: XXX XXX")

        self.start_battle(player_cards + computer_cards + cards_from_battle)

    def is_game_over(self):
        if self._player.has_empty_deck():
            print("\n == GAME OVER ==\n")
            print("The computer won. Try again.")
            return True
        elif self._computer.has_empty_deck():
            print("\n == GAME OVER ==\n")
            print(f"You won, {self._player.name}. Congratulations!")
            return True
        else:
            return False

    def print_stats(self):
        print("\n---")
        print(f"You have {self._player.deck.size} cards on your deck.")
        print(f"Computer has {self._computer.deck.size} cards on its deck.")
        print("---")

    def print_welcome_message(self):
        print("========================")
        print("WELCOME TO WAR CARD GAME")
        print("========================")