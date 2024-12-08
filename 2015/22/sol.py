from copy import deepcopy
b = [int(x[1]) for x in [x.strip().replace(' ','').split(':') for x in open('in').readlines()]]
spells = [('mm',53), ('d',73), ('s',113), ('p',173), ('r',229)]
me_hp,me_mana,me_armor = 0,1,2
boss_hp,boss_d = 0,1
name,cost_turn = 0,1

def apply_effects(m, b, e):
    remove = []
    for i in range(len(e)):
        e[i][cost_turn] -= 1
        if e[i][cost_turn] == 0:
            remove.append(i)
        
        spell = e[i][name]
        if spell == 's' and e[i][cost_turn] == 0:
            m[me_armor] = 0
        elif spell == 'p':
            b[boss_hp] -= 3
        elif spell == 'r':
            m[me_mana] += 101

    for i in remove: e.pop(i)

def game_over(m,b, mana_spent):
    global min_mana
    if m[me_hp] <= 0:
        return int(10e9)
    if b[boss_hp] <= 0:
        min_mana = min(min_mana,mana_spent)
        return mana_spent
    return -1

def cast_spell(spell,me,boss,effects):
    me[me_mana] -= spell[cost_turn]
    if spell[name] == 'mm':
        boss[boss_hp] -= 4
    elif spell[name] == 'd':
        boss[boss_hp] -= 2
        me[me_hp] += 2
    elif spell[name] == 's':
        me[me_armor] = 7
        effects.append(['s',6])
    elif spell[name] == 'p':
        effects.append(['p',6])
    elif spell[name] == 'r':
        effects.append(['r',5])

def boss_attack(me,boss):
    me[me_hp] -= max(boss[boss_d] - me[me_armor],1)

def fight(m, b, turn, e, mana_spent, p2):
    if p2 and turn == 0: m[me_hp] -= 1

    if (status := game_over(m,b,mana_spent)) != -1:
        return status
    
    apply_effects(m, b, e)

    if (status := game_over(m,b,mana_spent)) != -1:
        return status

    ans = int(10e9)
    if turn == 0: # player turn
        for spell in spells:
            me, boss, effects = deepcopy(m), deepcopy(b), deepcopy(e)
            if  spell[cost_turn] <= me[me_mana] and spell[name] not in [x[name] for x in effects]:
                cast_spell(spell,me,boss,effects)
                
                if mana_spent + spell[cost_turn] > min_mana:
                    continue

                ans = min(ans, fight(me, boss, 1, effects, mana_spent+spell[cost_turn], p2))
    else: # boss turn
        me, boss, effects = deepcopy(m), deepcopy(b), deepcopy(e)
        boss_attack(me,boss)
        ans = min(ans,fight(me,boss,0,effects,mana_spent,p2))
    
    return min(ans,min_mana)

min_mana = int(10e9)
p1 = fight([50,500,0], b, 0, [], 0, False)
min_mana = int(10e9)
p2 = fight([50,500,0], b, 0, [], 0, True)

print(f"{p1=} || {p2=}")