from collections import Counter
data = [x.strip() for x in open('in').readlines()]
cols = [[l[i] for l in data] for i in range(len(data[0]))]
p1 = ''.join(sorted(list(Counter(c).items()),key=lambda k: k[1],reverse=True)[0][0] for c in cols)
p2 = ''.join(sorted(list(Counter(c).items()),key=lambda k: k[1])[0][0] for c in cols)


print(f"{p1=} || {p2=}")
