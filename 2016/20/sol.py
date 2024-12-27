ranges = sorted([(int(x.strip().split('-')[0]),int(x.strip().split('-')[1])+1) for x in open('in').readlines()])

range_unions = []
for begin,end in ranges:
    if range_unions and range_unions[-1][1] >= begin - 1:
        range_unions[-1] = range(range_unions[-1][0], end)
    else:
        range_unions.append(range(begin, end))

max_ip = max([x.stop for x in range_unions])
i = 0
allowed = []
while i < max_ip:
    valid = True
    for r in range_unions:
        if i in r:
            valid = False
            i = r.stop
            break
    if valid:
        allowed.append(i)
        i +=1

p1 = min(allowed)
p2 = len(allowed)
print(f"{p1=} || {p2=}")