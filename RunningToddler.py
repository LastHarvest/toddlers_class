import math
from Toddler import Toddler



class RunningToddler(Toddler):


    def __init__(self, id, position, pos_table, direction):
        super().__init__(id, position, direction, pos_table)


    def strategy(self, candy, teacher):
        # Si il est sur sa table il se lève pour aller chercher un bonbon si la prof est loin
        if self.get_position == self._pos_table and self._table() == False:
            if self.distance(teacher.get_position())>3:
                self.set_table(True)
        # Si il est sur les bonbons il en prend un
        elif candy == self._position:
            self.collect_candy(self,candy)
        # Si il n'est pas sur sa table et qu'il devrait y être il y va
        elif self.get_position != self._pos_table and self._table() == False :
            self.move_to(self._pos_table)
        # Sinon il avance 2 fois
        else :
            self.to_candy(teacher, candy)
            self.to_candy(teacher, candy)
            


    def to_candy(self, teacher, candy):
        # Il va chercher son bonbon mais donne la priorité sur fuir la prof
        s = self._position
        t = teacher.get_position()
        c = candy
        # Il vérifie où est la prof
        # Si elle est assez loin il va chercher le bonbon
        if self.distance(t) > 3 :
            if s[0] < c[0] and s[0] < 6:
                self.move_left()
            elif s[0] > c[0] and s[0] > 0:
                self.move_right()
            else:
                if s[1] < c[1] and s[1] < 6:
                    self.move_down()
                elif s[1] > c[1] and s[1] > 0:
                    self.move_up()
        # Si elle est trop proche il l'a fuit
        else :
            if s[0] < t[0] and s[0] > 0:
                self.move_right()
            elif s[0] > t[0] and s[0] < 6:
                self.move_left()
            else:
                if s[1] < t[1] and s[1] > 0:
                    self.move_up()
                elif s[1] > t[1] and s[1] < 6:
                    self.move_down()


    
