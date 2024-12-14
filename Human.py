import heapq
from abc import ABC, abstractmethod
import math

class Human(ABC):
    all_toddlers = []
    teacher = None

    def __init__(self, id: int, position: tuple, direction: str, pos_table: tuple):
        self._id = id
        self._position = position
        self._direction = direction
        self._pos_table = pos_table
        self._table = True

    def distance(self, other) -> float:
        return abs(self._position[0] - other.get_position()[0]) + abs(self._position[1] - other.get_position()[1])

    def distance_to(self, other: tuple) -> float:
        position = self._position
        return math.sqrt((other[0] - position[0]) ** 2 + (other[1] - position[1]) ** 2)

    def at_table(self) -> bool:
        return self._position == self._pos_table

    def get_id(self) -> int:
        return self._id

    def get_position(self) -> tuple:
        return self._position

    def get_direction(self) -> str:
        return self._direction

    def get_pos_table(self) -> tuple:
        return self._pos_table

    def get_table(self) -> bool:
        return self._table

    def set_id(self, idBis):
        self._id = idBis

    def set_direction(self, direction: str):
        self._direction = direction

    def set_table(self, table: bool):
        self._table = table

    def set_position(self, position: tuple):
        self._position = position

    def set_pos_table(self, pos_table: tuple):
        self._pos_table = pos_table

    def next_to(self, other):
        return self.distance(other) == 1

    def next_to_tuple(self,other:tuple):
        return self.distance_to(other) == 1

    def move_down(self):
        tmp = (self._position[0], self._position[1] + 1)
        self._position = tmp

        self._direction = "down"

    def move_up(self):
        tmp = (self._position[0], self._position[1] - 1)
        self._position = tmp
        self._direction = "up"


    def move_left(self):
        tmp = (self._position[0] - 1, self._position[1])
        self._position = tmp
        self._direction = "left"


    def move_right(self):
        tmp = (self._position[0] + 1, self._position[1])
        self._position = tmp
        self._direction = "right"

    def move_to(self, goal, tables):
        def neighbors(pos):
            x, y = pos
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_pos = (x + dx, y + dy)
                if 0 <= new_pos[0] < 13 and 0 <= new_pos[1] < 13 and (
                        new_pos not in tables or new_pos == self._pos_table):
                    yield new_pos

        def dijkstra(start, goal):
            queue = [(0, start)]
            distances = {start: 0}
            previous = {start: None}

            while queue:
                current_distance, current_position = heapq.heappop(queue)

                if current_position == goal:
                    path = []
                    while current_position:
                        path.append(current_position)
                        current_position = previous[current_position]
                    return path[::-1]

                for neighbor in neighbors(current_position):
                    distance = current_distance + 1
                    if neighbor not in distances or distance < distances[neighbor]:
                        distances[neighbor] = distance
                        priority = distance
                        heapq.heappush(queue, (priority, neighbor))
                        previous[neighbor] = current_position

            return []

        if goal in tables and goal != self._pos_table:
            print("Goal is blocked by a table.")
            return

        path = dijkstra(self._position, goal)
        if not path:
            print("No path found to the goal.")
            return

        if len(path) > 1:
            next_step = path[1]
            if next_step in [t.get_position() for t in
                             Human.all_toddlers] and next_step != Human.teacher.get_position():
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