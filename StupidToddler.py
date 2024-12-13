import math
from Toddler import Toddler



class StupidToddler(Toddler):

<<<<<<< HEAD
    def __init__(self, position, id,  table, direction, hunger):
        super().__init__(id,position, direction, table)
=======
    def __init__(self, id, position,  table, direction, type):
        super().__init__(id,position,table, direction,type)
>>>>>>> a60b8c65fe18d08713072469fd25cf7077b88204

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