from hashlib import md5
import heapq
from copy import deepcopy
passcode = 'yjjvjgan'
grid = [x.strip() for x in open('grid').readlines()]
R,C = len(grid),len(grid[0])
UP,DOWN,LEFT,RIGHT = 0,1,2,3
OPEN = ['b','c','d','e','f']

dq = []
heapq.heappush(dq,(1,1,passcode,set()))
paths = set()
while dq:
    r,c,p,doors = heapq.heappop(dq)

    if grid[r][c] == 'V':
        paths.add(p[len(passcode):])
        continue

    for rr,cc,d in [(-1,0,'U'),(1,0,'D'),(0,-1,'L'),(0,1,'R')]:
        if r+rr in range(R) and c+cc in range(C) and grid[r+rr][c+cc] != '#':
            h = md5(p.encode()).hexdigest()[:4]
            drs = deepcopy(doors)
            if d == 'U' and h[UP] in OPEN:
                drs.add((d,r+rr,c+cc))
                heapq.heappush(dq,(r+rr-1,c+cc,p+d,drs))
            elif d == 'D' and h[DOWN] in OPEN:
                drs.add((d,r+rr,c+cc))
                heapq.heappush(dq,(r+rr+1,c+cc,p+d,drs))
            elif d == 'L' and h[LEFT] in OPEN:
                drs.add((d,r+rr,c+cc))
                heapq.heappush(dq,(r+rr,c+cc-1,p+d,drs))
            elif d == 'R' and h[RIGHT] in OPEN:
                drs.add((d,r+rr,c+cc))
                heapq.heappush(dq,(r+rr,c+cc+1,p+d,drs))
                
paths = sorted(paths,key=len)
p1 = paths[0]
p2 = len(paths[-1])

print(f"{p1=} || {p2=}")