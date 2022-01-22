from typing import List
from card import Card
from card_collection import CardCollection
# from notification import Observer



class Player(CardCollection):
    def __init__(self, name, cards: List[Card] = None):
        super().__init__(cards)
        self.name = name

    def sort_cards(self):
        SUITS_ORDER = {
            'H': 0,
            'D': 1,
            'S': 2,
            'C': 3,
        }
        VALUES_ORDER = {
            'J': 11,
            'Q': 12,
            'K': 13,
            'A': 14,
        }
        
        def get_value_order(value):
            # '2' .. 'A'
            if value.isdigit():
                return int(value)
            else:
                return VALUES_ORDER[value]
            
        self.cards.sort(key=lambda card: (SUITS_ORDER[card.suit], get_value_order(card.value)))

    # def update(self, topic: str, data: any) -> None:
    #     if topic == notification.game_start:
    #         print('[%s]: game started' % self.name)
    #     if topic == notification.game_finish:
    #         print('[%s]: game finished' % self.name)
    #     if topic == notification.player_exit_game:
    #         print('[%s]: exit the game' % self.name)
    #     if topic == notification.player_win_game:
    #         print('[%s]: win the game' % self.name)
        