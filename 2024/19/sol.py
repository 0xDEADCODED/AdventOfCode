import heapq
from collections import defaultdict
data = open('in').read().strip().split('\n\n')
towels,arr,DP = [x.replace(' ','') for x in data[0].split(',')],data[1].split('\n'),defaultdict(int)

def solve_p1(p1=0):
    for a in arr:
        dq,seen = [],set()
        heapq.heappush(dq,(0,''))
        while dq:
            pos,build = heapq.heappop(dq)

            if (pos,build) in seen: continue

            seen.add((pos,build))

            if build == a:
                p1 += 1
                break

            for t in towels:
                if a[pos:pos+len(t)] == t:
                    heapq.heappush(dq,(pos+len(t),build+t))

    return p1

def count_arrs(towels, a):
    if a in DP: return DP[a]
    if len(a) == 0: return 0
    for i in range(1, len(a)+1):
        if a[:i] in towels:
            if len(a) == i:
                DP[a] += 1
            else:
                if (rest := count_arrs(towels, a[i:])) > 0:
                    DP[a] += rest

    return DP.get(a,0)


print(f"p1={solve_p1()} || p2={sum(count_arrs(towels, a) for a in arr)}")
