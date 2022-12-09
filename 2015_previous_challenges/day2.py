def get_data():
    with open("day2_input.txt", "r") as f:
        lines = f.readlines()
    return lines

def calculate_paper(dimensions):
    total_paper = 0
    for d in dimensions:
        l, w, h = d.split('x')
        smallest = [l, w, h]
        smallest.sort()
        total_paper += ((2 * int(l) * int(w)) + (2 * int(w) * int(h)) + (2 * int(h) * int(l))) + (int(smallest[0]) * int(smallest[1]))
    return total_paper

dimensions = [d.strip() for d in get_data()]
tp = calculate_paper(dimensions)
print(tp)