
ADD = 1
MULT = 2
INPUT= 3
OUTPUT= 4
JTRUE = 5
JFALSE = 6
LTHAN = 7
EQUAL = 8
HALT = 99

POSITION = 0
IMMEDIATE = 1

def parse_opcode(number):
    opcode = number % 100
    
    parameter_modes = []
    for i in [100, 1000, 10000]:
        parameter_modes.append((number // i) % 10)
    return opcode, tuple(parameter_modes)

def run_codes(l, inp=1):
    lines = l.copy()
    output = None
    pc = 0
    while pc < len(lines):
        opp,m = parse_opcode(lines[pc])

        if opp == HALT:
            break
        elif opp == INPUT:
            lines[lines[pc+1]] = inp
            pc += 2
        elif opp == OUTPUT:
            output = lines[lines[pc+1]]
            pc += 2
        else: 
            p1 = lines[pc+1] if m[0] == 1 else lines[lines[pc+1]]
            p2 = lines[pc+2] if m[1] == 1 else lines[lines[pc+2]]
            if opp == ADD:
                lines[lines[pc+3]] = p1 + p2
                pc += 4
            elif opp == MULT:
                lines[lines[pc+3]] = p1 * p2
                pc += 4
            if opp in [JTRUE, JFALSE]:
                if (opp == JTRUE and p1 != 0) or (opp == JFALSE and p1 == 0):
                    pc = p2
                else:
                    pc +=3
            elif opp == LTHAN:
                lines[lines[pc+3]] = 1 if p1 < p2 else 0
                pc += 4
            elif opp == EQUAL:
                lines[lines[pc+3]] = 1 if p1 == p2 else 0
                pc += 4

    return output

def calculate():
    lines = [int(x) for x in open('./input.txt', 'r').readlines()[0].strip().split(',')]
    
    print(f"Part 1: {run_codes(lines)}")
    print(f"Part 1: {run_codes(lines, 5)}")

if __name__ == '__main__':
    calculate()