import math
from Toddler import Toddler

# Cherche juste à aller voir la prof.

class InLoveToddler(Toddler):
    def __init__(self, id, position, pos_table, direction):
        super().__init__(id, position, direction, pos_table)

    def strategy(self, candy, teacher):
        if self.get_position == self.__pos_table and self.__table == False:
            self.set_table(True)

        elif candy == self.__position:
            self.collect_candy(self,candy)
        else:
            self.move_to(teacher)
            


    def move_player_to_candy(self, teacher, candy):
        s = self.__position
        t = teacher.get_pos()
        c = candy
        if s[0] < t[0] and s[0] < 6:
            self.move_left()
        elif s[0] > t[0] and s[0] > 0:
            self.move_right()
        else:
            if s[1] < t[1] and s[1] < 6:
                self.move_down()
            elif s[1] > t[1] and s[1] > 0:
                self.move_up()