import math
from random import randrange
from Toddler import Toddler



class AfraidToddler(Toddler):

    def __init__(self, position, id,  Table, Pos_table, direction, nbCandy):
        super().__init__(position, id, Table, direction, nbCandy)


    def collect_resource(self,candy):
        if self.position == candy :
            self.update_Table(True)
            self.update_NbCandy()


    def Strategie(self, teacher, candy):
        if self.get_position == self.get_Pos_table() and self.get_Table() == False:
            self.update_Table(True)
        elif candy == self.pos():
            self.collect_resource(self,candy)
        elif self.get_position != self.get_Pos_table() and self.get_Table() == False :
            self.move_player_to_table()
        else :
            self.move_player_to_candy()
            


    def move_player_to_candy(self, teacher, candy):
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



    
