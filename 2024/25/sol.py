lnk = [x.strip().split('\n') for x in open('in').read().strip().split('\n\n')]
locks,keys = [],[]

def get_heights(d,is_key=True):
    R,C = len(d),len(d[0])
    cnts = []

    for c in range(C):
        col = []
        for r in range(R):
            col.append(d[r][c])

        cnts.append(col[:-1].count('#') if is_key else col[1:].count('#'))
    return cnts

for d in lnk:
    if all([x=='.' for x in d[0]]):
        keys.append(get_heights(d))
    else:
        locks.append(get_heights(d,False))

fit = set()
for k in keys:
    L = len(k)
    for l in locks:
        valid = True
        for i in range(L):
            if k[i] + l[i] > L:
                valid = False
                break
        if valid:
            fit.add((tuple(k),tuple(l)))
print(len(fit))