# AfraidToddler.py
from Toddler import Toddler

class AfraidToddler(Toddler):

    def __init__(self, id, position, pos_table, direction):
        super().__init__(id, position, direction, pos_table)

    def strategy(self, candy, teacher, tables):
        if self._has_candy:
            print("HAS CANDY")
            if self.at_table():
                self._has_candy = False
            else:
                print("moving to table")
                print(f"{self._pos_table} and {self._position}")
                self.move_to(self._pos_table, tables)
        else:
            print("NOT THE CANDY")
            if self._position == candy and not self._has_candy:
                self._has_candy = True
                print("GOt THE CANDY")
                self.move_to(self._pos_table, tables)

            elif self.distance_to(teacher.get_position()) < 2:
                self.move_to(self._pos_table, tables)
            else : self.move_to(candy,tables)




    def to_candy(self, teacher, candy, tables):
        pass