
from Toddler import Toddler

class SmartToddler(Toddler):
    TYPE = 4
    def __init__(self, id, position, direction,pos_table):
        super().__init__(id, position, direction, pos_table)
        self._initial_position = position

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

            elif self.distance_to(teacher.get_position()) < 2:
                self.move_to(self._pos_table, tables)
            else : self.move_to(candy,tables)

    def to_candy(self, teacher, candy, tables):
        pass