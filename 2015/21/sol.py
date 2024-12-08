import re

b,store,p1, p2 = [int(x[1]) for x in [x.strip().replace(' ','').split(':') for x in open('in').readlines()]],{},int(10e9),0
s = [x.split('\n') for x in open("store").read().strip().split('\n\n')]
IN,IC,ID,IA = 0,1,2,3
PHP,PD,PA = 0,1,2

for inv in s:
    t = re.findall(r"(Weapons|Armor|Rings):", inv[0])[0]
    store[t.lower()] = []
    for e in inv[1:]:
        (n,c,d,a) = re.findall(r"(Damage?\s?\S*|Defense?\s?\S*|\S*)\s*(\d+)\s*(\d+)\s*(\d+)", e)[0]
        store[t.lower()].append((n.lower(),int(c),int(d),int(a)))

def fight_won(m):
    me, boss, turn = m[:], b[:], 0
    while me[PHP] > 0 and boss[PHP] > 0:
        if turn == 0:
            damage = me[PD] - boss[PA]
            boss[PHP] -= max(damage,1)
            turn = 1
        else:
            damage = boss[PD] - me[PA]
            me[PHP] -= max(damage,1)
            turn = 0
    
    return me[PHP] > 0

def update_stats(me, cost, item):
    return [me[PHP], me[PD] + item[ID], me[PA] + item[IA]], cost + item[IC]

def rings(m,c):
    global p1,p2
    for r1 in store['rings']:
        me,c1 = update_stats(m, c, r1)
        
        if fight_won(me): p1 = min(p1,c1)
        else: p2 = max(p2,c1)

        for r2 in store['rings']:
            if r1 == r2: continue
            me2,c2 = update_stats(me, c1, r2)
            if fight_won(me2): p1 = min(p1,c2)
            else: p2 = max(p2,c2)
            
for weapon in store['weapons']:
    m,cost = update_stats([100,0,0],0,weapon)

    # try 0 armor, 0 rings
    if fight_won(m):p1 = min(p1,cost)
    else: p2 = max(p2,cost)
    
    # try 0 armor, and 1-2 rings
    rings(m,cost)

    for armor in store['armor']:
        me,c1 = update_stats(m,cost,armor)

        # try 1 armor, 0 rings
        if fight_won(me): p1 = min(p1,c1)
        else: p2 = max(p2,c1)

        # try 1 armor, 1-2 rings
        rings(me,c1)

print(f"{p1=} || {p2=}")