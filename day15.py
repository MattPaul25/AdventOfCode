
def get_data():
    with open("day15_input.txt", "r") as f:
        lines = f.readlines()
    return lines


class Sensor:

    def __init__(self, location, nearest_beacon):
        self.location = location
        self.beacon = nearest_beacon
        self.beacon_distance = self.get_beacon_distance()
        self.coverage_square = self.get_coverage_square()

    def get_beacon_distance(self):
        distance = abs(self.beacon[0] - self.location[0]) + abs(self.beacon[1] - self.location[1])
        return distance

    def get_coverage_square(self):
        coverage_square = {
            'l': (self.location[0] - self.beacon_distance, self.location[1]),
            'r': (self.location[0] + self.beacon_distance, self.location[1]),
            'u': (self.location[0], self.location[1] - self.beacon_distance),
            'd': (self.location[0], self.location[1] - self.beacon_distance)
        }
        return coverage_square


class AllSquares:

    def __init__(self, sensors):
        self.squares = sensors

    def check_item_against_squares(self, location):
        for sqr in self.squares:
            distance = abs(location[0] - sqr.location[0]) + abs(location[1] - sqr.location[1])
            if distance <= sqr.beacon_distance:
                return True
        return False

def get_blocked_locations_on_line(sensors, line_number):
    block_locations_on_line = set()
    beacon_locations_on_line = set()
    for s in sensors:
        if s.beacon[1] == line_number:
            beacon_locations_on_line.add((s.beacon[0], s.beacon[1]))
    for s in sensors:
        distance_from_line = s.location[1] - line_number
        distance_over_line = s.beacon_distance - abs(distance_from_line)
        if distance_over_line >= 0:
            start_location = (s.location[0] - abs(distance_over_line), line_number)
            end_location = (s.location[0] + abs(distance_over_line), line_number)
            while start_location[0] <= end_location[0]:
                if start_location not in beacon_locations_on_line:
                    block_locations_on_line.add(start_location)
                start_location = (start_location[0] + 1, line_number)

    return block_locations_on_line


def make_sensors(sensor_data):
    sensors = []
    for sensor in sensor_data:
        sensor, beacon = sensor.split(':')
        sensor_x, sensor_y = sensor.split(',')
        sensor_x = int(sensor_x[sensor_x.find('x=')+2:])
        sensor_y = int(sensor_y[sensor_y.find('y=')+2:])
        beacon_x, beacon_y = beacon.split(',')
        beacon_x = int(beacon_x[beacon_x.find('x=')+2:])
        beacon_y = int(beacon_y[beacon_y.find('y=') + 2:])
        s = Sensor([sensor_x, sensor_y], [beacon_x, beacon_y])
        sensors.append(s)
    return sensors


def out_dimensions(point):
    sq_dimensions = (0, 4000000)
    out_x_dimension = point[0] < sq_dimensions[0] or point[0] > sq_dimensions[1]
    out_y_dimension = point[1] < sq_dimensions[0] or point[1] > sq_dimensions[1]
    return out_x_dimension or out_y_dimension


def walk_border(move_point, comp_point, comp_func, adj_func, move_func):
    while comp_func(move_point, comp_point):
        adjacent_point = adj_func(move_point)
        outside_dimensions = out_dimensions(adjacent_point)
        if outside_dimensions:
            move_point = move_func(move_point)
            continue
        in_other_squares = sqrs.check_item_against_squares(adjacent_point)
        if not in_other_squares:
            return True, adjacent_point
        if move_point == comp_point:
            break
        move_point = move_func(move_point)
    return False, (0, 0)


def walk_borders(sqrs):
    for idx, sq in enumerate(sqrs.squares):
        print(f'Walking Square {idx}: dims: {sq.coverage_square}')
        move_guide = [
            {'name': 'upright', 'comp_func': lambda x, y: x[1] >= y[1], 'from_point': sq.coverage_square['l'], 'to_point': sq.coverage_square['u'], 'func': lambda x: (x[0] + 1, x[1] - 1), 'adj_func': lambda x: (x[0] - 1, x[1])},
            {'name': 'downright', 'comp_func': lambda x, y: x[0] <= y[0], 'from_point': sq.coverage_square['u'], 'to_point': sq.coverage_square['r'], 'func': lambda x: (x[0] + 1, x[1] + 1), 'adj_func': lambda x: (x[0] + 1, x[1])},
            {'name': 'downleft', 'comp_func': lambda x, y: x[1] <= y[1], 'from_point': sq.coverage_square['r'], 'to_point': sq.coverage_square['d'], 'func': lambda x: (x[0] - 1, x[1] + 1), 'adj_func': lambda x: (x[0] + 1, x[1])},
            {'name': 'upleft', 'comp_func': lambda x, y: x[0] <= y[0], 'from_point':  sq.coverage_square['d'], 'to_point': sq.coverage_square['l'], 'func': lambda x: (x[0] - 1, x[1] - 1), 'adj_func': lambda x: (x[0] - 1, x[1])}
        ]
        for move in move_guide:
            found = walk_border(move['from_point'], move['to_point'], move['comp_func'], move['adj_func'], move['func'])
            if found[0]:
                return found[1]
    return 0, 0


# ingest data
rd = [d.strip() for d in get_data()]

# part 1 ------
sensors = make_sensors(rd)
line = 2000000
x = get_blocked_locations_on_line(sensors, line)
print(f'part 1 blocked locations on line {line}: {len(x)}')

# part 2 ------- not optimized
sqrs = AllSquares(sensors)
found_guy = walk_borders(sqrs)
frequency = (found_guy[0] * 4000000) + found_guy[1]
print(f'part 2 found frequency {frequency}')
