

def get_data():
    with open("day4_input.txt", "r") as f:
        lines = f.readlines()
    return lines

def convert_section_to_list(sections):
    sections_list = [int(a) for a in sections.split('-')]
    return_list = []
    for section_number in range(sections_list[0], sections_list[1]+1):
        return_list.append(section_number)
    return return_list

def does_list_encompass_list(list_a, list_b):
    return_val = True
    for i in list_a:
        if i not in list_b:
            return_val = False
            break
    return return_val

def does_list_overlap_at_all(list_a, list_b):
    return_val = False
    for i in list_a:
        if i in list_b:
            return_val = True
            break
    return return_val

def get_encompassed_overlapped(section_assignments):
    total_encompassed_list, total_overlapped = 0, 0
    for pair in section_assignments:
        cleaned_pair = pair.strip('\n')
        sectionsA, sectionsB = cleaned_pair.split(',')
        sectionA_list = convert_section_to_list(sectionsA)
        sectionB_list = convert_section_to_list(sectionsB)
        encompassB = does_list_encompass_list(sectionA_list, sectionB_list)
        encompassA = does_list_encompass_list(sectionB_list, sectionA_list)
        if encompassA or encompassB:
            total_encompassed_list += 1
        is_overlapped = does_list_overlap_at_all(sectionA_list, sectionB_list)
        if is_overlapped:
            total_overlapped += 1

    return total_encompassed_list, total_overlapped

# section_assignments = get_data()
# total_encompassed, total_overlapped = get_encompassed_overlapped(section_assignments)
# print(f'Total encompassed {total_encompassed}')
# print(f'Total overlapped {total_overlapped}')

