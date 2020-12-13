
def part2(pixels, ix=25, iy=6):
    render = []
    for y in range(iy):
        line = ''
        for x in range(ix):
            l = 0
            while pixels[l][x+(y*ix)] == '2':
                l +=1
            print(pixels[l][x+(y*ix)])
            line += pixels[l][x+(y*ix)]

        print(line)

    

def calculate():
    w = 25
    h = 6
    lines = [line.strip().replace('\n','') for line in open('./input.txt','r').read()]
    layers = [lines[i : i + w * h] for i in range(0, len(lines), w * h)]
    
    fewest_0 = min(layers, key=lambda x: x.count("0"))
    print(f"Part 1: {fewest_0.count('1')*fewest_0.count('2')}")

    print(f"Part 2:")
    for y in range(h):
        line = ""
        for x in range(w):
            l = 0
            while layers[l][x + (y * w)] == "2":
                l += 1
            line += layers[l][x + (y * w)]
        print(line.replace("1", chr(9608)).replace("0", " "))

    

if __name__ == '__main__':
    calculate()