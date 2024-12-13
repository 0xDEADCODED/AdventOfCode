import re
import numpy as np
data,machines = [x.strip() for x in open('in').read().strip().split('\n\n')],[]
A_COST,B_COST,MAX_PRESS = 3,1,100
A,B,P = 0,1,2

for m in data:
    machines.append(list(map(lambda x: (int(x[0]),int(x[1])),re.findall(r"\D*(\d+)\D*(\d+)\D*",m))))

def play(machine,factor=0):
    ax,ay = machine[A]
    bx,by = machine[B]
    px,py = machine[P]

    x, y = np.linalg.solve(np.array([[ax, bx], [ay, by]]), np.array([px+factor, py+factor]))
    if round(x, 2).is_integer() and round(y, 2).is_integer():
        return int(round(x, 0) * 3 + round(y, 0))
    return 0

p1,p2 = 0,0
for m in machines:
    p1 += play(m)
    p2 += play(m,10000000000000)

print(f"{p1=} || {p2=}")