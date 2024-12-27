ranges = [range(int(x.strip().split('-')[0]),int(x.strip().split('-')[1])+1) for x in open('in').readlines()]
max_ip = max([x.stop for x in ranges])+1

i = 0
allowed = []
while i < max_ip:
    valid = True
    for r in ranges:
        if i in r:
            valid = False
            break
    if valid:
        print(f"found: {i}")
        allowed.append(i)
    i +=1

print(min(allowed))
print(len(allowed))