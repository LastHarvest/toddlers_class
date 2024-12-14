import math
from Toddler import Toddler



class HungryToddler(Toddler):
    TYPE = 2

    def __init__(self, id, position, direction, pos_table, hunger):
        super().__init__(id, position, direction, pos_table)
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
        self.add_cooldown()
        if self._has_candy:
            if self.at_table():
                self._has_candy = False
            else:
                self.move_to(self._pos_table, tables)
        else:
            if self.next_to_tuple(candy) and not self._has_candy:
                self.collect_candy(candy)
                self._cooldown = self._hunger
                self.move_to(self._pos_table, tables)
            elif self._cooldown < 0: self.move_to(candy, tables)

    def to_candy(self, teacher, candy, tables):
        pass