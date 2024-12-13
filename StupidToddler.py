import math
from Toddler import Toddler



class StupidToddler(Toddler):

    def __init__(self, position, id,  table, direction,type, hunger):
        super().__init__(id,position, table, direction,type )
        self._hunger = hunger
        self._cooldown = hunger

    def set_hunger(self,hung):
        self._hunger = hung

    def get_hunger(self):
        return self._hunger
    
    
    def get_cooldown(self):
        return self._cooldown

    def add_cooldown(self):
        self._cooldown -= 1


    def strategy(self, candy, teacher):
        if self._cooldown == 0 and self._table==True:
            self.set_table(False)
        elif self._cooldown == 0 and self._table()==False:
            if candy == self._position:
                self.collect_candy(candy)
                self._hunger = 0
            else :
                self.to_candy(teacher, candy)
        else :
            self.add_cooldown()
            if self._position != self._pos_table :
                self.move_to(self._pos_table)

    def to_candy(self,teacher, candy):
        s = self._position
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


    
