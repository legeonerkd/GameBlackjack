from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List, Dict


class Observer(ABC):
    @abstractmethod
    def update(self, topic: str, data: any) -> None:
        pass


class Publisher:
    observers: Dict[str, List[Observer]] = {}
    
    def attach(self, topic: str, observer: Observer) -> None:
        if topic not in self.observers:
            self.observers[topic] = []
        self.observers[topic].append(observer) # => list of observers

    def detach(self, topic: str, observer: Observer) -> None:
        self.observers[topic].remove(observer)

    def notify(self, topic: str, data: any = None) -> None:
        for observer in self.observers[topic]:
            observer.update(topic, data)


#join_game = 'game.player.join'
# win_game = 'game.player.win'

game_start = 'game.start'
game_finish = 'game.finish'
player_exit_game = 'game.player.exit'
player_win_game = 'game.player.win'
#TODO: notification who win, who loose, etc