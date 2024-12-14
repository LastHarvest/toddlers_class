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
        self._candy = (6, 12)
        self._initial_positions = []
        self.initialize_players(grid_size, 6)


    def init_pos(self, grid_size, initial_pos):
        max_attempts = 100  # Limiter les tentatives pour éviter une boucle infinie
        for _ in range(max_attempts):
            y = random.randrange(3, grid_size - 3)  # Respecte une marge de 3 en haut/bas
            x = random.randrange(0, grid_size)     # Toute la largeur est possible
            if (x, y) not in initial_pos:
                return (x, y)
        raise ValueError("Impossible de trouver une position disponible.")  # Gestion d'erreur si aucune position n'est libre


    def initialize_players(self, grid_size, nbToddler):
        tabToddlers =[
            AfraidToddler(0,(1,1), "right",(1,1)),
            CrazyToddler(1, (1,1), "left",(1,1)),
            StupidToddler(2, (1,1), "left",(1,1)),
            RunningToddler(3, (1,1), "left",(1,1)),
            SmartToddler(4, (1,1), "left",(1,1)),
            HungryToddler(5, (1,1), "left",(1,1),1)
        ]
        initial_pos=[]

        for i in range(nbToddler):
            r = random.randrange(0,5)
            toddler = tabToddlers[r]
            toddler.set_id(i+1)
            table = self.init_pos(grid_size,initial_pos)
            toddler.set_position(table)
            toddler.set_pos_table(table)

            initial_pos.append(table)  # Ajoute la table elle-même
            adjacent_positions = [
                (table[0] + 1, table[1]),  # Case en bas
                (table[0] - 1, table[1]),  # Case en haut
                (table[0], table[1] + 1),  # Case à droite
                (table[0], table[1] - 1),  # Case à gauche
            ]

            for pos in adjacent_positions:
                initial_pos.append(pos)

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