from collections import defaultdict
grid,p1,p2 = [list(x.strip()) for x in open('in').readlines()],set(),set()
R,C = len(grid),len(grid[0])
nodes = defaultdict(list)

for r in range(R):
    for c in range(C):
        if grid[r][c] != '.':
            nodes[grid[r][c]].append((r,c))

def resonate(r,rr,c,cc):
    first = True
    for rz,cz in zip(range(r+rr,-1 if rr < 0 else R,rr),range(c+cc,-1 if cc < 0 else C,cc)):
        if first:
            first = False
            p1.add((rz,cz))
        p2.add((rz,cz))

for ants in nodes.values():
    for (r1,c1) in ants:
        for (r2,c2) in ants:
            if (c1,r1) == (c2,r2):
                continue

            rr,cc = abs(r1-r2), abs(c1-c2)
            p2.add((r1,c1))
            p2.add((r2,c2))

            if r1 < r2 and c1 < c2:
                resonate(r1,-rr,c1,-cc)
                resonate(r2,rr,c2,cc)
            elif r1 < r2 and c1 > c2:
                resonate(r1,-rr,c1,cc)
                resonate(r2,rr,c2,-cc)
            elif r1 > r2 and c1 > c2:
                resonate(r1,rr,c1,cc)
                resonate(r2,-rr,c2,-cc)
            elif r1 > r2 and c1 < c2:
                resonate(r1,rr,c1,-cc)
                resonate(r2,-rr,c2,cc)


print(f"p1={len(p1)} || p2={len(p2)}")

#for (r,c) in p2:
#    if grid[r][c] == '.':
#        grid[r][c] = '#'
#for l in grid:
#    print(''.join(l))