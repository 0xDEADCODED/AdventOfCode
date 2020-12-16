
def process(lines):
    # Ticket Field rules
    rules = {}
    for f in lines[0]:
        field, r = [x.strip() for x in f.split(':')]
        r = r.split(' or ')
        ranges = []
        for r1 in r:
            l,h = [int(x) for x in r1.split('-')]
            ranges += list(range(l,h+1))

        rules[field] = ranges

    # Our ticket
    ticket = [int(x) for x in lines[1][1].split(',')]

    # Nearby tickets
    nearby = []
    for z in [x for x in [y.split(',') for y in lines[2][1:]]]:
        nearby.append([int(y) for y in z])

    return rules,ticket,nearby

def calculate():
    lines = [line.split('\n') for line in open('./input.txt','r').read().split('\n\n')]
    
    rules,mine,nearby = process(lines)

    error = 0
    chain = [item for sublist in list(rules.values()) for item in sublist]
    vt = []
    for ticket in nearby:
        valid  = True
        for num in ticket:
            if num not in chain:
                error += num
                valid = False
                break
        if valid:
            vt.append(ticket)

    print(f"Part 1: {error}")

    columns = []
    for i, k in enumerate(rules):
        columns.append([x[i] for x in vt])

    mapped = {}
    prod = 1
    while len(list(mapped.keys())) < len(mine):
        for i,c in enumerate(columns):
            match = []
            for k in rules.keys():
                if all(x in rules[k] for x in c) and k not in mapped:
                    match.append(k)
            if len(match) == 1:
                mapped[match[0]] = i
                if 'departure' in match[0]:
                    prod *= mine[i]

    print(f"Part 2: {prod}")


if __name__ == '__main__':
    calculate()