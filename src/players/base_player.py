from abc import ABC, abstractmethod

class BasePlayer(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_move(self, game_state):
        pass

    def __str__(self):
        return self.name