import copy as c
import collections

def get_data():
    with open("day12_input.txt", "r") as f:
        lines = f.readlines()
    return lines

maze = [[]]

def make_maze(raw_data):
    start_position, end_position = [], {}
    maze_matrix = []
    for vertical_idx, line in enumerate(raw_data):
        horiz_list = []
        for horizantal_idx, height in enumerate(line):
            if height == 'S':
                start_position.append({'x': horizantal_idx, 'y': vertical_idx})
                horiz_list.append(1)
            elif height == 'E':
                end_position = {'x': horizantal_idx, 'y': vertical_idx}
                horiz_list.append(26)
            elif height == 'a':
                start_position.append({'x': horizantal_idx, 'y': vertical_idx})
                horiz_list.append(ord(height)-96)
            else:
                horiz_list.append(ord(height) - 96)
        maze_matrix.append(horiz_list)
    return maze_matrix, start_position, end_position

def crawl_maze(start_position, end_position):
    queue = collections.deque()
    start_position.update()
    steps = 0
    queue.append((start_position['x'], start_position['y'], steps))
    seen_item = (start_position['x'], start_position['y'])
    seen = {seen_item}
    while queue:
        path = queue.popleft()
        x, y, steps = path[0], path[1], path[2]
        if x == end_position['x'] and y == end_position['y']:
            return x, y, steps
        height = maze[y][x]
        for nextx, nexty in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            in_bounds = nextx >= 0 and nextx < len(maze[0]) and nexty >=0 and nexty < len(maze)
            if in_bounds:
                flat_enough = (maze[nexty][nextx] - height) < 2
                not_seen = (nextx, nexty) not in seen
                if flat_enough and not_seen:
                    queue.append((nextx, nexty, steps + 1))
                    seen.add((nextx, nexty))
    return None




raw_data = [l.strip() for l in get_data()]
maze, start_positions, end_position = make_maze(raw_data)
paths = []
for start_position in start_positions:
    path = crawl_maze(start_position, end_position)
    if path:
        paths.append(path)
paths.sort(key=lambda x: x[2])
print(paths[0])