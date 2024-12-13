import math
from Toddler import Toddler



class StupidToddler(Toddler):
    TYPE = 5

    def __init__(self, id, position, direction, pos_table):
        super().__init__(id, position, direction, pos_table)


    def strategy(self, candy, teacher, tables):
        if self._has_candy and not self._table:
            print("\n HAS CANDY GOING BACK\n")
            self.move_to(self._pos_table, tables)
        elif self._has_candy and self._table:
            print("\n HAS CANDY GOING AGAIN\n")
            self._has_candy = False
        elif self._position == teacher.get_position():
            print("\n CAUGHT\n")
            self._position = self._pos_table
        elif not self._has_candy:
            self.move_to(candy, tables)


    def to_candy(self, teacher, candy, tables):
        pass