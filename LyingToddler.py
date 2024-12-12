import math
from random import randrange
from Toddler import Toddler



class LyingToddler(Toddler):

    def __init__(self, position, id,  Table, Pos_table, direction,nbCandy,Lying):
        super().__init__(position, id, Table, direction,nbCandy)
        self.Lying = False

    def get_Lying(self):
        return self.Lying
    
    def update_Lying(self,Bool):
        self.Lying = Bool

    def collect_resource(self,candy):
        if self.position == candy :
            self.update_Table(True)
            self.update_NbCandy()


    def Strategie(self, candy, teacher):
        if candy == self.pos():
            self.collect_resource(self,candy)
        elif self.get_position != self.get_Pos_table() and self.get_Table() == False and self.get_Lying() == False:
            self.move_player_to_table()
        else :
            r = randrange(1,4)
            if r == 1 :
                self.update_Lying(True)
                self.update_Table(False)
                self.move_player_to_candy()
            else :
                self.update_Lying(False)
                self.update_Table(True)
                self.move_player_to_candy()


            
            


    def move_player_to_candy(self, teacher, candy):
        s = self.get_pos()
        t = teacher.get_pos()
        c = candy
        if self.get_distance_resource(t) > 3 :
            if s[0] < c[0] and s[0] < 6:
                self.move_left()
            elif s[0] > c[0] and s[0] > 0:
                self.move_right()
            else:
                if s[1] < c[1] and s[1] < 6:
                    self.move_down()
                elif s[1] > c[1] and s[1] > 0:
                    self.move_up()
        
        else :
            if s[0] < t[0] and s[0] > 0:
                self.move_right()
            elif s[0] > t[0] and s[0] < 6:
                self.move_left()
            else:
                if s[1] < t[1] and s[1] > 0:
                    self.move_up()
                elif s[1] > c[1] and s[1] < 6:
                    self.move_down()


    
