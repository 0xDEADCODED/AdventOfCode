
current = 'E'

R90 = {'N':'E', 'E':'S', 'S':'W', 'W':'N'}
L90 = {'N':'W', 'W':'S', 'S':'E', 'E':'N'}

def move(opp, num, x, y):
    if opp == 'N':
        y += num
    elif opp == 'S':
        y -= num
    elif opp == 'E':
        x += num
    elif opp == 'W':
        x -= num

    return x,y

def rotate(opp, num):
    global R90
    global L90
    global current       

    for _ in range(num//90):
        current = R90[current] if opp == 'R' else L90[current]

def part1(dirs):
    global current
    x = 0
    y = 0
    for m in dirs:
        opp, num = m[0], int(m[1:])
        
        if opp in ['N','S','E','W']:
            x,y = move(opp, num, x, y)
        elif opp == 'F':
            x, y = move(current, num, x, y)
        elif opp in ['R', 'L']:
            rotate(opp, num)


    print(f"Part 1: {abs(x) + abs(y)}")

def part2(dirs):
    x = 0
    y = 0
    way_x = 10
    way_y = 1

    for m in dirs:
        opp, num = m[0], int(m[1:])
        if opp in ['N','S','E','W']:
            way_x, way_y = move(opp, num, way_x, way_y)
        elif opp == 'F':
            x += (num * way_x)
            y += (num * way_y)
        elif opp == 'L':
            for _ in range(num//90):
                way_x,way_y = -way_y,way_x
        elif opp == 'R':
            for _ in range(num//90):
                way_x,way_y = way_y,-way_x
            
    print(f"Part 2: {abs(x) + abs(y)}")


def calculate():
    dirs = [line.strip().replace('\n','') for line in open('./input.txt',  'r').readlines()]
    
    part1(dirs)
    part2(dirs)

if __name__ == '__main__':
    calculate()
