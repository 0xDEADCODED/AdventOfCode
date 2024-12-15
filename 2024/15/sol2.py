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
    
    # If the stone didn't move, robot can't move
    if move_p1(r+dr,c+dc,dir) == (r+dr,c+dc):
        return r,c

    # If we're here then the stone moved, robot can now move
    return move_item(grid,r,c,dr,dc)

def move_p2(grid,r,c,dir,to_move):
    dr,dc = convert[dir]
    
    if grid[r+dr][c+dc] == '#':
        return r,c
    
    if dir in ['<','>']:
        if grid[r+dr][c+dc] in ['[',']']:
            if move_p2(grid,r,c+dc,dir,to_move) == (r,c+dc):
                return (r,c)
            return move_item(grid,r,c,dr,dc)
        return move_item(grid,r,c,dr,dc)
    elif dir in ['^','v']:
        if grid[r+dr][c+dc] == '[':
            center_r,center_c = move_p2(grid,r+dr,c+dc,dir,to_move)
            close_r,close_c = move_p2(grid,r+dr,c+dc+1,dir,to_move)
            if (close_r,close_c) == (r+dr,c+1) or (center_r,center_c) == (r+dr,c+dc):
                to_move.append((False,0,0,0,0))
                return (r,c)
            to_move.append((True,r,c,r+dr,c+dc))
            to_move.append((True,r+dr,c+dc,center_r,center_c))
            to_move.append((True,r+dr,c+1,close_r,close_c))

            return r+dr,c+dc
        elif grid[r+dr][c+dc] == ']':
            center_r,center_c = move_p2(grid,r+dr,c+dc,dir,to_move)
            close_r,close_c = move_p2(grid,r+dr,c+dc-1,dir,to_move)
            if (close_r,close_c) == (r+dr,c-1) or (center_r,center_c) == (r+dr,c+dc):
                to_move.append((False,0,0,0,0))
                return (r,c)
            to_move.append((True,r,c,center_r,center_c))
            to_move.append((True,r+dr,c+dc,center_r,center_c))
            to_move.append((True,r+dr,c+dc-1,close_r,close_c))
            return r+dr,c+dc
            
        if grid[r][c] == '@':
            print(r,c,grid[r][c],to_move)
            if len(to_move) and all([x[0] for x in to_move]):
                for (_,ogr,ogc,tr,tc) in to_move[::-1]:
                    grid[tr][tc] = grid[ogr][ogc]
                    grid[ogr][ogc] = '.'

    return move_item(grid,r,c,dr,dc)
        


def calc_p2(grid):
    global moves
    print_grid(grid)
    sr,sc = [(r,c) for r in range(R) for c in range(C*2) if grid[r][c] == '@'][0]
    for d in moves:
        to_move = []
        sr,sc = move_p2(grid,sr,sc,d,to_move)
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