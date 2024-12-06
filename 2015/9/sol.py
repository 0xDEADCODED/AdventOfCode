import itertools
 
data = open("in").read().splitlines()
data = [d.split(' ') for d in data]
 
path = {}
locations = []
 
for d in data:
    city1 = d[0]
    city2 = d[2]
    distance = int(d[4])
 
    path[city1 + city2] = distance
    path[city2 + city1] = distance
 
    locations.append(city1)
    locations.append(city2)
 
locations = set(locations)  # find unique locations
 
#print(locations)
#print(path)
 
# find shortest and longest route
shortest = 999999
longest = 0
for route in itertools.permutations(locations):
    route_length = 0
    for city1, city2 in zip(route[:-1], route[1:]):
        route_length += path[city1 + city2]
    if route_length < shortest:
        shortest = route_length
    if route_length > longest:
        longest = route_length
    #print(route, route_length)
 
print("Shortest route length:", shortest)
print("Longest route length:", longest)