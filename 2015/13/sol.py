import re, itertools

data,choices = re.findall(r"(.*) would (gain|lose) (\d+) .* (.*).", open('in').read().strip()), {}
for (s,op,val,n) in data:
    if s not in choices: choices[s] = {}
    choices[s][n] = int(val) if op == 'gain' else -int(val)

def max_happiness():
    max_happy = 0
    for a in itertools.permutations(choices.keys()):
        happy = 0
        for p1, p2 in zip(a, a[1:]): 
            happy += choices[p1][p2] + choices[p2][p1]
        happy += choices[a[0]][a[-1]] + choices[a[-1]][a[0]]
        
        max_happy = max(max_happy,happy)
    return max_happy

p1 = max_happiness()
for p in choices.keys(): choices[p]['me'] = 0
choices['me'] = {}
for p in choices.keys(): choices['me'][p] = 0
p2 = max_happiness()

print(f"{p1=} || {p2=}")