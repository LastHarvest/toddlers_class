import heapq

from Human import Human


class Teacher(Human):

    def __init__(self, id, position, pos_table, direction):
        super().__init__(id, position, direction, pos_table)
        self._nb_caught = 0




    def get_position(self):
        return self._position

    def get_nb_caught(self):
        return self._nb_caught

    def distance(self, other) -> float:
        o = other.get_position()
        return abs(self._position[0] - o[0]) + abs(self._position[1] - o[1])

    def watch_children(self, toddlers, tables, candy):
        bad_toddlers = []
        for t in toddlers:
            if not t.get_position() == t.get_pos_table() and not t.get_position() == candy:
                bad_toddlers.append(t)
        if bad_toddlers:
            print("Following bad toddlers")
            t = self.choice_toddler_distance_from_candy(bad_toddlers, candy)
            self.move_to(t.get_position(), tables, candy)
            if self.caught(t):
                t.set_position(t.get_pos_table())
                if t._has_candy:
                    t._has_candy = False
                    t.minus_candy()
                    t.lose_candy_point()  # Increment the counter
                self._nb_caught += 1

    def choice_toddler_distance_from_teacher(self, toddlers):
        chosen_toddler = toddlers[0]
        for t in toddlers:
            if self.distance(t) < self.distance(chosen_toddler):
                chosen_toddler = t
        return chosen_toddler.get_position()

    def choice_toddler_distance_from_candy(self, toddlers, candy):
        toddlers_between = [t for t in toddlers if t.distance_to(candy) < self.distance(t)]

        if toddlers_between:
            chosen_toddler = toddlers_between[0]
            for t in toddlers_between:
                if t.distance_to(candy) < chosen_toddler.distance_to(candy):
                    chosen_toddler = t
        else:
            toddlers_with_candy = [t for t in toddlers if t._has_candy]
            if toddlers_with_candy:
                chosen_toddler = toddlers_with_candy[0]
            else:
                chosen_toddler = toddlers[0]
                for t in toddlers:
                    if self.distance(t) < self.distance(chosen_toddler):
                        chosen_toddler = t

        return chosen_toddler

    def move_to(self, goal, tables, candy):
        def neighbors(pos):
            x, y = pos
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                new_pos = (x + dx, y + dy)
                if 0 <= new_pos[0] < 13 and 0 <= new_pos[1] < 13 and (
                        new_pos not in tables or new_pos == self._pos_table) and new_pos != candy:
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
            print(f"{self.get_id()} Goal is blocked by a table.")
            return

        if goal == candy:
            print(f"{self.get_id()} Goal is the candy's position.")
            return

        path = dijkstra(self._position, goal)
        if not path:
            print(f"{self.get_id()} No path found to the goal.")
            return

        if len(path) > 1:
            next_step = path[1]
            if next_step in [t.get_position() for t in Human.all_toddlers] and next_step != Human.teacher.get_position():
                print("Next step is blocked by another toddler.")
                return
            if next_step == candy:
                print("Next step is the candy's position.")
                return
            if next_step[0] > self._position[0]:
                if next_step[1] > self._position[1]:
                    self.move_down_right()
                elif next_step[1] < self._position[1]:
                    self.move_up_right()
                else:
                    self.move_right()
            elif next_step[0] < self._position[0]:
                if next_step[1] > self._position[1]:
                    self.move_down_left()
                elif next_step[1] < self._position[1]:
                    self.move_up_left()
                else:
                    self.move_left()
            else:
                if next_step[1] > self._position[1]:
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

    def move_up_left(self):
        self._position = (self._position[0] - 1, self._position[1] - 1)
        self._direction = "up_left"

    def move_up_right(self):
        self._position = (self._position[0] + 1, self._position[1] - 1)
        self._direction = "up_right"

    def move_down_left(self):
        self._position = (self._position[0] - 1, self._position[1] + 1)
        self._direction = "down_left"

    def move_down_right(self):
        self._position = (self._position[0] + 1, self._position[1] + 1)
        self._direction = "down_right"

    def caught(self, t):
       return self.next_to(t)