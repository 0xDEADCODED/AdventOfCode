trails = [list(map(int,list(x.strip()))) for x in open('in').readlines()]
R,C = len(trails), len(trails[0])
starts = [(x,y) for x in range(R) for y in range(C) if trails[x][y] == 0]

def blaze_trail(x,y,reached,p2):
    if trails[x][y] == 9:
        if p2: return 1

        if (x,y) not in reached:
            reached.add((x,y))
            return 1
        else:
            return 0
    
    ans = 0
    for xx,yy in [(0,-1),(0,1),(-1,0),(1,0)]:
        if x + xx in range(R) and y + yy in range(C) and trails[x+xx][y+yy] == trails[x][y] + 1:
            ans += blaze_trail(x+xx,y+yy,reached,p2)
    return ans


p1 = sum([blaze_trail(x,y,set(),False) for (x,y) in starts])
p2 = sum([blaze_trail(x,y,set(),True) for (x,y) in starts])
print(f"{p1=} || {p2=}")
