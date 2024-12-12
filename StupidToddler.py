import math
from Toddler import Toddler



class StupidToddler(Toddler):

    def __init__(self, position, id,  table, direction, hunger, cooldown):
        super().__init__(id,position, direction, table)
        self.__hunger = hunger
        self.__cooldown = cooldown


    # Getters
    def get_Hunger(self):
        return self.__hunger
    
    def get_Cooldown(self):
        return self.__cooldown

    

    #Setters
    def add_Cooldown(self):
        self.Cool__cooldown -= 1

    def init_Cooldown(self):
        self.__cooldown = self.__hunger


    def collect_resource(self,candy):
        if self.__position == candy :
            self.__hunger = self.__hunger
            self.update_Table(True)


    def strategie(self, teacher):
        if self.__cooldown == 0 and self.get_table()==True:
            self.update_Table(False)
        elif self.Cooldown == 0 and self.get_Table()==False:
            if candy == self.pos():
                self.collect_resource(self,candy)
            else :
                self.move_player_to_candy()

        else :
            self.add_Cooldown()
            if self.get_position != self.get_Pos_table() :
                self.move_player_to_table()
            


    def move_player_to_candy(self,teacher, candy):
        s = self.get_pos()
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


    
