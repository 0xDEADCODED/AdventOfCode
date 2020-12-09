
def find_bad_num(numbers):
    prei = 0
    i = 25
    while i < len(numbers):
        preamble = numbers[prei:i]
        curr = numbers[i]
        found = False
        for x in preamble:
            for y in preamble:
                if x != y and x + y == curr:
                    found = True
                    continue
        if not found:
            return curr

        prei += 1
        i += 1

def find_weakness(preamble, bad_num):
    for j in range(len(preamble)):
        acc = 0
        cont = []
        for i in range(j, len(preamble)):
            if acc == bad_num:
                cont.sort()
                return cont[0] + cont[-1]
            elif acc > bad_num:
                break

            cont.append(preamble[i])
            acc += preamble[i]

def calculate():
    numbers = []
    with open('./input.txt', 'r') as fp:
        numbers = [int(line.strip().replace('\n','')) for line in fp.readlines()]

    part1 = find_bad_num(numbers)
    print(f"Part 1: {part1}")

    part2 = find_weakness(numbers, part1)
    print(f"Part 2: {part2}")


if __name__ == '__main__':
    calculate()