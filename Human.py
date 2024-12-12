from abc import ABC, abstractmethod


class Human(ABC):
    def __init__(self,id: int, position: tuple, direction: str):
        self.__id = id
        self.__position = position
        self.__direction = direction

    def distance(self, other) -> float:
        #Return the Manhattan distance between the current agent and another agent.
        return abs(self.__position[0] - other.position[0]) + abs(self.__position[1] - other.position[1])

    def get_id(self) -> int:
        return self.__id

    def get_position(self) -> tuple:
        return self.__position

    def set_position(self, position: tuple):
        self.__position = position

    def move_up(self):
        self.__position = (self.__position[0], self.__position[1] + 1)

    def move_down(self):
        self.__position = (self.__position[0], self.__position[1] - 1)

    def move_left(self):
        self.__position = (self.__position[0] - 1, self.__position[1])
        self.__direction="left"

    def move_right(self):
        self.__position = (self.__position[0] + 1, self.__position[1])
        self.__direction="right"