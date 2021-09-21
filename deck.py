from card import Card
from typing import List
import random
from card_collection import CardCollection


class Deck(CardCollection):
    def __init__(self, cards: List[Card] = None):
        super().__init__(cards)

    def shuffle(self):
        random.shuffle(self.cards)
    
    def turn_deck(self):
        for i in range(len(self.cards) // 2):
            self.cards[i], self.cards[-1 - i] = self.cards[-1 - i], self.cards[i]