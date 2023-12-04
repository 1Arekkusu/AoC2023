a = []

with open("advent2023\input.txt", 'r') as f:
    for line in f:
        line = line.strip()
        a.append(line)

NEW_I = [-1, -1, -1, 0, 1, 1, 1, 0]
NEW_J = [-1, 0, 1, 1, 1, 0, -1, -1]

#part 1

ans1 = 0

for i in range(0, len(a)):
    number = 0
    ok = False
    for j in range(0, len(a[i])):
        if a[i][j].isdigit():
            number = number*10 + int(a[i][j])
            for k in range(0,8):
                ni = i + NEW_I[k]
                nj = j + NEW_J[k]
                if ni >= 0 and nj >= 0 and ni < 140 and nj < 140:
                    if (not a[ni][nj].isdigit()) and (not a[ni][nj]=='.'):
                        ok = True
        else:
            if ok == True:
                ans1 += number
                ok = False
            number = 0
    if ok == True:
        ans1 += number

print(ans1)

#part 2

ans2 = 0

for i in range (0, len(a)):
    for j in range(0, len(a[i])):
        number1 = 0
        number2 = 0
        if a[i][j] == '*':
            for k in range(0, 8):
                ni = i + NEW_I[k]
                nj = j + NEW_J[k]
                if a[ni][nj].isdigit():
                    nr = 0
                    if k != 1 and k!= 2 and k!= 5 and k!=6:
                        x=nj
                        y=nj
                        while  x-1>=0 and a[ni][x-1].isdigit():
                            x += -1
                        while y+1<140 and a[ni][y+1].isdigit():
                            y += 1
                        for h in range (x,y+1):
                            nr = nr*10 + int(a[ni][h])
                    else:
                        if not a[i+NEW_I[k-1]][j+NEW_J[k-1]].isdigit():
                            x=nj
                            y=nj

                            while  x-1>=0 and a[ni][x-1].isdigit():
                                x += -1
                            while y+1<140 and a[ni][y+1].isdigit():
                                y += 1
                            for h in range (x,y+1):
                                 nr = nr*10 + int(a[ni][h])
                    if nr!=0:
                        if number1 == 0:
                            number1 = nr
                        elif number2 == 0:
                            number2 = nr
                        else:
                            number1 = 0
                            number2 = 0
                            break
            if number1 != 0 and number2 !=0:
                ans2 += number1 * number2

print(ans2)


                        

        


