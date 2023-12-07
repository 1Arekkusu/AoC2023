#part 1

id = 0
v = []
ok = []

with open("advent2023\input.txt" , 'r') as f:
    for line in f:
        id += 1
        map = 0
        line = line.strip()
        if id == 1:
            number = 0
            for i in range(7, len(line)):
                if line[i].isdigit():
                    number = number * 10 + int(line[i])
                else:
                    v.append(number)
                    ok.append(0)
                    number = 0
            v.append(number)
            ok.append(0)
        else:
            if len(line)>=1 and line[0].isalpha():
                map += 1
                for i in range (0,len(ok)):
                    ok[i] = 0
            elif len(line)>=1 and line[0].isdigit():
                numbers  = line.split()
                destination = int(numbers[0])
                source = int(numbers[1])
                length = int(numbers[2])
                for j in range(0, len(v)):
                    if v[j] >= source and v[j] <= source + length - 1 and ok[j] == 0:
                        v[j] = destination + (v[j]-source)
                        ok[j] = 1


print(min(v))

#part 2

id = 0
v = []
ok = []

with open("advent2023\input.txt" , 'r') as f:
    for line in f:
        id += 1
        map = 0
        line = line.strip()
        if id == 1:
            number = 0
            copy = 0
            k = 0
            for i in range(7, len(line)):
                if line[i].isdigit():
                    number = number * 10 + int(line[i])
                else:
                    k += 1
                    k %= 2
                    if k == 1:
                        copy = number
                        number = 0
                    else: 
                        v.append([copy, int(copy+number)])
                        ok.append(0)
                        number = 0
                        copy = 0
            v.append([copy, copy+number])
            ok.append(0)
        else:
            if len(line) >= 1:
                if line[0].isalpha():
                    map += 1
                    for i in range(0, len(ok)):
                        ok[i] = 0
                else:
                    numbers  = line.split()
                    destination = int(numbers[0])
                    source = int(numbers[1])
                    length = int(numbers[2]) - 1
                    for j in range(0, len(v)):
                        if ok[j] == 0:
                            if v[j][0] >= source and v[j][1] <= source + length:
                                v[j][0] = destination + (v[j][0] - source)
                                v[j][1] = destination + (v[j][1] - source)
                                ok[j] = 1
                            elif v[j][0] >= source and v[j][1] > source + length and v[j][0] <= source + length:
                                v.append([source+length+1, v[j][1]])
                                ok.append(0)
                                v[j][0] = destination + (v[j][0] - source)
                                v[j][1] = destination + length
                                ok[j] = 1
                            elif v[j][0] < source and v[j][1] <= source + length and v[j][1] >= source:
                                v.append([v[j][0], source - 1])
                                ok.append(0)
                                v[j][0] = destination
                                v[j][1] = destination + (v[j][1] - source)
                                ok[j] = 1
                            elif v[j][0] < source and v[j][1] > source + length:
                                v.append([v[j][0], source-1])
                                ok.append(0)
                                v.append([source + length + 1, v[j][1]])
                                ok.append(0)
                                ok[j] = 1
                                v[j][0] = destination
                                v[j][1] = destination + length

print(min(v)[0])
