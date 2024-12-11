import re
comp = open('in').read().strip()

def decompress(comp,p2=False):
    bracket = re.search(r'\((\d+)x(\d+)\)', comp)
    if not bracket:
        return len(comp)
    pos = bracket.start(0)
    num_chars = int(bracket.group(1))
    rep = int(bracket.group(2))
    i = pos + len(bracket.group())
    return  len(comp[:pos]) + decompress(comp[i:i+num_chars],p2) * rep + decompress(comp[i+num_chars:],p2) if p2 else \
        len(comp[:pos]) + len(comp[i:i+num_chars]) * rep + decompress(comp[i+num_chars:],p2)

p1 = decompress(comp)
p2 = decompress(comp,True)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
print(f"{p1=} || {p2=}")
