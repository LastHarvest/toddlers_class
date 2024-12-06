import math
from Human import Human
from abc import ABC, abstractmethod


class Toddler(Human):

    def __init__(self,position,id, table, pos_table, direction):
        super().__init__(self, position)
        self.id = id
        self.table = True
        self.pos_table = pos_table
        self.direction = direction

    # Getters

    def get_id(self):
        return self.id

    def get_pos(self):
        """Return the current position of the agent."""
        return self.position
    
    def get_Table(self):
        """Return the current points of the agent."""
        return self.table
    
    def get_direction(self):
        return self.direction
    
    def get_Pos_table(self):
        return self.pos_table


    #Setters
    def update_pos(self, new_position):
        """Update the agent's position."""
        self.position = new_position

    def update_Pos_table(self, pos):
        self.pos_table = pos
    
    def update_direction(self, dir):
        self.direction = dir
    
    def update_Table(self, state):
        self.table = state


    # Déplacements
    def move_up(self):
            self.position = (self.position[0], self.position[1] + 1)

    def move_down(self):
        self.position = (self.position[0], self.position[1] - 1)

    def move_left(self):
        self.position = (self.position[0] - 1, self.position[1])
        self.direction="left"

    def move_right(self):
        self.position = (self.position[0] + 1, self.position[1])
        self.direction="right"
    

    # autres fonctions
    def get_distance_resource(self, pos):
        pos_student = self.get_pos()
        return math.sqrt((pos[0] - pos_student[0])**2 + (pos[1] - pos_student[1])**2)

    def move_player_to_table(self):
        s = self.get_pos()
        b = self.get_Pos_table()
        if s[0] < b[0] and s[0] < 6:
            self.move_right()
        elif s[0] > b[0] and s[0] > 0:
            self.move_left()
        else:
            if s[1] < b[1] and s[1] < 6:
                self.move_up()
            elif s[1] > b[1] and s[1] > 0:
                self.move_down()

    # fonctions abstraites
    @abstractmethod
    def collect_resource(self,candy):
        pass

    @abstractmethod
    def Strategie(self, teacher, candy):
        pass

    @abstractmethod
    def move_player_to_candy(self,teacher, candy):
        pass

    
