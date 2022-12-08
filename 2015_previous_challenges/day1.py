def get_data():
    with open("day1_input.txt", "r") as f:
        lines = f.readlines()
    return lines

def get_final_floor(floor_data):
    current_floor = 0
    floor_translator = {
        '(': 1,
        ')': -1
    }
    for floor_move in floor_data:
        current_floor += floor_translator[floor_move]
    return current_floor

def get_basement_floor_move(floor_data):
    current_floor = 0
    floor_translator = {
        '(': 1,
        ')': -1
    }
    for idx, floor_move in enumerate(floor_data):
        current_floor += floor_translator[floor_move]
        if current_floor == -1:
            return idx + 1
    return

floor_data = get_data()[0]
floor = get_final_floor(floor_data)
move_of_basement_floor = get_basement_floor_move(floor_data)
print(move_of_basement_floor)
print()