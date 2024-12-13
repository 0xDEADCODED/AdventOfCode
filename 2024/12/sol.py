from collections import defaultdict
gardens = [list(x.strip()) for x in open('in').readlines()]
R,C = len(gardens),len(gardens[0])
locations = defaultdict(list)
plots = defaultdict(list)
seen = set()

def count_sides(plot):
    sides = 0
    for rr, cc in [(-1,0),(1,0),(0,-1),(0,1)]:
        seen = set()
        for (r,c) in plot:
            if (r,c) in seen or (r+rr, c+cc) in plot:
                continue

            sides += 1

            for step in (-1, 1):
                r1,c1 = r,c
                while (r1, c1) in plot and (r1+rr, c1+cc) not in plot:
                    seen.add((r1, c1))
                    r1 += cc * step
                    c1 += rr * step
    return sides

def perimeter(plot):
    edges = []
    for r,c in plot:
        for rr,cc in [(-1,0),(1,0),(0,-1),(0,1)]:
            if (r+rr,c+cc) not in plot and (r+rr,c+cc) not in edges:
                edges.append((r+rr,c+cc))
    return len(edges)

def traverse_plot(plant,r,c,plot):
    if r in range(R) and c in range(C) and gardens[r][c] == plant and (r,c) not in seen:
        plot.add((r,c))
        seen.add((r,c))
        for rr,cc in [(-1,0),(1,0),(0,-1),(0,1)]:
            traverse_plot(plant,r+rr,c+cc,plot)

for r in range(R):
    for c in range(C):
        locations[gardens[r][c]].append((r,c))

for k,v in locations.items():
    i = 0
    for (r,c) in v:
        if (r,c) not in seen:
            plot = set()
            traverse_plot(k,r,c,plot)
            plots[k+str(i)] = plot
            i += 1

p1,p2 = 0,0 
for k,v in plots.items():
    p1 += len(v)*perimeter(v)
    p2 += len(v) * count_sides(v)

print(f"{p1=} || {p2=}")

