# Teacher.py

from Human import *
class Teacher(Human):

    def __init__(self, id, position, pos_table, direction):
        super().__init__(id, position, direction, pos_table)

    def get_position(self):
        return self._position

    def distance(self, other) -> float:
        return abs(self._position[0] - other.get_position()[0]) + abs(self._position[1] - other.get_position()[1])

    def watch_children(self, toddlers):
        bad_toddlers = []
        for toddler in toddlers:
            if not toddler.get_table():
                bad_toddlers.append(toddler)
        if bad_toddlers:
            print("Following bad toddlers")
            self.move_to(self.choice_toddler(bad_toddlers))

    def choice_toddler(self, toddlers):
        chosen_toddler = toddlers[0]
        for t in toddlers:
            if self.distance(t) < self.distance(chosen_toddler):
                chosen_toddler = t
        return chosen_toddler

    def move_player_to_toddler(self, toddler):
        s = self.get_position()
        t = toddler.get_position()
        if s[0] < t[0] and s[0] < 6:
            self.move_right()
        elif s[0] > t[0] and s[0] > 0:
            self.move_left()
        else:
            if s[1] < t[1] and s[1] < 6:
                self.move_up()
            elif s[1] > t[1] and s[1] > 0:
                self.move_down()