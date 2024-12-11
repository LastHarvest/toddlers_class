from abc import ABC, abstractmethod


class Human(ABC):
    def __init__(self, position: tuple):
        self.__position = position

    def distance(self, other) -> float:
        #Return the Manhattan distance between the current agent and another agent.
        return abs(self.position[0] - other.position[0]) + abs(self.position[1] - other.position[1])


    def get_position(self) -> tuple:
        return self.__position

    def set_position(self, position: tuple):
        self.__position = position

    def move_up(self):
        self.position = (self.position[0], self.position[1] + 1)

    def move_down(self):
        self.position = (self.position[0], self.position[1] - 1)

    def move_left(self):
        self.position = (self.position[0] - 1, self.position[1])
        self.direction="left"

    def move_right(self):
        self.position = (self.position[0] + 1, self.position[1])
        self.direction="right"