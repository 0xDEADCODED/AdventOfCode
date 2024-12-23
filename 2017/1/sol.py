captcha = open('in').read().strip()
L = len(captcha)

p1,p2 = 0,0
for i in range(L):
    if captcha[i] == captcha[(i+1)%L]:
        p1 += int(captcha[i])
    if captcha[i] == captcha[(i+(L//2))%L]:
        p2 += int(captcha[i])

print(f"{p1=} || {p2=}")