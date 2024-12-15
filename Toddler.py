from Human import Human
from abc import ABC, abstractmethod

class Toddler(Human):

    def __init__(self, id,position, direction, pos_table, cooldown):
        super().__init__(id,position, direction, pos_table)
        self._type = type
        self._nb_candy = 0
        self._has_candy = False
        self._lost_candy = 0
        self._cooldown = cooldown
        self._rest = cooldown

    def lose_candy_point(self):
        self._lost_candy += 1

    def get_lost_candy_points(self):
        return self._lost_candy

    def get_type(self):
        return self._type

    def get_has_candy(self):
        return self._has_candy

    def get_candies(self):
        return self._nb_candy


    def get_points(self):
        return self._nb_candy

    def collect_candy(self,candy):
        if self.next_to_tuple(candy):
            self._has_candy = True
            self._nb_candy += 1

    def minus_candy(self):
        self._nb_candy -= 1

    @abstractmethod
    def strategy(self, candy,teacher, tables):
        pass

    @abstractmethod
    def to_candy(self, candy, teacher, toddler):
        pass

    
