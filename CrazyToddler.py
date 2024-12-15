import math
from random import randrange
from Toddler import Toddler

class CrazyToddler(Toddler):
    TYPE = 1
    def __init__(self, id, position, direction, pos_table, cooldown):
        super().__init__(id, position, direction, pos_table, cooldown)

    def strategy(self, candy, teacher, tables):
        if self._cooldown != 0: self._cooldown -=1
        elif self._has_candy:
            if self.at_table():
                self._has_candy = False
                self._cooldown = self._rest
            else:
                self.move_to(self._pos_table, tables)
        else:
            if self.next_to_tuple(candy) and not self._has_candy:
                self.collect_candy(candy)
                self.move_to(self._pos_table, tables)

            else :
                choice = randrange(2)
                if choice == 0:
                    self.move_to(teacher.get_position(),tables)
                else:
                    self.move_to(candy,tables)


    def to_candy(self, teacher, candy, tables):
        pass



    
