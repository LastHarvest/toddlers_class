# Game.py
from Teacher import Teacher
from CrazyToddler import CrazyToddler
from AfraidToddler import AfraidToddler

class Game:
    def __init__(self):
        self._running = True
        self._time = 0
        self._toddlers = [AfraidToddler(1, (0, 0), (0, 0), "right"), CrazyToddler(2, (1, 1), (1, 1), "left")]
        self._teacher = Teacher(3, (1, 0), (2, 3), "right")
        self._candy = (2, 2)

    def action(self):
        toddlers = self._toddlers
        for toddler in toddlers:
            toddler.strategy(self._candy, self._teacher)

    def get_running(self):
        return self._running

    def get_time(self) -> int:
        return self._time

    def get_toddlers(self) -> list:
        return self._toddlers

    def get_teacher(self) -> Teacher:
        return self._teacher

    def get_candy(self):
        return self._candy

    def set_time(self, time: int):
        self._time = time

    def set_toddlers(self, toddlers: list):
        self._toddlers = toddlers

    def set_teacher(self, teacher: Teacher):
        self._teacher = teacher

    def increment_time(self):
        self._time += 1

    def stop_game(self):
        self._running = False