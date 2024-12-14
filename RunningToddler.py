import math
from Toddler import Toddler



class RunningToddler(Toddler):
    TYPE = 4

    def __init__(self, id, position, direction, pos_table):
        super().__init__(id, position, direction, pos_table)


    def strategy(self, candy, teacher, tables):
        if self._has_candy:
            if self.at_table():
                self._has_candy = False
            else:
                self.move_to(self._pos_table, tables)
        else:
            if self.next_to_tuple(candy) and not self._has_candy:
                self.collect_candy(candy)
                self.move_to(self._pos_table, tables)

            else:
                 for i in range(2):
                     self.move_to(candy, tables)


    def to_candy(self, teacher, candy, tables):
        pass