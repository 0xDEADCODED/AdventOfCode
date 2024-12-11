comp = open('in').read().strip()

def decompress(comp,p2=False):
    build,i = '',0
    while i < len(comp):
        if comp[i] == '(':
            end = comp.find(')',i)
            num,rep = comp[i:end+1].replace('(','').replace(')','').split('x')
            seq = comp[end+1:end+int(num)+1]
            if not p2 or '(' not in seq:
                build += seq*int(rep)
            else:
                build += decompress(seq,p2) * int(rep)

            i = end+int(num)+1
        else:
            build += comp[i]
            i += 1
    return build

p1 = decompress(comp)
print(f"p1={len(p1)}")

# 1057308 too low
p2 = decompress(comp,True)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
print(f"p2={len(p2)}")
