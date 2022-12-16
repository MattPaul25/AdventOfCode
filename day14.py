
def get_data():
    with open("day14_input.txt", "r") as f:
        lines = f.readlines()
    return lines


class Cave:

    def __init__(self, cave_size, sand_point):
        self.cave_size = cave_size
        self.sand_point = sand_point
        self.matrix = self.create_matrix()
        self.lowest_floor = 0
        self.sand_count = 0

    def create_matrix(self):
        matrix = []
        for i_y in range(0, self.cave_size[1] + 1):
            horizontal_line = []
            for i_x in range(0, self.cave_size[0] + 1):
                if i_x == self.sand_point[0] and i_y == 0:
                    horizontal_line.append('+')
                else:
                    horizontal_line.append('.')
            matrix.append(horizontal_line)
        return matrix

    def print_matrix(self):
        for line in self.matrix:
            print(''.join(line))

    def drop_sand(self):
        start_point_x, start_point_y = self.sand_point

        falling = self.matrix[start_point_y][start_point_x] in ['.', '+']
        while falling:
            if start_point_y + 1 >= len(self.matrix) - 1:
                return falling
            if self.matrix[start_point_y + 1][start_point_x] == '.':
                start_point_y += 1
                continue
            else:
                if self.matrix[start_point_y + 1][start_point_x - 1] == '.':
                    start_point_y += 1
                    start_point_x -= 1
                    continue
                elif self.matrix[start_point_y + 1][start_point_x + 1] == '.':
                    start_point_y += 1
                    start_point_x += 1
                    continue
                else:
                    self.matrix[start_point_y][start_point_x] = 'o'
                    self.sand_count += 1
                    falling = False
        return falling

    def add_rock(self, rock_formation):
        rock_points = rock_formation.split('->')
        for idx, rock in enumerate(rock_points):
            if idx < (len(rock_points) - 1):
                start_rock_x, start_rock_y = [int(r) for r in rock.split(',')]
                next_rock_x, next_rock_y = [int(r) for r in rock_points[idx + 1].split(',')]
                self.lowest_floor = next_rock_y if next_rock_y > self.lowest_floor else self.lowest_floor
                if start_rock_x == next_rock_x:
                    y_diff = next_rock_y - start_rock_y
                    y_diff_pos = y_diff > 0
                    for i in range(0, abs(y_diff) + 1):
                        new_i = i if y_diff_pos else -i
                        self.matrix[start_rock_y + new_i][start_rock_x] = '#'
                elif start_rock_y == next_rock_y:
                    x_diff = next_rock_x - start_rock_x
                    x_diff_pos = x_diff > 0
                    for i in range(0, abs(x_diff) + 1):
                        new_i = i if x_diff_pos else -i
                        self.matrix[start_rock_y][start_rock_x + new_i] = '#'

    def make_floor(self):
        for idx, _ in enumerate(self.matrix[self.lowest_floor + 2]):
            self.matrix[self.lowest_floor + 2][idx] = '#'


def drop_sands(cave, cycles=100):
    for i in range(0, cycles):
        falling = cave.drop_sand()
        if falling:
            return i
    return i


def draw_rocks(cave, rock_data):
    for rock_formation in rock_data:
        cave.add_rock(rock_formation)


rd = [d.strip() for d in get_data()]
c = Cave((1000, 300), (500, 0))
draw_rocks(c, rd)
drop_sands(c, 10000)
print(c.sand_count)

# part 2
c = Cave((700, 170), (500, 0))
draw_rocks(c, rd)
c.make_floor()
sand_count = drop_sands(c, 100000)
c.print_matrix()
print(c.sand_count)