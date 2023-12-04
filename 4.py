GoodNumbers = [-1, -1, -1, -1, -1, -1, -1 ,-1 ,-1, -1]

#part 1

ans1 = 0

with open("advent2023\input.txt", 'r') as f:
    for line in f:

        line = line.strip()
        number = 0
        x = 0
        power = -1
        for i in range(10, len(line)):
            if line[i].isdigit():
                number = number * 10 + int(line[i])
            elif number > 0:
                if x < 10 and number > 0:
                    GoodNumbers[x] = number
                    x += 1
                else: 
                    if number in GoodNumbers:
                        power += 1
                number = 0
        if number in GoodNumbers:
            power += 1
        if power >= 0:
            ans1 += 2**power

print(ans1)

#part 2

ans2 = 0
v = []
for i in range (0, 197):
    v.append(1)

id = 0    

with open("advent2023\input.txt", "r")as f:
    for line in f:

        line = line.strip()
        id += 1
        ans2 += v[id]
        number  = 0
        x = 0
        power = 0
        for i in range(10, len(line)):
            if line[i].isdigit():
                number = number * 10 + int(line[i])
            elif number > 0:
                if x < 10:
                    GoodNumbers[x] = number
                    x += 1
                else:
                    if number in GoodNumbers:
                        power += 1
                number = 0
        if number in GoodNumbers:
            power += 1
        for i in range(1, power+1):
            if id + i <= 196:
                v[id+i] += v[id]
        print(id, power, v[id])

print(ans2)