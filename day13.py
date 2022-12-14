import functools, math

def get_data():
    with open("day13_input.txt", "r") as f:
        lines = f.readlines()
    return lines

def clean_data(raw_data):
    packet_dict, packet_list = {}, []
    for idx, _ in enumerate(raw_data):
        if 0 < idx and (idx + 1) % 2 == 0:
            packet_dict.update({int((idx + 1) / 2): {'l': eval(raw_data[idx - 1]), 'r': eval(raw_data[idx])}})
            packet_list.extend([ eval(raw_data[idx - 1]), eval(raw_data[idx])])

    return packet_dict, packet_list

def compare_packet_lists(left_packet, right_packet):
    for left_item, right_item in zip(left_packet, right_packet):
        if type(left_item) == int and type(right_item) == int:
            if left_item > right_item:
                return False
            elif left_item == right_item:
                continue
            elif left_item < right_item:
                return True
        if type(left_item) == list and type(right_item) == list:
            outcome = compare_packet_lists(left_item, right_item)
            if outcome in [True, False]:
                return outcome
            continue
        if type(left_item) == list and type(right_item) == int:
            outcome = compare_packet_lists(left_item, [right_item])
            if outcome in [True, False]:
                return outcome
            continue
        if type(left_item) == int and type(right_item) == list:
            outcome = compare_packet_lists([left_item], right_item)
            if outcome in [True, False]:
                return outcome
            continue
    if len(left_packet) < len(right_packet):
        return True
    elif len(left_packet) > len(right_packet):
        return False
    else:
        return None


def compare(left_packet, right_packet):
    for left_item, right_item in zip(left_packet, right_packet):
        if type(left_item) == int and type(right_item) == int:
            if left_item > right_item:
                return 1
            elif left_item == right_item:
                continue
            elif left_item < right_item:
                return -1
        if type(left_item) == list and type(right_item) == list:
            outcome = compare_packet_lists(left_item, right_item)
            if outcome == True:
                return -1
            elif outcome == False:
                return 1
            continue
        if type(left_item) == list and type(right_item) == int:
            outcome = compare_packet_lists(left_item, [right_item])
            if outcome == True:
                return -1
            elif outcome == False:
                return 1
            continue
        if type(left_item) == int and type(right_item) == list:
            outcome = compare_packet_lists([left_item], right_item)
            if outcome == True:
                return -1
            elif outcome == False:
                return 1
            continue
    if len(left_packet) < len(right_packet):
        return -1
    elif len(left_packet) > len(right_packet):
        return 1
    else:
        return 0

def compare_packet_dict(packets):
    current_sum = 0
    for i in range(1, len(packets) + 1):
        l_packet, r_packet = packets[i]['l'], packets[i]['r']
        packets_in_order = compare_packet_lists(l_packet, r_packet)
        packets_in_order = packets_in_order in [None, True]
        current_sum += i if packets_in_order else 0
    return current_sum

raw_data = [d.strip() for d in get_data() if d != '\n']
packets, packet_list = clean_data(raw_data)
total = compare_packet_dict(packets)
print(f'pt 1 total: {total}')

packet_list.extend([[[6]], [[2]]])

new_list = sorted(packet_list, key=functools.cmp_to_key(compare))
indexes = [idx + 1 for idx, i in enumerate(new_list) if i == [[6]] or i == [[2]]]
mult = indexes[0] * indexes[1]
print(f'pt 2 total: {mult}')
