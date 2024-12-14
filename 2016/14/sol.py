from hashlib import md5
salt = 'zpqevtbw'
#salt = 'abc'

def get_triple(digest):
    for i in range(len(digest)-3):
        if len(set(digest[i:i+3])) == 1:
            return digest[i]
    return ''

def gen_keys(p2=False):
    possible,keys,i = [],[],0
    while len(keys) != 64:
        pt = salt + str(i)
        digest = md5(pt.encode()).hexdigest()
        if p2:
            for _ in range(2016):
                digest = md5(digest.encode()).hexdigest()

        rem = []
        for j,(si,ti,c,d) in enumerate(possible):
            if i <= ti and c*5 in digest:
                keys.append((si,d))
                if len(keys) == 64: 
                    break
                rem.append(j)

        possible = [possible[k] for k in range(len(possible)) if k not in rem]

        trip = get_triple(digest)
        if trip != '':
            possible.append((i,i+1000,trip,digest))

        i += 1
    return sorted(keys)[-1][0] if not p2 else sorted(keys)[-2][0]

p1 = gen_keys()
p2 = gen_keys(True)
print(f"{p1=} || {p2=}")