import math
from abc import ABC, abstractmethod


class Toddler():

    def __init__(self,position,id, Table, Pos_table, direction):
        self.position = position
        self.id = id
        self.Table = True
        self.Pos_table = Pos_table
        self.direction = direction

    # Getters

    def get_id(self):
        return self.id

    def get_pos(self):
        """Return the current position of the agent."""
        return self.position
    
    def get_Table(self):
        """Return the current points of the agent."""
        return self.Table
    
    def get_direction(self):
        return self.direction
    
    def get_Pos_table(self):
        return self.Pos_table


    #Setters
    def update_pos(self, new_position):
        """Update the agent's position."""
        self.position = new_position

    def update_Pos_table(self, pos):
        self.Pos_table = pos
    
    def update_direction(self, dir):
        self.direction = dir
    
    def update_Table(self, state):
        self.Table = state


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
    def get_distance_resource(self, teacher):
        pos_student = self.get_pos()
        pos_teacher = teacher.get_pos()
        return math.sqrt((pos_teacher[0] - pos_student[0])**2 + (pos_teacher[1] - pos_student[1])**2)


    # fonctions abstraites
    @abstractmethod
    def collect_resource(self,bonbon):
        pass

    @abstractmethod
    def Strategie(self, teacher):
        pass

    @abstractmethod
    def move_player_to_bonbon(self, bonbon):
        pass

    
