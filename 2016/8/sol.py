grid = [['.']*50 for _ in range(6)]
#grid = [['.']*7 for _ in range(3)]
inst = [x.strip().split() for x in open('in').readlines()]
R,C = len(grid),len(grid[0])

def parse_op(op):
    if op[0] == 'rect':
        dims = op[1].split('x')
        return op[0],int(dims[0]),int(dims[1]),None
    else:
        return op[0],op[1],int(op[2].split('=')[1]), int(op[-1])
    
def print_grid():
    for l in grid:
        print(''.join(l))
    print('\n')

for o in inst:
    op,arg1,arg2,arg3 = parse_op(o)

    if op == 'rect':
        for r in range(arg2):
            for c in range(arg1):
                grid[r][c] = '#'
    else:
        if arg1 == 'row':
            row = [x for x in grid[arg2]]
            for c in range(C):
                grid[arg2][(c+arg3)%C] = row[c]
        else:
            col = [grid[r][arg2] for r in range(R)]
            for r in range(R):
                grid[(r+arg3)%R][arg2] = col[r]

p1 = sum([x.count('#') for x in grid])  
print(p1)
print_grid()
