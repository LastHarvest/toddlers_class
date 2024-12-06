import math
from Toddler import Toddler



class AfraidToddler(Toddler):

    def __init__(self, position, id,  Table, Pos_table, direction):
        super().__init__(position, id, Table, direction)


    def collect_resource(self,candy):
        if self.position == candy :
            self.update_Table(True)


    def Strategie(self, candy, teacher):
        if candy == self.pos():
            self.collect_resource(self,candy)
        elif self.get_position != self.get_Pos_table() :
            self.move_player_to_table()
        else :
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


    
