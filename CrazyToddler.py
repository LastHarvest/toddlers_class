import math
from random import randrange
from Toddler import Toddler

class CrazyToddler(Toddler):
    TYPE = 1
    def __init__(self, id, position, direction, pos_table):
        super().__init__(id, position, direction, pos_table)

    def strategy(self, candy, teacher, tables):
        if self._has_candy:
            if self.at_table():
                self._has_candy = False
            else:
                self.move_to(self._pos_table, tables)
        else:
            if self._position == candy and not self._has_candy:
                self._has_candy = True
                self.move_to(self._pos_table, tables)

            else :
                choice = randrange(2)
                if choice == 0:
                    self.move_to(teacher.get_position(),tables)
                else:
                    self.move_to(candy,tables)


    def to_candy(self, teacher, candy, tables):
        pass



    
