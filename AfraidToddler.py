# AfraidToddler.py
import heapq
from Human import Human
from Toddler import Toddler

class AfraidToddler(Toddler):
    TYPE = 0

    def __init__(self, id, position, direction, pos_table):
        super().__init__(id, position, direction, pos_table)

    def strategy(self, candy, teacher, tables):
        if self._has_candy:
            if self.at_table():
                self._has_candy = False
            else:
                self.move_to2(self._pos_table, tables)
        else:
            if self.next_to_tuple(candy) and not self._has_candy:
                self.collect_candy(candy)
                self.move_to2(self._pos_table, tables)

            elif self.distance_to(teacher.get_position()) < 2:
                self.move_to2(self._pos_table, tables)
            else:
                self.move_to2(candy, tables)

    def move_to2(self, goal, tables):
        def heuristic(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        def neighbors(pos):
            x, y = pos
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_pos = (x + dx, y + dy)
                if 0 <= new_pos[0] < 13 and 0 <= new_pos[1] < 13 and (
                        new_pos not in tables or new_pos == self._pos_table):
                    yield new_pos

        def a_star(start, goal):
            open_set = []
            heapq.heappush(open_set, (0, start))
            came_from = {}
            g_score = {start: 0}
            f_score = {start: heuristic(start, goal)}

            while open_set:
                _, current = heapq.heappop(open_set)

                if current == goal:
                    path = []
                    while current in came_from:
                        path.append(current)
                        current = came_from[current]
                    path.append(start)
                    return path[::-1]

                for neighbor in neighbors(current):
                    tentative_g_score = g_score[current] + 1
                    if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g_score
                        f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))

            return []

        if goal in tables and goal != self._pos_table:
            print(f"{self.get_id()} Goal is blocked by a table.")
            return

        path = a_star(self._position, goal)
        if not path:
            print(f"{self.get_id()} No path found to the goal.")
            return

        if len(path) > 1:
            next_step = path[1]
            if next_step in [t.get_position() for t in Human.all_toddlers] and next_step != Human.teacher.get_position():
                print("Next step is blocked by another toddler.")
                return
            if next_step[0] > self._position[0]:
                self.move_right()
            elif next_step[0] < self._position[0]:
                self.move_left()
            elif next_step[1] > self._position[1]:
                self.move_down()
            elif next_step[1] < self._position[1]:
                self.move_up()

    def move_up(self):
        self._position = (self._position[0], self._position[1] - 1)
        self._direction = "up"

    def move_down(self):
        self._position = (self._position[0], self._position[1] + 1)
        self._direction = "down"

    def move_left(self):
        self._position = (self._position[0] - 1, self._position[1])
        self._direction = "left"

    def move_right(self):
        self._position = (self._position[0] + 1, self._position[1])
        self._direction = "right"

    def to_candy(self, teacher, candy, tables):
        pass