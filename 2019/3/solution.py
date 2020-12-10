import math

def get_points(wire):
    x = 0
    y = 0
    steps = 0
    points = []

    for move in wire:
        points.append((x,y))
        d, num = move[0], int(move[1:])
        if d == 'R':
            for x1 in range(1,num+1):
                points.append((x+x1,y))
            x += num
        elif d == 'L':
            for x1 in range(1,num+1):
                points.append((x-x1,y))
            x -= num
        elif d == 'U':
            for y1 in range(1,num+1):
                points.append((x,y+y1))
            y += num
        elif d == 'D':
            for y1 in range(1,num+1):
                points.append((x,y-y1))
            y -= num

    points.remove((0,0))
    return points

def calculate():
    wires = [line.split(',') for line in open('./input.txt', 'r').read().split('\n')]

    pts1 = get_points(wires[0])
    pts2 = get_points(wires[1])
    common = set(pts1).intersection(set(pts2))
    
    part1 = math.inf
    part2 = math.inf
    for point in common:
        part1 = min(part1, abs(point[0]) + abs(point[1]))
        part2 = min(part2, pts1.index(point) + pts2.index(point)+2)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == '__main__':
    calculate()