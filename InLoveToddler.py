import math
from Toddler import Toddler

# Cherche juste à aller voir la prof.

class InLoveToddler(Toddler):
    def __init__(self, id, position, pos_table, direction, type):
        super().__init__(id, position, pos_table, direction, type)

<<<<<<< HEAD
    def strategy(self, candy, teacher, tables):
        if self._has_candy and not self._table:
            print("\n HAS CANDY GOING BACK\n")
            self.move_to(self._pos_table, tables)
        elif self._has_candy and self._table:
            print("\n HAS CANDY GOING AGAIN\n")
            self._has_candy = False
        elif self._position == teacher.get_position():
            print("\n CAUGHT\n")
            self._position = self._pos_table
        elif not self._has_candy and self.distance_to(teacher.get_position()) < 2:
            self.move_to(self._pos_table, tables)
        else:
            self.move_to(candy, tables)

    def to_candy(self, teacher, candy, tables):
        pass
=======
    def strategy(self, candy, teacher,tables):
        # Si il est à sa place il se lève
        if self.get_position == self._pos_table and self._table == False:
            self.set_table(True)
        # Si il est sur la position des bonbons il en prend un
        elif candy == self._position:
            self.collect_candy(self,candy)
        # Sinon il va voir la prof
        else:
            self.move_to(teacher)

    def to_candy(self, candy, teacher):
        pass
            
>>>>>>> a60b8c65fe18d08713072469fd25cf7077b88204
