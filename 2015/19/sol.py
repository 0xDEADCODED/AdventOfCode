import re
ops,ct = open('in').read().strip().split('\n\n')
ops,L,mols = list(tuple(y.split(' => ')) for y in [x for x in ops.split('\n')]), len(ct), set()

for (k,v) in ops:
    lk = len(k)
    for i in range(L):
        if i+lk in range(L+1) and ct[i:i+lk] == k:
            mod = ct[:i] + v + ct[i+lk:]
            mols.add(mod)

p1,p2 = len(mols),0

while ct != 'e':
    for (k,v) in ops:
        if v in ct:
            ct = ct.replace(v,k,1)
            p2 += 1
            break

print(f"{p1=} || {p2=}")