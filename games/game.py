from abc import ABC, abstractmethod


class Game(ABC):
    @abstractmethod
    def actions(self, state):
        pass

    @abstractmethod
    def result(self, state, action):
        pass

    @abstractmethod
    def is_terminal(self, state):
        pass

    @abstractmethod
    def utility(self, state, player):
        pass

    @abstractmethod
    def to_move(self, state):
        pass

    @abstractmethod
    def display(self, state):
        print(state)
