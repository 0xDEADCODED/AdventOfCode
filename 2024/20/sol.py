import heapq
from collections import defaultdict

grid = [list(x.strip()) for x in open('in').readlines()]
R,C = len(grid),len(grid[0])
sr,sc = [(r,c) for r in range(R) for c in range(C) if grid[r][c] == 'S'][0]
er,ec = [(r,c) for r in range(R) for c in range(C) if grid[r][c] == 'E'][0]

def find_path(x,y):
    dist,dq = defaultdict(lambda:int(10e9)),[]
    heapq.heappush(dq,(0,x,y))
    dist[(x,y)] = 0

    while dq:
        score,r,c = heapq.heappop(dq)

        for rr,cc in [(-1,0),(1,0),(0,-1),(0,1)]:
            if 0 <= r+rr < R and 0 <= c+cc < C and grid[r+rr][c+cc] != '#' and score + 1 < dist[r+rr,c+cc]:
                dist[r+rr,c+cc] = score+1
                heapq.heappush(dq,(score+1,r+rr,c+cc))

    return dist

forwards = find_path(sr,sc)
backwards = find_path(er,ec)
p1,p2,baseline = 0,0,forwards[(er,ec)]

walls = [(r,c) for r in range(R-1) for c in range(C-1) if grid[r][c] == '#']
for wr,wc in walls:
    grid[wr][wc] = '.'
    d = find_path(sr,sc)[(er,ec)]
    if baseline - d >= 100:
        p1 += 1
    grid[wr][wc] = '#'

for r1,c1 in forwards.keys():
    for r2,c2 in backwards.keys():
        d = abs(r1-r2) + abs(c1-c2)
        if d <= 20 and forwards[(r1,c1)] + d + backwards[(r2,c2)] <= baseline - 100:
            p2 += 1


print(f"{p1=} || {p2=}")