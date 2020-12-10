import re
    
def valid_count(si):
    counts = dict((i, si.count(i)) for i in si)
    
    for key,val in counts.items():
        if val == 2:
            index = si.index(key)
            try:
                if si[index - 1] == key:
                    return True
            except:
                pass

            try:
                if si[index + 1] == key:
                    return True
            except:
                pass

    return False

def calculate():
    valid = 0
    
    for i in range(387638, 919123):
        si = str(i)

        if valid_count(si):
            prev = si[0]
            met = True
            for j in range(1, len(si)):
                if int(si[j]) < int(prev):
                    met = False
                    break
                prev = si[j]
                
            if met:
                valid +=1

    print(valid)


if __name__ == '__main__':
    calculate()