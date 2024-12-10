from hashlib import md5
id,p1,p2 = 'ffykfhsq','',[False]*8

for i in range(1000000000):
    hash = md5((id+str(i)).encode()).hexdigest()
    if hash[:5] == '00000':
        if len(p1) < 8: p1 += hash[5]
        if hash[5].isdigit():
            idx = int(hash[5])
            if 0 <= idx <= 7 and p2[idx] == False: p2[int(hash[5])] = hash[6]
    if len(p1) == 8 and all(p2):
        break

print(f"p1={p1} || p2={''.join(p2)}")