import math
from abc import ABC

from Toddler import Toddler



class AfraidToddler(Toddler):

    def __init__(self, id,position, pos_table, direction):
        super().__init__(id,position, direction, pos_table)



    def strategy(self, candy, teacher):
        if self.__position == self.__pos_table and self.__table == False:
            if self.distance_to(teacher.get_pos())>3:
                self.set_table(True)
        elif candy == self.__position:
            self.collect_candy(candy)
        elif self.__position != self.__pos_table and self.__table == False :
            self.move_to(self.__pos_table)
        else :
            self.to_candy(teacher, candy)
            


    def to_candy(self, teacher, candy):
        s = self.__position
        t = teacher.get_position()
        c = candy
        if self.distance_to(t) > 3 :
            if s[0] < c[0] and s[0] < 6:
                self.move_left()
            elif s[0] > c[0] and s[0] > 0:
                self.move_right()
            else:
                if s[1] < c[1] and s[1] < 6:
                    self.move_down()
                elif s[1] > c[1] and s[1] > 0:
                    self.move_up()

    
