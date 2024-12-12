import math
from random import randrange
from Toddler import Toddler

class CrazyToddler(Toddler):

    def __init__(self, id, position, pos_table, direction):
        super().__init__(id, position, direction, pos_table)

    def strategy(self,candy, teacher):
        if self._position == self._pos_table and self._table == False:
            self.set_table(True)
        elif candy == self._position:
            self.collect_candy(candy)

        elif not self._table:
            #On lance un piéce, si pile on va vers les bonbons, sinon on va vers la table
            if random.choice([True,False]):
                self.move_to(self._pos_table)
            else :
                self.to_candy(candy,teacher)

    def to_candy(self, teacher, candy):
       pass



    
