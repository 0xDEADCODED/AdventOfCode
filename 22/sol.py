from collections import defaultdict
seeds = dict((x,x) for x in [int(x.strip()) for x in open('in').readlines()])
mix,prune = lambda val,secret: val ^ secret, lambda val: val % 16777216
changes = defaultdict(int)

for s in seeds:
    seq,seen = [s%10],set()
    for i in range(2000):
        seeds[s] = prune(mix(seeds[s]*64,seeds[s]))
        seeds[s] = prune(mix(seeds[s] // 32,seeds[s]))
        seeds[s] = prune(mix(seeds[s]*2048,seeds[s]))

        seq.append(seeds[s] % 10)
        if len(seq) == 5:
            cs = tuple([seq[j+1] - seq[j] for j in range(len(seq)-1)])
            if cs not in seen:
                changes[cs] += seeds[s] % 10
                seen.add(cs)
            seq.pop(0)

p1,p2 = sum(seeds.values()),max(v for v in changes.values())

print(f"{p1=} || {p2=}")