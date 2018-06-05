from random import shuffle
from card import Card


class Deck:
    def __init__(self):
        values = ["A", "2", "3", "4", "5", "6",
                  "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.cards = [Card(v, s) for s in suits for v in values]

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def __iter__(self):
        return iter(self.cards)
        # allows "for x in my_deck" instead of "for x in my_deck.cards"

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()

        if count == 0:
            raise ValueError("All cards have been dealt")

        deal_count = min([count, num])
        selection = self.cards[:deal_count]

        del self.cards[:deal_count]
        return selection

    def shuffle(self):
        if len(self.cards) < 52:
            raise ValueError("Only full decks can be shuffled")
            return
        shuffle(self.cards)
        return self

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, num):
        return self._deal(num)
