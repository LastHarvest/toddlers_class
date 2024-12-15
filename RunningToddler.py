import math

from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray

from Toddler import Toddler



class RunningToddler(Toddler):
    TYPE = 4

    def __init__(self, id, position, direction, pos_table,cooldown):
        super().__init__(id, position, direction, pos_table, cooldown)

    def strategy(self, candy, teacher, tables):
        print(f"RunningToddler: I'm cadny to the table{self._position}")
        print(f"Candy: {candy}")
        print(f"Has candy: {self._has_candy}")
        if self._cooldown != 0: self._cooldown -=1

        elif self._has_candy:
            print(f"RunningToddler: I'me table{self._pos_table}")
            if self.at_table():
                self._has_candy = False
                self._cooldown = self._rest
            else:
                print("RunningToddler: I'm running to the table")
                self.move_to(self._pos_table, tables)
        else:
            if self.next_to_tuple(candy) or self._position == candy and not self._has_candy:
                self.collect_candy(candy)
                self._has_candy = True
                self.move_to(self._pos_table, tables)
            else:
                for i in range(2):
                    self.move_to(candy, tables)


    def to_candy(self, teacher, candy, tables):
        pass