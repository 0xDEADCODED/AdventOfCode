steps = open('in').read().strip().replace(' ','').split(',')
x,y,dx,dy,seen,p2 = 0,0,-1,0,set(), 0
turn = {
    (0,-1,'R'): (-1,0), (0,-1,'L'): (1,0), # left
    (0,1,'R'): (1,0), (0,1,'L'): (-1,0), # right
    (-1,0,'R'): (0,1), (-1,0,'L'): (0,-1),  # up
    (1,0,'R'): (0,-1), (1,0,'L'): (0,1) # down
}

def dist(x,y): return abs(x) + abs(y)

for s in steps:
    d,c = s[0],int(s[1:])
    dx,dy = turn[(dx,dy,d)]
    for _ in range(c):
        x += 1*dx
        y += 1*dy
        if (x,y) in seen and p2 == 0:
            p2 = (x,y)
        seen.add((x,y))

p1 = dist(x,y)
p2 = dist(p2[0],p2[1])
print(f"{p1=} || {p2=}")