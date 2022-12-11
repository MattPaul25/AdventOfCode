def get_data():
    with open("day11_input.txt", "r") as f:
        lines = f.readlines()
    return lines


class Monkey:

    def __init__(self, name, items, operation, test):
        self.name = name
        self.items = items
        self.operation = operation
        self.inspect_count = 0
        self.divide_test = test
        self.super_mod = 1
        self.function = self.parse_operation()

    def parse_operation(self):
        if 'old * old' in self.operation:
            return lambda x: x * x
        elif '*' in self.operation:
            number = self.operation[self.operation.find('* ') + 2:]
            return lambda x: x * int(number)
        elif '+' in self.operation:
            number = self.operation[self.operation.find('+ ') + 2:]
            return lambda x: x + int(number)

    def inspect(self, item):
        # print(f'Monkey {self.name} inspects item {item}')
        worry_level = self.function(int(item))
        divisible = worry_level % self.divide_test == 0
        worry_level = worry_level % self.super_mod
        self.inspect_count += 1
        return divisible, worry_level

    def throw(self, item, catch_monkey):
        # print(f'Monkey {self.name} throws {item} to {catch_monkey.name}')
        self.items.pop(0)
        catch_monkey.catch(item)

    def catch(self, item):
        # print(f'Monkey {self.name} catches {item}')
        self.items.append(item)


def make_monkeys(monkey_data):
    monkeys, relationships = [], {}
    for idx, monkey_datum in enumerate(monkey_data):
        if 'Monkey' in monkey_datum:
            name = monkey_datum[monkey_datum.find(' ')+1:].strip(':')
            items = monkey_data[idx + 1]
            clean_items = [int(n) for n in items[items.find(': ') + 2:].split(',')]
            operation = monkey_data[idx + 2]
            test = monkey_data[idx + 3].split(' ')
            test = int(test[len(test)-1])
            monkey = Monkey(name=name, items=clean_items, operation=operation, test=test)
            monkeys.append(monkey)
            true_relationship, false_relationship = monkey_data[idx + 4], monkey_data[idx + 5]
            true_relationship = true_relationship[true_relationship.find('key ') + 4:]
            false_relationship = false_relationship[false_relationship.find('key ') + 4:]
            relationships.update({name: {True: true_relationship, False: false_relationship}})
    return monkeys, relationships


def monkey_business(monkeys, relationships, rounds):
    for i in range(0, rounds):
        print(f'Round {i + 1}')
        for monkey in monkeys:
            while len(monkey.items) > 0:
                divisible, item = monkey.inspect(monkey.items[0])
                toss_to = relationships[monkey.name][divisible]
                catch_monkey = [m for m in monkeys if m.name == toss_to][0]
                monkey.throw(item, catch_monkey)
    return monkeys


def apply_mod(monkeys):
    super_mod = 1
    for m in monkeys:
        super_mod *= m.divide_test
    for m in monkeys:
        m.super_mod = super_mod


monkey_data = [d.strip() for d in get_data()]
monkeys, relationships = make_monkeys(monkey_data)
apply_mod(monkeys)
monkeys = monkey_business(monkeys, relationships, 10000)
monkeys.sort(key=lambda m: -m.inspect_count)
total = monkeys[0].inspect_count * monkeys[1].inspect_count
print(total)