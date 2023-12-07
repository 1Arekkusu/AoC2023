#part 1

Time = []
Distance = []
id = 0

ans1 = 1

with open("advent2023\input.txt", 'r') as f:
    for line in f:
        id += 1
        line = line.strip()
        numbers = line.split()
        for i in range(1,len(numbers)):
            if id == 1:
                Time.append(int(numbers[i]))
            else:
                Distance.append(int(numbers[i]))

for i in range (0, len(Time)):
    time = Time[i]
    nr = 0
    distance = Distance[i]
    for j in range (1, time):
        if j * (time-j) > distance:
            nr += 1
    ans1 = ans1 * nr

print(ans1)

#part 2

id = 0
ans2 = 0

TimeString = ""
DistanceString = ""

with open("advent2023\input.txt", 'r') as f:
    for line in f:
        id += 1
        line = line.strip()
        numbers = line.split()
        for i in range(1, len(numbers)):
            if id == 1:
                TimeString += numbers[i]
            else:
                DistanceString += numbers[i]

time = int(TimeString)
distance = int(DistanceString)

n = time // 2
if time % 2 == 0:
    n += 1

for i in range(1, n):
    if i * (time-i) > distance:
        if i == time // 2:
            ans2 += 1
        else:
            ans2 += 2

print(ans2)
