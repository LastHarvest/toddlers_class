# Teacher.py

from Human import *


class Teacher(Human):

    def __init__(self, id, position, pos_table, direction):
        super().__init__(id, position, direction, pos_table)

    def get_position(self):
        return self._position

    def distance(self, other) -> float:
        o = other.get_position()
        return abs(self._position[0] - o[0]) + abs(self._position[1] - o[1])

    def watch_children(self, toddlers, tables, candy):
        bad_toddlers = []
        for t in toddlers:
            if not t.get_table():
                bad_toddlers.append(t)
                if self._position == t.get_position():
                    print(f"Toddler{t.get_position()} Teacher {self.get_position()}")
                    t.get_position = t.get_pos_table()
                    self.move_to(t.get_position, tables)
                    return
        if bad_toddlers:
            print("Following bad toddlers")
            self.move_to(self.choice_toddler_distance_from_candy(bad_toddlers,candy), tables)

    def choice_toddler_distance_from_teacher(self, toddlers):
        chosen_toddler = toddlers[0]
        for t in toddlers:
            if self.distance(t) < self.distance(chosen_toddler):
                chosen_toddler = t
        return chosen_toddler.get_position()

    def choice_toddler_distance_from_candy(self, toddlers, candy):
        chosen_toddler = toddlers[0]
        for t in toddlers:
            if t.distance_to(candy) < chosen_toddler.distance_to(candy):
                chosen_toddler = t
        return chosen_toddler.get_position()

    def caught(self, t):
        return t == self._position