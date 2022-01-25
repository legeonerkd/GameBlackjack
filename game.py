from typing import List
from player import Player
from deck import Deck
from card import Card
from summators import BlackjackCardSummator
# from notification import Publisher
# import notification
import abc


class Game(abc.ABC):
    def __init__(self, players: List[Player], deck: Deck):
        self.players = players
        self.deck = deck
            
    def shuffle(self):
        self.deck.shuffle()

    @abc.abstractmethod
    def deal(self):
        pass
    
    @abc.abstractmethod
    def run(self):
        pass
    

# BlackjackGame([Player(1), Player(2)], Deck(....))
# BlackjackGame([Player(1), Player(2)])

class BlackjackGame(Game):
    def __init__(self, players: List[Player], deck: Deck = None):
        super().__init__(players, deck)
        if deck is None:
            self.deck = self._generate_deck()

    def set_startfn(self, startfn):
        self._startfn = startfn
    
    def set_finishfn(self, finishfn):
        self._finishfn = finishfn
                
    def shuffle(self):
        print('before')
        super().shuffle()
        print('after')
         
    def _generate_deck(self) -> Deck:
        VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        SUITS = ['H', 'D', 'C', 'S']

        cards = []
        for suit in SUITS:
            for value in VALUES:
                cards.append(Card(value=value, suit=suit)) 
        return Deck(cards)
        
    def deal(self):
        for player in self.players:
            #TODO: раздать 2 карты игроку
            self.deck.move_cards(player, 2)

    def run(self):
        self.shuffle()
        # for player in self.players:
        #     self.attach(notification.game_start, player)
        self.deal()
        self._startfn(self.players)
        self._finishfn(self.players)
        # self.notify(notification.game_start)

    def take_card(self, player) -> bool:
        self.deck.move_cards(player, 1)
        return BlackjackCardSummator.get_sum(player.cards) > 21




           
        

       #TODO: summator cards and comparison with 21 => почитать про статические методы, вызвать get_sum
       #TODO: с учетом очередности хода

# class DurakGame(Game):
#     def __init__(self, players: List[Player], deck: Deck = None):
#         super().__init__(players, deck)
#         if deck is None:
#             self.deck = self._generate_deck()
        
#     def _generate_deck(self) -> Deck:
#         VALUES = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
#         SUITS = ['H', 'D', 'C', 'S']

#         cards = []
#         for suit in SUITS:
#             for value in VALUES:
#                 cards.append(Card(value=value, suit=suit))
                
#         return Deck(cards)
    
#     def deal(self):
#         for player in self.players:
#             #TODO: раздать 6 карты игроку
#             self.deck.move_cards(player, 6)
            
#     def run(self):
#         self.shuffle()
#         self.deal()


