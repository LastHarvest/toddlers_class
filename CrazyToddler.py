import math
from random import randrange
from Toddler import Toddler

class CrazyToddler(Toddler):

    def __init__(self, id, position, pos_table, direction):
        super().__init__(id, position, direction, pos_table)


    def strategy(self,candy,teacher):
        # si l'élève est sur sa table alors il se relève pour partir
        if self._position == self._pos_table and self._table == False: 
            self.set_table(True)
        # si l'élève est les bonbons il en ramasse un
        elif candy == self._position:
            self.collect_candy(candy)
        # sinon il est debout et va n'importe où
        elif not self._table:
            # il a eu son bonbon et retourne à sa place
            if self._table == False :
                self.move_to(self._pos_table)
            #Il n'a pas eu son bonbon et va le récupérer :
            else :
                self.to_candy(candy,teacher)
            

    def to_candy(self, teacher, candy):
        # Il va se déplacer de façon random sans chercher à éviter la prof ou à prendre un bonbon
        s = self.get_pos()
        r = randrange(1,5)
        if r == 1 and s[0] < 6 :
            self.move_left()
        elif r==2 and s[0] > 0 :
            self.move_right()
        else:
            if r==3 and s[1] < 6:
                self.move_down()
            elif r==4 and s[1] > 0:
                self.move_up()



    
