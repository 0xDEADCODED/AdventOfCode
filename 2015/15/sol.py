import re, itertools
data,facts,poss = re.findall(r"(.*):.* (-?\d+), .* (-?\d+), .* (-?\d+), .* (-?\d+), .* (-?\d+)", open('in').read().strip()),{},[]
for (i,cap,d,f,t,cal) in data:
    facts[i] = {}
    facts[i]['cp'] = int(cap)
    facts[i]['d'] = int(d)
    facts[i]['f'] = int(f)
    facts[i]['t'] = int(t)
    facts[i]['cl'] = int(cal)

p1,p2 = 0,0
for a in range(101):
    for b in range(101):
        for c in range(101):
            for d in range(101):
                if a+b+c+d == 100:
                    cp,dd,f,t,cl = 0,0,0,0,0
                    for ff,z in zip(facts.keys(), [a,b,c,d]):
                        cp += facts[ff]['cp'] * z
                        dd += facts[ff]['d'] * z
                        f += facts[ff]['f'] * z
                        t += facts[ff]['t'] * z
                        cl += facts[ff]['cl'] * z
                    if cp >= 0 and dd >= 0 and f >= 0 and t >= 0:
                        p1 = max(p1, cp*dd*f*t)
                        if cl == 500: p2 = max(p2, cp*dd*f*t)

print(f"{p1=} || {int(p2)=}")          