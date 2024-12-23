import re
data = list(map(lambda x: [int(y) for y in x],[re.findall(r"(\d+)",x.strip()) for x in open('in').readlines()]))
p1,p2 = sum(list(map(lambda x: max(x) - min(x),data))),0
for row in data:
    found = False
    for i in range(len(row)):
        for j in range(i+1,len(row)):
            mn,mx = min(row[i],row[j]), max(row[i],row[j])
            if mx % mn == 0:
                p2 += mx//mn
                found = True
                break
        if found: break

print(f"{p1=} || {p2=}")