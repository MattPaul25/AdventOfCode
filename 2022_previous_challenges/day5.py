stack_dict = {}

def get_data():
    with open("day5_input.txt", "r") as f:
        lines = f.readlines()
    return lines

def clean_data(raw_instructions):
    return_instructions, start_data = [], []
    past_new_line = False
    separation_mark = '\n'
    for instruction in raw_instructions:
        new_instruction = instruction.replace(separation_mark, '')
        if past_new_line:
            return_instructions.append(new_instruction)
        elif new_instruction != '':
            start_data.append(new_instruction)
        if new_instruction == '':
            past_new_line = True
    return return_instructions, start_data

def update_crates(move_amount, from_crate, to_crate):
    for i in range(0, move_amount):
        x = stack_dict[str(from_crate)].pop(0)
        stack_dict[str(to_crate)].insert(0, x)

def update_crates_in_order(move_amount, from_crate, to_crate):
    movables = stack_dict[str(from_crate)][:move_amount]
    stack_dict[str(from_crate)] = stack_dict[str(from_crate)][len(movables):]
    stack_dict[str(to_crate)][:0] = movables

def move_crates(instructions):
    find_from_word = 'from'
    find_to_word = 'to'
    for instruction in instructions:
        move_amount = int(instruction[5:instruction.find(find_from_word)-1])
        from_crate = int(instruction[instruction.find(find_from_word) + len(find_from_word): instruction.find(find_to_word)])
        to_crate = int(instruction[instruction.find(find_to_word) + len(find_to_word):])
        update_crates_in_order(move_amount, from_crate, to_crate)

def print_top_crates():
    top_piece = ''
    keys = list(stack_dict.keys())
    keys.sort()
    for stack_key in keys:
        top_piece += (stack_dict[stack_key][0])
    return top_piece

def create_character_positions(start_data):
    character_position_set = []
    for sd in start_data:
        next_char_is_it = False
        character_index = 0
        character_positions = {}
        for char in sd:
            if next_char_is_it:
                character_positions.update({character_index: char})
            if char == '[':
                next_char_is_it = True
            else:
                next_char_is_it = False
            character_index += 1
        if character_positions != {}:
            character_position_set.append(character_positions)
    return character_position_set

def reorganize_character_positions(character_position_set):
    return_stack = {}
    for character_positions in character_position_set:
        for k, v in character_positions.items():
            position = str(int(((k - 1)/4) + 1))
            if position not in return_stack:
                return_stack.update({position: [v]})
            else:
                return_stack[position].append(v)
    return return_stack


raw_data = get_data()
instructions, start_data = clean_data(raw_data)
character_position_set = create_character_positions(start_data)
stack_dict = reorganize_character_positions(character_position_set)
move_crates(instructions)
top_piece = print_top_crates()
print(top_piece)