cnt = 3014387

def pass_gifts(n,k,p1=True):
    f = 1
    while (k ** f) <= n:
        f += 1
    if p1:
        current = k ** (f - 1)
        return k * (n - current) + 1
    else:
        current = k ** (f - 1) + 1
        inc2 = k ** f * 2 // k
        return max(2 * (n - inc2), 0) + (min(n, inc2) - current) + 1

p1 = pass_gifts(cnt,2)
p2 = pass_gifts(cnt,3,False)
print(f"{p1=} || {p2=}")