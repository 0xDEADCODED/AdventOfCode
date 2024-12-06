import re,json
p1,p2 = sum([int(x) for x in re.findall(r"-?\d+", open('in').read().strip())]),0
data = json.load(open('in'))

def parse_json(obj):
    if type(obj) == int: return obj
    if type(obj) == str: return 0
    
    total = 0
    if type(obj) == list:
        for o in obj: total += parse_json(o)
    elif type(obj) == dict:
        if 'red' not in obj and 'red' not in obj.values():
            for v in obj.values(): total += parse_json(v)

    return total

for j in data: p2 += parse_json(j)

print(f"{p1=} || {p2=}")
