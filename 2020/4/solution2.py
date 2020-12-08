import re

NUM_ATTRS = 7

validators = {
    'byr' : re.compile(r'byr:(19[2-9][0-9]|200[0-2])'),
    'iyr' : re.compile(r'iyr:(201[0-9]|2020)'),
    'eyr' : re.compile(r'eyr:(202[0-9]|2030)'),
    'hgt' : re.compile(r'hgt:((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)'),
    'hcl' : re.compile(r'hcl:(#([0-9a-f]{6}))'),
    'ecl' : re.compile(r'ecl:(amb|blu|brn|gry|grn|hzl|oth)'),
    'pid' : re.compile(r'pid:([0-9]{9})'),
}

def calculate():
    valid = 0
    with open('./input.txt', 'r') as fp:
        
        passports = fp.read().replace("\n"," ").split("  ")
        for p in passports:
            found = 0
            
            if re.search(r'byr:(19[2-9][0-9]|200[0-2])\b', p):
                found += 1
            if re.search(r'iyr:(201[0-9]|2020)\b', p):
                found += 1
            if re.search(r'eyr:(202[0-9]|2030)\b', p):
                found += 1
            if re.search(r'hgt:((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)\b', p):
                found += 1
            if re.search(r'hcl:(#([0-9a-f]{6}))\b', p):
                found += 1
            if re.search(r'ecl:(amb|blu|brn|gry|grn|hzl|oth)\b', p):
                found += 1
            if re.search(r'pid:([0-9]{9})\b', p):
                found += 1
                
            if found == NUM_ATTRS:
                valid +=1
            
    print(f"Part 2: {valid}")
    

if __name__ == '__main__':
    calculate()
    
    
"""
byr:((19[0-9][0-9]|200[0-2]) )|iyr:((201[0-9]|2020) )|eyr:((202[0-9]|2030) )|hgt:(((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in))|hcl:#([0-9]{1}|[a-f]{1}){6}|ecl:(amb|blu|brn|gry|grn|hzl|oth)|pid:([0-9]){9} 
"""
# SPACE AFTER END OF REGEX

#byr
#byr:(19[0-9][0-9]|200[0-2]) 

#iyr
#iyr:(201[0-9]|2020) 

#eyr
#eyr:(202[0-9]|2030) 

#hgt
#hgt:(((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in))

#hcl
#hcl:#([0-9]{1}|[a-f]{1}){6} 

#ecl
#ecl:(amb|blu|brn|gry|grn|hzl|oth) 

#pid
#