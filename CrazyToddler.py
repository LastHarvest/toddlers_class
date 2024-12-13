import math
from random import randrange
from Toddler import Toddler

class CrazyToddler(Toddler):

    def __init__(self, id, position, pos_table, direction):
        super().__init__(id, position, direction, pos_table)

    def strategy(self,candy, teacher, tables):
        # if self._position == self._pos_table and self._table == False:
        #     self.set_table(True)
        # elif candy == self._position:
        #     self.collect_candy(candy)
        #
        # elif not self._table:
        #     #On lance un piéce, si pile on va vers les bonbons, sinon on va vers la table
        #     if random.choice([True,False]):
        #         self.move_to(self._pos_table)
        #     else :
        #         self.to_candy(candy,teacher)
        if self._has_candy and self._table:
            print("\n HAS CANDY GOING AGAIN\n")
            self._has_candy = False
        elif self._position == teacher.get_position():
            print("\n CAUGHT\n")
            self._position = self._pos_table
        else:
            choice = randrange(2)
            if choice == 0: self.move_to(self._pos_table, tables)
            else: self.move_to(candy, tables)

    def to_candy(self, teacher, candy, tables):
        pass



    
