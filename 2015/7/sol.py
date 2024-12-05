actions = [x.strip().split(' -> ') for x in open('in').readlines()]
wires = dict((dest,signal) for (signal,dest) in actions)

def trace(wire):
    if wire.isdigit(): return int(wire)
    
    signal = wires[wire]
    if type(signal) == int or signal.isdigit(): return int(signal)

    if 'AND' in signal:
        a,b = signal.split(' AND ')
        wires[wire] = trace(a) & trace(b)
    elif 'OR' in signal:
        a,b = signal.split(' OR ')
        wires[wire] = trace(a) | trace(b)
    elif 'LSHIFT' in signal:
        a,b = signal.split(' LSHIFT ')
        wires[wire] = trace(a) << int(b)
    elif 'RSHIFT' in signal:
        a,b = signal.split(' RSHIFT ')
        wires[wire] = trace(a) >> int(b)
    elif 'NOT' in signal:
        a = signal.split(' ')[1]
        wires[wire] = trace(a) ^ 0xFFFF
    else:
        wires[wire] = trace(signal)

    return wires[wire]

p1 = trace('a')
wires = dict((dest,signal) for (signal,dest) in actions)
wires['b'] = p1
p2 = trace('a')

print(f"{p1=} || {p2=}")