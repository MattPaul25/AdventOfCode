from previous_challenges.day3_data import priorities

def get_data():
    with open("day3input.txt", "r") as f:
        lines = f.readlines()
    return lines

def clean_and_split_sacks(rucksacks):
    reformatted_rucksacks = []
    cleaned_rucksacks = []
    for rucksack in rucksacks:
        rucksack = rucksack.replace('\n', '')
        half_point = int(len(rucksack) / 2)
        reformatted_rucksack = {
            'compartment_a': rucksack[:half_point],
            'compartment_b': rucksack[half_point:]
        }
        reformatted_rucksacks.append(reformatted_rucksack)
        cleaned_rucksacks.append(rucksack)
    return reformatted_rucksacks, cleaned_rucksacks

def compare_compartments(rucksacks):
    my_count = 0
    for rucksack in rucksacks:
        similar_items = {}
        intersect = set(rucksack['compartment_a']).intersection(set(rucksack['compartment_b']))
        for item in intersect:
            similar_items.update({item: priorities[item]})
        total = sum(similar_items.values())
        my_count += total
    return my_count

def split_bags_into_groups(rucksacks):
    rucksack_group, rucksacks_grouped = [], []
    group_counter = 0
    for rucksack in rucksacks:
        rucksack_group.append(rucksack)
        group_counter += 1
        if group_counter == 3:
            rucksacks_grouped.append(rucksack_group)
            rucksack_group = []
            group_counter = 0
    return rucksacks_grouped

def get_rucksacks_badge_total(rucksacks_grouped):
    badge_total = 0
    for rucksack_group in rucksacks_grouped:
        common_items = set(rucksack_group[0]).intersection(rucksack_group[1])
        for c in rucksack_group[2]:
            if c in common_items:
                badge_total += priorities[c]
                break
    return badge_total



# part 1
rucksacks = get_data()
reformatted_rucksacks, rucksacks = clean_and_split_sacks(rucksacks)
total_count = compare_compartments(reformatted_rucksacks)
print(total_count)


#part 2
rucksacks_grouped = split_bags_into_groups(rucksacks)
badge_total = get_rucksacks_badge_total(rucksacks_grouped)
print(badge_total)