inst = [x.strip().split() for x in open('in').readlines()]

def run(a,b,c,d):
    regs,i = {'a':a, 'b':b, 'c':c, 'd':d},0
    while i < len(inst):
        curr = inst[i]
        if curr[0] == 'cpy':
            regs[curr[2]] = int(curr[1]) if curr[1].isdigit() else regs[curr[1]]
            i += 1
        elif curr[0] == 'inc':
            regs[curr[1]] += 1
            i += 1
        elif curr[0] == 'dec':
            regs[curr[1]] -= 1
            i += 1
        elif curr[0] == 'jnz':
            if (curr[1].isdigit() and int(curr[1])) or regs[curr[1]] != 0:
                i += int(curr[2])
            else:
                i += 1
    return regs['a']

print(f"p1={run(0,0,0,0)} || p2={run(0,0,1,0)}")