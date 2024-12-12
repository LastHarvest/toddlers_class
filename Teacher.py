from Human import Human
from Toddler import Toddler
from Game import Game


class Teacher(Human):
    def __init__(self, id,position, direction):
        super().__init__(id,position, direction)
        self.direction = direction

    def distance(self, other) -> float:
        # Return the Manhattan distance between the current agent and another agent.
        return abs(self.position[0] - other.position[0]) + abs(self.position[1] - other.position[1])

    def watch_children(self):
        toddlers = Game.get_toddlers()
        bad_toddlers = []
        for toddler in toddlers:
            if not toddler.get_Table():
                bad_toddlers.append(toddler)
        return self.choice_toddler(bad_toddlers)

    def choice_toddler(self, toddlers):
        #TODO : Impémenter d'autres stratégies ?
        #Strategie que sur la distance Manhattan
        chosen_toddler = toddlers[0]
        for t in toddlers:
            if self.distance(t) < self.distance(chosen_toddler):
                chosen_toddler = t
        return chosen_toddler

    def move_player_to_toddler(self, toddler):
        #TODO: Rajouter les conditions sur les tables
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


