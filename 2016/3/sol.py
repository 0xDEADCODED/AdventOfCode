import re
triangles = [list(map(int,x[0])) for x in [re.findall(f"(\d+)\s*(\d+)\s*(\d+)",x.strip()) for x in open('in').readlines()]]
p1,p2 = 0,0

for (a,b,c) in triangles:
    if a+b > c and a+c > b and b+c > a:
        p1 += 1


for r in range(len(triangles[0])):
    for c in range(0,len(triangles),3):
        a,b,c = triangles[c][r], triangles[c+1][r], triangles[c+2][r]
        if a+b > c and a+c > b and b+c > a:
            p2 += 1

print(f"{p1=} || {p2=}")