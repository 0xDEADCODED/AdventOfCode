from collections import defaultdict
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

def walk():
    global maze,sr,sc,er,ec,neighbors,R,C
    dist,seen,dq = defaultdict(lambda:int(10e9)),set(),[]
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

    return dist[(er,ec)]

def count_seats(grid,sr,sc,er,ec):
    dirs = [(0,1), (1,0), (0,-1), (-1,0)]
    dq,visited,best,seats = [],set(),int(10e9),{(sr,sc)}
    heapq.heappush(dq,(0,sr,sc,0,[(sr,sc)]))
    while True:
        score,r,c,d,path = heapq.heappop(dq)
        if score > best:
            return len(seats)
        visited.add((r,c,d))
        for i in [0,-1,1,2]:
            ndir = (d+i)%4
            dr,dc = dirs[ndir]
            r1,c1 = r+dr,c+dc
            if grid[r1][c1]=='#':
                continue
            if (r1,c1,ndir) in visited:
                continue
            s = score+abs(i)*1000+1
            if (r1,c1)==(er,ec):
                best = s
                seats.update(path+[(r1,c1)])
            else:
                path_cp = path + [(r1,c1)]
                heapq.heappush(dq, (s,r1,c1,ndir,path_cp))

p1 = walk()
p2 = count_seats(maze,sr,sc,er,ec)
print(f"{p1=} || {p2=}")
