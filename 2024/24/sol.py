from collections import defaultdict
devs,gates = open('in').read().strip().split('\n\n')
devs = dict((x.split(': ')[0],int(x.split(': ')[1])) for x in devs.split('\n'))
gates = [(x.split(' ')[0],x.split(' ')[1],x.split(' ')[2],x.split(' ')[4]) for x in gates.split('\n')]
zs = []
GATES = {
    'AND': lambda a,b: int(a==1 and b==1),
    'OR': lambda a,b: int(a==1 or b==1),
    'XOR': lambda a,b: int(a != b)
}

while gates:
    a,op,b,d = gates.pop(0)
    if a in devs and b in devs:
        devs[d] = GATES[op](devs[a],devs[b])
        if d.startswith('z'):
            zs.append(d)
    else:
        gates.append((a,op,b,d))

num = ''
for k in sorted(zs)[::-1]:
    num += str(devs[k])
print(int(num,2))

