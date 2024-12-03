import re
valid, p1, p2, do = re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", open("in").read().strip()), 0, 0, True

for l in valid:
    if l == 'do()': do = True
    elif l == "don't()": do = False
    else: p1,p2 = (lambda x,y,z: (x+z,y+z if do else y+0))(p1,p2,(lambda x: int(x[0]) * int(x[1]))(re.findall(r"\d{1,3}",l)))

print(f"{p1=} || {p2=}")