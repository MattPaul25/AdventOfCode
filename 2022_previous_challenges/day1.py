
def count_calories():
    max_cals = -1
    sums = []
    with open("day1input.txt", "r") as f:
        lines = f.readlines()
        current_elf_sum = 0
        for line in lines:
            if line == "\n":
                sums.append(current_elf_sum)
                current_elf_sum = 0
            else:
                cals = int(line)
                current_elf_sum += cals
    sums.sort()
    top3 = sum(sums[len(sums)-3:])
    print(top3)


count_calories()