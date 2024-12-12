import random
from time import sleep

from Toddler import Toddler
from Teacher import Teacher
from CrazyToddler import *
from AfraidToddler import *


class Game:
    def __init__(self):
        self.__running = True
        self.__time = 0
        self.__toddlers = [AfraidToddler( 1,(0, 0), (0, 0) , "right"), CrazyToddler(2,(1, 1),   (1, 1), "left")]
        self.__teacher = Teacher(3,(1, 0), (2,3), "right")

    #METHODS

    def action(self):
        toddlers = self.__toddlers
        for toddler in toddlers:
            toddler.strategy()

    def get_running(self):
        return self.__running

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