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
            if not t.get_position() == t.get_pos_table() and not t.get_position() == candy:
                bad_toddlers.append(t)
        if bad_toddlers:
            print("Following bad toddlers")
            t = self.choice_toddler_distance_from_candy(bad_toddlers, candy)
            self.move_to(t.get_position(), tables)
            if self.caught(t):
                t.set_position(t.get_pos_table())
                t._has_candy = False
    def choice_toddler_distance_from_teacher(self, toddlers):
        chosen_toddler = toddlers[0]
        for t in toddlers:
            if self.distance(t) < self.distance(chosen_toddler):
                chosen_toddler = t
        return chosen_toddler.get_position()

    def choice_toddler_distance_from_candy(self, toddlers, candy):
        # Check if there are any toddlers between the teacher and the candy
        toddlers_between = [t for t in toddlers if t.distance_to(candy) < self.distance(t)]

        if toddlers_between:
            # Choose the closest toddler between the teacher and the candy
            chosen_toddler = toddlers_between[0]
            for t in toddlers_between:
                if t.distance_to(candy) < chosen_toddler.distance_to(candy):
                    chosen_toddler = t
        else:
            # Choose a toddler who has the candy
            toddlers_with_candy = [t for t in toddlers if t._has_candy]
            if toddlers_with_candy:
                chosen_toddler = toddlers_with_candy[0]
            else:
                # Default to the closest toddler if no one has candy
                chosen_toddler = toddlers[0]
                for t in toddlers:
                    if self.distance(t) < self.distance(chosen_toddler):
                        chosen_toddler = t

        return chosen_toddler

    def caught(self, t):
        return self.next_to(t)