data,p1,p2 = list(map(lambda x: [int(y) for y in x], [x.strip().split() for x in open('in').readlines()])),0,0

def valid(l):
    return all([((l[0] < l[1] and l[i] < l[i+1] and 1 <= l[i+1] - l[i] <= 3) or (not l[0] < l[1] and l[i] > l[i+1] and 1 <= l[i] - l[i+1] <= 3)) for i in range(len(l)-1)])

for l in data:
    if valid(l): p1 += 1; p2 += 1
    elif any([valid(x) for x in [l[:i] + l[i+1:] for i in range(len(l))]]): p2 += 1

print(f"{p1=} || {p2=}")
