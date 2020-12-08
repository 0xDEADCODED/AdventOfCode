
ATTRS = [b'byr', b'iyr', b'eyr', b'hgt', b'hcl', b'ecl', b'pid', b'cid']


class Passports:
    
    def __init__(self, passports):
        self.passports = passports
        self.valid = 0
        
        self.count_valid_passports()
        
    def count_valid_passports(self):
        for passport in self.passports:
            if len(passport.keys()) == len(ATTRS):
                self.valid +=1
            elif len(passport.keys()) == len(ATTRS) -1 and b'cid' not in passport.keys():
                self.valid +=1

def calculate():
    passports = []
    
    with open('./input.txt', 'rb') as fp:
        lines = fp.read().split(b'\n\n')
        for p in lines:
            replaced = p.replace(b'\n', b' ')
            items = replaced.split(b' ')
            passport = {}
            for field in items:
                attr, val = field.split(b':')
                passport[attr] = val
            passports.append(passport)
        
    passports = Passports(passports)
    
    print(f"Part 1: {passports.valid}")


if __name__ == '__main__':
    calculate()