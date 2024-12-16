import pickle
from collections import deque,defaultdict
from functools import lru_cache
import heapq

maze = [list(x.strip()) for x in open('in').readlines()]
R,C = len(maze),len(maze[0])
sr,sc = [(r,c) for r in range(R) for c in range(C) if maze[r][c] == 'S'][0]
er,ec = [(r,c) for r in range(R) for c in range(C) if maze[r][c] == 'E'][0]
neighbors = {
    (-1,0): [(-1,0),(0,-1),(0,1)],
    (1,0): [(1,0),(0,-1),(0,1)],
    (0,-1): [(0,-1),(1,0),(-1,0)],
    (0,1): [(0,1),(1,0),(-1,0)]
}

@lru_cache(None)
def walk():
    global maze,sr,sc,er,ec,neighbors,R,C
    dist = defaultdict(lambda:int(10e9))
    seen = set()
    dq = []
    heapq.heappush(dq,(0,sr,sc,0,1))
    dist[(sr,sc)] = 0

    while dq:
        score,r,c,dr,dc = heapq.heappop(dq)

        if (r,c,dr,dc) in seen and dist[(r,c)] < score:
            continue

        if (r,c) == (er,ec):
            dist[(r,c)] = min(dist[(r,c)],score)

        for rr,cc in neighbors[(dr,dc)]:
            if 0 <= r+rr < R and 0 <= c+cc < C and maze[r+rr][c+cc] != '#':
                s = score
                if (rr,cc) == (dr,dc):
                    s += 1
                else:
                    s += 1001
                if s >= dist[(er,ec)]:
                    continue
                if (r+rr,c+cc,rr,cc) not in seen or dist[(r+rr,c+cc)] > s:
                    seen.add((r+rr,c+cc,rr,cc))
                    dist[(r+rr,c+cc)] = s
                    heapq.heappush(dq,(s,r+rr,c+cc,rr,cc))

    return dist

def count_locs(dist):
    global er,ec
    seen = set()
    dq = [(er,ec)]

    while dq:
        r,c = dq.pop()

        seen.add((r,c))


dist = walk()
p1 = dist[(er,ec)]
print(p1)
