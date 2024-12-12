from abc import ABC, abstractmethod
import math

class Human(ABC):
    def __init__(self,id: int, position: tuple, direction: str, pos_table: tuple):
        self._id = id
        self._position = position
        self._direction = direction
        self._pos_table = pos_table
        self._table = True

    def distance(self, other) -> float:
        #Return the Manhattan distance between the current agent and another agent.
        return abs(self._position[0] - other.get_position()[0]) + abs(self._position[1] - other.get_position()[1])

    def distance_to(self, other: tuple) -> float:
        position = self._position
        return math.sqrt((other[0] - position[0]) ** 2 + (other[1] - position[1]) ** 2)

    def at_table(self):
        self._table = (self._position == self._pos_table)

    def get_id(self) -> int:
        return self._id

    def get_position(self) -> tuple:
        return self._position

    def get_direction(self) -> str:
        return self._direction

    def get_pos_table(self) -> tuple:
        return self._pos_table

    def get_table(self) -> bool:
        return self._table

    def set_direction(self, direction: str):
        self._direction = direction

    def set_table(self, table: bool):
        self._table = table

    def set_position(self, position: tuple):
        self._position = position

    def set_pos_table(self, pos_table: tuple):
        self._pos_table = pos_table


    def move_down(self):
        print("Teacher")
        self._position = (self._position[0], self._position[1] + 1)

    def move_up(self):
        self._position = (self._position[0], self._position[1] - 1)

    def move_left(self):
        self._position = (self._position[0] - 1, self._position[1])
        self._direction= "left"

    def move_right(self):
        self._position = (self._position[0] + 1, self._position[1])
        self._direction= "right"

    def move_to(self, goal):
        s = self._position
        g = goal.get_position()
        if s[0] < g[0] and s[0] < 13:
            self.move_right()
        elif s[0] > g[0] and s[0] > 0:
            self.move_left()
        else:
            if s[1] < g[1] and s[1] < 13:
                self.move_down()
            elif s[1] > g[1] and s[1] > 0:
                self.move_up()