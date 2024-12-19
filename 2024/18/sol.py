from collections import defaultdict
import heapq
locs = list(map(lambda x: (int(x[0]),int(x[1])),[x.strip().split(',') for x in open('in').readlines()]))
R,C = 71,71
grid = [['.' for _ in range(C)] for _ in range(R)]

def fill_grid(s,e):
    for i in range(s,e):
        c,r = locs[i]
        grid[r][c] = '#'

def find_path():
    sr,sc = 0,0
    er,ec = R-1,C-1
    dist,seen,dq = defaultdict(lambda:int(10e9)),set(),[]
    heapq.heappush(dq,(0,sr,sc,0,1))
    dist[(sr,sc)] = 0

    while dq:
        score,r,c,dr,dc = heapq.heappop(dq)

        if (r,c,dr,dc) in seen and dist[(r,c)] < score:
            continue

        if (r,c) == (er,ec):
            dist[(r,c)] = min(dist[(r,c)],score)

        for rr,cc in [(-1,0),(1,0),(0,-1),(0,1)]:
            if 0 <= r+rr < R and 0 <= c+cc < C and grid[r+rr][c+cc] != '#':
                s = score + 1
                if s >= dist[(er,ec)]:
                    continue
                if (r+rr,c+cc,rr,cc) not in seen or dist[(r+rr,c+cc)] > s:
                    seen.add((r+rr,c+cc,rr,cc))
                    dist[(r+rr,c+cc)] = s
                    heapq.heappush(dq,(s,r+rr,c+cc,rr,cc))

    return dist[(er,ec)]

fill_grid(0,1023)
p1,p2 = find_path(),0
for i in range(1024,len(locs)):
    fill_grid(i,i+1)
    if find_path() == int(10e9):
        p2 = locs[i]
        break

print(f"{p1=} || {p2=}")