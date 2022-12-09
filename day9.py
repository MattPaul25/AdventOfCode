

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tracker = {f'{str(self.x)},{str(self.y)}'}

    def move_left(self):
        self.x = self.x - 1
        self.tracker.add(f'{str(self.x)},{str(self.y)}')

    def move_right(self):
        self.x = self.x + 1
        self.tracker.add(f'{str(self.x)},{str(self.y)}')

    def move_up(self):
        self.y = self.y + 1
        self.tracker.add(f'{str(self.x)},{str(self.y)}')

    def move_down(self):
        self.y = self.y - 1
        self.tracker.add(f'{str(self.x)},{str(self.y)}')

    def set_location(self, x_move, y_move):
        self.x += x_move
        self.y += y_move
        self.tracker.add(f'{str(self.x)},{str(self.y)}')

class Rope:

    def __init__(self, knots):
        self.knots = knots
        self.rope = self.build_rope()
        self.move_map = {
            'L': self.rope[0].move_left,
            'R': self.rope[0].move_right,
            'U': self.rope[0].move_up,
            'D': self.rope[0].move_down
        }

    def build_rope(self):
        rope = []
        for knot in range(0, self.knots+1):
            rope.append(Location(50, 50))
        return rope


    def move_head(self, direction, steps):
        head_move = self.move_map[direction]
        for step in range(1, int(steps) + 1):
            head_move()
            self.move_tail()

    def move_tail(self):
        previous_knot = self.rope[0]
        for knot in self.rope[1:]:
            x_diff = previous_knot.x - knot.x
            y_diff = previous_knot.y - knot.y
            x_move, y_move = 0, 0
            if abs(x_diff) > 1:
                x_move = -1 if x_diff < 0 else 1
                if abs(y_diff) > 0:
                    y_move = -1 if y_diff < 0 else 1
            elif abs(y_diff) > 1:
                y_move = -1 if y_diff < 0 else 1
                if abs(x_diff) > 0:
                    x_move = -1 if x_diff < 0 else 1
            knot.set_location(x_move, y_move)
            previous_knot = knot


def get_data():
    with open("day9_input.txt", "r") as f:
        lines = f.readlines()
    return lines

steps = [d.strip() for d in get_data()]
rope = Rope(9)
for s in steps:
    direction, step_count = s.split(' ')
    rope.move_head(direction, step_count)

tail = rope.rope[len(rope.rope)-1]
print(f'tail spots are {len(tail.tracker)}')
