from copy import deepcopy
fav_num = 1362
tx,ty = 31,39
p2 = set()

def is_open(x,y):
    check = x*x + 3*x + 2*x*y + y + y*y
    check += fav_num
    check = bin(check)[2:]
    return check.count('1') % 2 == 0

def walk_p1(x,y,steps,seen):
    global p2
    if (x,y) in seen:
        return int(10e9)
    seen.add((x,y))

    if (x,y) == (tx,ty):
        return steps
    
    ans = int(10e9)
    for xx,yy in [(-1,0),(1,0),(0,-1),(0,1)]:
        if x+xx >= 0 and y+yy >= 0 and is_open(x+xx,y+yy):
            if steps+1 <= 50: p2.add((x+xx,y+yy))
            s = deepcopy(seen)
            ans = min(ans,walk_p1(x+xx,y+yy,steps+1,s))
    return ans

p1 = walk_p1(1,1,0,set())
print(f"{p1=} || p2={len(p2)}")