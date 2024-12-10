import re
rooms = re.findall(r"(.*)-(\d+)\[(.*)\]", open('ex').read().strip())

def sort_counts(cnts):
    cnts = sorted(cnts,key=lambda x: x[1],reverse=True)
    return cnts

    for n in range(len(cnts) - 1, 0, -1):
        
        # Initialize swapped to track if any swaps occur
        swapped = False  

        # Inner loop to compare adjacent elements
        for i in range(n):
            if cnts[i] > cnts[i + 1]:
              
                # Swap elements if they are in the wrong order
                cnts[i], cnts[i + 1] = cnts[i + 1], cnts[i]
                
                # Mark that a swap has occurred
                swapped = True
        
        # If no swaps occurred, the list is already sorted
        if not swapped:
            break
    return cnts
    


p1 = 0
for (name,id,crc) in rooms:
    cnts,counted,valid = [],set(),True
    for n in name:
        if n != '-' and n not in counted:
            cnts.append((n, name.count(n)))
            counted.add(n)
    
    cnts = sort_counts(cnts)

    for i in range(len(crc)):
        if cnts[i][0] != crc[i] :#and not tie_breaker(cnts[i],cnts,crc):
            print(cnts[i][0],crc[i])
            valid = False
    print(name,id,crc,cnts,valid)