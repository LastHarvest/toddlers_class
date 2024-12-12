from Human import Human



class Teacher(Human):

    def __init__(self, id, position, pos_table, direction):
        super().__init__(id, position, direction, pos_table)


    def watch_children(self, toddlers : list):
        bad_toddlers = []
        for toddler in toddlers:
            if not toddler.get_table():
                bad_toddlers.append(toddler)
        return self.choice_toddler(bad_toddlers)

    def choice_toddler(self, toddlers : list):
        #TODO : Impémenter d'autres stratégies ?
        #Strategie que sur la distance Manhattan
        chosen_toddler = toddlers[0]
        for t in toddlers:
            if self.distance(t) < self.distance(chosen_toddler):
                chosen_toddler = t
        return chosen_toddler




