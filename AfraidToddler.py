# AfraidToddler.py
from Toddler import Toddler

class AfraidToddler(Toddler):

    def __init__(self, id, position, pos_table, direction):
        super().__init__(id, position, direction, pos_table)

    def strategy(self, candy, teacher):
        if self._position == self._pos_table and not self._table:
            if self.distance_to(teacher.get_position()) > 3:
                self.set_table(True)
        elif candy == self._position:
            self.collect_candy(candy)
        elif self._position != self._pos_table and not self._table:
            self.move_to(self._pos_table)
        else:
            self.to_candy(teacher, candy)

    def to_candy(self, teacher, candy):
        s = self._position
        t = teacher.get_position()
        c = candy
        if self.distance_to(t) > 3:
            if s[0] < c[0] and s[0] < 6:
                self.move_left()
            elif s[0] > c[0] and s[0] > 0:
                self.move_right()
            else:
                if s[1] < c[1] and s[1] < 6:
                    self.move_down()
                elif s[1] > c[1] and s[1] > 0:
                    self.move_up()