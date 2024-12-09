seed, step, div = 20151125, 252533, 33554393
tr,tc = 3010,3019

def next(s): return (s * step) % div

def get_points(start_x, start_y, end_x, end_y):
    result = []
    for i, j in zip(range(start_x, end_x), range(start_y, end_y, -1)):
        result.append((i,j))
    result.append((end_x,end_y))
    return result

diags = [[seed]]
for i in range(1,tr + (tc*2+1)):
    diag = []
    for r,c in get_points(0,i,i,0):
        seed = next(seed)
        diag.append(seed)
    diags.append(diag)

print(f"p1={diags[((tr-1)*2)+(tc-tr)][tc-1]}")