numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

s = 0

with open("advent2023\input.txt", "r") as f:
    for line in f:
        line = line.strip()
        nr1 = -1
        nr2 = -1
        p1 = -1
        p2 = -1
        i=-1
        for a in line:
            i += 1
            if a.isnumeric():
                if nr1 < 0:
                    nr1 = int(a)
                    nr2 = int(a)
                    p1 = i
                    p2 = i
                    
                else:
                    nr2 = int(a)
                    p2 = i
        i= 0
        for number in numbers:
            i += 1
            x = y = -1
            x = line.find(number, 0, p1)
            y = line.rfind(number, p2)
            if x < p1 and x >= 0:
                p1 = x + len(number) -1
                nr1 = i
            if y > p2:
                p2 = y
                nr2 = i
        s += nr1*10 + nr2
print(s)
        


