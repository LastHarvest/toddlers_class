import random
from time import sleep

from Toddler import Toddler
from Teacher import Teacher

class Game:
    def __init__(self):
        self.__running = True
        self.__time = 0
        self.__toddlers =  [Toddler(0, 0, 0, 0, 0, 0, 0, 0, 0, 0), Toddler(1, 0, 0, 0, 0, 0, 0, 0, 0, 0)]
        self.__teacher = Teacher(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


    #METHODS

    def action(self):
        toddlers = self.__toddlers
        for toddler in toddlers:
            toddler.action()



    #GETTER
    def get_time(self) -> int:
        return self.__time

    def get_toddlers(self) -> list:
        return self.__toddlers

    def get_teacher(self) -> Teacher:
        return self.__teacher



    ##SETTERS
    def set_time(self, time: int):
        self.__time = time

    def set_toddlers(self, toddlers: list[Toddler]):
        self.__toddlers = toddlers

    def set_teacher(self, teacher: Teacher):
        self.__teacher = teacher

    ##ADDERS
    def increment_time(self):
        self.__time += 1

    def stop_game(self):
        self.__running = False