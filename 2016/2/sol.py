inst = [x.strip() for x in open('in').readlines()]
p1_pad = [['1','2','3'],['4','5','6'],['7','8','9']]
p2_pad = [[None,None,'1',None,None],[None,'2','3','4',None],['5','6','7','8','9'],[None, 'A','B','C',None],[None,None,'D',None,None]]

def find_code(pad,x,y):
    code,L = '', len(pad)
    for moves in inst:
        for move in moves:
            if move == 'U' and x - 1 in range(L) and pad[x-1][y]:
                x -= 1
            elif move == 'D' and x + 1 in range(L) and pad[x+1][y]:
                x += 1
            elif move == 'R' and y + 1 in range(L) and pad[x][y+1]:
                y += 1
            elif move == 'L' and y - 1 in range(L) and pad[x][y-1]:
                y -= 1

        code += pad[x][y]
    return code

p1 = find_code(p1_pad,1,1)
p2 = find_code(p2_pad,2,0)

print(f"{p1=} || {p2=}")