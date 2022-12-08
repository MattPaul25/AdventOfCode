def get_data():
    with open("day7_input.txt", "r") as f:
        lines = f.readlines()
    return lines




def create_directory_tree(commands, starting_index=0):
    current_directory = {}
    i = starting_index
    while i < len(commands):
        command = commands[i]
        if '..' in command:
            return current_directory, i
        elif '$ cd ' in command:
            directory_name = command[command.find('cd ') + 3:]
            new_directory, i = create_directory_tree(commands, i + 1)
            if directory_name in current_directory:
                current_directory[directory_name].update(new_directory)
            else:
                current_directory.update({directory_name: new_directory})
            i += 1
        elif '$ ls' in command:
            i += 1
            continue
        elif 'dir' in command:
            current_directory.update({command[command.find(' ')+1:]: {}})
            i += 1
        else:
            file_name = command[command.find(' ') + 1:]
            bites = command[:command.find(' ')]
            current_directory.update({file_name: bites})
            i += 1
    return current_directory, i

def list_directories(parent_directory, name='/'):
    directory_list = []
    sum = 0
    current_directory = {name: 0}
    for item_name, item_value in parent_directory.items():
        if type(item_value) == dict:
            new_directory_list, directory_sum = list_directories(item_value, item_name)
            for dir in new_directory_list:
                directory_list.append(dir)
            sum += directory_sum
        else:
            sum += int(item_value)
    current_directory[name] = sum
    directory_list.append(current_directory)
    return directory_list, sum


def get_sum_of_values_under(list, value):
    total = 0
    dir_list = []
    for item in list:
        for k, v in item.items():
            new_dir = {'dir_name': k, 'dir_val': v}
            if v < value:
                total += v
            dir_list.append(new_dir)
    return total, dir_list

def smallest_dir_over_space_needed(dir_list, space_needed):
    dir_list.sort(key=lambda x: x['dir_val'])
    for dir in dir_list:
        if dir['dir_val'] > space_needed:
            return dir
    return


commands = get_data()
commands = [line.strip('\n') for line in commands]
directory, i = create_directory_tree(commands)
list_directories, sum = list_directories(directory)
total, dir_list = get_sum_of_values_under(list_directories, 100000)
space_being_used = [i for i in dir_list if i['dir_name'] == '/']
space_left_over = 70000000 - space_being_used[0]['dir_val']
space_needed = 30000000 - space_left_over
smallest_dir = smallest_dir_over_space_needed(dir_list, space_needed)


print()