import itertools

def calculate():
    inputs = []
    with open("./input.txt", 'rb') as fp:
        inputs = [int(line.strip()) for line in fp]
    
    for a,b,c in itertools.combinations(inputs, 3):
        if(a+b+c == 2020):
            print(f"a: {a}")
            print(f"b: {b}")
            print(f"c: {c}")
            print(f"Product: {a*b*c}")


if __name__ == '__main__':
    calculate()