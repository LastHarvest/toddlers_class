from Human import Human
from abc import ABC, abstractmethod

class Toddler(Human):

    def __init__(self, id,position, direction, pos_table,type):
        super().__init__(id,position, direction, pos_table)
        self._type = type
        self._nb_candy = 0
        self._has_candy = False
<<<<<<< HEAD
=======

    def get_type(self):
        return self._type
>>>>>>> a60b8c65fe18d08713072469fd25cf7077b88204

    def get_nb_candy(self):
        return self._nb_candy

    def collect_candy(self,candy):
        if self._position == candy :
            self.set_table(True)
            self._nb_candy += 1

    @abstractmethod
    def strategy(self, candy,teacher, tables):
        pass

    @abstractmethod
    def to_candy(self, candy, teacher, toddler):
        pass

    
