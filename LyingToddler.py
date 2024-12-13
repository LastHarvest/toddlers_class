import math
from random import randrange
from Toddler import Toddler



class LyingToddler(Toddler):

    def __init__(self, id, position, pos_table, direction):
        super().__init__(id, position, direction, pos_table)

    def strategy(self, candy, teacher, tables):
        # if self._position == self._pos_table and not self._table:
        #     if self.distance_to(teacher.get_position()) > 3:
        #         self.set_table(True)
        # elif candy == self._position:
        #     self.collect_candy(candy)
        # elif self._position != self._pos_table and not self._table:
        #     self.move_to(self._pos_table, tables)
        # else:
        #     self.to_candy(teacher.get_position(), candy, tables)

        # if self._position == teacher.get_position():
        #     self._position = self._pos_table
        # elif self.distance_to(teacher.get_position()) < 1:
        #     self.move_to(self._pos_table, tables)
        # else: self.move_to(candy, tables)
        if self._has_candy and not self._table:
            print("\n HAS CANDY GOING BACK\n")
            self.move_to(self._pos_table, tables)
        elif self._has_candy and self._table:
            print("\n HAS CANDY GOING AGAIN\n")
            self._has_candy = False
        elif self._position == teacher.get_position():
            print("\n CAUGHT\n")
            self.move_to(self._pos_table, tables)
            self.move_to(self._pos_table, tables)
        elif not self._has_candy and self.distance_to(teacher.get_position()) > 2:
            self.move_to(candy, tables)

    def to_candy(self, teacher, candy, tables):
        pass