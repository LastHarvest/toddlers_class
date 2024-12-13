import math
from Toddler import Toddler



class HungryToddler(Toddler):

    def __init__(self, id, position, table, direction,type, hunger):
        super().__init__(id, position, table, direction,type)
        self._hunger = hunger
        self._cooldown = hunger

    def set_hunger(self,hung):
        self._hunger = hung

    def get_hunger(self):
        return self._hunger

    def get_cooldown(self):
        return self._cooldown

    def add_cooldown(self):
        self._cooldown -= 1

    def strategy(self, candy, teacher, tables):
        if self._cooldown != 0: return
        else:
            if self._has_candy and not self._table and self._cooldown != 0:
                print("case 1")
                self.add_cooldown()
                self.move_to(self._pos_table, tables)
            elif self._has_candy and self._table:
                print("case 2")
                self._has_candy = False
            elif self._position == candy:
                print("case 3")
                self._has_candy = True
                self._cooldown = self._hunger
                self.move_to(self._pos_table, tables)
            elif not self._has_candy and self.distance_to(candy) < 2:
                print("case 4")
                self.move_to(self._pos_table, tables)
            else:
                print("case 5")
                self.move_to(candy, tables)

    def to_candy(self, teacher, candy, tables):
        pass