
Galaxies = []
EmptyRows = []
EmptyCols = []
row = -1

with open("advent2023\input.txt", 'r') as f:
    for line in f:
        row += 1
        Empty = 999999
        line = line.strip()
        for col in range (0, len(line)):
            if row == 0:
                EmptyCols.append(999999)
            if(line[col] == '#'):
                Galaxies.append([row, col])
                EmptyCols[col] = 0
                Empty = 0
        if row >= 1:
            EmptyRows.append(EmptyRows[row-1] + Empty)
        else:
            EmptyRows.append(Empty)

for i in range (0, len(EmptyCols) - 1):
    EmptyCols[i+1] += EmptyCols[i]

ans1 = 0

for i in range(0,len(Galaxies)):
    for j in range(i+1, len(Galaxies)):
        ans1 += abs(Galaxies[i][0] - Galaxies[j][0]) + abs(Galaxies[i][1] - Galaxies[j][1]) + abs(EmptyRows[Galaxies[i][0]] - EmptyRows[Galaxies[j][0]]) + abs(EmptyCols[Galaxies[j][1]] - EmptyCols[Galaxies[i][1]])

print(ans1)
        

