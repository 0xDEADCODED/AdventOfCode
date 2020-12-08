
class Landscape:
    
    def __init__(self, landscape, x=3, y=1):
        self.landscape = landscape
        self.n_trees = 0
        
        self.count_trees(x, y)
            
    def count_trees(self, x, y):
        current_x = x
        current_y = y
        self.n_trees = 0
        
        while current_x < len(self.landscape[0]) and current_y < len(self.landscape):
            if self.landscape[current_y][current_x] == b'#':
                self.n_trees += 1
                
            current_x += x
            current_y += y
            
        return self.n_trees

def calculate():
    landscape = []
    with open('./input.txt', 'rb') as fp:
        for line in fp:
            landscape.append([bytes([x]) for x in line.strip()] * 100)
    
    landscape = Landscape(landscape)

    total_trees = landscape.n_trees

    print(f"Part 1: {total_trees}")
    
    for x,y in [[1,1], [5, 1], [7, 1], [1, 2]]:
        total_trees *= landscape.count_trees(x,y)
        
    print(f"Part 2: {total_trees}")

if __name__ == '__main__':
    calculate()