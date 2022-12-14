def get_data():
    with open("day14_input.txt", "r") as f:
        lines = f.readlines()
    return lines

rd = [d.strip() for d in get_data()]
print(rd)