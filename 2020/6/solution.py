import string

def count_answers(groups):
    total1 = 0
    total2 = 0
    
    for group in groups:
        group = group.split('\n')
        tracker = dict(zip(string.ascii_lowercase, [0]*26))
        for person in group:
            for answer in person:
                tracker[answer] += 1
            
        values = list(tracker.values())
        total1 += len(values) - values.count(0)
        total2 += values.count(len(group))
        
    return total1, total2

def calculate():
    groups = []
    
    with open('./input.txt', 'r') as fp:
        groups = fp.read().split('\n\n')
        
    total1, total2 = count_answers(groups)
    
    print(f'Part 1: {total1}')
    print(f'Part 2: {total2}')
    

if __name__ == '__main__':
    calculate()