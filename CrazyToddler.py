import math
from random import randrange
from Toddler import Toddler

class CrazyToddler(Toddler):

    def __init__(self, id, position, pos_table, direction,type):
        super().__init__(id, position,pos_table, direction,type)

    def strategy(self,candy, teacher, tables):
        def strategy(self, candy, teacher, tables):
            if self._has_candy:
                if self._table:
                    self._table = False
                else:
                    self.move_to(self._pos_table, tables)
            else:
                if self._position == candy and not self._has_candy:
                    self._has_candy = True
                    self.move_to(self._pos_table, tables)

                if self.distance_to(teacher.get_position()) < 2:
                    self.move_to(self._pos_table, tables)
                elif not self._has_candy:
                    choice = randrange(2)
                    if choice == 0: self.move_to(teacher.get_position(), tables)
                    else: self.move_to(candy, tables)

    def to_candy(self, teacher, candy, tables):
        pass



    
