from itertools import permutations, islice
presents, groups = [int(x.strip()) for x in open('ex').readlines()],[]

L = len(presents)
for p in permutations(presents):
    it = iter(p)
    for a in range(1,L+1):
        for b in range(1,L+1):
            for c in range(1,L+1):
                sliced =[list(islice(it, 0, i)) for i in [a,b,c]]
                if all(sliced):
                    s1,s2,s3 = sum(sliced[0]),sum(sliced[1]),sum(sliced[2])
                    if s1 == s2 and s1 == s3 and s2 == s3:
                        groups.append(sliced)

print(groups)
