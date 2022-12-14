def get_data():
    with open("day8_input.txt", "r") as f:
        lines = f.readlines()
    return lines


def count_visible_trees(tree_grid):
    visible_tree_count = ((len(tree_grid) * 2) + (len(tree_grid[0]) * 2))-4
    for verticle_idx, tree_line in enumerate(tree_grid):
        outer_tree = verticle_idx == 0 or verticle_idx == (len(tree_grid)-1)
        if outer_tree:
            continue
        tree_line_list = list(tree_line)
        for horizontal_idx, tree_height in enumerate(tree_line_list):
            outer_tree = horizontal_idx == 0 or horizontal_idx == (len(tree_line_list)-1)
            if outer_tree:
                continue
            west_max = max(tree_line_list[:horizontal_idx])
            viewable_from_west = west_max < tree_height
            if viewable_from_west:
                visible_tree_count += 1
                continue
            east_max = max(tree_line_list[horizontal_idx + 1:])
            viewable_from_east = east_max < tree_height
            if viewable_from_east:
                visible_tree_count += 1
                continue
            south_trees = [t[horizontal_idx] for t in tree_grid[verticle_idx + 1:]]
            south_max = max(south_trees)
            viewable_from_south = south_max < tree_height
            if viewable_from_south:
                visible_tree_count += 1
                continue
            north_trees = [t[horizontal_idx] for t in tree_grid[:verticle_idx]]
            north_max = max(north_trees)
            viewable_from_north = north_max < tree_height
            if viewable_from_north:
                visible_tree_count += 1
                continue
    return visible_tree_count

def get_score(tree_line, tree):
    idx = 0
    for idx, t in enumerate(tree_line):
        if t >= tree:
            return idx + 1
    return idx + 1

def calculate_highest_tree_score(tree_grid):
    max_score = 0
    for verticle_idx, tree_line in enumerate(tree_grid):
        outer_tree = verticle_idx == 0 or verticle_idx == (len(tree_grid)-1)
        if outer_tree:
            continue
        tree_line_list = list(tree_line)
        for horizontal_idx, tree_height in enumerate(tree_line_list):
            outer_tree = horizontal_idx == 0 or horizontal_idx == (len(tree_line_list) - 1)
            if outer_tree:
                continue
            west_trees = tree_line_list[:horizontal_idx]
            west_trees.reverse()
            west_score = get_score(west_trees, tree_height)

            east_trees = tree_line_list[horizontal_idx + 1:]
            east_score = get_score(east_trees, tree_height)

            south_trees = [t[horizontal_idx] for t in tree_grid[verticle_idx + 1:]]
            south_score = get_score(south_trees, tree_height)

            north_trees = [t[horizontal_idx] for t in tree_grid[:verticle_idx]]
            north_trees.reverse()
            north_score = get_score(north_trees, tree_height)
            score = west_score * south_score * east_score * north_score
            max_score = score if score > max_score else max_score
    return max_score



tree_grid = get_data()
tree_grid = [tl.strip('\n') for tl in tree_grid]
tree_count = count_visible_trees(tree_grid)
calculate_highest_tree_score(tree_grid)