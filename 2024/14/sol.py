import re
from math import prod
robots = [list(map(int,x)) for x in [re.findall(r"(-?\d+)",x.strip()) for x in open("in").readlines()]]
num_robots = len(robots)
pr,pc,vel_r,vel_c = 1,0,3,2
#R,C = 7,11
R,C = 103,101

def draw():
    grid = [[' ' for _ in range(C)] for y in range(R)]
    for (c,r,_,_) in robots:
        grid[r][c] = '*'
    for l in grid:
        print(''.join([str(x) for x in l]))
    print('\n\n')

def get_points(rs,re,cs,ce):
    quad = []
    for r in range(rs,re):
        for c in range(cs,ce):
            quad.append((r,c))
    return quad

def get_quadrants():
    mid_r,mid_c = R//2,C//2
    return [get_points(0,mid_r,0,mid_c), get_points(0,mid_r,mid_c+1,C), get_points(mid_r+1,R,0,mid_c), get_points(mid_r+1,R,mid_c+1,C)]

def count_robots():
    quads = get_quadrants()
    cnts = []
    for q in quads:
        cnt = 0
        for (c,r,_,_) in robots:
            if (r,c) in q:
                cnt += 1
        cnts.append(cnt)
    return cnts

def no_overlap():
    pts = [(x[0],x[1]) for x in robots]
    return len(pts) == len(set(pts))

def sim(iters=100):
    p1,p2 = 0,0
    for j in range(iters):
        for i in range(num_robots):
            _,_,vc,vr = robots[i]
            robots[i][pr] = (robots[i][pr] + vr) % R
            robots[i][pc] = (robots[i][pc] + vc) % C

        if j+1 == 100:
            p1 = prod(count_robots())
        if no_overlap():
            draw()
            p2 = j+1
            break
    return p1,p2

p1,p2 = sim(9000)
print(f"{p1=} || {p2=}")
