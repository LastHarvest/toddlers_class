import math
from Toddler import Toddler



class StupidToddler(Toddler):

    def __init__(self, position, id,  Table, Pos_table, direction, hunger, Cooldown):
        super().__init__(position, id, Table, direction)
        self.hunger = hunger
        self.Cooldown = Cooldown


    # Getters
    def get_Hunger(self):
        return self.hunger
    
    def get_Cooldown(self):
        return self.Cooldown

    

    #Setters
    def add_Cooldown(self):
        self.Cooldown -= 1

    def init_Cooldown(self):
        self.Cooldown = self.hunger


    def collect_resource(self,bonbon):
        if self.position == bonbon :
            self.Cooldown = self.Faim


    def Strategie(self, teacher):
        if self.Cooldown == 0 and self.get_Table()==True:
            self.update_Table(False)
        elif self.Cooldown == 0 and self.get_Table()==False:
            self.move_player_to_bonbon(bonbon)
        else :
            self.add_Cooldown()
            if self.get_position != self.get_Pos_table() :
                self.move_player_to_table()



    def move_player_to_candy(self,teacher, candy):
        s = self.get_pos()
        b = bonbon
        if s[0] < b[0] and s[0] < 6:
            self.move_right()
        elif s[0] > b[0] and s[0] > 0:
            self.move_left()
        else:
            if s[1] < b[1] and s[1] < 6:
                self.move_up()
            elif s[1] > b[1] and s[1] > 0:
                self.move_down()


    
