from typing import List
from card import Card


class CardSummator:
    def get_sum(cards: List[Card]):
        pass
        

class BlackjackCardSummator(CardSummator):
    VALUES = {
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 11,
    }
    
    @staticmethod
    def get_sum(cards: List[Card]):
        sum_cards = 0
        for card in cards:
            if card.value.isdigit():
                sum_cards += int(card.value)
            else:
                sum_cards += BlackjackCardSummator.VALUES[card.value]
        return sum_cards

# class PokerCardSummator(CardSummator):
#     VALUES = {
        
#     }
    
#     @staticmethod
#     def get_sum(cards: List[Card]):
#         sum_cards = 0
#         for card in cards:
#             sum_cards += int(card.value)
#         return sum_cards

#! ВСЕ, что пишется без кавычек - ПЕРЕМЕННЫЕ
# H = 4

# cards = [Card('5', 'H'), Card('10', 'D')]
# cards = [Card('A', 'H'), Card('3', 'D')]

# c = Card('4', 'D')
# Card('4', 'H').get()...
# 20
# print(SumCards(cards).get_sum_cards())

# SumCards(cards).get_sum_cards()

# SumCards.get_sum_cards()

# print(BlackjackCardSummator.get_sum(cards))