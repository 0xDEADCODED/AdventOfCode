grid = [list(x.strip()) for x in open("in").readlines()]
R,C,sdr,sdc,path = len(grid), len(grid[0]), -1, 0, []
sr,sc = [(r,c) for r in range(R) for c in range(C) if grid[r][c] == '^'][0]
turn = {(0,-1):(-1,0), (1,0):(0,-1), (0,1): (1,0), (-1,0):(0,1)}

def find_path():
    path,seen,r,c,dr,dc = set(),set(),sr,sc,sdr,sdc
    while 0 <= r < R and 0 <= c < C and grid[r][c]:
        if (r,c,dr,dc) in seen: return set()
        seen.add((r,c,dr,dc)); path.add((r,c))
        if 0 <= r+dr < R and 0 <= c+dc < C and grid[r+dr][c+dc] == '#': 
            while grid[r+dr][c+dc] == '#': dr,dc = turn[(dr,dc)]

        r,c = r+dr,c+dc
    return path

p1,p2 = find_path(), 0
for (r,c) in p1:
    if (r,c) == (sr,sc): continue
    grid[r][c] = '#'
    if len(find_path()) == 0: p2 += 1
    grid[r][c] = '.'

print(f"p1={len(p1)} || {p2=}")

