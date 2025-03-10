class Suit:

    SUIT_AND_SYMBOL = {
        "spades": "♠",
        "hearts": "♥",
        "diamonds": "♦",
        "clubs": "♣"
    }

    def __init__(self, description: str):
        """Initialize an instance of Suit

        :argument description: string representing the suit.
            Must be one of the following values: clubs, diamonds, hearts, or spades
        """
        if description.lower() not in Suit.SUIT_AND_SYMBOL.keys():
            raise ValueError(f"Invalid suit description: {description}")
        self._description = description.lower()
        self._symbol = Suit.SUIT_AND_SYMBOL[description.lower()]

    @property
    def description(self):
        return self._description

    @property
    def symbol(self):
        return self._symbol
