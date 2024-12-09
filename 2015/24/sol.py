from itertools import combinations
presents, groups = sorted([int(x.strip()) for x in open('in').readlines()], reverse=True),[]
p1,p1_ml = 0,int(10e9)
p2,p2_ml = 0,int(10e9)

def product(l):
    total = 1
    for i in l: total *= i
    return total

def valid(g,rest):
    check = str(sum(rest) / sum(g))
    common = len(check) == 3 and check[-1] == '0'
    return common and check[0] == '2', common and check[0] == '3'

for s in range(2,len(presents)+1):
    for g in combinations(presents, s):
        rest = [x for x in presents if x not in g]
        
        p1v,p2v = valid(g,rest)
        if p1v and len(g) <= p1_ml:
            p1_ml = min(p1_ml,len(g))
            prod = product(g)
            p1 = prod if p1 == 0 else min(p1,prod)
        elif p2v and len(g) <= p2_ml:
            p2_ml = min(p2_ml,len(g))
            prod = product(g)
            p2 = prod if p2 == 0 else min(p2,prod)
    
    if p1 and p2: break

print(f"{p1=} || {p2=}")
