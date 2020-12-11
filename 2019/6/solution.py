import math
from collections import defaultdict
def count_orbits(graph, curr, visited):
    if curr in visited or curr not in graph:
        return 0
    
    visited.add(curr)
    
    total = len(graph[curr])
    for edge in graph[curr]:
        total += count_orbits(graph, edge, visited)

    return total
    
def get_orbits(parent, name):
    while (name := parent[name]) :
        yield name

def calculate():
    rules = [x.strip().replace('\n','') for x in open('./input.txt', 'r').readlines()]
    
    graph = {}
    start = ''
    goal = ''

    for relationship in rules:
        a,b = relationship.split(')')
        if a not in graph:
            graph[a] = {b}
        else:
            graph[a].add(b)

        if 'YOU' in b:
            start = a
        if 'SAN' in b:
            goal = a

    print(graph)
    total = 0
    routes = []
    for x in graph:
        total += count_orbits(graph, x, set())
    
    print(f"Part 1: {total}")
    
    parent = defaultdict(str)

    for rel in rules:
        obj, orbit = rel.split(")")
        parent[orbit] = obj

    from_you = list(get_orbits(parent, "YOU"))
    from_san = list(get_orbits(parent, "SAN"))

    common = set(from_you).intersection(set(from_san))

    part_two = min(from_you.index(a) + from_san.index(a) for a in common)
    print(part_two)

if __name__ == '__main__':
    calculate()