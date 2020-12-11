import copy

total = 0

def get_seat(seats, r, s, adj):
        if r >= len(seats) or r < 0 \
            or s >= len(seats[r]) or s < 0 \
            or seats[r][s] == '.':
            return False
        adj.append(seats[r][s])
        return True

def part2_adj(seats, r, s):
    adj = []
    for s1 in [list(reversed(range(s))), list(range(s+1, len(seats[r])))]:
        for n in s1:
            if get_seat(seats, r, n, adj):
                break
    for r1 in [list(reversed(range(r))), list(range(r+1, len(seats)))]:
        si = 0
        left = False
        right  = False
        middle = False
        for n in r1:
            si += 1
            if not left:
                left = get_seat(seats, n, s-si, adj)
            if not right:
                right = get_seat(seats, n, s+si, adj)
            if not middle:
                middle = get_seat(seats, n, s, adj)

    return adj

def part1_adj(seats, r, s):
    adj = []

    for r1 in [r-1, r, r+1]:
        for s1 in [s-1, s, s+1]:
            if r1 == r and s1 == s:
                continue
            get_seat(seats, r1, s1, adj)
    return adj

def modify(seats, tracker, r, s, oc, p1=True):
    if seats[r][s] == '.':
        return 0

    if p1:
        adj = part1_adj(seats, r, s)
    else:
        adj = part2_adj(seats, r, s)

    global total
    if seats[r][s] == 'L' and '#' not in adj:
        tracker[r][s] = '#'
        total += 1
        return 1
    elif seats[r][s] == '#' and adj.count('#') >= oc:
        tracker[r][s] = 'L'
        total -= 1
        return -1
    else:
        return 0

def stabilize(s, oc=4, p1=True):
    seats = copy.deepcopy(s)
    tracker = copy.deepcopy(s)
    while True:
        changed = 0
        for r in range(len(seats)):
            for s in range(len(seats[r])):
                changed += modify(seats, tracker, r, s, oc, p1)

        if changed == 0:
            break

        seats = copy.deepcopy(tracker)

def test():
    t = [['.','#','#','.','#','#','.'],
         ['#','.','#','.','#','.','#'],
         ['#','#','.','.','.','#','#'],
         ['.','.','.','L','.','.','.'],
         ['#','#','.','.','.','#','#'],
         ['#','.','#','.','#','.','#'],
         ['.','#','#','.','#','#','.']]

    assert len(part2_adj(t, 3, 3)) == 0

def calculate():
    seats = [[x for x in line.strip().replace('\n','')] for line in open('./input.txt').readlines()]
    global total

    test()

    stabilize(seats)
    print(f"Part 1: {total}")
    
    total = 0
    stabilize(seats, 5, False)
    print(f"Part 2: {total}")

if __name__ == '__main__':
    calculate()