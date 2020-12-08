
def find_duplicate_opp(opcodes):
    accumulator = 0
    i = 0
    seen = set()
    dup = False

    while i < len(opcodes):
        opp, val = opcodes[i]
        if i in seen:
            dup = True
            break

        seen.add(i)

        if opp == 'acc':
            accumulator += val
            i += 1
        elif opp == 'jmp':
            i += val
        elif opp == 'nop':
            i += 1

    return accumulator, dup

def opposite(opp):
    if opp == 'jmp':
        return 'nop'
    
    return 'jmp'

def replace_bad_opp(opcodes):
    i = 0
    while i < len(opcodes):
        opp, val = opcodes[i]
        if opp == 'jmp' or opp == 'nop':
            cp = opcodes.copy()
            cp[i] = ((opposite(opp), val))
            accumulator, dup = find_duplicate_opp(cp)
            if not dup:
                return accumulator
        i +=1

def calculate():
    opcodes = []

    with open('./input.txt', 'r') as fp:
        lines = fp.readlines()
        for code in lines:
            opp, val = code.split()
            opcodes.append((opp.strip(), int(val.strip())))
    
    accumulator,_ = find_duplicate_opp(opcodes)
    print(f"Part 1: {accumulator}")

    accumulator = replace_bad_opp(opcodes)
    print(f"Part 2: {accumulator}")

if __name__ == '__main__':
    calculate()