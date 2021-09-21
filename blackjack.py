### 21 ###

# card = 'J'

from summators import BlackjackCardSummator
from typing import List
import random
from card import Card
from deck import Deck
from game import BlackjackGame, Game
from player import Player
# from sumcards import SumCards
# import card
# card.Card

# deck = ['8♥', '9', '10', 'J', 'Q', 'K',    '2', 'J', '7♠', '8♠', 'A♠', 'K♥', '9', '10', 'J', 'Q', 'J', '7♠', '8♠', 'A♠']
# player1 = ['A', 'K']
# player2 = ['7', '8']
# player3 = ['2', 'J']

# player1 = []
# player2 = []
# player3 = []

# def move_cards_to_player(deck: List[str], player: List[str], count: int):
# # deck = ['8', '9', '10', 'J', 'Q', 'K',    '2', 'J', '7', '8', 'A', 'K']
#   #TODO: get 2 last cards from the deck
#   cards = deck[-count:]
  
#   #TODO: put them to the player
#   player += cards
#   # -> get last (count) cards
#   # deck[-count:] # => ['A', 'K']
  
#   #TODO: remove them
#   del deck[-count:]


# print('Initial deck: ', deck)

# random.shuffle(deck)
# count = 2

# print('Shuffled deck: ', deck)
# print(len(deck))

# # players = [player1, player2, player3] # => List[List[str]]
# players = [player1, player2]
# # players.append(['4'])
# for player in players:
#   move_cards_to_player(deck, player, count)
#   print(player)

# print('Finished deck: ', deck)
# print(len(deck))

# Домашнее задание
# Изучить классы и объекты
# class Card:
# Переделать игру, используя классы и ООП (Объектно-ориентированное программирование)

# print(Card(value='5', suit='H'), Card(value='A', suit='S'))

# VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# SUITS = ['H', 'D', 'C', 'S']

# deck = []
# for suit in SUITS:
#   for value in VALUES:
#     deck.append(Card(value=value, suit=suit))
    
# print(deck)
# random.shuffle(deck)
# print('Shuffled deck: ', deck)

# players = [player1, player2]
# count = 2

# for player in players:
#   move_cards_to_player(deck, player, count)
#   print(player)

# print('Finished deck: ', deck)
# print(len(deck))




# # for suits....
# # for values...
# # deck+++++++



# # card = Card(value='J', suit='H')
# # print(card)
# # print('9999')

# # print([Card(value='J', suit='H'), Card(value='A', suit='S')])

# # michael_deck = Deck([
# #   Card(value='5', suit='H'), 
# #   Card(value='5', suit='D'), 
# #   Card(value='A', suit='S'),
# # ])



#VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
#SUITS = ['H', 'D', 'C', 'S']

#deck_cards = []
#for suit in SUITS:
#     for value in VALUES:
#         deck_cards.append(Card(value=value, suit=suit))
#print(deck_cards)




#michael_deck = Deck([
#   Card(value='5', suit='H'), 
#   Card(value='5', suit='D'), 
#   Card(value='A', suit='S'),
# ])
#print(michael_deck)
#print(michael_deck.turn_deck())
#michael_deck = Deck(deck_cards)

# players = [
#     Player('Tom'),
#     Player('Igor'),
#     Player('Mikhail'),
#  ]
# # print(deck.cards)

# # deck.shuffle()

# # print(deck.cards)

# # game2 = Game(deck=, players=)

# # games = [Game(...), Game(...)]

# game = Game(deck=michael_deck, players=players)
# game.shuffle()
# game.deal(2)

# print(game.deck.cards)

# for player in players:
#   print(player.name, player.cards)

#igor = Player('Igor', [Card('5', 'H'), Card('8', 'D')])
#mikhail = Player('Mikhail', [Card('9', 'H'), Card('10', 'D'), Card('J', 'H')])

#deck = Deck([Card('2', 'H'), Card('3', 'D'), Card('4', 'H'), 
#            Card('5', 'H'), Card('6', 'D'), Card('7', 'H'),
#            Card('8', 'H'), Card('9', 'D'), Card('10', 'H')])
#print(deck.cards)
#deck.turn_deck()
#print(deck.cards)
#deck.shuffle()
#print(deck.shuffle())
#deck.turn_deck()
#print(deck.turn_deck())
#deck.move_cards(igor, 1)
#deck.move_cards(mikhail, 1)

#mikhail.move_cards(igor, len(mikhail.cards))

#print('Igor: ', igor.cards)
#print('Mikhail: ', mikhail.cards)
#print('Deck: ', deck.cards)


players = [
    # Player('Tom'),
    Player('Igor'),
    Player('Mikhail'),
]

game = BlackjackGame(players)
game.run()

def show_state(player):
    print('%s cards: %s    sum: %d' % (player.name, player, BlackjackCardSummator.get_sum(player.cards)))
        
            

def get_choice(player):
    return input('%s, do you want a card? (y/n): ' % player.name)


for player in players:
    show_state(player)
    # ? <= get_choice(player)
    choice = get_choice(player)
    
    while True: 
        if choice == 'y':
            overflow = game.take_card(player)
            #! if overflow:
                #! break
            show_state(player)
        
        elif choice == 'n':
            break

        else:
            print('Incorrect input. Try to input (y/n)')

        choice = get_choice(player)
    
        
        #! breakpoint - точка ОСТАНОВА
        #! break - полная остановка всего цикла
        #! continue - остановка текущей итерации и начало новой
   
    #TODO: return to the start
  


# print('Deck: ', game.deck)

# from game import DurakGame
# durak = DurakGame(players)
# durak.run()

# for player in players:
#    print(player.name, player)
   
# print('Deck: ', durak.deck)