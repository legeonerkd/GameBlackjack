from typing import List
from card import Card


class CardCollection:
    def __init__(self, cards: List[Card]=None):
        if cards is None:
            self.cards = []
        else:
            self.cards = cards

    def move_cards(self, destination, count: int):
        #TODO: get 2 last cards from the deck
        cards = self.cards[-count:]
        
        #TODO: put them to the player
        destination.cards += cards
        
        #TODO: remove them
        del self.cards[-count:]
        
    def __str__(self):
        return str(self.cards)