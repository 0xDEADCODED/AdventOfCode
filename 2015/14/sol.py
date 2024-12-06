import re
data,facts,stats = re.findall(r"(.*) can.* (\d+) km\/s .* (\d+) seconds, .* (\d+) seconds", open('in').read().strip()),{},{}
for (p,s,d,r) in data:
    facts[p] = {}
    facts[p]['kms'] = int(s)
    facts[p]['fly_time'] = int(d)
    facts[p]['rest_time'] = int(r)
    stats[p] = {'dist':0,'ft':0,'rt':0,'pts':0}

for _ in range(2503):
    for r in stats.keys():
        if stats[r]['ft'] < facts[r]['fly_time']: 
            stats[r]['dist'] += facts[r]['kms']
            stats[r]['ft'] += 1
        elif stats[r]['rt'] < facts[r]['rest_time']:
            stats[r]['rt'] += 1
        else:
            stats[r]['rt'] = 0
            stats[r]['ft'] = 1
            stats[r]['dist'] += facts[r]['kms']

    winning = max([x['dist'] for x in stats.values()])
    for k in stats.keys():
        if stats[k]['dist'] == winning:
            stats[k]['pts'] += 1

print(f"p1={winning} || p2={max([x['pts'] for x in stats.values()])}")