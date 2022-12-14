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
            packet_list.extend([eval(raw_data[idx - 1]), eval(raw_data[idx])])

    return packet_dict, packet_list


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
            outcome = compare(left_item, right_item)
            if outcome == 0:
                continue
            else:
                return outcome
        if type(left_item) == list and type(right_item) == int:
            outcome = compare(left_item, [right_item])
            if outcome == 0:
                continue
            else:
                return outcome
        if type(left_item) == int and type(right_item) == list:
            outcome = compare([left_item], right_item)
            if outcome == 0:
                continue
            else:
                return outcome
    if len(left_packet) < len(right_packet):
        return -1
    elif len(left_packet) > len(right_packet):
        return 1
    return 0

def compare_packet_dict(packets):
    current_sum = 0
    compare_lookup = {
        -1: True,
         0: True,
         1: False
    }
    for i in range(1, len(packets) + 1):
        l_packet, r_packet = packets[i]['l'], packets[i]['r']
        packets_in_order = compare(l_packet, r_packet)

        current_sum += i if compare_lookup[packets_in_order] else 0
    return current_sum

# part 1
raw_data = [d.strip() for d in get_data() if d != '\n']
packets, packet_list = clean_data(raw_data)
total = compare_packet_dict(packets)
print(f'pt 1 total: {total}')

# part 2
packet_list.extend([[[6]], [[2]]])
new_list = sorted(packet_list, key=functools.cmp_to_key(compare))
indexes = [idx + 1 for idx, i in enumerate(new_list) if i == [[6]] or i == [[2]]]
mult = indexes[0] * indexes[1]
print(f'pt 2 total: {mult}')
