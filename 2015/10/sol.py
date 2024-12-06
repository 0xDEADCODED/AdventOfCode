data,p1 = '3113322113',0

for j in range(50):
    if j == 40: p1 = len(data)
    build,i = '', 0
    while i < len(data):
        c,cnt = data[i], 1
        for j in range(i+1,len(data)):
            if data[j] == c:
                cnt += 1
            else:
                break
        build += str(cnt) + c
        i += cnt
    data = build

print(f"{p1=}, p2={len(data)}")

