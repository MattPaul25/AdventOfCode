def get_data():
    with open("day6_input.txt", "r") as f:
        lines = f.readlines()
    return lines

def find_buffer_bytes(message, buffer_length):
    for idx, char in enumerate(message):
        potential_buffer = message[idx:idx + buffer_length]
        data = set([letter for letter in potential_buffer])
        if len(data) == buffer_length:
            return idx + buffer_length
    return len(message)

message = get_data()[0]
buffer_size = find_buffer_bytes(message, 4)
message_start = find_buffer_bytes(message, 14)
print(buffer_size)
print(message_start)
print('test')