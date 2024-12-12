from Human import Human
from abc import ABC, abstractmethod



class Toddler(Human):

    def __init__(self, id,position, direction, pos_table):
        super().__init__(id,position, direction, pos_table)
        self.__nb_candy = 0

    def get_nb_candy(self):
        return self.__nb_candy

    def collect_candy(self,candy):
        if self.__position == candy :
            self.set_table(True)
            self.__nb_candy += 1

    @abstractmethod
    def strategy(self, candy,teacher):
        pass

    @abstractmethod
    def to_candy(self, candy, teacher):
        pass

    
