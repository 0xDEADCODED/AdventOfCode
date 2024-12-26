a = list('01111001100111011')

def dragon(a,l):
    while len(a) < l:
        b = a[:][::-1]
        zeros = [i for i in range(len(b)) if a[i] == '0']
        ones = [i for i in range(len(b)) if a[i] == '1']
        for i in zeros: b[i] = '1'
        for i in ones: b[i] = '0'
        a = a + ['0'] + b[::-1]
    return a

def crc(checksum):
    while True:
        build = []
        for i in range(0,len(checksum),2):
            if checksum[i] == checksum[i+1]:
                build.append('1')
            else:
                build.append('0')

        checksum = build
        if len(checksum) % 2 != 0:
            break
    return ''.join(checksum)

p1 = crc(dragon(a,272)[:272])
p2 = crc(dragon(a,35651584)[:35651584])

print(f"{p1=} || {p2=}")