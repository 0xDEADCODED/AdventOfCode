import sys

l1,l2 = list(map(sorted, map(list,zip(*[[int(z) for z in y] for y in [x.strip('\n').split() for x in open(sys.argv[1]).readlines()]]))))
p1,p2 = sum(list(map(lambda x,y: abs(x-y), l1, l2))), sum(list(map(lambda x,y: x*y, l1, [l2.count(z) for z in l1])))
print(f"{p1=} || {p2=}")