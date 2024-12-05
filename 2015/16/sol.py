data = [x.strip().split()[2:] for x in open('in').readlines()]
s = [x.strip().split(':') for x in open("ex").readlines()]
sues,search,p1,p2 = {},{},0,0

for x in s: search[x[0]] = int(x[1])

for i in range(len(data)):
    if (i+1) not in sues.keys():
        sues[i+1] = {}
    #    sues[i+1] = {'children':0, 'cats':0, 'samoyeds':0, 'pomeranians':0, 'akitas':0, 'vizslas': 0, 'goldfish': 0, 'trees':0, 'cars':0,'perfumes':0}
    csue = data[i]
    for (k,v) in zip(*[iter(csue)]*2):
        try:
            sues[i+1][k.replace(':','')] += int(v.replace(',',''))
        except:
            sues[i+1][k.replace(':','')] = int(v.replace(',',''))

for k,v in sues.items():
    first,second = True,True
    for kk,vv in v.items():
        if search[kk] != vv: first = False
        if kk in ['cats', 'trees']:
            if vv <= search[kk]:
                second = False
        elif kk in ['pomeranians', 'goldfish']:
            if vv >= search[kk]:
                second = False
        elif search[kk] != vv: 
            second = False
    if first: p1 = k
    if second: p2 = k

print(f"{p1=} || {p2=}")