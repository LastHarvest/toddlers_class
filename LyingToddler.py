import math
from random import randrange
from Toddler import Toddler



class LyingToddler(Toddler):
    TYPE = 3

    def __init__(self, id, position, direction, pos_table):
        super().__init__(id, position, direction, pos_table)
        self._truth = False

    def strategy(self, candy, teacher, tables):
        if self._truth:
            if self.at_table():
                self._truth = False
            else:
                self.move_to(self._pos_table, tables)
        else:
            if self.next_to_tuple(candy) and not self._has_candy:
                self.collect_candy(candy)
                self.move_to(self._pos_table, tables)

            elif self.distance_to(teacher.get_position()) < 2:
                self.move_to(self._pos_table, tables)
            else :
                self.move_to(candy,tables)

    def to_candy(self, teacher, candy, tables):
        pass