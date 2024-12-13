# AfraidToddler.py
from Toddler import Toddler

class AfraidToddler(Toddler):

    def __init__(self, id, position, pos_table, direction):
        super().__init__(id, position, direction, pos_table)

    def strategy(self, candy, teacher, tables):
        print(self._position)
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
            elif self._position[0] not in [0,13] and self._position[1] != candy[1]:
                left_border = (0, self._position[1])
                right_border = (13, self._position[1])
                if self.distance_to(left_border) < self.distance_to(right_border):
                    self.move_to(left_border, tables)
                else:
                    self.move_to(right_border, tables)

            else: self.move_to(candy, tables)




    def to_candy(self, teacher, candy, tables):
        pass