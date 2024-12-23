from collections import defaultdict
import networkx as nx
data = [x.strip().split('-') for x in open('in').readlines()]
links = defaultdict(list)
trips = set()

for n1,n2 in data:
    links[n1].append(n2)
    links[n2].append(n1)

def find_loop(target,curr,path):
    if curr == target and path and len(path) == 3 and any([x.startswith('t') for x in path]):
        trips.add(tuple(sorted(path)))
    
    if len(path) > 3:
        return 
    
    for n in links[curr]:
        if n not in path:
            find_loop(target,n,path[:]+[n])

for k in links.keys():
    find_loop(k,k,[])

p1 = len(trips)

G = nx.Graph(data)
cliques = list(nx.find_cliques(G))
p2 = ','.join(sorted(max(cliques, key=len)))

print(f"{p1=} || {p2=}")