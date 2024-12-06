from abc import ABC, abstractmethod


class Human(ABC):
    def __init__(self, position: tuple):
        self.__position = position


    @abstractmethod
    def action(self):
        pass

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