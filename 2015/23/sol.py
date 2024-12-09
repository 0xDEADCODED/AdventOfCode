inst = [x.strip().replace(',','').split() for x in open('in').readlines()]
OPS = {
    'hlf': lambda r: r//2,
    'tpl': lambda r: r*3,
    'inc': lambda r: r+1,
    'jie': lambda r,d: d if r%2==0 else 1,
    'jio': lambda r,d: d if r == 1 else 1,
    'jmp': lambda d: d
}

def run(a,b):
    regs,i = {'a': a, 'b': b},0
    while i in range(len(inst)):
        op = inst[i]
        if op[0] in ['hlf', 'tpl', 'inc']: 
            regs[op[1]] = OPS[op[0]](regs[op[1]])
            i+=1
        elif op[0] in ['jie', 'jio']:
            i += OPS[op[0]](regs[op[1]],int(op[2]))
        else:
            i += int(op[1])
    
    return regs['b']

print(f"p1={run(0,0)} || p2={run(1,0)}")