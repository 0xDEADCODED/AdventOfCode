import re
ips = [x.strip() for x in open('in').readlines()]
a1,a2 = [],[]
def contains_abba(s):
    for l in s:
        L = len(l)
        for i in range(L):
            if i+1 < L and i+2 < L and i+3 < L and l[i] != l[i+1] and l[i] == l[i+3] and l[i+1] == l[i+2]:
                return True
    return False

def get_abas(s):
    s = ''.join(s)
    abas = []
    L = len(s)
    for i in range(L-2):
        if s[i] == s[i+2] and s[i] != s[i+1]:
            abas.append(s[i:i+3])
    
    return abas

def contains_bab(s, abas):
    s = ''.join(s)
    L = len(s)
    for i in range(L-2):
        if s[i] == s[i+2] and s[i] != s[i+1] and s[i+1]+s[i]+s[i+1] in abas:
            return True
    return False

p1,p2 = 0,0
for ip in ips:
    hypernets = re.findall(r"\[([^\[\]]*)\]", ip)
    supernets = [x for m in re.findall(r"([^\[]*)?\[[^\[\]]*\]([^\[]*)?", ip) for x in m if x]
    
    if not contains_abba(hypernets) and contains_abba(supernets):
        p1 += 1
    
    if (abas := get_abas(supernets)) and contains_bab(hypernets,abas):
        p2 += 1
    

print(f"{p1=} || {p2=}")