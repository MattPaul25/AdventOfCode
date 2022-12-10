def get_data():
    with open("day10_input.txt", "r") as f:
        lines = f.readlines()
    return lines

def run_cycles(instructions):
    x, idx = 1, 0
    cycle_numbers = {
        20: 0,
        60: 0,
        100: 0,
        140: 0,
        180: 0,
        220: 0
    }
    for instruction in instructions:
        idx += 1
        if idx in cycle_numbers:
            cycle_numbers[idx] = idx * x
        if 'addx' in instruction:
            idx += 1
            if idx in cycle_numbers:
                cycle_numbers[idx] = idx * x
            x += int(instruction[instruction.find(' ')+1:])

    return cycle_numbers

def print_lines(lines):
    for line in lines:
        print(line)

def draw_pixels(instructions):
    horiz_idx, register_x = 0, 1
    line, lines = '', []
    for instruction in instructions:
        replace_char = ' ' if horiz_idx not in [register_x - 1, register_x, register_x + 1] else '#'
        line = line[:horiz_idx] + replace_char + line[horiz_idx + 1:]
        horiz_idx += 1
        if len(line) == 40:
            lines.append(line)
            horiz_idx = 0
            line = ''
        if 'noop' not in instruction:
            replace_char = ' ' if horiz_idx not in [register_x - 1, register_x, register_x + 1] else '#'
            line = line[:horiz_idx] + replace_char + line[horiz_idx + 1:]
            command, sprite_placement = instruction.split(' ')
            register_x += int(sprite_placement)
            horiz_idx += 1
            new_line = len(line) == 40
            if new_line:
                lines.append(line)
                horiz_idx = 0
                line = ''
    return lines


instructions = [d.strip() for d in get_data()]
numbers = run_cycles(instructions)
total = sum([v for k, v in numbers.items()])
lines = draw_pixels(instructions)
print_lines(lines)

print()