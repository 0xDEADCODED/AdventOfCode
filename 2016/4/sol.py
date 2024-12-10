import re
rooms,p1,p2 = re.findall(r"(.*)-(\d+)\[(.*)\]", open('in').read().strip()),0,0
key = 'abcdefghijklmnopqrstuvwxyz'

def sort_counts(cnts):
    cnts = sorted(cnts,key=lambda x: x[1],reverse=True)
    for n in range(len(cnts) - 1, 0, -1):
        swapped = False
        for i in range(n):
            if cnts[i][1] == cnts[i+1][1] and cnts[i][0] > cnts[i + 1][0]:
                cnts[i], cnts[i + 1] = cnts[i + 1], cnts[i]
                swapped = True
        
        if not swapped: break
    return cnts
    
def shift(name,id):
    name = [x.strip() for x in list(name.replace('-', ' '))]
    for _ in range(int(id)):
        for n in range(len(name)):
            if n != ' ':
                name[n] = key[(key.index(name[n]) + 1) % 26]
    return ''.join(name)

for (name,id,crc) in rooms:
    cnts,counted,valid = [],set(),True
    for n in name:
        if n != '-' and n not in counted:
            cnts.append((n, name.count(n)))
            counted.add(n)
    
    cnts = sort_counts(cnts)

    for i in range(len(crc)):
        if cnts[i][0] != crc[i]: valid = False
    if valid: 
        p1 += int(id)
        if shift(name,id) == 'northpolewobjectwstorage':
            p2 = int(id)
        
print(f"{p1=} || {p2=}")