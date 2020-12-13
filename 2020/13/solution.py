
def part1(lines):
    estimate = int(lines[0])
    busses = [int(x) for x in lines[1].strip().split(',') if x != 'x']

    ts = estimate - 1
    match = 0
    while match == 0:
        ts += 1
        for b in busses:
            if ts%b == 0:
                match = b
                break
    
    print(f"Part 1: {(ts - estimate) * match}")

def modInverse(a, m): 
    m0 = m 
    y = 0
    x = 1
  
    if (m == 1): 
        return 0
  
    while (a > 1): 
  
        # q is quotient 
        q = a // m 
  
        t = m 
  
        # m is remainder now, process 
        # same as Euclid's algo 
        m = a % m 
        a = t 
        t = y 
  
        # Update x and y 
        y = x - q * y 
        x = t 
  
    # Make x positive 
    if (x < 0): 
        x = x + m0 
  
    return x

def get_relevant(busses):
    rel = []
    prod = 1
    for i,b in enumerate(busses):
        if b != 'x':
            b = int(b)
            i %= b
            rel.append(((b-i)%b,b))
            prod *= b

    return rel, prod

def part2(lines):
    busses = lines[1].split(',')
    
    rel, prod = get_relevant(busses)
    ts = 0

    for i,b in rel:
        ni = prod//b
        mi = modInverse(ni, b)
        ts += i*mi*ni

    ts %= prod

    print(f"Part 2: {ts}")
                    

def calculate():
    lines = [line.strip().replace('\n','') for line in open('./input.txt').readlines()]
    
    part1(lines)
    part2(lines)

if __name__ == '__main__':
    calculate()