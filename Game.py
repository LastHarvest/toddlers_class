from CrazyToddler import CrazyToddler
from HungryToddler import HungryToddler
from LyingToddler import LyingToddler
from RunningToddler import RunningToddler
from SmartToddler import SmartToddler
from StupidToddler import StupidToddler
from Teacher import Teacher
from AfraidToddler import *

import random

class Game:
    def __init__(self, grid_size):
        self._running = True
        self._time = 0
        self._toddlers = []
        self._teacher = Teacher(3, (6, 0), (6, 0), "right")
        self._candy = (6, 7)
        self._initial_positions = []
        self.initialize_players(grid_size, 12)

    def initialize_players(self, grid_size, nbToddler):
        tabToddlers =[
            AfraidToddler(0,(1,1), "right",(1,1)),
            CrazyToddler(1, (1,1), "left",(1,1)),
            StupidToddler(2, (1,1), "left",(1,1)),
            RunningToddler(3, (1,1), "left",(1,1)),
            SmartToddler(4, (1,1), "left",(1,1)),
            HungryToddler(5, (1,1), "left",(1,1),1)
        ]
        pos = [(0,4),(12,11),(6,12),(3,5),(8,10),(12,5),(1,12),(1,9),(9,4),(9,12),(3,11),(11,8)]

        for i in range(nbToddler):
            if i%2 != 0 :
                r = int((i-1)/2)
            else :
                r = int(i/2)
            toddler = tabToddlers[r]
            toddler.set_id(i+1)
            table = pos[i]
            toddler.set_position(table)
            toddler.set_pos_table(table)
            self._initial_positions.append(table)

            if r == 5 :
                temp = random.randrange(10,16)
                toddler.set_hunger(temp)

            self._toddlers.append(toddler)



    def get_initial_positions(self):
        return self._initial_positions

    def action(self):
        toddlers = self._toddlers
        for i in range(1):
            self._teacher.watch_children(toddlers, self._initial_positions, self._candy)
            print("WATCHING")
        for toddler in toddlers:
            toddler.strategy(self._candy, self._teacher, self._initial_positions)
            if toddler.at_table() and not toddler.get_table():
                toddler.set_table(True)
            if not toddler.at_table() and toddler.get_table():
                toddler.set_table(False)



    def get_running(self):
        return self._running

    #GETTER
    def get_time(self) -> int:
        return self._time

    def get_toddlers(self) -> list:
        return self._toddlers

    def get_teacher(self) -> Teacher:
        return self._teacher

    def get_candy(self):
        return self._candy


    ##SETTERS
    def set_time(self, time: int):
        self._time = time

    def set_toddlers(self, toddlers: list[Toddler]):
        self._toddlers = toddlers

    def set_teacher(self, teacher: Teacher):
        self._teacher = teacher

    ##ADDERS
    def increment_time(self):
        self._time += 1

    def stop_game(self):
        self._running = False