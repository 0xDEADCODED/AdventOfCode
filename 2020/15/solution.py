from collections import defaultdict

turn = 1

def find_num(spoken, previous, goal=2020):
    global turn
    while turn <= goal:
        if len(spoken[previous]) == 1:
            spoken[0].append(turn)
            previous = 0
        else:
            last = spoken[previous]
            speak = (last[-1]) - (last[-2])
            spoken[speak].append(turn)
            previous = speak
            
        turn += 1

    return previous

def calculate():
    global turn
    spoken = defaultdict(list)
    for x in open('./input.txt','r').read().split(','):
        spoken[int(x)].append(turn)
        turn += 1

    res = find_num(spoken, list(spoken.keys())[-1], 2020)
    print(f"Part 1: {res}")

    res = find_num(spoken, res, 30000000)
    print(f"Part 2: {res}")
                


if __name__ == '__main__':
    calculate()