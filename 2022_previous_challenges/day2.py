
my_rps_dict = {
    'X': 'Rock',
    'Y': 'Paper',
    'Z': 'Scissors'
}

opponent_rps_dict = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors'
}

result_dict = {
    'Rock': {'Scissors': 'Win', 'Paper': 'Loss', 'Rock': 'Draw'},
    'Paper': {'Scissors': 'Loss', 'Paper': 'Draw', 'Rock': 'Win'},
    'Scissors': {'Scissors': 'Draw', 'Paper': 'Win', 'Rock': 'Loss'}
}

shape_points = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3
}

outcome_points = {
    'Loss': 0,
    'Draw': 3,
    'Win': 6
}

def get_data():
    with open("day2input.txt", "r") as f:
        lines = f.readlines()
    return lines

def convert_data(raw_data):
    new_data = []
    for line in raw_data:
        line_items = line.replace('\n', '').split(' ')
        converted_data = [opponent_rps_dict[line_items[0]], my_rps_dict[line_items[1]]]
        new_data.append(converted_data)
    return new_data

def get_my_total_score(games):
    my_score = 0
    for game in games:
        opponent_plays, i_play = game
        my_result = result_dict[i_play][opponent_plays]
        # print(f'I play {i_play} and he plays {opponent_plays}: {my_result}')
        result_score = outcome_points[my_result]
        play_score = shape_points[i_play]
        my_score += (result_score + play_score)
    return my_score


raw_data = get_data()
games = convert_data(raw_data)
score = get_my_total_score(games)
print()