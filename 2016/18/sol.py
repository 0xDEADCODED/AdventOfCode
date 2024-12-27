rows = [x.strip() for x in open('in').readlines()]

def get(r,i):
    if i not in range(len(r)):
        return '.'
    return r[i]

def gen_row(prev):
    nr = ''
    for i in range(len(prev)):
        l = get(prev,i-1)
        c = get(prev,i)
        r = get(prev,i+1)

        if l == '^' and c == '^' and r == '.':
            nr += '^'
        elif r == '^' and c == '^' and l == '.':
            nr += '^'
        elif l == '^' and c == '.' and r == '.':
            nr += '^'
        elif r == '^' and c == '.' and l == '.':
            nr += '^'
        else:
            nr += '.'
    return nr

def get_rows(r,cnt):
    for _ in range(cnt-1):
        r.append(gen_row(r[-1]))
    return r
    
p1 = sum([x.count('.') for x in get_rows(rows[:],40)])
p2 = sum([x.count('.') for x in get_rows(rows[:],400000)])
print(f"{p1=} || {p2=}")