from CrazyToddler import CrazyToddler
from HungryToddler import HungryToddler
from LyingToddler import LyingToddler
from SmartToddler import SmartToddler
from StupidToddler import StupidToddler
from Teacher import Teacher

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
            if i < 2:
                self._toddlers.append(AfraidToddler(i + 1, pos, pos, "right"))
            elif i < 4:
                self._toddlers.append(LyingToddler(i + 1, pos, pos, "right"))
            elif i < 6:
                self._toddlers.append(SmartToddler(i + 1, pos, pos, "left"))
            else:
                self._toddlers.append(HungryToddler(i + 1, pos, pos, "left"))
        print(self._toddlers)


    def get_initial_positions(self):
        return self._initial_positions

    def action(self):
        toddlers = self._toddlers
        for i in range(1):
            self._teacher.watch_children(toddlers, self._initial_positions, self._candy)
            print("WATCHING")
        for toddler in toddlers:
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