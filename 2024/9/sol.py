def convert(fs):
    converted, blocks, fs1,fs2, id = [], [], [], [], 0
    for i in range(0,len(fs),2):
        if i < len(fs) - 1: 
            block = [id, len(converted)]
            converted += [id]*int(fs[i])
            block.append(len(converted)-1)
            blocks.insert(0,(block))
            free_space = [j for j in range(len(converted), len(converted) + int(fs[i+1]))]
            if free_space:
                fs1 += free_space
                fs2.append(free_space)
            converted += ['.']*int(fs[i+1])
        else: 
            block = [id, len(converted)]
            converted += [id]*int(fs[i])
            block.append(len(converted)-1)
            blocks.insert(0,(block))

        id += 1
    return converted, blocks, fs1, fs2

def done_moving(mem_map, c):
    found_free_space = False
    for i in range(c,len(mem_map)):
        if mem_map[i] == '.' and not found_free_space:
            found_free_space = True
            continue

        if found_free_space and mem_map[i] != '.':
            return False
        
    return True

def defragment_p1(mem_map, free_spaces, mm_len):
    i,c = mm_len-1,0
    while not done_moving(mem_map,c) and free_spaces:
        if mem_map[i] != '.':
            to_move = mem_map[i]
            mem_map[i] = '.'
            c = free_spaces.pop(0)
            mem_map[c] = to_move
        i -= 1

def defragment_p2(mem_map, blocks,free_spaces):
    while blocks and free_spaces:
        id,s,e = blocks.pop(0)
        cnt = e-s+1

        found = -1
        for j in range(len(free_spaces)):
            if cnt <= len(free_spaces[j]) and free_spaces[j][0] < s:
                found = j
                break

        if found == -1:
            continue

        space = free_spaces.pop(found)
        for _ in range(cnt):
            nxt = space.pop(0)
            mem_map[nxt] = id

        if space:
            free_spaces.insert(found,space)

        for j in range(s,s+cnt):
            mem_map[j] = '.'

def calculate_checksum(mem_map):
    crc,mm_len = 0, len(mem_map)
    for i in range(mm_len):
        if mem_map[i] != '.':
            crc += mem_map[i] * i
    
    return crc

fs = open('in').read().strip()

### PART 1 ###
mem_map,_,free_spaces,_ = convert(fs)
mm_len = len(mem_map)
defragment_p1(mem_map, free_spaces, mm_len)
p1 = calculate_checksum(mem_map)

### PART 2 ###
# 8450064123278 too high
mem_map,blocks,_,free_spaces = convert(fs)
defragment_p2(mem_map, blocks, free_spaces)
p2 = calculate_checksum(mem_map)

print(f"{p1=} || {p2=}")
