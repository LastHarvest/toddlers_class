import math
from Toddler import Toddler

# Cherche juste à aller voir la prof.

class InLoveToddler(Toddler):
    def __init__(self, id, position, pos_table, direction, type):
        super().__init__(id, position, pos_table, direction, type)

    def strategy(self, candy, teacher):
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
            