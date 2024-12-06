import re
data = [x.strip() for x in open("in").readlines()]
counts,p2 = list(map(lambda l: (len(l),len(eval(l))),data)),0

for l in data:
    build = '"'
    for i in range(len(l)):
        if l[i] == '"': build += '\\"'
        elif l[i] == '\\': build += '\\\\'
        else:build += l[i]
    build += '"'
    p2 += len(build)
print(f"p1={sum([x[0] for x in counts]) - sum([x[1] for x in counts])} || p2={p2 - sum([x[0] for x in counts])}")