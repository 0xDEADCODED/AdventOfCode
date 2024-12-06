from itertools import combinations
data,p1,p2,smallest = [int(x.strip()) for x in open('in').readlines()],0,0,int(10e9)

for i in range(2,len(data)):
    for comb in combinations(data, i):
        if sum(comb) == 150: 
            p1 += 1 
            smallest = min(smallest, len(comb))
            if len(comb) <= smallest: p2 += 1
            
print(f"{p1=} || {p2=}")