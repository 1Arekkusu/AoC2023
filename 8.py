import numpy

map = numpy.full((26,26,26,2), 0)

#part 1

ans1 = 0
id = 0

with open("advent2023\input.txt", 'r') as f:
    for line in f:
        line = line.strip()
        line = line.replace('(', ' ')
        line = line.replace(')', ' ')
        line = line.replace(',', ' ')
        line = line.replace('=', ' ')
        letters = line.split()
        if id == 0:
            id = 1
            directions = line
        if(len(letters) == 3):
            start1 = ord(letters[0][0]) - 65
            start2 = ord(letters[0][1]) - 65
            start3 = ord(letters[0][2]) - 65

            map[start1][start2][start3][0] = (ord(letters[1][0]) - 65) * 10000 + (ord(letters[1][1]) - 65) * 100 + (ord(letters[1][2]) - 65)
            map[start1][start2][start3][1] = (ord(letters[2][0]) - 65) * 10000 + (ord(letters[2][1]) - 65) * 100 + (ord(letters[2][2]) - 65)

k = -1
poz1 = 0
poz2 = 0
poz3 = 0
while True:
    ans1 += 1
    k += 1
    if k == len(directions):
        k = 0
    if directions[k] == 'L':
        move = 0
    else:
        move = 1
    if(map[poz1][poz2][poz3][move] == 252525):
        break
    next1 = map[poz1][poz2][poz3][move] // 10000
    next2 = map[poz1][poz2][poz3][move] % 10000 // 100
    next3 = map[poz1][poz2][poz3][move] % 100 
    poz1 = next1
    poz2 = next2
    poz3 = next3
    break

#part 2

def CMMDC(a, b):
    while(b != 0):
        r = a % b
        a = b
        b = r
    return a

map = numpy.full((26,26,26,2), 0)

poz = []
ans2= 0
id = 0

with open("advent2023\input.txt", 'r')as f:
    for line in f:
        line = line.strip()
        line = line.replace('(', ' ')
        line = line.replace(')', ' ')
        line = line.replace(',', ' ')
        line = line.replace('=', ' ')
        letters = line.split()
        if id == 0:
            id = 1
            directions = line
        if len(letters) == 3:
            start1 = ord(letters[0][0]) - 65
            start2 = ord(letters[0][1]) - 65
            start3 = ord(letters[0][2]) - 65

            map[start1][start2][start3][0] = (ord(letters[1][0]) - 65) * 10000 + (ord(letters[1][1]) - 65) * 100 + (ord(letters[1][2]) - 65)
            map[start1][start2][start3][1] = (ord(letters[2][0]) - 65) * 10000 + (ord(letters[2][1]) - 65) * 100 + (ord(letters[2][2]) - 65)

            if start3 == 0:
                poz.append([start1, start2, start3])

x = 0
numbers = []

for i in range(0, len(poz)):
    poz1 = poz[i][0]
    poz2 = poz[i][1]
    poz3 = poz[i][2]
    nr = 0
    ok = 0
    k = -1
    while True:
        k += 1
        nr += 1
        if k == len(directions):
            k = 0
        if directions[k] == 'L':
            move = 0
        else:
            move = 1
        if(map[poz1][poz2][poz3][move] % 100 == 25):
            break
        next1 = map[poz1][poz2][poz3][move] // 10000
        next2 = map[poz1][poz2][poz3][move] % 10000 // 100
        next3 = map[poz1][poz2][poz3][move] % 100 
        poz1 = next1
        poz2 = next2
        poz3 = next3
    numbers.append(nr)

x = numbers[0]

for i in range(1, len(numbers)):
    x = x*numbers[i] / CMMDC(x, numbers[i])

print(x)

