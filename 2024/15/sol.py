data = open('ex3').read().strip().split('\n\n')
grid,moves = [list(x) for x in data[0].split('\n')],data[1].replace('\n','')
R,C = len(grid),len(grid[0])
convert = {'^':(-1,0), 'v':(1,0), '<':(0,-1), '>':(0,1)}

def print_grid(grid):
    print('\n'.join([''.join(x) for x in grid]),end='\n\n')

def generate_p2_grid():
    g2,c2 = [['.' for x in range(C*2)] for y in range(R)],0
    for r in range(R):
        c2 = 0
        for c in range(C):
            if grid[r][c] == '#':
                g2[r][c2] = '#'
                g2[r][c2+1] = '#'
            elif grid[r][c] == 'O':
                g2[r][c2] = '['
                g2[r][c2+1] = ']'
            elif grid[r][c] == '@':
                g2[r][c2] = '@'
            c2 += 2

    return g2


def calc_gps(grid,search):
    return sum([100*r+c for r in range(R) for c in range(C) if grid[r][c] == search])

def move_item(grid,r,c,dr,dc):
        grid[r+dr][c+dc] = grid[r][c] 
        grid[r][c] = '.'
        return r+dr,c+dc

def move_p1(r,c,dir):
    dr,dc = convert[dir]
    
    if grid[r+dr][c+dc] == '#':
        return r,c 
    
    if grid[r+dr][c+dc] == '.':
        return move_item(grid,r,c,dr,dc)
    
    if move_p1(r+dr,c+dc,dir) == (r+dr,c+dc):
        return r,c

    return move_item(grid,r,c,dr,dc)

to_move = []
def move_p2(grid,r,c,dir):
    global to_move
    dr,dc = convert[dir]
    
    if grid[r+dr][c+dc] == '#':
        return r,c
    
    if grid[r+dr][c+dc] == '.':
        to_move.append((r,c,r+dr,c+dc))
    else:
        if dir in ['<','>']:
            if grid[r+dr][c+dc] in ['[',']']:
                if move_p2(grid,r+dr,c+dc,dir) == (r,c):
                    return r,c
                to_move.append((r,c,r+dr,c+dc))
        elif dir in ['^','v']:
            if grid[r+dr][c+dc] == '[':
                lr,lc = move_p2(grid,r+dr,r+dc,dir)
                rr,rc = move_p2(grid,r+dr,r+dc+1,dir)
                if (lr,lc) == (r+dr,c+dc) or (rr,rc) == (r+dr,c+dc+1):
                    return r,c
                to_move.append((r,c,r+dr,c+dc))
                to_move.append((r+dr,c+dc,lr,lc))
                to_move.append((r+dr,c+dc+1,rr,rc))
            elif grid[r+dr][c+dc] == ']':
                rr,rc = move_p2(grid,r+dr,r+dc,dir)
                lr,lc = move_p2(grid,r+dr,r+dc-1,dir)
                if (rr,rc) == (r+dr,c+dc) or (lr,lc) == (r+dr,c+dc-1):
                    return r,c
                to_move.append((r,c,r+dr,c+dc))
                to_move.append((r+dr,c+dc,rr,rc))
                print(lr,lc)
                to_move.append((r+dr,c+dc-1,lr,lc))


    if grid[r][c] == '@':
        print(to_move)
        for (sr,sc,tr,tc) in to_move:
            grid[tr][tc] = grid[sr][sc]
            grid[sr][sc] = '.'

    return r+dr,c+dc
        


def calc_p2(grid):
    global moves,to_move
    print_grid(grid)
    sr,sc = [(r,c) for r in range(R) for c in range(C*2) if grid[r][c] == '@'][0]
    for d in moves:
        to_move = []
        sr,sc = move_p2(grid,sr,sc,d)
        print(d)
        print_grid(grid)


    return calc_gps(grid,'[')

def calc_p1(grid):
    global moves
    sr,sc = [(r,c) for r in range(R) for c in range(C) if grid[r][c] == '@'][0]
    for d in moves:
        sr,sc = move_p1(sr,sc,d)

    return calc_gps(grid,'O')


p2_grid = generate_p2_grid()
p1 = calc_p1(grid)
p2 = calc_p2(p2_grid)