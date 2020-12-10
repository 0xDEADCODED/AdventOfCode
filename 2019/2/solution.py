from itertools import product


ADD_OPP = 1
MULT_OPP = 2
HALT_OPP = 99

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

def run_intcodes(i, noun, verb):
    inputs = i.copy()
    inputs[1] = noun
    inputs[2] = verb
    pos = 0
    
    while inputs[pos] != HALT_OPP:
        if inputs[pos] == ADD_OPP:
            inputs[inputs[pos+3]] = inputs[inputs[pos+1]] + inputs[inputs[pos+2]]
        elif inputs[pos] == MULT_OPP:
            inputs[inputs[pos+3]] = inputs[inputs[pos+1]] * inputs[inputs[pos+2]]
        
        pos += 4
            
    return inputs[0]

def calculate():
    inputs = []
    with open('./input.txt', 'rb') as fp:
        inputs = [int(x) for x in fp.readlines()[0].split(b',')]

    print(f"Part 1: {run_intcodes(inputs, 12, 2)}")
    
    for noun, verb in product(range(0, 100), range(0, 100)):
        if run_intcodes(inputs, noun, verb) == 19690720:
            print(f"Part 2: {100 * noun + verb}")
            break


if __name__ == '__main__':
    calculate()