r,p = open('in').read().strip().split('\n\n')
regs,program = dict((k,v,) for k,v in list(map(lambda x: (x[0][-1],int(x[1])),[x.split(':') for x in r.split('\n')]))),list(map(int,p.split(' ')[1].split(',')))
prg_out = ''
combo = {
    0: lambda: 0,
    1: lambda: 1,
    2: lambda: 2,
    3: lambda: 3,
    4: lambda: regs['A'],
    5: lambda: regs['B'],
    6: lambda: regs['C']
}
def adv(regs,combo,operand):
    regs['A'] //= (2**combo[operand]())
    return 2

def blx(regs,_,operand): 
    regs['B'] ^= operand
    return 2

def bst(regs,combo,operand): 
    regs['B'] = (combo[operand]() % 8)
    return 2

def jnz(regs,_,operand):
    return (2,True) if regs['A'] == 0 else (operand,False)

def bxc(regs,_,__): 
    regs['B'] ^= regs['C']
    return 2

def out(_,combo,operand):
    global prg_out
    prg_out += str(combo[operand]() % 8)
    return 2

def bdv(regs,combo,operand):
    regs['B'] = regs['A'] // (2**combo[operand]())
    return 2

def cdv(regs,combo,operand):
    regs['C'] = regs['A'] // (2**combo[operand]())
    return 2

execute = {
    0: adv,
    1: blx,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv
}

def matches(p2,prog):
    if len(p2) != prog:
        return False
    
    for i in range(len(p2)):
        if p2[i] != prog[i]:
            return False
        
    return True

def run(A,p2=False):
    global regs,prg_out
    regs = dict((k,v,) for k,v in list(map(lambda x: (x[0][-1],int(x[1])),[x.split(':') for x in r.split('\n')])))
    regs['A'] = A
    prg_out = ''
    i = 0
    while i < len(program):
        if program[i] == 3:
            n,inc = execute[program[i]](regs,combo,program[i+1])
            if inc: i += n
            else: i = n
        else:
            i += execute[program[i]](regs,combo,program[i+1])
        
        if p2 and program[i] == 5:
            if prg_out and prg_out[-1] != program[len(prg_out)-1]:
                return []

    return list(map(int,list(prg_out)))


p1 = run(regs['A'])

print(f"{p1=}")