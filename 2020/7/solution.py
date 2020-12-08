
def parse_rules(rules):
    r_dic = {}
    
    for rule in rules:
        current_rule, deps = rule.split('bags contain')
        deps = deps.split(',')
        
        current_rule = current_rule.strip()
        r_dic[current_rule.strip()] = {}

        
        for dep in deps:
            parts = dep.replace('bags', '').replace('bag', '').split()
            
            if not parts[0].strip().isdigit():
                continue
            
            count = int(parts[0])
            bag_color = parts[1] + ' ' + parts[2]
            
            r_dic[current_rule][bag_color] = count
            
    return r_dic
    

def in_bag(r_dic, item, desired='shiny gold'):
    if not r_dic[item]:
        return False
    
    if item == desired:
        return True
    
    contains = False
    for dep in r_dic[item]:
        if dep == desired:
            return True
        contains |= in_bag(r_dic, dep)
        
    return contains
    

def find_valid_bags(r_dic, desired='shiny gold'):
    valid = 0
    
    for key, value in r_dic.items():
        if key == desired:
            continue

        for item in value:
            if in_bag(r_dic, item, desired):
                valid += 1
                break

    return valid


def count_bags(r_dic, item='shiny gold'):
    total = 0
    
    for key, value in r_dic[item].items():
        count = count_bags(r_dic, key) * value
        total += count + value

    return total
    

def calculate():
    rules = []
    with open('./input.txt', 'r') as fp:
        rules = fp.readlines()
        
    r_dic = parse_rules(rules)
    
    part1 = find_valid_bags(r_dic)
    print(f"Part 1: {part1}")
    
    part2 = count_bags(r_dic)
    print(f"Part 2: {part2}")

if __name__ == '__main__':
    calculate()