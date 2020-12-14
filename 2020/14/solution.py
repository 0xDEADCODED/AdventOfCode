import re
from itertools import product 

def and_opp(mask, num, p1=True):
    lst = [x for x in num]
    for i in range(len(mask)):
        if p1:
            if mask[i] != 'X':
                lst[i] = mask[i]
        else:
            if mask[i] == '1':
                lst[i] = '1'
            elif mask[i] == 'X':
                lst[i] = mask[i]
    
    return ''.join(lst)


def part1(lines):
    mask = ''
    mem = {}
    for cmd in lines:
        opp, arg = [x.strip() for x in cmd.split('=')]

        if opp == 'mask':
            mask = arg
        elif 'mem' in opp:
            addr = int(re.findall(r'\[(\d*)\]', opp)[0])
            bin_n = f'{int(arg):036b}'
            masked = int(and_opp(mask, bin_n),2)
            mem[addr] = masked

    print(f"Part 1: {sum(list(mem.values()))}")

def combos(masked):
    keyletters = 'X'
    seq = list(masked)

    indices = [ i for i, c in enumerate(seq) if c in keyletters ]
    
    res = []
    for t in product(keyletters, repeat=len(indices)):
        for i, _ in zip(indices, t):
            seq[i] = '0'
            res.append(''.join(seq))
            res += combos(''.join(seq))
            seq[i] = '1'
            res.append(''.join(seq))
            res += combos(''.join(seq))
    
    return res

def part2(lines):
    mask = ''
    mem = {}
    for cmd in lines:
        opp, arg = [x.strip() for x in cmd.split('=')]

        if opp == 'mask':
            mask = arg
        elif 'mem' in opp:
            addr = int(re.findall(r'\[(\d*)\]', opp)[0])
            bin_n = f'{int(addr):036b}'
            masked = and_opp(mask, bin_n, False)

            if 'X' in masked:
                c = set(combos(masked))
                c = [x for x in c if 'X' not in x]
            else:
                c = [masked]
            
            for a in c:
                addr = int(a,2)
                mem[addr] = int(arg)

    print(f"Part 2: {sum(list(mem.values()))}")

def calculate():
    lines = [line.strip().replace('\n','') for line in open('./input.txt', 'r').readlines()]

    part1(lines)
    part2(lines)

if __name__ == '__main__':
    calculate()