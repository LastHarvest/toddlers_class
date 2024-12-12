import math
import random
from random import randrange
from Toddler import Toddler

class CrazyToddler(Toddler):

    def __init__(self, id, position, pos_table, direction):
        super().__init__(id, position, direction, pos_table)

    def strategy(self,candy, teacher):
        if self.__position == self.__pos_table and self.__table == False:
            self.set_table(True)

        elif candy == self.__position:
            self.collect_candy(candy)

        elif not self.__table:
            #On lance un piéce, si pile on va vers les bonbons, sinon on va vers la table
            if random.choice([True,False]):
                self.move_to(self.__pos_table)
            else :
                self.to_candy(candy,teacher)

    def to_candy(self, teacher, candy):
       pass



    
