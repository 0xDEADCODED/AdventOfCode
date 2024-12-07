from functools import reduce
target,delivered,p1,p2 = 34000000,0,0,0

def factors(n):
    return set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

for house in range(1,11):
    facts = factors(house)
    d1 = sum(facts) * 10
    d2 = sum(d for d in facts if house // d <= 50) * 11

    if p1 == 0 and d1 >= target: p1 = house
    if p2 == 0 and d2 >= target: p2 = house

    if p1 and p2: break

print(f"{p1=} || {p2=}")