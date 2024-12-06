from copy import deepcopy
lights = [list(x.strip()) for x in open('in').readlines()]
R,C = len(lights), len(lights[0])
ignore = [(0,0), (0,C-1), (R-1,0), (R-1,C-1)]

def get_neighbors(r,c,g):
    n = []
    for rr in [-1,0,1]:
        for cc in [-1,0,1]:
            if (r+rr,cc+c) != (r,c) and r+rr in range(R) and c+cc in range(C):
                n.append(g[r+rr][c+cc])
    return n

def change_lights(l,p2=False):
    for _ in range(100):
        g = deepcopy(l)
        for r in range(R):
            for c in range(C):
                if p2 and (r,c) in ignore: continue
                n = get_neighbors(r,c,g)
                if g[r][c] == '#' and n.count('#') not in [2,3]:
                    l[r][c] = '.'
                elif g[r][c] == '.' and n.count('#') == 3:
                    l[r][c] = '#'
    return sum([x.count('#') for x in l])

p1 = change_lights(deepcopy(lights))
for x,y in ignore: lights[x][y] = '#'
p2 = change_lights(lights, True)

print(f"{p1=} || {p2=}")