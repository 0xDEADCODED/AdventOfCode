from functools import cache

@cache
def blink(stone, i):
    if i == 0: 
        return 1
    if stone == 0: 
        return blink(1, i - 1)
    if len(s := str(stone)) % 2 == 0: 
        return blink(int(s[:len(s) // 2]), i - 1) + blink(int(s[len(s) // 2:]), i - 1)
    return blink(stone * 2024, i - 1)

stones = open('in').read().split()
p1 = sum(blink(int(stone), 25) for stone in stones)
p2 = sum(blink(int(stone), 75) for stone in stones)

print(f"{p1=} || {p2=}")