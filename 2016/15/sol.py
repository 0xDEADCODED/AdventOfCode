import re 

discs = list(map(lambda x: [int(x[0]),int(x[1]),int(x[2])],[re.findall(r"#(\d+) has (\d+) .* (\d)",x)[0] for x in open('in').readlines()]))
ID,NUM,POS = 0,1,2

def sim():
    found,i = False,0
    while not found:
        valid = True
        for j in range(len(discs)):
            if (discs[j][POS] + (i+j+1)) % discs[j][NUM] != 0:
                valid = False
                break
        if valid: found = True
        else: i += 1
    return i

p1 = sim()
discs.append([0,11,0])
p2 = sim()
print(f"{p1=} || {p2=}")