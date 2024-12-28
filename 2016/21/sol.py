moves = [x.strip().split(' ') for x in open('in').readlines()]

def swap_pos(seed,a,b):
    t = seed[a]
    seed[a] = seed[b]
    seed[b] = t

def rotate_right(seed,n):
    return seed[-n:] + seed[:-n]

def rotate_left(seed,n):
    return seed[n:] + seed[:n]

def scramble(seed,reverse=False):
    for m in moves[::-1] if reverse else moves:
        if m[0] == 'swap':
            if m[1] == 'position':
                a = int(m[2])
                b = int(m[-1])
                swap_pos(seed,a,b)
            else:
                assert m[1] == 'letter'
                a = seed.index(m[2])
                b = seed.index(m[-1])
                swap_pos(seed,a,b)
        elif m[0] == 'rotate':
            if m[1] == 'left':
                n = int(m[2])
                if reverse:
                    seed = rotate_right(seed,n)
                else:
                    seed = rotate_left(seed,n)
            elif m[1] == 'right':
                n = int(m[2])
                if reverse:
                    seed = rotate_left(seed,n)
                else:
                    seed = rotate_right(seed,n)
            else:
                assert m[1] == 'based'
                n = seed.index(m[-1])
                if reverse:
                    cnt = (n // 2 + (1 if ((n % 2) or not n) else 5))
                    seed = rotate_left(seed,cnt)
                else:
                    cnt = n + 1
                    if n >= 4:
                        cnt += 1
                    seed = rotate_right(seed,cnt)
        elif m[0] == 'reverse':
            a = int(m[2])
            b = int(m[-1])
            y = seed[a:b+1]
            seed = seed[:a] + y[::-1] + seed[b+1:]
        else:
            assert m[0] == 'move'
            a = int(m[2])
            b = int(m[-1])
            if reverse:
                seed.insert(a,seed.pop(b))
            else:
                seed.insert(b,seed.pop(a))

    return ''.join(seed)


p1 = scramble(list('abcdefgh'))
p2 = scramble(list('fbgdceah'),True)
print(f"{p1=} || {p2=}")
