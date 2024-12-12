import math
from Human import Human

class Toddler(Human):

    def __init__(self, id,position, pos_table, direction):
        super().__init__(id,position, direction)
        #self.table = table
        self.__table = pos_table



    def get_table(self):
        """Return the current table state of the agent."""
        return self.table

    def get_direction(self):
        return self.__direction

    def get_table(self):
        return self.__table

    # Setters
    def update_pos(self, new_position):
        """Update the agent's position."""
        self.__position = new_position

    def update_Pos_table(self, pos):
        self.__pos_table = pos

    def update_direction(self, dir):
        self.__direction = dir

    def update_Table(self, state):
        self.__table = state

    # Movements
    def move_up(self):
        self.__position = (self.__position[0], self.__position[1] + 1)

    def move_down(self):
        self.__position = (self.__position[0], self.__position[1] - 1)

    def move_left(self):
        self.__position = (self.__position[0] - 1, self.__position[1])
        self.__direction = "left"

    def move_right(self):
        self.__position = (self.__position[0] + 1, self.__position[1])
        self.__direction = "right"

    # Other functions
    def get_distance_resource(self, teacher):
        pos_student = self.get_position()
        pos_teacher = teacher.get_position()
        return math.sqrt((pos_teacher[0] - pos_student[0])**2 + (pos_teacher[1] - pos_student[1])**2)

    def move_player_to_table(self):
        s = self.get_position()
        b = self.get_table()
        if s[0] < b[0] and s[0] < 6:
            self.move_right()
        elif s[0] > b[0] and s[0] > 0:
            self.move_left()
        else:
            if s[1] < b[1] and s[1] < 6:
                self.move_up()
            elif s[1] > b[1] and s[1] > 0:
                self.move_down()

    # Implementing previously abstract methods
    def collect_resource(self, candy):
        # Implementation for collecting resource
        pass

    def strategie(self, teacher):
        # Implementation for strategy
        pass

    def move_player_to_bonbon(self, bonbon):
        # Implementation for moving player to bonbon
        pass