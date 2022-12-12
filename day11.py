def get_data():
    with open("day11_input.txt", "r") as f:
        lines = f.readlines()
    return lines


class Monkey:

    def __init__(self, name, items, operation, test, relationship, worry_reducer):
        self.name = name
        self.items = items
        self.operation = operation
        self.relationship = relationship
        self.inspect_count = 0
        self.divide_test = test
        self.worry_reducer = worry_reducer
        self.super_mod = 1
        self.function = self.parse_operation()

    def parse_operation(self):
        operation = self.operation[self.operation.find('= ')+2:]
        return lambda old: eval(operation)

    def inspect(self):
        return_list = []
        for idx, item in enumerate(self.items):
            self.inspect_count += 1
            print(f'Monkey {self.name} inspects item with worry level {item}')
            worry_level = self.function(int(item))
            worry_level = int(worry_level / 3) if self.worry_reducer else worry_level % self.super_mod
            divisible = worry_level % self.divide_test == 0
            return_list.append((divisible, worry_level))
        self.items = [i for _, i in return_list]
        return return_list

    def throw(self):
        print(f'Monkey {self.name} throws {self.items[0]}')
        return self.items.pop(0)

    def catch(self, item):
        print(f'Monkey {self.name} catches {item}')
        self.items.append(item)


def make_monkeys(monkey_data, worry_reducer=True):
    monkeys = []
    for idx, monkey_datum in enumerate(monkey_data):
        if 'Monkey' in monkey_datum:
            name = monkey_datum[monkey_datum.find(' ')+1:].strip(':')
            items = monkey_data[idx + 1]
            clean_items = [int(n) for n in items[items.find(': ') + 2:].split(',')]
            operation = monkey_data[idx + 2]
            test = monkey_data[idx + 3].split(' ')
            test = int(test[len(test)-1])
            true_relationship, false_relationship = monkey_data[idx + 4], monkey_data[idx + 5]
            true_relationship = true_relationship[true_relationship.find('key ') + 4:]
            false_relationship = false_relationship[false_relationship.find('key ') + 4:]
            relationship = {True: true_relationship, False: false_relationship}
            monkey = Monkey(name=name, items=clean_items, operation=operation, test=test, relationship=relationship, worry_reducer=worry_reducer)
            monkeys.append(monkey)
    return monkeys


def monkey_business(monkeys, rounds):
    for i in range(0, rounds):
        print(f'Round {i + 1}')
        for monkey in monkeys:
            monkey_inspected_items = monkey.inspect()
            for divisible, item in monkey_inspected_items:
                toss_to = monkey.relationship[divisible]
                catch_monkey = [m for m in monkeys if m.name == toss_to][0]
                catch_monkey.catch(monkey.throw())


def apply_mod(monkeys):
    super_mod = 1
    for m in monkeys:
        super_mod *= m.divide_test
    for m in monkeys:
        m.super_mod = super_mod

# pt 1
monkey_data = [d.strip() for d in get_data()]
monkeys = make_monkeys(monkey_data, True)
monkey_business(monkeys, 20)
monkeys.sort(key=lambda m: -m.inspect_count)
total = monkeys[0].inspect_count * monkeys[1].inspect_count
print(f'part1: {total}')

# pt 2
monkeys = make_monkeys(monkey_data, False)
apply_mod(monkeys)
monkey_business(monkeys, 10000)
monkeys.sort(key=lambda m: -m.inspect_count)
total = monkeys[0].inspect_count * monkeys[1].inspect_count
print(f'part2: {total}')
