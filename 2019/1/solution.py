

def calc_fuel(mass):
    return int(mass/3) - 2

def calculate():
    inputs = []
    
    with open('./input.txt', 'rb') as fp:
        inputs = [int(line.strip()) for line in fp]
        
    sum = 0
    for i in inputs:
        fuel = calc_fuel(i)
        sum += fuel
        while fuel != 0:
            fuel = max(0, calc_fuel(fuel))
            sum += fuel
        
    print(sum)


if __name__ == '__main__':
    calculate()