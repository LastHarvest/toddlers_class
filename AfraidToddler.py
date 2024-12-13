# AfraidToddler.py
from Toddler import Toddler

class AfraidToddler(Toddler):

    def __init__(self, id, position, pos_table, direction):
        super().__init__(id, position, direction, pos_table)

    def strategy(self, candy, teacher):
        # si l'élève est sur sa table alors il se relève pour partir mais il fait attention à où est le professeur
        if self._position == self._pos_table and not self._table:
            if self.distance_to(teacher.get_position()) > 3:
                self.set_table(True)
        # Si il est sur la boite de bonbons il en récupère un
        elif candy == self._position:
            self.collect_candy(candy)
        # Si il n'est pas sur sa table alors qu'il a son bonbon il y va
        elif self._position != self._pos_table and not self._table:
            self.move_to(self._pos_table)
        # Sinon il va chercher son bonbon
        else:
            self.to_candy(teacher, candy)

    def to_candy(self, teacher, candy):
        # Il va chercher son bonbon mais donne la priorité à fuir la prof.
        s = self._position
        t = teacher.get_position()
        c = candy
        # Il vérifie où est la prof
        # Si elle est assez loin il va chercher le bonbon
        if self.distance_to(t) > 3:
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