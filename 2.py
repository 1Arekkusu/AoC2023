id = 0
ans1 = 0
ans2 = 0

with open("advent2023\input.txt", 'r') as f:
    for line in f:

        line = line.strip()

        id += 1
        c = id
        nr = 0
        while c > 0:
            nr += 1
            c = c // 10
        i = 7 + nr
        red = 0
        green = 0
        blue = 0
        while i < len(line):
            sum = 0
            while line[i].isdigit():
                sum = sum*10 + int(line[i])
                i += 1
            i += 1
            if line[i] == 'r':
                red = max(red, sum)
                i += 5
            elif line[i] == 'b':
                blue = max(blue ,sum)
                i += 6
            else:
                green = max(green, sum)
                i += 7
        if red < 13 and green < 14 and blue < 15:
            ans1 = ans1 + id
        ans2 += red * green * blue

print(ans1)

print(ans2)