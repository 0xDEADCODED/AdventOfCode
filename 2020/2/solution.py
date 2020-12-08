

class Password:
    def __init__(self, input):
        parts = input.split()
        range = parts[0].split(b'-')
        self.low = int(range[0])
        self.high = int(range[1])
        self.letter = parts[1].replace(b':', b'').strip()
        self.password = parts[2].strip()
        self.p1_valid = False
        self.p2_valid = False
        self.validate()
        
    def validate(self):
        counter = 0
        
        for x in self.password:
            counter += 1 if self.equal(x) else 0
        
        if counter in range(self.low, self.high+1):
            self.p1_valid = True
    
        if (self.low_set() and not self.high_set()) or (self.high_set() and not self.low_set()):
            self.p2_valid = True
    
    def equal(self, c):
        return c == int.from_bytes(self.letter, "big") 
    
    def low_set(self):
        return self.equal(self.password[self.low-1])
    
    def high_set(self):
        return self.equal(self.password[self.high-1])
    
    def print_pass(self):
        print(f"Bounds: {self.low} - {self.high}")
        print(f"Letter: {self.letter}")
        print(f"Password: {self.password}")
        print(f"Valid: {self.valid}")
        print()

def calculate():
    p1_valid = 0
    p2_valid = 0
    
    with open('./input.txt', 'rb') as fp:
        for line in fp:
            p = Password(line)
            p1_valid += 1 if p.p1_valid else 0
            p2_valid += 1 if p.p2_valid else 0
            
    print(f"Part 1: {p1_valid}")
    print(f"Part 2: {p2_valid}")

if __name__ == '__main__':
    calculate()