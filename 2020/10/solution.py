
visited = {}
def count_valid_combos(lines, i):
    if i == len(lines)-1:
        return 1

    if i in visited:
        return visited[i]

    routes = 0
    for j in range(i+1, len(lines)):      
        if lines[j] - lines[i] <= 3:
            routes += count_valid_combos(lines, j)

    visited[i] = routes
    return routes
    

def calculate():
    lines = [int(line) for line in open('./input.txt', 'r').readlines()]
    lines.append(0)
    lines = sorted(lines)
    lines.append(max(lines)+3)
    print(lines)

    one = 0
    three = 0
    for i in range(len(lines)-1):
        diff = lines[i+1] - lines[i]
        if diff == 1:
            one += 1
        if diff == 3:
            three += 1
    
    print(f"Part 1: {three*one}")

    part2 = count_valid_combos(lines, 0)
    print(f"Part 2: {part2}")

if __name__ == '__main__':
    calculate()