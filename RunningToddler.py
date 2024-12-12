import math
from Toddler import Toddler



class RunningToddler(Toddler):


    def __init__(self, id, position, pos_table, direction):
        super().__init__(id, position, direction, pos_table)


    def strategy(self, candy, teacher):
        if self.get_position == self._pos_table and self._table() == False:
            if self.distance(teacher.get_pos())>3:
                self.set_table(True)
        elif candy == self._position:
            self.collect_candy(self,candy)
        elif self.get_position != self._pos_table and self._table() == False :
            self.move_to(self._pos_table)
        else :
            self.to_candy(teacher, candy)
            self.to_candy(teacher, candy)
            


    def to_candy(self, teacher, candy):
        s = self._position
        t = teacher.get_pos()
        c = candy
        if self.distance(t) > 3 :
            if s[0] < c[0] and s[0] < 6:
                self.move_left()
            elif s[0] > c[0] and s[0] > 0:
                self.move_right()
            else:
                if s[1] < c[1] and s[1] < 6:
                    self.move_down()
                elif s[1] > c[1] and s[1] > 0:
                    self.move_up()


    