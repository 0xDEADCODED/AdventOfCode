def valid_pw(pw):
    # check for sequence
    num_seq = 0
    for i in range(len(pw)):
        if i + 2 < len(pw):
            t = [ord(pw[i]), ord(pw[i+1]), ord(pw[i+2])]
            if t[0] + 1 == t[1] and t[0] + 2 == t[2]:
                num_seq += 1
    if num_seq < 1: 
        return False

    if 'i' in pw or 'o' in pw or 'l' in pw: 
        return False

    #check for doubles
    dubs = []
    for i in range(len(pw)):
        if i + 1 < len(pw) and pw[i] == pw[i+1] and (i + 2 >= len(pw) or pw[i] != pw[i+2]) and (i-1 < 0 or pw[i-1] != pw[i]):
            dubs.append(pw[i]*2)
    if len(set(dubs)) < 2: return False

    return True

def increment_pw(pw):
    pw = list(pw)
    pos = -1
    while abs(pos) <= len(pw):
        if pw[pos] == 'z': pw[pos] = 'a'
        else:
            inc = chr(ord(pw[pos]) + 1)
            pw[pos] = inc
            if inc <= 'z': break

        pos -= 1
    return ''.join(pw)

def find_next_pw(pw, check=None):
    valid, inc_pos = False, 0
    while not valid:
        if (valid := valid_pw(pw)): continue
        pw = increment_pw(pw)

    if check: assert(pw == check)
    return pw
    

assert(valid_pw('hijklmmn') == False)
assert(valid_pw('abbceffg') == False)
assert(valid_pw('abbcegjk') == False)
find_next_pw('ghijklmn', 'ghjaabcc')
find_next_pw('abcdefgh', 'abcdffaa')
p1 = find_next_pw('vzbxkghb')
p2 = find_next_pw(increment_pw(p1))

print(f"{p1=} || {p2=}")

        
    
