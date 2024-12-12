import math
from Toddler import Toddler



class StupidToddler(Toddler):

    def __init__(self, position, id,  table, direction, hunger):
        super().__init__(id,position, direction, table)
        self.__hunger = hunger
        self.__cooldown = hunger

    def get_hunger(self):
        return self.__hunger
    
    def get_cooldown(self):
        return self.__cooldown

    def add_cooldown(self):
        self.__cooldown -= 1


    def strategy(self, candy, teacher):
        if self.__cooldown == 0 and self.__table==True:
            self.set_table(False)
        elif self.__cooldown == 0 and self.__table()==False:
            if candy == self.__position:
                self.collect_candy(candy)
                self.__hunger = 0
            else :
                self.to_candy(teacher, candy)
        else :
            self.add_cooldown()
            if self.__position != self.__pos_table :
                self.move_to(self.__pos_table)

    def to_candy(self,teacher, candy):
        s = self.__position
        b = candy
        if s[0] < b[0] and s[0] < 6:
            self.move_right()
        elif s[0] > b[0] and s[0] > 0:
            self.move_left()
        else:
            if s[1] < b[1] and s[1] < 6:
                self.move_up()
            elif s[1] > b[1] and s[1] > 0:
                self.move_down()


    
