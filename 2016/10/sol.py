from math import prod
inst = [x.strip().split() for x in open('in').readlines()]
robots = {}
p1 = 0

def add_robot_if_needed(i):
    if i[0] == 'value':
        if i[-2]+i[-1] not in robots:
            robots[i[-2]+i[-1]] = {'stones':[],'instructions':[]}
    else:
        if i[0]+i[1] not in robots:
            robots[i[0]+i[1]] = {'stones':[],'instructions':[]}
        if i[5]+i[6] not in robots:
            robots[i[5]+i[6]] = {'stones':[],'instructions':[]}
        if i[-2]+i[-1] not in robots:
            robots[i[-2]+i[-1]] = {'stones':[],'instructions':[]}

def more_to_do():
    return any([len(x['instructions']) != 0 for x in robots.values()])

def move_stones(bot,r):
    global p1
    if 61 in robots[bot]['stones'] and 17 in robots[bot]['stones']:
        p1 = bot[3:]
    low,high = r[0],r[1]
    mins,maxs = min(robots[bot]['stones']), max(robots[bot]['stones'])
    robots[low]['stones'].append(mins)
    robots[high]['stones'].append(maxs)
    robots[bot]['stones'] = []

for i in inst:
    add_robot_if_needed(i)
    
    if i[0] == 'value':
        robots[i[-2]+i[-1]]['stones'].append(int(i[1]))
    elif len(robots[i[0]+i[1]]['stones']) == 2:
        move_stones(i[0]+i[1],(i[5]+i[6],i[-2]+i[-1]))
    else:
        robots[i[0]+i[1]]['instructions'].append((i[5]+i[6],i[-2]+i[-1]))

while more_to_do():
    for k,v in robots.items():
        if len(v['stones']) == 2:
            move_stones(k,v['instructions'][0])
            v['instructions'].pop(0)

p2 = prod([v['stones'][0] for k,v in robots.items() if k == 'output0' or k == 'output1' or k == 'output2'])
print(f"p1={p1} || {p2=}")