### 21 ###

# card = 'J'

from typing import List
import random


deck = ['8♥', '9', '10', 'J', 'Q', 'K',    '2', 'J', '7♠', '8♠', 'A♠', 'K♥', '9', '10', 'J', 'Q', 'J', '7♠', '8♠', 'A♠']
# player1 = ['A', 'K']
# player2 = ['7', '8']
# player3 = ['2', 'J']

player1 = []
player2 = []
player3 = []

def move_cards_to_player(deck: List[str], player: List[str], count: int):
# deck = ['8', '9', '10', 'J', 'Q', 'K',    '2', 'J', '7', '8', 'A', 'K']
  #TODO: get 2 last cards from the deck
  cards = deck[-count:]
  
  #TODO: put them to the player
  player += cards
  # -> get last (count) cards
  # deck[-count:] # => ['A', 'K']
  
  #TODO: remove them
  del deck[-count:]


print('Initial deck: ', deck)

random.shuffle(deck)
count = 6

print('Shuffled deck: ', deck)
print(len(deck))

# players = [player1, player2, player3] # => List[List[str]]
players = [player1, player2]
# players.append(['4'])
for player in players:
  move_cards_to_player(deck, player, count)
  print(player)

print('Finished deck: ', deck)
print(len(deck))

# Домашнее задание
# Изучить классы и объекты
# class Card:
# Переделать игру, используя классы и ООП (Объектно-ориентированное программирование)

