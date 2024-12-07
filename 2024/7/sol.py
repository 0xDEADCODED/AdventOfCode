eqs = [(int(x[0]),list(map(int,x[1].split(' ')))) for x in [x.strip().split(': ') for x in open('in').readlines()]]
p1,p2 = 0,0

def operate(nums, total, totals, p2=False):
    if len(nums) == 0:
        totals.append(total)
        return

    next = nums.pop(0)
    operate(nums[:], total + next, totals,p2)
    operate(nums[:], total * next, totals,p2)
    if p2:
        concat = int(str(total) + str(next))
        operate(nums[:], concat, totals,p2)

for tv,nums in eqs:
    p1t,p2t = [],[]

    operate(nums[:],0,p1t)
    if tv in p1t: p1 += tv

    operate(nums,0,p2t,True)
    if tv in p2t: p2 += tv

print(f"{p1=} || {p2=}")