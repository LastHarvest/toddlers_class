import math
from random import randrange
from Toddler import Toddler



class LyingToddler(Toddler):

    def __init__(self, id, position, pos_table, direction):
        super().__init__(id, position, direction, pos_table)
        self.__lying = False


    def get_lying(self):
        return self.__lying
    
    def set_lying(self,tf : bool):
        self.__lying = tf

    def strategy(self, candy, teacher):
        if self.get_position == self.__pos_table and self.__table == False:
            if self.distance(teacher.get_pos())>3:
                self.set_table(True)
        elif candy == self.__position:
            self.collect_candy(self,candy)
        elif self.get_position != self.__pos_table and self.__table == False and self.__lying == False:
            self.move_to(self.__pos_table)
        else :
            r = randrange(1,4)
            if r == 1 :
                self.set_lying(True)
                self.set_table(False)
                self.to_candy(teacher, candy)
            else :
                self.set_lying(False)
                self.set_table(True)
                self.to_candy(teacher, candy)


            
    def to_candy(self, teacher, candy):
        s = self.__position
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


    
