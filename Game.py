import random
from time import sleep

from Toddler import Toddler
from Teacher import Teacher
from CrazyToddler import *
from AfraidToddler import *


class Game:
    def __init__(self, grid_size):
        self._running = True
        self._time = 0
        self._toddlers = []
        self._teacher = Teacher(3, (6, 0), (6, 0), "right")
        self._candy = (6, 12)
        self._initial_positions = []
        self.initialize_players(grid_size)

    def initialize_players(self, grid_size):
        grid_center_x = grid_size // 2
        grid_center_y = grid_size // 2
        left_positions = [(grid_center_x - 2, grid_center_y - 3 + i * 2) for i in range(4)]
        right_positions = [(grid_center_x + 2, grid_center_y - 3 + i * 2) for i in range(4)]
        self._initial_positions = left_positions + right_positions
        for i, pos in enumerate(self._initial_positions):
            print(i)
            if i < 4:
                self._toddlers.append(AfraidToddler(i + 1, pos, pos, "right"))
            else:
                self._toddlers.append(CrazyToddler(i + 1, pos, pos, "left"))
        print(self._toddlers)
    def get_initial_positions(self):
        return self._initial_positions

    def action(self):
        toddlers = self._toddlers
        for i in range(2):
            for t in toddlers:
                if self._teacher.caught(t):
                    print("CAUGHT")
                    self._running = False
            self._teacher.watch_children(toddlers, self._initial_positions, self._candy)
        for toddler in toddlers:
            if toddler.get_position() == self._teacher.get_position():
                self._running = False
            toddler.strategy(self._candy, self._teacher, self._initial_positions)
            toddler.at_table()

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