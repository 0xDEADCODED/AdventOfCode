grid = [x.strip() for x in open("in").readlines()]
R,C,p1,p2 = len(grid), len(grid[0]), 0, 0

def check_one(r,c):
    res = 0
    for (rr,cc) in [(0,1), (0,-1), (-1,0), (-1,1), (-1,-1), (1,0), (1,1), (1,-1)]:
        search = ''
        for i in range(len('XMAS')):
            if not (0 <= r+(rr*i) < R and 0 <= c+(cc*i) < C): continue

            search += grid[r+(rr*i)][c+(cc*i)]
            if search != 'XMAS'[:i+1]: break
        
        if search == 'XMAS': res += 1
    return res

def check_two(r,c):
    if grid[r][c] != 'A': return 0
    if r-1 >= 0 and c-1 >= 0 and r + 1 < R and c + 1 < C \
        and grid[r-1][c-1] + grid[r][c] + grid[r+1][c+1] in ['MAS', 'SAM'] \
        and grid[r+1][c-1] + grid[r][c] + grid[r-1][c+1] in ['MAS', 'SAM']:
        return 1
    return 0

for r in range(R):
    for c in range(C):
        p1 += check_one(r,c)
        p2 += check_two(r,c)

print(f"{p1=} || {p2=}")