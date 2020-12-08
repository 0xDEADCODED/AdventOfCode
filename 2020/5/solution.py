from math import ceil

HIGHEST_SEAT = -1

SEAT_MAP = {}

for i in range(128):
    SEAT_MAP[i] = [-1, -1, -1, -1, -1, -1, -1, -1]

class BoardingPass:
    
    def __init__(self, bpass):
        self.row = self.binary_search(0,127, bpass[:7])
        self.column = self.binary_search(0,7, bpass[7:])
        self.seat_id = self.row * 8 + self.column
        
        global HIGHEST_SEAT
        HIGHEST_SEAT = max(self.seat_id, HIGHEST_SEAT)
        
        global SEAT_MAP
        SEAT_MAP[self.row-1][self.column-1] = self.seat_id
        
    def binary_search(self, low, high, items):
        if len(items) == 1:
            if items[0] == 'F' or items[0] == 'L':
                return low
            if items[0] == 'B' or items[0] == 'R':
                return high
        
        counter = 0
        mid  = (low + high) / 2
        if items[0] == 'F' or items[0] == 'L':
            counter = self.binary_search(low, int(mid), items[1:])
        elif items[0] == 'B' or items[0] == 'R':
            counter = self.binary_search(ceil(mid), high, items[1:])
                
        return counter
                

def found_bounds(id):
    global SEAT_MAP
    
    found_low = False
    found_high = False
    
    for row in SEAT_MAP.values():
        for seat in row:
            if seat == id - 1:
                found_low = True
            elif seat == id + 1:
                found_high = True
                
    return found_low and found_high

def find_seat():
    global SEAT_MAP
    
    seat_id = -1
    for i in range(128):
        row = SEAT_MAP[i]
        if row.count(-1) == 1:
            seat_id = ((i+1) * 8) + (row.index(-1)+1)
            if found_bounds(seat_id):
                break
                
    return seat_id

def  calculate():
    global HIGHEST_SEAT
    global SEAT_MAP
    
    with open('./input.txt', 'r') as fp:
        for line in fp:
            BoardingPass(line.strip())

    print(f'Part 1: {HIGHEST_SEAT}')
    
    seat_id = find_seat()
       
    print(f"Part 2: {seat_id}")
        
if __name__  == '__main__':
    calculate()